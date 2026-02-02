import pandas as pd
import numpy as np

# Carregar dados
print("="*80)
print("ANÁLISE INICIAL DOS DADOS PEDE 2024")
print("="*80)

df = pd.read_excel('data/raw/BASE DE DADOS PEDE 2024 - DATATHON.xlsx')

print(f"\n📊 DIMENSÕES DO DATASET")
print(f"   Linhas: {df.shape[0]}")
print(f"   Colunas: {df.shape[1]}")

print(f"\n📋 COLUNAS DO DATASET:")
for i, col in enumerate(df.columns, 1):
    print(f"   {i:2d}. {col}")

print(f"\n🔍 TIPOS DE DADOS:")
print(df.dtypes.value_counts())

print(f"\n❓ VALORES MISSING:")
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing': missing[missing > 0],
    'Percentual': missing_pct[missing > 0]
}).sort_values('Missing', ascending=False)

if len(missing_df) > 0:
    print(missing_df)
else:
    print("   ✅ Nenhum valor missing encontrado!")

print(f"\n📈 ESTATÍSTICAS DESCRITIVAS (Numéricas):")
print(df.describe())

print(f"\n🎯 PRIMEIRAS 5 LINHAS:")
print(df.head())

print(f"\n💾 SALVANDO INFORMAÇÕES...")
# Salvar info básica
with open('data/raw/data_info.txt', 'w', encoding='utf-8') as f:
    f.write(f"Dataset PEDE 2024 - Informações Básicas\n")
    f.write(f"="*80 + "\n\n")
    f.write(f"Shape: {df.shape}\n\n")
    f.write(f"Colunas:\n")
    for col in df.columns:
        f.write(f"  - {col}\n")
    f.write(f"\nTipos de dados:\n{df.dtypes}\n")

print("\n✅ Análise concluída! Informações salvas em 'data/raw/data_info.txt'")
