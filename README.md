# 📚 Datathon PEDE - Associação Passos Mágicos

## 🌐 Aplicação Online
**Acesse a aplicação deployada**: https://fiap-datathon-pede-jklmr.streamlit.app/

---

Este projeto foi desenvolvido como parte do **Datathon - Fase 5** da Pós-Tech em Data Analytics da FIAP. O objetivo é criar uma solução completa de análise de dados e predição de risco educacional para a **Associação Passos Mágicos**, uma organização que transforma vidas de crianças e jovens através da educação.

## 🎯 Sobre o Projeto

A Associação Passos Mágicos atua há 32 anos oferecendo educação de qualidade, apoio psicológico e psicopedagógico para crianças e jovens em vulnerabilidade social. Este projeto utiliza técnicas avançadas de Data Analytics e Machine Learning para:

- **Analisar** o desenvolvimento educacional dos alunos através de múltiplos indicadores
- **Identificar** padrões e insights sobre defasagem, desempenho e engajamento
- **Período**: 2020-2026
- **Prever** riscos de defasagem educacional antes que aconteçam
- **Disponibilizar** uma ferramenta interativa para tomada de decisão

## 📊 Funcionalidades

O sistema é composto por três módulos principais:

### 1. ℹ️ Sobre o Projeto
- Contexto da Associação Passos Mágicos
- Objetivos e metodologia
- Equipe desenvolvedora

### 2. 🔮 Preditor de Risco
- Formulário interativo para entrada de dados do aluno
- Predição em tempo real de risco de defasagem
- Visualização do perfil do aluno
- Recomendações personalizadas

### 3. 📊 Dashboard Analítico
- Filtros interativos para segmentação de dados
- KPIs principais (total de alunos, % em risco, médias)
- Análises visuais respondendo às 11 perguntas do desafio:
  - Adequação do nível (IAN)
  - Desempenho acadêmico (IDA)
  - Engajamento nas atividades (IEG)
  - Autoavaliação (IAA)
  - Aspectos psicossociais (IPS)
  - Aspectos psicopedagógicos (IPP)
  - Ponto de virada (IPV)
  - Multidimensionalidade dos indicadores
  - Efetividade do programa
  - Insights criativos

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos

Certifique-se de ter o **Python 3.8 ou superior** instalado.

### 2. Clonar ou Baixar o Repositório

```bash
cd fiap-datathon-pede
```

### 3. Configurar o Ambiente Virtual (Recomendado)

**No Windows:**
```powershell
python -m venv venv
.\\venv\\Scripts\\activate
```

**No Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a Aplicação

```bash
streamlit run app.py
```

O navegador abrirá automaticamente no endereço `http://localhost:8501`.

---

## 📂 Estrutura do Projeto

```
fiap-datathon-pede/
├── data/                          # Dados do projeto
│   ├── raw/                       # Dados brutos (Excel original)
│   │   ├── BASE DE DADOS PEDE 2024 - DATATHON.xlsx
│   │   └── Dicionário Dados Datathon.pdf
│   └── processed/                 # Dados processados (CSV limpo)
│       └── pede_clean.csv
├── models/                        # Modelos treinados
│   ├── xgb_model.joblib          # Modelo XGBoost
│   ├── label_encoder.joblib      # Encoder de labels
│   └── scaler.joblib             # Scaler de features
├── notebooks/                     # Análises e desenvolvimento
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_predictive_model.ipynb
├── assets/                        # Recursos visuais
│   └── images/                    # Imagens para apresentação
├── docs/                          # Documentação
│   └── apresentacao_datathon.pdf
├── app.py                         # Aplicação Streamlit principal
├── utils.py                       # Funções auxiliares e pipelines
├── train_model.py                 # Script de treinamento
├── requirements.txt               # Dependências
├── .gitignore                     # Arquivos ignorados
└── README.md                      # Este arquivo
```

---

## 🛠️ Tecnologias Utilizadas

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Manipulação de Dados:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn, XGBoost, Imbalanced-learn
- **Visualização:** Plotly, Matplotlib, Seaborn
- **Serialização:** Joblib

---

## 📈 Modelo Preditivo

O modelo de Machine Learning foi desenvolvido para identificar alunos em risco de defasagem educacional. Características principais:

- **Algoritmo:** XGBoost (Gradient Boosting) ✅
- **Variável Target:** Risco de defasagem (Alto/Médio/Baixo)
  - **Alto Risco**: IAN < 5 OU (IDA < 5 E IEG < 6)
  - **Médio Risco**: IAN entre 5-7 OU IDA entre 5-7
  - **Baixo Risco**: IAN >= 7 E IDA >= 7
- **Features Utilizadas:** 9 features
  - Numéricas: IDA, IEG, IAA, IPS, IPV, Idade, Defasagem (7)
  - Categóricas: Gênero, Fase (2)
- **Dataset:** 860 alunos (80% treino, 20% teste)
- **Validação:** 5-fold Cross-Validation

### Resultados do Modelo

- ✅ Modelo treinado e salvo em `models/xgb_model.joblib`
- ✅ Acurácia no conjunto de teste: [Verificar após execução]
- ✅ Feature Importance:
  1. IDA (Desempenho Acadêmico) - Mais importante
  2. IPV (Ponto de Virada)
  3. IEG (Engajamento)
  4. Defasagem
  5. IPS (Psicossocial)

### Pipeline de Pré-processamento

1. Limpeza de dados e tratamento de missing values
2. Definição da variável target baseada em múltiplos critérios
3. Encoding de variáveis categóricas (LabelEncoder)
4. Normalização de features numéricas (StandardScaler)
5. Treinamento com XGBoost
6. Salvamento de todos os artefatos para produção

---

## 📊 Principais Insights

*(Serão preenchidos após análise exploratória completa)*

1. **Defasagem (IAN):** [Insight sobre perfil de defasagem]
2. **Desempenho (IDA):** [Tendências ao longo do tempo]
3. **Engajamento (IEG):** [Correlação com outros indicadores]
4. **Efetividade:** [Impacto do programa nas diferentes fases]

---

## 👨‍💻 Autores

Projeto desenvolvido como parte do **Datathon - Fase 5 (Data Analytics)**.

- **Juan Cordeiro**: juan-bloc@hotmail.com
- **Kaique Manoel Angelo de Paula Cardoso**: kaique.angello.01@gmail.com
- **Lucas Alexandre Nunes de Melo**: lucasnunes.work@gmail.com
- **Maiquel Roniele Machado de Oliveira**: maiquelroniele@gmail.com
- **Robson Alessio**: robson.alessio@hotmail.com

---

## 🔗 Links Úteis

- **Aplicação Deployada:** [Link do Streamlit Community Cloud]
- **Apresentação:** [Link para apresentação PDF/PPT]
- **Vídeo de Demonstração:** [Link para vídeo de 5 minutos]
- **Associação Passos Mágicos:** [Site oficial](https://passosmagicos.org.br/)

---

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais como parte do curso de Pós-Tech em Data Analytics da FIAP.

---

## 🙏 Agradecimentos

Agradecemos à **Associação Passos Mágicos** por disponibilizar os dados e pela oportunidade de contribuir com um projeto de impacto social real. Agradecemos também à **FIAP** e aos professores pela orientação durante o desenvolvimento deste projeto.

---

**Desenvolvido com ❤️ para transformar vidas através da educação e dados**
