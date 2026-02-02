"""
Funções e classes auxiliares para o projeto Datathon PEDE
Inclui transformadores personalizados para o pipeline de pré-processamento
"""

import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, OrdinalEncoder, LabelEncoder


class DropFeatures(BaseEstimator, TransformerMixin):
    """
    Transformer para remover features específicas do DataFrame
    """
    def __init__(self, features_to_drop=None):
        self.features_to_drop = features_to_drop if features_to_drop is not None else []

    def fit(self, df, y=None):
        return self

    def transform(self, df):
        df_copy = df.copy()
        if set(self.features_to_drop).issubset(df_copy.columns):
            df_copy.drop(self.features_to_drop, axis=1, inplace=True)
            return df_copy
        else:
            print('⚠️ Uma ou mais features para dropar não estão no DataFrame')
            return df_copy


class OneHotEncodingNames(BaseEstimator, TransformerMixin):
    """
    Transformer para aplicar One-Hot Encoding em features categóricas
    mantendo os nomes das features
    """
    def __init__(self, categorical_features=None):
        self.categorical_features = categorical_features if categorical_features is not None else []
        self.encoder = None

    def fit(self, df, y=None):
        if set(self.categorical_features).issubset(df.columns):
            self.encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
            self.encoder.fit(df[self.categorical_features])
        return self

    def transform(self, df):
        df_copy = df.copy()
        if self.encoder and set(self.categorical_features).issubset(df_copy.columns):
            # Aplicar one-hot encoding
            encoded_array = self.encoder.transform(df_copy[self.categorical_features])
            feature_names = self.encoder.get_feature_names_out(self.categorical_features)
            
            # Criar DataFrame com features encodadas
            encoded_df = pd.DataFrame(
                encoded_array,
                columns=feature_names,
                index=df_copy.index
            )
            
            # Concatenar com as outras features
            other_features = [col for col in df_copy.columns if col not in self.categorical_features]
            df_result = pd.concat([encoded_df, df_copy[other_features]], axis=1)
            
            return df_result
        else:
            return df_copy


class OrdinalFeature(BaseEstimator, TransformerMixin):
    """
    Transformer para aplicar Ordinal Encoding em features ordinais
    """
    def __init__(self, ordinal_features=None, categories=None):
        self.ordinal_features = ordinal_features if ordinal_features is not None else []
        self.categories = categories  # Lista de listas com a ordem das categorias
        self.encoder = None

    def fit(self, df, y=None):
        valid_features = [f for f in self.ordinal_features if f in df.columns]
        if valid_features:
            if self.categories:
                self.encoder = OrdinalEncoder(categories=self.categories, handle_unknown='use_encoded_value', unknown_value=-1)
            else:
                self.encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
            self.encoder.fit(df[valid_features])
        return self

    def transform(self, df):
        df_copy = df.copy()
        valid_features = [f for f in self.ordinal_features if f in df_copy.columns]
        if valid_features and self.encoder:
            df_copy[valid_features] = self.encoder.transform(df_copy[valid_features])
            return df_copy
        else:
            return df_copy


class MinMaxWithFeatNames(BaseEstimator, TransformerMixin):
    """
    Transformer para aplicar MinMax Scaling mantendo os nomes das features
    """
    def __init__(self, numerical_features=None):
        self.numerical_features = numerical_features if numerical_features is not None else []
        self.scaler = None

    def fit(self, df, y=None):
        valid_features = [f for f in self.numerical_features if f in df.columns]
        if valid_features:
            self.scaler = MinMaxScaler()
            self.scaler.fit(df[valid_features])
        return self

    def transform(self, df):
        df_copy = df.copy()
        valid_features = [f for f in self.numerical_features if f in df_copy.columns]
        if valid_features and self.scaler:
            df_copy[valid_features] = self.scaler.transform(df_copy[valid_features])
            return df_copy
        else:
            return df_copy


# Funções auxiliares para análise de dados

def calcular_estatisticas_basicas(df, coluna):
    """
    Calcula estatísticas básicas para uma coluna numérica
    """
    stats = {
        'média': df[coluna].mean(),
        'mediana': df[coluna].median(),
        'desvio_padrão': df[coluna].std(),
        'mínimo': df[coluna].min(),
        'máximo': df[coluna].max(),
        'q1': df[coluna].quantile(0.25),
        'q3': df[coluna].quantile(0.75)
    }
    return stats


def identificar_outliers_iqr(df, coluna, multiplicador=1.5):
    """
    Identifica outliers usando o método IQR (Interquartile Range)
    """
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - multiplicador * IQR
    upper_bound = Q3 + multiplicador * IQR
    
    outliers = df[(df[coluna] < lower_bound) | (df[coluna] > upper_bound)]
    
    return outliers, lower_bound, upper_bound


def criar_faixas_categoricas(valor, faixas, labels):
    """
    Converte um valor numérico em categoria baseado em faixas
    
    Exemplo:
        faixas = [0, 5, 7, 10]
        labels = ['Baixo', 'Médio', 'Alto']
    """
    for i in range(len(faixas) - 1):
        if faixas[i] <= valor < faixas[i + 1]:
            return labels[i]
    return labels[-1]


def calcular_taxa_missing(df):
    """
    Calcula a taxa de valores missing por coluna
    """
    missing_stats = pd.DataFrame({
        'total_missing': df.isnull().sum(),
        'percentual_missing': (df.isnull().sum() / len(df)) * 100
    })
    missing_stats = missing_stats[missing_stats['total_missing'] > 0].sort_values('total_missing', ascending=False)
    return missing_stats


def criar_features_temporais(df, coluna_ano):
    """
    Cria features derivadas de ano (se aplicável)
    """
    df_copy = df.copy()
    if coluna_ano in df_copy.columns:
        df_copy['ano_normalizado'] = (df_copy[coluna_ano] - df_copy[coluna_ano].min()) / (df_copy[coluna_ano].max() - df_copy[coluna_ano].min())
    return df_copy


def balancear_classes_info(y):
    """
    Retorna informações sobre o balanceamento das classes
    """
    contagem = pd.Series(y).value_counts()
    percentuais = (contagem / len(y)) * 100
    
    info = pd.DataFrame({
        'contagem': contagem,
        'percentual': percentuais
    })
    
    return info


def criar_feature_risco(df, indicador, threshold_baixo, threshold_alto):
    """
    Cria uma feature de risco baseada em thresholds
    
    Args:
        df: DataFrame
        indicador: nome da coluna do indicador
        threshold_baixo: valor abaixo do qual é considerado risco alto
        threshold_alto: valor acima do qual é considerado risco baixo
    
    Returns:
        Series com categorias: 'Baixo Risco', 'Médio Risco', 'Alto Risco'
    """
    def classificar_risco(valor):
        if pd.isna(valor):
            return 'Desconhecido'
        elif valor >= threshold_alto:
            return 'Baixo Risco'
        elif valor >= threshold_baixo:
            return 'Médio Risco'
        else:
            return 'Alto Risco'
    
    return df[indicador].apply(classificar_risco)


# Dicionário de mapeamento de fases (específico do PEDE)
FASES_PROGRAMA = {
    'Quartzo': 1,
    'Ágata': 2,
    'Ametista': 3,
    'Topázio': 4
}

# Dicionário de mapeamento de níveis de adequação (IAN)
NIVEIS_IAN = {
    'Adequado': 0,
    'Moderadamente Defasado': 1,
    'Severamente Defasado': 2
}
