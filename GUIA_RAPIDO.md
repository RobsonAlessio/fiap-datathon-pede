# 🚀 Guia Rápido - Datathon PEDE

## ⚡ Início Rápido (5 minutos)

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Executar Análise Preliminar (Opcional)
```bash
python preliminary_analysis.py
```
Gera estatísticas e visualizações em `data/processed/`

### 3. Treinar Modelo (Opcional - Já treinado)
```bash
python train_model.py
```
Treina o modelo XGBoost e salva em `models/`

### 4. Executar Aplicação
```bash
streamlit run app.py
```
Abre automaticamente em `http://localhost:8501`

---

## 📊 Usando a Aplicação

### Aba 1: ℹ️ Sobre o Projeto
- Informações sobre a Associação Passos Mágicos
- Objetivos do projeto
- Tecnologias utilizadas
- Equipe desenvolvedora

### Aba 2: 🔮 Preditor de Risco
**Como usar:**
1. Preencha os dados do aluno nos 3 painéis:
   - **Dados Pessoais**: Idade, Gênero, Fase, Defasagem
   - **Indicadores Acadêmicos**: IDA, IEG, IPV
   - **Indicadores Comportamentais**: IAA, IPS

2. Clique em "🎯 Calcular Risco"

3. Veja os resultados:
   - 🔴 **Alto Risco**: Atenção urgente necessária
   - 🟡 **Médio Risco**: Monitoramento recomendado
   - 🟢 **Baixo Risco**: Manutenção do desempenho

4. Analise:
   - Confiança do modelo (%)
   - Probabilidade de defasagem (%)
   - Gráfico de distribuição de probabilidades
   - Recomendações personalizadas

### Aba 3: 📊 Dashboard Analítico
**Recursos disponíveis:**

1. **Filtros Interativos** (topo da página):
   - Fase do Programa (0-7)
   - Gênero (Masculino/Feminino)
   - Atingiu Ponto de Virada (Sim/Não)
   - Ano de Ingresso

2. **KPIs Principais** (5 métricas):
   - Total de Alunos
   - IDA Médio (Desempenho)
   - IEG Médio (Engajamento)
   - INDE Médio (Desenvolvimento)
   - % em Risco (IAN < 5)

3. **Visualizações**:
   - Distribuição por Fase (gráfico de barras)
   - Evolução dos Indicadores (gráfico de linhas)
   - Matriz de Correlação (heatmap)
   - Scatter plot IEG vs IDA

4. **Insights Textuais**:
   - Engajamento e Desempenho
   - Ponto de Virada
   - Adequação de Nível

---

## 🔧 Troubleshooting

### Erro ao carregar dados
```
Erro ao carregar dados: [Errno 2] No such file or directory
```
**Solução:** Verifique se o arquivo Excel está em `data/raw/BASE DE DADOS PEDE 2024 - DATATHON.xlsx`

### Modelo não encontrado
```
⚠️ Modelo em Desenvolvimento
```
**Solução:** Execute `python train_model.py` para treinar o modelo

### Erro de dependências
```
ModuleNotFoundError: No module named 'streamlit'
```
**Solução:** Execute `pip install -r requirements.txt`

### Porta já em uso
```
Port 8501 is already in use
```
**Solução:** 
- Feche outras instâncias do Streamlit
- Ou use: `streamlit run app.py --server.port 8502`

---

## 📁 Estrutura de Arquivos Importantes

```
fiap-datathon-pede/
├── app.py                     ⭐ Aplicação principal
├── train_model.py             🤖 Treinamento do modelo
├── preliminary_analysis.py    📊 Análise rápida
├── utils.py                   🔧 Funções auxiliares
├── requirements.txt           📦 Dependências
│
├── data/
│   ├── raw/                   📂 Dados originais (não modificar)
│   └── processed/             💾 Dados processados
│
├── models/                    🎯 Modelos treinados
│   ├── xgb_model.joblib      ✅ Modelo XGBoost
│   ├── scaler.joblib         ✅ Normalizador
│   ├── target_encoder.joblib ✅ Encoder de classes
│   └── label_encoders.joblib ✅ Encoders categóricos
│
└── notebooks/                 📓 Análises exploratórias
    └── 01_exploratory_analysis.ipynb
```

---

## 💡 Dicas de Uso

### Para Análise Exploratória
1. Use os **filtros** para segmentar os dados
2. Compare indicadores entre **diferentes fases**
3. Identifique **correlações** na matriz
4. Observe a **evolução temporal**

### Para Predição de Risco
1. Teste com **valores extremos** (0 e 10) para ver os limites
2. Compare **diferentes combinações** de indicadores
3. Observe como cada indicador **afeta o risco**
4. Use as **recomendações** como guia de ação

### Para Apresentação
1. Capture **screenshots** das visualizações
2. Use os **insights textuais** como base
3. Demonstre o **preditor** com casos reais
4. Mostre a **evolução** dos indicadores

---

## 🎯 Principais Descobertas

### Correlações Importantes
- **IEG x IDA**: 0.56 (Moderada-Forte) ✅
- **IDA x IPV**: 0.62 (Forte) ✅
- **INDE x IDA**: 0.82 (Muito Forte) ✅
- **INDE x IEG**: 0.80 (Muito Forte) ✅

### Insights Chave
1. 📊 **Engajamento** tem forte relação com **Desempenho**
2. 🎯 **INDE** é fortemente influenciado por **IDA** e **IEG**
3. ⚠️ **IAN** (defasagem) é relativamente **independente**
4. 📈 Alunos mais **engajados** atingem o **ponto de virada**

---

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique a seção **Troubleshooting** acima
2. Consulte o **README.md** principal
3. Revise os **notebooks** de análise
4. Entre em contato com a equipe

---

**Desenvolvido com ❤️ para a Associação Passos Mágicos**
