"""
Aplicação Streamlit - Datathon PEDE
Associação Passos Mágicos

Sistema de Predição e Análise de Risco Educacional
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import joblib
from utils import *

# ==================== CONFIGURAÇÃO DA PÁGINA ====================
st.set_page_config(
    page_title="Datathon PEDE - Passos Mágicos",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== TÍTULO PRINCIPAL ====================
st.title("📚 Datathon PEDE - Associação Passos Mágicos")
st.markdown("### Sistema de Análise e Predição de Risco Educacional")
st.markdown("---")

# ==================== CARREGAMENTO DE DADOS ====================
@st.cache_data
def load_data():
    """Carrega os dados do PEDE"""
    try:
        df = pd.read_excel('data/raw/BASE DE DADOS PEDE 2024 - DATATHON.xlsx')
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return None

@st.cache_resource
def load_model_assets():
    """Carrega modelo e artefatos"""
    try:
        model = joblib.load('models/xgb_model.joblib')
        scaler = joblib.load('models/scaler.joblib')
        target_encoder = joblib.load('models/target_encoder.joblib')
        label_encoders = joblib.load('models/label_encoders.joblib')
        feature_info = joblib.load('models/feature_info.joblib')
        return model, scaler, target_encoder, label_encoders, feature_info
    except:
        return None, None, None, None, None

# Carregar dados
df = load_data()

if df is None:
    st.stop()

# Tentar carregar modelo
model, scaler, target_encoder, label_encoders, feature_info = load_model_assets()

# ==================== ABAS DA APLICAÇÃO ====================
tab1, tab2, tab3 = st.tabs([
    "ℹ️ Sobre o Projeto",
    "🔮 Preditor de Risco",
    "📊 Dashboard Analítico"
])

# ==================== ABA 1: SOBRE O PROJETO ====================
with tab1:
    st.header("Sobre o Projeto")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🎯 Associação Passos Mágicos
        
        A **Associação Passos Mágicos** atua há **32 anos** transformando vidas de crianças e jovens 
        de baixa renda através da educação de qualidade, apoio psicológico e psicopedagógico.
        
        #### 📊 Sobre este Projeto
        
        Este sistema foi desenvolvido como parte do **Datathon - Fase 5** da Pós-Tech em Data Analytics 
        da FIAP. O objetivo é utilizar técnicas avançadas de Data Analytics e Machine Learning para:
        
        - 📈 **Analisar** o desenvolvimento educacional dos alunos
        - 🔍 **Identificar** padrões e insights sobre defasagem e desempenho
        - 🎯 **Prever** riscos de defasagem educacional antes que aconteçam
        - 💡 **Disponibilizar** ferramentas para tomada de decisão baseada em dados
        
        #### 📚 Indicadores Analisados
        
        - **IAN**: Indicador de Adequação de Nível
        - **IDA**: Indicador de Desempenho Acadêmico
        - **IEG**: Indicador de Engajamento
        - **IAA**: Indicador de Autoavaliação
        - **IPS**: Indicador Psicossocial
        - **IPV**: Indicador de Ponto de Virada
        - **INDE**: Indicador de Desenvolvimento Educacional
        """)
    
    with col2:
        st.info(f"""
        **📊 Dados do Projeto**
        
        - **Alunos**: {len(df)}
        - **Variáveis**: {df.shape[1]}
        - **Fases**: {df['Fase'].nunique() if 'Fase' in df.columns else 'N/A'}
        - **Período**: 2020-2024
        """)
        
        st.success("""
        **🎓 Fases do Programa**
        
        1. **Quartzo** - Inicial
        2. **Ágata** - Intermediária 1
        3. **Ametista** - Intermediária 2
        4. **Topázio** - Avançada
        """)
        
        if model is not None:
            st.success("""
            **🤖 Modelo Ativo**
            
            ✅ XGBoost treinado
            ✅ Predições disponíveis
            """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 👨‍💻 Equipe Desenvolvedora
    
    Projeto desenvolvido como parte do **Datathon - Fase 5 (Data Analytics)**.
    
    - **[Seu Nome]**: [seu.email@example.com]
    - **[Nome do Colega 2]**: [email2@example.com]
    - **[Nome do Colega 3]**: [email3@example.com]
    - **[Nome do Colega 4]**: [email4@example.com]
    - **[Nome do Colega 5]**: [email5@example.com]
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 🛠️ Tecnologias Utilizadas
    
    - **Frontend**: Streamlit
    - **Análise de Dados**: Pandas, NumPy
    - **Machine Learning**: Scikit-Learn, XGBoost
    - **Visualização**: Plotly, Matplotlib, Seaborn
    """)

# ==================== ABA 2: PREDITOR DE RISCO ====================
with tab2:
    st.header("🔮 Preditor de Risco de Defasagem Educacional")
    
    if model is None:
        st.warning("""
        ⚠️ **Modelo em Desenvolvimento**
        
        O modelo preditivo ainda está sendo treinado. Esta funcionalidade estará disponível em breve.
        
        Por enquanto, você pode explorar o **Dashboard Analítico** para visualizar os dados e insights.
        """)
    else:
        st.markdown("""
        Preencha os dados do aluno abaixo para obter uma predição de risco de defasagem educacional.
        O modelo utiliza **XGBoost** treinado com dados de 860 alunos.
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("Dados Pessoais")
            input_idade = st.number_input("Idade", min_value=6, max_value=25, value=12)
            input_genero = st.selectbox("Gênero", ["Masculino", "Feminino"])
            input_fase = st.selectbox("Fase Atual", [0, 1, 2, 3, 4, 5, 6, 7], 
                                     format_func=lambda x: f"Fase {x}")
            input_defas = st.number_input("Defasagem (anos)", min_value=0, max_value=10, value=0)
        
        with col2:
            st.subheader("Indicadores Acadêmicos")
            input_ida = st.slider("IDA (Desempenho Acadêmico)", 0.0, 10.0, 6.0, 0.1)
            input_ieg = st.slider("IEG (Engajamento)", 0.0, 10.0, 7.0, 0.1)
            input_ipv = st.slider("IPV (Ponto de Virada)", 0.0, 10.0, 7.0, 0.1)
        
        with col3:
            st.subheader("Indicadores Comportamentais")
            input_iaa = st.slider("IAA (Autoavaliação)", 0.0, 10.0, 8.0, 0.1)
            input_ips = st.slider("IPS (Psicossocial)", 0.0, 10.0, 7.0, 0.1)
        
        if st.button("🎯 Calcular Risco", type="primary", use_container_width=True):
            try:
                # Preparar dados para predição
                input_data = pd.DataFrame({
                    'IDA': [input_ida],
                    'IEG': [input_ieg],
                    'IAA': [input_iaa],
                    'IPS': [input_ips],
                    'IPV': [input_ipv],
                    'Idade 22': [input_idade],
                    'Defas': [input_defas],
                    'Gênero': [input_genero],
                    'Fase': [input_fase]
                })
                
                # Aplicar label encoding
                for col in ['Gênero', 'Fase']:
                    if col in label_encoders:
                        try:
                            input_data[col] = label_encoders[col].transform(input_data[col].astype(str))
                        except:
                            input_data[col] = 0
                
                # Normalizar features numéricas
                numerical_cols = ['IDA', 'IEG', 'IAA', 'IPS', 'IPV', 'Idade 22', 'Defas']
                input_data[numerical_cols] = scaler.transform(input_data[numerical_cols])
                
                # Fazer predição
                prediction = model.predict(input_data)[0]
                prediction_proba = model.predict_proba(input_data)[0]
                
                # Decodificar predição
                risk_class = target_encoder.inverse_transform([prediction])[0]
                confidence = prediction_proba[prediction] * 100
                
                # Exibir resultados
                st.success("✅ Análise Concluída!")
                
                # Definir cor baseada no risco
                if risk_class == 'Alto Risco':
                    color = '🔴'
                    delta_color = 'inverse'
                elif risk_class == 'Médio Risco':
                    color = '🟡'
                    delta_color = 'off'
                else:
                    color = '🟢'
                    delta_color = 'normal'
                
                col_res1, col_res2, col_res3 = st.columns(3)
                
                with col_res1:
                    st.metric("Classificação de Risco", f"{color} {risk_class}")
                
                with col_res2:
                    st.metric("Confiança do Modelo", f"{confidence:.1f}%")
                
                with col_res3:
                    # Calcular probabilidade de defasagem (Alto + Médio Risco)
                    prob_defasagem = (prediction_proba[target_encoder.transform(['Alto Risco'])[0]] + 
                                     prediction_proba[target_encoder.transform(['Médio Risco'])[0]]) * 100
                    st.metric("Probabilidade de Defasagem", f"{prob_defasagem:.1f}%")
                
                # Gráfico de probabilidades
                st.markdown("---")
                st.markdown("### 📊 Distribuição de Probabilidades")
                
                prob_df = pd.DataFrame({
                    'Classe': target_encoder.classes_,
                    'Probabilidade': prediction_proba * 100
                }).sort_values('Probabilidade', ascending=False)
                
                fig_prob = px.bar(prob_df, x='Classe', y='Probabilidade',
                                 title='Probabilidade por Classe de Risco',
                                 labels={'Probabilidade': 'Probabilidade (%)'},
                                 color='Probabilidade',
                                 color_continuous_scale='RdYlGn_r')
                
                st.plotly_chart(fig_prob, use_container_width=True)
                
                # Recomendações
                st.markdown("---")
                st.markdown("### 💡 Recomendações")
                
                if risk_class == 'Alto Risco':
                    st.error("""
                    **⚠️ Atenção Urgente Necessária**
                    
                    - Acompanhamento psicopedagógico intensivo
                    - Reforço escolar imediato
                    - Avaliação psicossocial
                    - Reunião com família
                    """)
                elif risk_class == 'Médio Risco':
                    st.warning("""
                    **⚠️ Monitoramento Recomendado**
                    
                    - Acompanhamento regular
                    - Atividades de engajamento
                    - Apoio pedagógico
                    - Avaliação trimestral
                    """)
                else:
                    st.success("""
                    **✅ Manutenção do Desempenho**
                    
                    - Continuar acompanhamento regular
                    - Incentivar participação em atividades
                    - Reconhecer progressos
                    - Avaliação semestral
                    """)
                
            except Exception as e:
                st.error(f"Erro na predição: {e}")
                st.info("Verifique se todos os campos foram preenchidos corretamente.")

# ==================== ABA 3: DASHBOARD ANALÍTICO ====================
with tab3:
    st.header("📊 Dashboard Analítico - Explorador de Dados")
    
    # ========== FILTROS ==========
    st.markdown("### 🔎 Filtros de Segmentação")
    
    with st.expander("Clique para abrir os filtros", expanded=True):
        f_col1, f_col2, f_col3, f_col4 = st.columns(4)
        
        with f_col1:
            if 'Fase' in df.columns:
                fases_disponiveis = sorted(df['Fase'].unique())
                sel_fase = st.multiselect("Fase do Programa", fases_disponiveis, default=fases_disponiveis)
            else:
                sel_fase = None
        
        with f_col2:
            if 'Gênero' in df.columns:
                sel_genero = st.multiselect("Gênero", df['Gênero'].unique(), default=df['Gênero'].unique())
            else:
                sel_genero = None
        
        with f_col3:
            if 'Atingiu PV' in df.columns:
                sel_pv = st.multiselect("Atingiu Ponto de Virada", df['Atingiu PV'].unique(), 
                                       default=df['Atingiu PV'].unique())
            else:
                sel_pv = None
        
        with f_col4:
            if 'Ano ingresso' in df.columns:
                anos = sorted(df['Ano ingresso'].unique())
                sel_ano = st.multiselect("Ano de Ingresso", anos, default=anos)
            else:
                sel_ano = None
    
    # Aplicar filtros
    df_filtered = df.copy()
    
    if sel_fase is not None and 'Fase' in df.columns:
        df_filtered = df_filtered[df_filtered['Fase'].isin(sel_fase)]
    
    if sel_genero is not None and 'Gênero' in df.columns:
        df_filtered = df_filtered[df_filtered['Gênero'].isin(sel_genero)]
    
    if sel_pv is not None and 'Atingiu PV' in df.columns:
        df_filtered = df_filtered[df_filtered['Atingiu PV'].isin(sel_pv)]
    
    if sel_ano is not None and 'Ano ingresso' in df.columns:
        df_filtered = df_filtered[df_filtered['Ano ingresso'].isin(sel_ano)]
    
    st.markdown("---")
    
    # ========== KPIs ==========
    if len(df_filtered) == 0:
        st.warning("⚠️ Nenhum dado encontrado com os filtros selecionados.")
    else:
        st.markdown("### 📈 Indicadores Principais (KPIs)")
        
        kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
        
        with kpi1:
            st.metric("Total de Alunos", len(df_filtered))
        
        with kpi2:
            if 'IDA' in df_filtered.columns:
                st.metric("IDA Médio", f"{df_filtered['IDA'].mean():.2f}")
        
        with kpi3:
            if 'IEG' in df_filtered.columns:
                st.metric("IEG Médio", f"{df_filtered['IEG'].mean():.2f}")
        
        with kpi4:
            if 'INDE 22' in df_filtered.columns:
                st.metric("INDE Médio", f"{df_filtered['INDE 22'].mean():.2f}")
        
        with kpi5:
            if 'IAN' in df_filtered.columns:
                pct_risco = (df_filtered['IAN'] < 5).sum() / len(df_filtered) * 100
                st.metric("% em Risco (IAN<5)", f"{pct_risco:.1f}%")
        
        st.markdown("---")
        
        # ========== VISUALIZAÇÕES ==========
        st.markdown("### 📊 Análise Visual dos Indicadores")
        
        # Linha 1: Distribuição e Evolução
        row1_col1, row1_col2 = st.columns([1, 2])
        
        with row1_col1:
            st.markdown("#### Distribuição por Fase")
            if 'Fase' in df_filtered.columns:
                fase_dist = df_filtered['Fase'].value_counts().sort_index()
                fig_fase = px.bar(x=fase_dist.index, y=fase_dist.values,
                                 labels={'x': 'Fase', 'y': 'Número de Alunos'},
                                 title='Alunos por Fase do Programa')
                st.plotly_chart(fig_fase, use_container_width=True)
        
        with row1_col2:
            st.markdown("#### Evolução dos Indicadores por Fase")
            if 'Fase' in df_filtered.columns:
                indicadores = ['IDA', 'IEG', 'IPV']
                indicadores_disponiveis = [i for i in indicadores if i in df_filtered.columns]
                
                if indicadores_disponiveis:
                    evolucao = df_filtered.groupby('Fase')[indicadores_disponiveis].mean().reset_index()
                    
                    fig_evolucao = go.Figure()
                    for ind in indicadores_disponiveis:
                        fig_evolucao.add_trace(go.Scatter(
                            x=evolucao['Fase'],
                            y=evolucao[ind],
                            mode='lines+markers',
                            name=ind,
                            line=dict(width=3),
                            marker=dict(size=8)
                        ))
                    
                    fig_evolucao.update_layout(
                        title='Evolução dos Indicadores Principais',
                        xaxis_title='Fase',
                        yaxis_title='Valor Médio',
                        hovermode='x unified'
                    )
                    
                    st.plotly_chart(fig_evolucao, use_container_width=True)
        
        st.markdown("---")
        
        # Linha 2: Correlações e Distribuições
        row2_col1, row2_col2 = st.columns(2)
        
        with row2_col1:
            st.markdown("#### Correlação entre Indicadores")
            indicadores_corr = ['IAN', 'IDA', 'IEG', 'IAA', 'IPS', 'IPV']
            indicadores_corr_disp = [i for i in indicadores_corr if i in df_filtered.columns]
            
            if len(indicadores_corr_disp) > 1:
                corr_matrix = df_filtered[indicadores_corr_disp].corr()
                
                fig_corr = px.imshow(corr_matrix,
                                    text_auto='.2f',
                                    aspect='auto',
                                    color_continuous_scale='RdBu_r',
                                    title='Matriz de Correlação')
                
                st.plotly_chart(fig_corr, use_container_width=True)
        
        with row2_col2:
            st.markdown("#### Relação IEG vs IDA")
            if 'IEG' in df_filtered.columns and 'IDA' in df_filtered.columns:
                fig_scatter = px.scatter(df_filtered, x='IEG', y='IDA',
                                        opacity=0.6,
                                        title='Engajamento vs Desempenho',
                                        labels={'IEG': 'Engajamento (IEG)', 
                                               'IDA': 'Desempenho (IDA)'})
                
                st.plotly_chart(fig_scatter, use_container_width=True)
        
        st.markdown("---")
        
        # Insights textuais
        st.markdown("### 💡 Insights Principais")
        
        insight_col1, insight_col2, insight_col3 = st.columns(3)
        
        with insight_col1:
            st.info("""
            **📊 Engajamento e Desempenho**
            
            Existe uma correlação positiva moderada (0.56) entre IEG e IDA, 
            indicando que alunos mais engajados tendem a ter melhor desempenho.
            """)
        
        with insight_col2:
            st.success("""
            **🎯 Ponto de Virada**
            
            O IPV tem forte correlação com IDA (0.62) e IEG (0.59), 
            mostrando que o ponto de virada está relacionado ao desempenho e engajamento.
            """)
        
        with insight_col3:
            st.warning("""
            **⚠️ Adequação de Nível**
            
            O IAN tem correlação fraca com outros indicadores, 
            sugerindo que a defasagem é um fator independente que precisa atenção especial.
            """)

# ==================== RODAPÉ ====================
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>📚 Desenvolvido para a <b>Associação Passos Mágicos</b> | Datathon PEDE - Fase 5</p>
    <p>FIAP Pós-Tech em Data Analytics | 2024</p>
</div>
""", unsafe_allow_html=True)
