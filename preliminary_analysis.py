"""
Script para análise rápida dos dados PEDE e geração de insights preliminares
Este script pode ser executado antes dos notebooks para ter uma visão geral
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

print("="*80)
print("ANÁLISE PRELIMINAR - DATATHON PEDE 2024")
print("="*80)

# Carregar dados
df = pd.read_excel('data/raw/BASE DE DADOS PEDE 2024 - DATATHON.xlsx')

print(f"\n📊 DIMENSÕES: {df.shape[0]} linhas x {df.shape[1]} colunas\n")

# Indicadores principais
indicadores = ['IAN', 'IDA', 'IEG', 'IAA', 'IPS', 'IPV', 'INDE 22']

print("📈 ESTATÍSTICAS DOS INDICADORES PRINCIPAIS")
print("-"*80)
stats_df = df[indicadores].describe().T
stats_df['missing'] = df[indicadores].isnull().sum()
stats_df['missing_%'] = (stats_df['missing'] / len(df)) * 100
print(stats_df[['count', 'mean', 'std', 'min', 'max', 'missing_%']])

# Análise por Fase
print("\n\n📊 INDICADORES POR FASE DO PROGRAMA")
print("-"*80)
fase_analysis = df.groupby('Fase')[indicadores].mean()
print(fase_analysis)

# Correlações principais
print("\n\n🔗 CORRELAÇÕES ENTRE INDICADORES")
print("-"*80)
corr_matrix = df[indicadores].corr()
print(corr_matrix)

# Identificar alunos em risco (IAN baixo)
print("\n\n⚠️ ANÁLISE DE RISCO (baseado em IAN)")
print("-"*80)

def categorizar_risco_ian(ian):
    if pd.isna(ian):
        return 'Desconhecido'
    elif ian >= 7:
        return 'Baixo Risco'
    elif ian >= 4:
        return 'Médio Risco'
    else:
        return 'Alto Risco'

df['Risco_IAN'] = df['IAN'].apply(categorizar_risco_ian)
risco_dist = df['Risco_IAN'].value_counts()
risco_pct = (risco_dist / len(df)) * 100

print("\nDistribuição de Risco:")
for risco in risco_dist.index:
    print(f"  {risco}: {risco_dist[risco]} alunos ({risco_pct[risco]:.1f}%)")

# Análise de gênero
if 'Gênero' in df.columns:
    print("\n\n👥 ANÁLISE POR GÊNERO")
    print("-"*80)
    genero_stats = df.groupby('Gênero')[indicadores].mean()
    print(genero_stats)

# Análise de defasagem
if 'Defas' in df.columns:
    print("\n\n📉 ANÁLISE DE DEFASAGEM")
    print("-"*80)
    print(f"Defasagem média: {df['Defas'].mean():.2f} anos")
    print(f"Defasagem mediana: {df['Defas'].median():.2f} anos")
    print(f"Alunos com defasagem > 0: {(df['Defas'] > 0).sum()} ({(df['Defas'] > 0).sum()/len(df)*100:.1f}%)")

# Análise de Ponto de Virada
if 'Atingiu PV' in df.columns:
    print("\n\n🎯 ANÁLISE DE PONTO DE VIRADA")
    print("-"*80)
    pv_dist = df['Atingiu PV'].value_counts()
    print(pv_dist)
    
    # Comparar indicadores de quem atingiu vs não atingiu PV
    print("\nMédia dos indicadores por Ponto de Virada:")
    pv_comparison = df.groupby('Atingiu PV')[indicadores].mean()
    print(pv_comparison)

# Salvar resumo
print("\n\n💾 SALVANDO RESUMO DA ANÁLISE...")
with open('data/processed/analise_preliminar.txt', 'w', encoding='utf-8') as f:
    f.write("ANÁLISE PRELIMINAR - DATATHON PEDE 2024\n")
    f.write("="*80 + "\n\n")
    f.write(f"Dimensões: {df.shape}\n\n")
    f.write("Estatísticas dos Indicadores:\n")
    f.write(stats_df.to_string())
    f.write("\n\nIndicadores por Fase:\n")
    f.write(fase_analysis.to_string())
    f.write("\n\nCorrelações:\n")
    f.write(corr_matrix.to_string())

print("✅ Resumo salvo em 'data/processed/analise_preliminar.txt'")

# Criar visualização rápida
print("\n\n📊 GERANDO VISUALIZAÇÕES...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Distribuição de Risco
axes[0, 0].pie(risco_dist.values, labels=risco_dist.index, autopct='%1.1f%%', startangle=90)
axes[0, 0].set_title('Distribuição de Risco (IAN)')

# 2. Indicadores por Fase
fase_analysis[['IDA', 'IEG', 'IPV']].plot(kind='bar', ax=axes[0, 1])
axes[0, 1].set_title('Indicadores Principais por Fase')
axes[0, 1].set_xlabel('Fase')
axes[0, 1].set_ylabel('Valor Médio')
axes[0, 1].legend(title='Indicador')
axes[0, 1].grid(True, alpha=0.3)

# 3. Correlação IEG vs IDA
axes[1, 0].scatter(df['IEG'], df['IDA'], alpha=0.5)
axes[1, 0].set_xlabel('IEG (Engajamento)')
axes[1, 0].set_ylabel('IDA (Desempenho)')
axes[1, 0].set_title('Relação Engajamento vs Desempenho')
axes[1, 0].grid(True, alpha=0.3)

# 4. Distribuição do INDE
axes[1, 1].hist(df['INDE 22'].dropna(), bins=20, edgecolor='black')
axes[1, 1].set_xlabel('INDE (Desenvolvimento Educacional)')
axes[1, 1].set_ylabel('Frequência')
axes[1, 1].set_title('Distribuição do INDE')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('data/processed/analise_preliminar.png', dpi=150, bbox_inches='tight')
print("✅ Gráficos salvos em 'data/processed/analise_preliminar.png'")

print("\n" + "="*80)
print("✅ ANÁLISE PRELIMINAR CONCLUÍDA!")
print("="*80)
print("\nPróximos passos:")
print("  1. Executar notebook 01_exploratory_analysis.ipynb")
print("  2. Responder às 11 perguntas do desafio")
print("  3. Criar modelo preditivo")
print("  4. Desenvolver aplicação Streamlit")
