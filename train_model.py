"""
Script de Treinamento do Modelo Preditivo - Datathon PEDE
Predição de Risco de Defasagem Educacional

Este script treina um modelo XGBoost para prever o risco de defasagem
baseado nos indicadores educacionais dos alunos.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, accuracy_score
from xgboost import XGBClassifier
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

print("="*80)
print("TREINAMENTO DO MODELO PREDITIVO - DATATHON PEDE")
print("="*80)

# ==================== CARREGAMENTO DOS DADOS ====================
print("\n📂 Carregando dados...")
df = pd.read_excel('data/raw/BASE DE DADOS PEDE 2024 - DATATHON.xlsx')
print(f"   Dataset carregado: {df.shape[0]} linhas x {df.shape[1]} colunas")

# ==================== DEFINIÇÃO DA VARIÁVEL TARGET ====================
print("\n🎯 Definindo variável target (Risco de Defasagem)...")

# Criar variável target baseada no IAN (Indicador de Adequação de Nível)
def criar_target_risco(row):
    """
    Define o risco de defasagem baseado em múltiplos indicadores
    
    Critérios:
    - Alto Risco: IAN < 5 OU (IDA < 5 E IEG < 6)
    - Médio Risco: IAN entre 5-7 OU IDA entre 5-7
    - Baixo Risco: IAN >= 7 E IDA >= 7
    """
    ian = row['IAN']
    ida = row['IDA']
    ieg = row['IEG']
    
    if pd.isna(ian) or pd.isna(ida):
        return None
    
    # Alto Risco
    if ian < 5 or (ida < 5 and ieg < 6):
        return 'Alto Risco'
    # Baixo Risco
    elif ian >= 7 and ida >= 7:
        return 'Baixo Risco'
    # Médio Risco
    else:
        return 'Médio Risco'

df['Risco_Defasagem'] = df.apply(criar_target_risco, axis=1)

# Remover linhas com target nulo
df_model = df.dropna(subset=['Risco_Defasagem']).copy()

print(f"\n📊 Distribuição da variável target:")
print(df_model['Risco_Defasagem'].value_counts())
print(f"\nPercentuais:")
print(df_model['Risco_Defasagem'].value_counts(normalize=True) * 100)

# ==================== SELEÇÃO DE FEATURES ====================
print("\n🔧 Selecionando features para o modelo...")

# Features numéricas
numerical_features = ['IDA', 'IEG', 'IAA', 'IPS', 'IPV', 'Idade 22', 'Defas']

# Features categóricas
categorical_features = ['Gênero', 'Fase']

# Verificar quais features estão disponíveis
available_numerical = [f for f in numerical_features if f in df_model.columns]
available_categorical = [f for f in categorical_features if f in df_model.columns]

print(f"   Features numéricas: {available_numerical}")
print(f"   Features categóricas: {available_categorical}")

# Criar dataset de features
X = df_model[available_numerical + available_categorical].copy()
y = df_model['Risco_Defasagem'].copy()

# Remover linhas com valores missing nas features
mask = X.notna().all(axis=1)
X = X[mask]
y = y[mask]

print(f"\n   Dataset final: {X.shape[0]} amostras, {X.shape[1]} features")

# ==================== ENCODING DE VARIÁVEIS CATEGÓRICAS ====================
print("\n🔄 Aplicando encoding...")

# Label encoding para variáveis categóricas
label_encoders = {}
for col in available_categorical:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    label_encoders[col] = le

# Label encoding para target
target_encoder = LabelEncoder()
y_encoded = target_encoder.fit_transform(y)

print(f"   Classes: {target_encoder.classes_}")

# ==================== NORMALIZAÇÃO ====================
print("\n📏 Normalizando features numéricas...")

scaler = StandardScaler()
X[available_numerical] = scaler.fit_transform(X[available_numerical])

# ==================== SPLIT TREINO/TESTE ====================
print("\n✂️ Dividindo dados em treino e teste...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, 
    test_size=0.2, 
    random_state=42, 
    stratify=y_encoded
)

print(f"   Treino: {X_train.shape[0]} amostras")
print(f"   Teste: {X_test.shape[0]} amostras")

# ==================== TREINAMENTO DO MODELO ====================
print("\n🤖 Treinando modelo XGBoost...")

# Configuração do modelo
model = XGBClassifier(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    random_state=42,
    eval_metric='mlogloss'
)

# Treinar modelo
model.fit(X_train, y_train)

print("   ✅ Modelo treinado com sucesso!")

# ==================== AVALIAÇÃO ====================
print("\n📊 Avaliando modelo...")

# Predições
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Acurácia
train_acc = accuracy_score(y_train, y_pred_train)
test_acc = accuracy_score(y_test, y_pred_test)

print(f"\n   Acurácia Treino: {train_acc:.4f}")
print(f"   Acurácia Teste: {test_acc:.4f}")

# Relatório de classificação
print("\n📋 Relatório de Classificação (Teste):")
print(classification_report(y_test, y_pred_test, target_names=target_encoder.classes_))

# Matriz de confusão
print("\n📊 Matriz de Confusão:")
cm = confusion_matrix(y_test, y_pred_test)
print(cm)

# Feature importance
print("\n🎯 Importância das Features:")
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print(feature_importance)

# ==================== VALIDAÇÃO CRUZADA ====================
print("\n🔄 Validação Cruzada (5-fold)...")

cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
print(f"   Scores: {cv_scores}")
print(f"   Média: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

# ==================== SALVAMENTO DO MODELO ====================
print("\n💾 Salvando modelo e artefatos...")

# Criar diretório se não existir
import os
os.makedirs('models', exist_ok=True)

# Salvar modelo
joblib.dump(model, 'models/xgb_model.joblib')
print("   ✅ Modelo salvo: models/xgb_model.joblib")

# Salvar scaler
joblib.dump(scaler, 'models/scaler.joblib')
print("   ✅ Scaler salvo: models/scaler.joblib")

# Salvar encoders
joblib.dump(target_encoder, 'models/target_encoder.joblib')
print("   ✅ Target encoder salvo: models/target_encoder.joblib")

joblib.dump(label_encoders, 'models/label_encoders.joblib')
print("   ✅ Label encoders salvos: models/label_encoders.joblib")

# Salvar lista de features
feature_info = {
    'numerical_features': available_numerical,
    'categorical_features': available_categorical,
    'all_features': list(X.columns)
}
joblib.dump(feature_info, 'models/feature_info.joblib')
print("   ✅ Feature info salvo: models/feature_info.joblib")

# ==================== VISUALIZAÇÕES ====================
print("\n📊 Gerando visualizações...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Feature Importance
axes[0, 0].barh(feature_importance['feature'], feature_importance['importance'])
axes[0, 0].set_xlabel('Importância')
axes[0, 0].set_title('Importância das Features')
axes[0, 0].invert_yaxis()

# 2. Matriz de Confusão
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0, 1],
            xticklabels=target_encoder.classes_,
            yticklabels=target_encoder.classes_)
axes[0, 1].set_title('Matriz de Confusão')
axes[0, 1].set_ylabel('Real')
axes[0, 1].set_xlabel('Predito')

# 3. Distribuição de Predições
axes[1, 0].hist([y_test, y_pred_test], label=['Real', 'Predito'], bins=3, alpha=0.7)
axes[1, 0].set_title('Distribuição Real vs Predito')
axes[1, 0].set_xlabel('Classe')
axes[1, 0].set_ylabel('Frequência')
axes[1, 0].legend()

# 4. Acurácia por Classe
class_accuracies = []
for i, class_name in enumerate(target_encoder.classes_):
    mask = y_test == i
    if mask.sum() > 0:
        acc = accuracy_score(y_test[mask], y_pred_test[mask])
        class_accuracies.append(acc)
    else:
        class_accuracies.append(0)

axes[1, 1].bar(target_encoder.classes_, class_accuracies)
axes[1, 1].set_title('Acurácia por Classe')
axes[1, 1].set_ylabel('Acurácia')
axes[1, 1].set_ylim([0, 1])

plt.tight_layout()
plt.savefig('models/model_evaluation.png', dpi=150, bbox_inches='tight')
print("   ✅ Visualizações salvas: models/model_evaluation.png")

# ==================== RESUMO FINAL ====================
print("\n" + "="*80)
print("✅ TREINAMENTO CONCLUÍDO COM SUCESSO!")
print("="*80)
print(f"\n📊 Resumo do Modelo:")
print(f"   Algoritmo: XGBoost Classifier")
print(f"   Features: {len(X.columns)}")
print(f"   Amostras de Treino: {len(X_train)}")
print(f"   Amostras de Teste: {len(X_test)}")
print(f"   Acurácia Teste: {test_acc:.4f}")
print(f"   Classes: {', '.join(target_encoder.classes_)}")
print(f"\n📁 Artefatos salvos em: models/")
print(f"   - xgb_model.joblib")
print(f"   - scaler.joblib")
print(f"   - target_encoder.joblib")
print(f"   - label_encoders.joblib")
print(f"   - feature_info.joblib")
print(f"   - model_evaluation.png")
print("\n🎯 Próximo passo: Integrar modelo na aplicação Streamlit")
print("="*80)
