# 📊 Resumo Executivo - Datathon PEDE
## Principais Descobertas e Insights

---

## 🎯 Visão Geral do Projeto

**Organização**: Associação Passos Mágicos (32 anos transformando vidas)  
**Dataset**: 860 alunos, 42 variáveis, período 2022-2024
**Indicadores**: IAN, IDA, IEG, IAA, IPS, IPV, INDE  
**Objetivo**: Análise + Predição de Risco + Ferramenta Interativa

---

## 📈 Respostas às 11 Perguntas do Desafio

### 1️⃣ Adequação do Nível (IAN)
**Pergunta**: Qual é o perfil geral de defasagem dos alunos (IAN) e como ele evolui ao longo do ano?

**Descobertas**:
- Média IAN: **6.42** (escala 0-10)
- Desvio padrão: **2.39** (alta variabilidade)
- **Distribuição de Risco**:
  - Adequado (IAN ≥ 7): ~45% dos alunos
  - Moderadamente Defasado (IAN 4-7): ~40%
  - Severamente Defasado (IAN < 4): ~15%

**Insight**: Aproximadamente **55% dos alunos** apresentam algum nível de defasagem, indicando necessidade de intervenção em mais da metade do público atendido.

---

### 2️⃣ Desempenho Acadêmico (IDA)
**Pergunta**: O desempenho acadêmico médio (IDA) está melhorando, estagnado ou caindo ao longo das fases e anos?

**Descobertas**:
- Média IDA: **6.09** (escala 0-10)
- Variação por fase: Fase 0 (7.14) → Fase 7 (5.25)
- Tendência: **Decrescente** nas fases mais avançadas

**Insight**: Há uma **queda de desempenho** nas fases mais avançadas, sugerindo que alunos mais antigos enfrentam desafios crescentes ou que os critérios de avaliação se tornam mais rigorosos.

---

### 3️⃣ Engajamento (IEG)
**Pergunta**: Há relação entre engajamento e desempenho/ponto de virada?

**Descobertas**:
- **IEG x IDA**: Correlação **0.564** (Moderada-Forte) ✅
- **IEG x IPV**: Correlação **0.589** (Moderada-Forte) ✅
- Média IEG: **7.89** (maior que IDA)

**Insight**: **Engajamento é um preditor forte de sucesso**. Alunos mais engajados têm significativamente melhor desempenho e maior probabilidade de atingir o ponto de virada.

**Recomendação**: Investir em atividades que aumentem o engajamento pode ter impacto direto no desempenho acadêmico.

---

### 4️⃣ Autoavaliação (IAA)
**Pergunta**: As percepções dos alunos sobre si mesmos (IAA) são coerentes com seu desempenho real (IDA) e engajamento (IEG)?

**Descobertas**:
- Média IAA: **8.27** (maior que IDA: 6.09 e IEG: 7.89)
- Correlação IAA x IDA: **0.209** (Fraca)
- Correlação IAA x IEG: **0.183** (Muito Fraca)
- **Discrepância**: Alunos tendem a se **superestimar** tanto no desempenho quanto no engajamento

**Categorização (em relação ao IDA)**:
- Coerentes (|IAA-IDA| < 1.5): ~60%
- Superestimação (IAA > IDA + 1.5): ~30%
- Subestimação (IAA < IDA - 1.5): ~10%

**Insight**: Há uma **desconexão entre autopercepção e realidade** — tanto no desempenho quanto no engajamento. A baixa correlação com IEG sugere que alunos pouco engajados tendem a não perceber seu próprio baixo engajamento.

**Recomendação**: Trabalhar autoconhecimento e feedback construtivo para alinhar autopercepção com a realidade acadêmica e comportamental.

---

### 5️⃣ Aspectos Psicossociais (IPS)
**Pergunta**: Há padrões psicossociais (IPS) que antecedem quedas de desempenho acadêmico ou de engajamento?

**Descobertas**:
- Média IPS: **6.91**
- Correlação IPS x IDA: **0.132** (Fraca) — impacto no desempenho
- Correlação IPS x IEG: **0.093** (Muito Fraca) — impacto no engajamento

**Análise por Categoria**:
- IPS Alto (≥7): IDA médio = 6.3 | IEG médio = 8.1
- IPS Médio (4-7): IDA médio = 5.8 | IEG médio = 7.7
- IPS Baixo (<4): IDA médio = 5.2 | IEG médio = 7.3

**Insight**: Alunos com **IPS baixo apresentam pior desempenho e menor engajamento**. Embora as correlações sejam fracas, o padrão é consistente: o IPS funciona como **indicador de alerta precoce** para quedas tanto acadêmicas quanto comportamentais.

---

### 6️⃣ Aspectos Psicopedagógicos (IPP)
**Pergunta**: Os aspectos psicopedagógicos confirmam ou contradizem a defasagem?

**Descobertas**:
- Número de avaliações correlaciona com IAN
- Alunos com mais avaliações tendem a ter **maior atenção** da equipe
- Recomendações de psicologia são mais frequentes em alunos com IAN baixo

**Insight**: Os aspectos psicopedagógicos **confirmam** a defasagem observada no IAN, validando a necessidade de acompanhamento especializado.

---

### 7️⃣ Ponto de Virada (IPV)
**Pergunta**: Quais comportamentos — acadêmicos, emocionais ou de engajamento — mais influenciam o IPV ao longo do tempo?

**Descobertas - Correlações com IPV por categoria de comportamento**:

| Categoria | Indicador | Correlação com IPV |
|---|---|---|
| Acadêmico | IDA (Desempenho) | **0.617** (Forte) |
| Engajamento | IEG (Engajamento) | **0.589** (Moderada-Forte) |
| Emocional/Psicossocial | IPS (Psicossocial) | **0.208** (Fraca) |
| Autopercepção | IAA (Autoavaliação) | **0.256** (Fraca) |

**Evolução Temporal do IPV**:
- Fases iniciais (Quartzo): IPV mais elevado, responde bem ao desempenho acadêmico
- Fases intermediárias (Ágata/Ametista): engajamento ganha peso crescente
- Fases avançadas (Topázio): IPV se estabiliza, influenciado pela combinação IDA + IEG

**Combinações por nível de IPV**:
- IDA Alto + IEG Alto → IPV médio: **8.5**
- IDA Baixo + IEG Baixo → IPV médio: **6.2**

**Insight**: Os **comportamentos acadêmicos (IDA)** têm o maior impacto individual, mas o **engajamento (IEG)** é o diferencial ao longo do tempo. O componente emocional/psicossocial (IPS) atua como base: quando comprometido, limita o potencial de atingir o ponto de virada mesmo com bom desempenho.

---

### 8️⃣ Multidimensionalidade do INDE
**Pergunta**: Quais combinações de indicadores (IDA + IEG + IPS + IPP) **mais elevam** o desempenho global do aluno (INDE)?

**Descobertas - Combinações que mais elevam o INDE**:

| Combinação de Indicadores | INDE Médio |
|---|---|
| IDA Alto (≥7) + IEG Alto (≥7) + IPS Alto (≥7) | **8.95** |
| IDA Alto (≥7) + IEG Alto (≥7) + IAA Alta (≥7) | **8.83** |
| IDA Alto (≥7) + IEG Alto (≥7) | **8.72** |
| IDA Médio (4-7) + IEG Alto (≥7) | **7.45** |
| IDA Médio (4-7) + IEG Médio (4-7) | **6.60** |
| IDA Baixo (<4) + IEG Alto (≥7) | **6.83** |
| IDA Baixo (<4) + IEG Baixo (<4) | **5.12** |

**Peso de Cada Indicador no Aumento do INDE**:
1. **IDA** (Desempenho Acadêmico): ~40% do impacto total 🥇
2. **IEG** (Engajamento): ~35% do impacto total 🥈
3. **IPS** (Psicossocial): ~15% do impacto total 🥉
4. **IAA** (Autoavaliação): ~10% do impacto total

**Correlações de Apoio**:
- IDA: 0.818 | IEG: 0.802 | IPV: 0.789 | IAA: 0.455 | IAN: 0.395 | IPS: 0.269

**Combinação Ótima**: IDA > 7 + IEG > 7 + IPS > 7 → INDE médio = **8.95** (+75% vs combinação mínima)

**Insight**: A combinação que **mais eleva** o INDE é o investimento simultâneo em Desempenho Acadêmico (IDA) e Engajamento (IEG). Elevar IDA de baixo para alto mantendo IEG alto representa ganho médio de **+1.9 pontos** no INDE. O IPS atua como amplificador: quando saudável, potencializa o efeito dos demais indicadores.

**Recomendação**: Priorizar ações que elevem **simultaneamente IDA e IEG**. Intervenções isoladas em apenas um indicador geram ganhos parciais. O trio IDA + IEG + IPS é a combinação de maior impacto mensurável no INDE.

---

### 9️⃣ Previsão de Risco com Machine Learning
**Pergunta**: Quais padrões nos indicadores permitem identificar alunos em risco antes de queda no desempenho ou aumento da defasagem? Construa um modelo preditivo que mostre a **probabilidade** do aluno entrar em risco de defasagem.

**Resposta**: **SIM, é possível! ✅**

**Modelo Desenvolvido**:
- **Algoritmo**: XGBoost Classifier
- **Features**: 9 (IDA, IEG, IAA, IPS, IPV, Idade, Defas, Gênero, Fase)
- **Saída**: Probabilidade (0-100%) de entrar em risco de defasagem, com 3 classes
- **Validação**: Split 80/20 + 5-fold Cross-Validation

**Classes e Critérios**:
- **Alto Risco**: IAN < 5 OU (IDA < 5 E IEG < 6)
- **Médio Risco**: IAN entre 5-7 OU IDA entre 5-7
- **Baixo Risco**: IAN ≥ 7 E IDA ≥ 7

**Padrões identificados pelo modelo (Feature Importance)**:
1. IDA (Desempenho) — **35%** → queda abaixo de 5 é sinal crítico
2. IPV (Ponto de Virada) — **22%** → IPV baixo precede risco
3. IEG (Engajamento) — **18%** → desengajamento antecede a queda
4. Defasagem — **12%** → defasagem acumulada eleva risco
5. IPS (Psicossocial) — **8%** → alerta precoce emocional

**Insight**: O modelo identifica alunos em risco **antes** da queda no desempenho ou aumento da defasagem, exibindo a **probabilidade individual** de cada cenário. Isso permite intervenção preventiva e não remediativa.

---

### 🔟 Efetividade do Programa
**Pergunta**: Os indicadores mostram melhora consistente ao longo do ciclo nas diferentes fases (Quartzo, Ágata, Ametista e Topázio), confirmando o impacto real do programa?

**Descobertas por fase do programa**:

| Fase | Nível | IDA | IEG | IPV |
|---|---|---|---|---|
| Quartzo (0-1) | Inicial | 7.14 | 8.09 | 7.56 |
| Ágata (2-3) | Intermediária 1 | 6.45 | 7.95 | 7.40 |
| Ametista (4-5) | Intermediária 2 | 5.80 | 7.58 | 7.28 |
| Topázio (6-7) | Avançada | 5.25 | 7.24 | 7.18 |

**Tendências**:
- **IDA**: Queda de **-1.89 pontos** de Quartzo a Topázio
- **IEG**: Queda de **-0.85 pontos** — menor queda, mais resiliente
- **IPV**: Queda de **-0.38 pontos** — mais estável entre fases

**Insight**: **NÃO há melhora consistente** ao longo das fases. A queda é progressiva de Quartzo a Topázio, com maior intensidade nas fases Ágata/Ametista. Isso pode indicar: (1) critérios de avaliação mais rigorosos nas fases avançadas; (2) desafios crescentes que os alunos enfrentam; (3) necessidade de revisar estratégias para as fases intermediárias.

**Recomendação**: Implementar intervenções específicas para as transições entre Quartzo→Ágata e Ágata→Ametista, onde ocorrem as maiores quedas.

---

### 1️⃣1️⃣ Insights Criativos
**Pergunta**: Há padrões adicionais não cobertos pelas perguntas anteriores?

**Descoberta 1 - Diferenças por Gênero**:
- Análise estatística revela diferenças significativas em alguns indicadores
- Importante para personalização de estratégias

**Descoberta 2 - Perfis de Alunos (Clustering)**:
Identificamos **3 perfis distintos**:
1. **Alto Desempenho**: IDA alto, IEG alto, IPS alto (~25%)
2. **Desempenho Moderado**: Indicadores médios (~50%)
3. **Necessita Suporte**: IDA baixo, IEG baixo, IPS baixo (~25%)

**Descoberta 3 - Evolução Temporal**:
- Alunos que ingressaram mais recentemente apresentam indicadores ligeiramente melhores
- Sugere melhoria nas estratégias de seleção/acolhimento

**Descoberta 4 - Alunos Destaque**:
- Alunos "Indicados" têm médias **significativamente superiores** em todos os indicadores
- Perfil de destaque: IDA > 8, IEG > 9, IPV > 8.5

---

## 🎯 Principais Conclusões

### ✅ O Que Funciona:
1. **Engajamento é fundamental** - Forte correlação com sucesso
2. **Modelo preditivo é viável** - Identifica riscos com precisão
3. **Intervenção precoce é possível** - IPS e IEG são sinais de alerta

### ⚠️ Pontos de Atenção:
1. **Queda de desempenho nas fases avançadas** - Requer investigação
2. **Defasagem é independente** - Não se resolve apenas com engajamento
3. **Autopercepção desalinhada** - Alunos se superestimam

### 💡 Recomendações Estratégicas:

**Curto Prazo (Imediato)**:
1. Usar modelo preditivo para identificar alunos em risco
2. Implementar ações de engajamento para todos os alunos
3. Acompanhamento psicossocial intensivo para IPS baixo

**Médio Prazo (3-6 meses)**:
1. Revisar estratégias pedagógicas para fases avançadas
2. Trabalhar autoconhecimento e feedback com alunos
3. Personalizar abordagens por perfil de aluno

**Longo Prazo (1 ano)**:
1. Monitorar evolução dos indicadores trimestralmente
2. Avaliar efetividade das intervenções
3. Ajustar modelo preditivo com novos dados

---

## 📊 Números-Chave para Memorizar

- **860** alunos analisados
- **42** variáveis no dataset
- **7** indicadores principais
- **0.56** correlação IEG-IDA (engajamento → desempenho)
- **0.82** correlação INDE-IDA (desenvolvimento ← desempenho)
- **55%** dos alunos com algum nível de defasagem
- **3** perfis distintos de alunos identificados
- **9** features no modelo preditivo
- **8.95** INDE médio com combinação ótima IDA+IEG+IPS altos

---

## 🚀 Entregas do Projeto

✅ **Análise Completa**: 11 perguntas respondidas com rigor estatístico  
✅ **Modelo Preditivo**: XGBoost treinado e validado  
✅ **Aplicação Web**: Streamlit com 4 abas — deploy no Community Cloud
✅ **Dashboard Interativo**: Filtros, KPIs e visualizações
✅ **Preditor de Risco**: Probabilidade individual de defasagem em tempo real
✅ **Resumo Executivo**: 11 perguntas respondidas diretamente na aplicação
✅ **Documentação**: README, Guia Rápido, Roteiro de Apresentação
✅ **Notebooks**: Feature engineering, treino/teste, modelagem e avaliação
✅ **Vídeo**: Apresentação de até 5 minutos com storytelling e resultados

---

## 💬 Mensagem Final

Este projeto demonstra o **poder dos dados** para gerar **impacto social real**. Ao transformar 860 histórias em insights acionáveis, contribuímos para que a **Associação Passos Mágicos** continue sua missão de **transformar vidas através da educação**.

**Da análise à ação. Dos dados ao impacto. Da informação à transformação.**

---

**Desenvolvido com ❤️ para a Associação Passos Mágicos**  
**FIAP Pós-Tech em Data Analytics - Datathon Fase 5 - 2026**
