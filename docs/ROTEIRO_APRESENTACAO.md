# 🎤 Roteiro de Apresentação - Datathon PEDE
## Associação Passos Mágicos
### Tempo Total: 5 minutos (1 minuto por pessoa) - 2026

---

## 👤 PESSOA 1: Introdução e Contexto (1 minuto)

### Script:

"Olá! Apresentamos o projeto **Datathon PEDE**, desenvolvido para a **Associação Passos Mágicos**, uma organização que há **32 anos** transforma vidas de crianças e jovens em vulnerabilidade social através da educação.

**Nosso desafio** foi analisar dados de **860 alunos** com **42 variáveis**, incluindo 7 indicadores educacionais principais: IAN, IDA, IEG, IAA, IPS, IPV e INDE.

**Nossos objetivos** foram:
- ✅ Analisar o desenvolvimento educacional dos alunos
- ✅ Identificar padrões de defasagem e desempenho
- ✅ Criar um modelo preditivo de risco
- ✅ Desenvolver uma ferramenta interativa para tomada de decisão

O projeto foi estruturado seguindo as melhores práticas de Data Science, com pastas organizadas para dados, modelos e notebooks, incorporando o feedback do professor sobre organização e qualidade de visualizações."

### Elementos Visuais:
- Mostrar logo da Associação Passos Mágicos
- Slide com números-chave: 32 anos, 860 alunos, 42 variáveis, 7 indicadores
- Estrutura de pastas do projeto

---

## 👤 PESSOA 2: Análise Exploratória e Principais Descobertas (1 minuto)

### Script:

"Nossa análise exploratória revelou **insights fundamentais** sobre os indicadores educacionais:

**Descoberta 1 - Engajamento é Crucial:**
O IEG (Engajamento) apresentou **correlação moderada-forte** com IDA (Desempenho) de **0.56** e com IPV (Ponto de Virada) de **0.59**. Isso significa que **alunos mais engajados têm melhor desempenho e maior chance de atingir o ponto de virada**.

**Descoberta 2 - Combinações que mais elevam o INDE:**
Identificamos que a combinação **IDA Alto + IEG Alto + IPS Alto** eleva o INDE médio para **8.95** — 75% acima da combinação mínima. O IDA responde por ~40% do impacto, o IEG por ~35% e o IPS amplifica os resultados quando saudável. Intervenções simultâneas nos dois primeiros geram ganho de **+1.9 pontos** no INDE.

**Descoberta 3 - Defasagem é Independente:**
O IAN (Adequação de Nível) apresentou **correlações fracas** com outros indicadores (< 0.2), sugerindo que a defasagem é um **fator independente** que requer atenção especial e não se resolve apenas com engajamento.

**Descoberta 4 - Evolução por Fases:**
Identificamos que os indicadores variam significativamente entre as 8 fases do programa, com padrões distintos de evolução que permitem intervenções direcionadas."

### Elementos Visuais:
- Matriz de correlação (heatmap)
- Gráfico de evolução dos indicadores por fase
- Scatter plot IEG vs IDA mostrando correlação
- Tabela de combinações ótimas de INDE (IDA + IEG + IPS)
- Gráfico de barras com impacto de cada combinação no INDE

---

## 👤 PESSOA 3: Modelo Preditivo e Tecnologia (1 minuto)

### Script:

"Desenvolvemos um **modelo preditivo de risco** usando **XGBoost**, um algoritmo de gradient boosting de alta performance.

**Características do Modelo:**
- **9 features**: IDA, IEG, IAA, IPS, IPV, Idade, Defasagem, Gênero e Fase
- **3 classes de risco**: Alto, Médio e Baixo
- **Critérios inteligentes**:
  - Alto Risco: IAN < 5 OU (IDA < 5 E IEG < 6)
  - Médio Risco: IAN entre 5-7 OU IDA entre 5-7
  - Baixo Risco: IAN >= 7 E IDA >= 7

**Validação Robusta:**
- Dataset dividido em 80% treino e 20% teste
- Validação cruzada 5-fold para garantir generalização
- Métricas de avaliação completas

**Feature Importance revelou** que os 5 indicadores mais importantes são:
1. **IDA** (Desempenho Acadêmico) - O mais importante
2. **IPV** (Ponto de Virada)
3. **IEG** (Engajamento)
4. **Defasagem** (anos de atraso)
5. **IPS** (Psicossocial)

O modelo está **totalmente integrado** na aplicação web e permite **predições em tempo real**."

### Elementos Visuais:
- Diagrama do pipeline de ML (dados → features → modelo → predição)
- Gráfico de feature importance
- Matriz de confusão do modelo
- Screenshot do modelo em ação no Streamlit

---

## 👤 PESSOA 4: Aplicação Streamlit e Funcionalidades (1 minuto)

### Script:

"Desenvolvemos uma **aplicação web interativa** usando Streamlit com **4 abas principais**:

**Aba 1 - Sobre o Projeto:**
Apresenta o contexto da Associação Passos Mágicos, objetivos do projeto, indicadores analisados e tecnologias utilizadas.

**Aba 2 - Preditor de Risco:** *[DEMONSTRAÇÃO AO VIVO]*
- Formulário intuitivo dividido em 3 seções: Dados Pessoais, Indicadores Acadêmicos e Comportamentais
- Ao clicar em 'Calcular Risco', o modelo retorna:
  - **Classificação de risco** com emoji colorido (🔴 Alto, 🟡 Médio, 🟢 Baixo)
  - **Confiança do modelo** em percentual
  - **Probabilidade de defasagem** combinada
  - **Gráfico de distribuição** de probabilidades por classe
  - **Recomendações personalizadas** baseadas no nível de risco

**Aba 3 - Dashboard Analítico:**
- **Filtros interativos** por Fase, Gênero, Ponto de Virada e Ano de Ingresso
- **5 KPIs principais** no topo: Total de Alunos, IDA Médio, IEG Médio, INDE Médio e % em Risco
- **Múltiplas visualizações**: distribuição por fase, evolução temporal, matriz de correlação, scatter plots
- **Insights textuais** incluindo as combinações que mais elevam o INDE

**Aba 4 - Resumo Executivo:** *(nova)*
- Todas as **11 perguntas** respondidas em seções colapsáveis
- **Q8 em destaque**: tabela e gráfico das combinações que mais elevam o INDE
- Conclusões, recomendações estratégicas e números-chave do projeto

Todas as melhorias foram implementadas: mais gráficos, insights textuais, filtros interativos e o Resumo Executivo integrado."

### Elementos Visuais:
- GIF ou vídeo curto da aplicação em uso
- Screenshots das 3 abas
- Demonstração ao vivo do preditor (se possível)
- Dashboard com filtros aplicados

---

## 👤 PESSOA 5: Resultados, Impacto e Conclusão (1 minuto)

### Script:

"**Resultados Alcançados:**

✅ **Análise Completa**: Respondemos às 11 perguntas do desafio com análises estatísticas robustas
✅ **Modelo Preditivo**: XGBoost com capacidade de identificar alunos em risco **antes** do agravamento
✅ **Aplicação Funcional**: Sistema web completo, testado e pronto para uso
✅ **Insights Acionáveis**: Descobertas que podem orientar decisões pedagógicas

**Impacto Esperado:**

🎯 **Intervenção Precoce**: Identificar alunos em risco permite ação preventiva
📊 **Decisões Baseadas em Dados**: Dashboard fornece visão clara para gestores
💡 **Personalização**: Recomendações adaptadas ao nível de risco de cada aluno
📈 **Monitoramento Contínuo**: Acompanhar evolução dos indicadores ao longo das fases

**Recomendações Principais:**

1. **Trio Ótimo IDA + IEG + IPS**: Elevar os três simultaneamente leva o INDE a **8.95** — a combinação de maior impacto comprovado
2. **Priorizar Engajamento**: Investir em atividades que aumentem o IEG — peso de 35% no INDE
3. **Usar o Modelo**: Aplicar predições trimestralmente para identificar riscos antes do agravamento
4. **Acompanhamento Diferenciado**: Estratégias específicas por perfil de risco e por fase do programa

**Conclusão:**

Este projeto demonstra como **Data Analytics e Machine Learning** podem ser ferramentas poderosas para **impacto social**. Ao transformar dados em insights acionáveis, contribuímos para que a **Associação Passos Mágicos** continue sua missão de **transformar vidas através da educação**.

**Obrigado!**"

### Elementos Visuais:
- Slide com checklist de resultados alcançados
- Infográfico de impacto esperado
- Gráfico mostrando potencial de redução de defasagem
- Slide final com agradecimentos e contatos

---

## 📋 Checklist de Preparação

### Antes da Gravação:
- [ ] Testar aplicação Streamlit localmente
- [ ] Preparar slides com elementos visuais
- [ ] Ensaiar transições entre apresentadores
- [ ] Verificar tempo de cada pessoa (máximo 1 minuto)
- [ ] Preparar demonstração ao vivo do preditor
- [ ] Ter screenshots de backup caso a demo falhe

### Durante a Gravação:
- [ ] Falar de forma clara e pausada
- [ ] Mostrar entusiasmo e confiança
- [ ] Apontar para elementos visuais relevantes
- [ ] Manter contato visual com a câmera
- [ ] Respeitar o tempo de 1 minuto por pessoa

### Elementos Visuais Necessários:
- [ ] Logo da Associação Passos Mágicos
- [ ] Matriz de correlação
- [ ] Gráficos de evolução por fase
- [ ] Tabela de combinações ótimas de INDE (Q8)
- [ ] Feature importance do modelo
- [ ] Screenshots da aplicação (4 abas)
- [ ] GIF/vídeo da aplicação em uso
- [ ] Infográfico de impacto

---

## 🎬 Dicas de Apresentação

### Para Todos:
- **Energia**: Mantenha tom de voz animado e confiante
- **Clareza**: Fale devagar o suficiente para ser compreendido
- **Objetividade**: Vá direto ao ponto, sem rodeios
- **Transição**: Termine passando a palavra para o próximo: "Agora, [Nome] vai apresentar..."

### Linguagem Corporal:
- Sorria naturalmente
- Gesticule para enfatizar pontos importantes
- Mantenha postura ereta e profissional
- Olhe para a câmera (não para a tela)

### Técnicas:
- Use a regra dos 3: agrupe informações em trios
- Destaque números com ênfase vocal
- Pause brevemente após pontos importantes
- Termine cada seção com uma frase de impacto

---

## 📊 Estrutura de Slides Sugerida

1. **Slide de Abertura**: Logo + Título + Nomes da Equipe
2. **Contexto**: Associação Passos Mágicos + Números-chave
3. **Objetivos**: 4 objetivos principais
4. **Descobertas**: Matriz de correlação + Insights
5. **Modelo**: Arquitetura + Feature Importance
6. **Aplicação**: Screenshots das 4 abas
7. **Demo**: Vídeo ou demonstração ao vivo
8. **Resultados**: Checklist de entregas
9. **Impacto**: Infográfico de benefícios
10. **Conclusão**: Mensagem final + Agradecimentos

---

## ⏱️ Cronometragem Sugerida

| Pessoa | Tempo | Conteúdo |
|--------|-------|----------|
| 1 | 0:00-1:00 | Introdução e Contexto |
| 2 | 1:00-2:00 | Análise e Descobertas |
| 3 | 2:00-3:00 | Modelo Preditivo |
| 4 | 3:00-4:00 | Aplicação Streamlit |
| 5 | 4:00-5:00 | Resultados e Conclusão |

**Total**: 5:00 minutos

---

## 💡 Frases de Impacto para Usar

- "Transformando dados em ação para transformar vidas"
- "860 alunos, infinitas possibilidades"
- "Prevenção é melhor que remediação - nosso modelo identifica riscos antes do agravamento"
- "Engajamento não é apenas importante, é fundamental"
- "Data Science a serviço do impacto social"
- "Da análise à ação: um sistema completo para decisões inteligentes"

---

**Desenvolvido com ❤️ para a Associação Passos Mágicos**
**FIAP Pós-Tech em Data Analytics - Datathon Fase 5 - 2026**
