import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from config.database import fetch_data
from src.data_generator import generate_synthetic_data

# Configuração da página
st.set_page_config(page_title="FarmTech Solutions", layout="wide")

# Carregar Modelo
@st.cache_resource
def load_model():
    try:
        model = joblib.load('model.joblib')
        return model
    except:
        return None

model = load_model()

# Carregar Dados
@st.cache_data
def get_data():
    df = fetch_data()
    if df.empty:
        st.warning("Falha na conexão com o banco de dados ou banco vazio. Usando dados sintéticos para demonstração.")
        df = generate_synthetic_data(1000)
    return df

df = get_data()

# Barra Lateral
st.sidebar.title("FarmTech Solutions")
page = st.sidebar.radio("Navegação", ["Início", "Visualização de Dados", "Previsões", "Analytics"])

# Início
if page == "Início":
    st.title("🌱 FarmTech Solutions: Agricultura Inteligente")
    st.markdown("""
    Bem-vindo ao Dashboard da FarmTech Solutions. Esta aplicação utiliza Machine Learning para ajudar agricultores a otimizar suas colheitas.
    
    ### Funcionalidades:
    - **Visualização de Dados**: Explore os dados agrícolas.
    - **Previsões**: Preveja a produtividade da colheita com base nas condições do solo e clima.
    - **Analytics**: Visualize tendências e correlações.
    
    ### Stack Tecnológico:
    - **Python**: Lógica principal.
    - **Oracle Database**: Armazenamento de dados.
    - **Scikit-Learn**: Machine Learning.
    - **Streamlit**: Interface de Usuário.
    """)

# Visualização de Dados
elif page == "Visualização de Dados":
    st.title("📊 Dados Agrícolas")
    st.dataframe(df)
    
    st.subheader("Estatísticas dos Dados")
    st.write(df.describe())

# Previsões
elif page == "Previsões":
    st.title("🔮 Previsão de Produtividade")
    
    if model:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            soil_humidity = st.slider("Umidade do Solo (%)", 0.0, 100.0, 50.0)
            ph_level = st.slider("Nível de pH", 0.0, 14.0, 6.5)
            temperature = st.slider("Temperatura (°C)", 0.0, 50.0, 25.0)
            
        with col2:
            rainfall = st.slider("Chuva (mm)", 0.0, 300.0, 100.0)
            nitrogen = st.slider("Nitrogênio", 0.0, 100.0, 50.0)
            
        with col3:
            phosphorus = st.slider("Fósforo", 0.0, 100.0, 50.0)
            potassium = st.slider("Potássio", 0.0, 100.0, 50.0)
            
        input_data = pd.DataFrame({
            'soil_humidity': [soil_humidity],
            'ph_level': [ph_level],
            'temperature': [temperature],
            'rainfall': [rainfall],
            'nitrogen': [nitrogen],
            'phosphorus': [phosphorus],
            'potassium': [potassium]
        })
        
        if st.button("Prever Produtividade"):
            prediction = model.predict(input_data)[0]
            st.success(f"Produtividade Prevista: {prediction:.2f}")
            
            # Recomendações
            st.subheader("Recomendações")
            
            recommendations = []
            
            # Análise de Umidade do Solo
            if soil_humidity < 40:
                recommendations.append("💧 **Umidade do Solo Baixa**: Considere irrigação imediata para evitar estresse hídrico nas plantas.")
            elif soil_humidity > 80:
                recommendations.append("⚠️ **Umidade do Solo Alta**: Garanta drenagem adequada para evitar apodrecimento das raízes.")
            
            # Análise de pH
            if ph_level < 5.5:
                recommendations.append("🧪 **Solo Ácido**: Adicione calcário para corrigir o pH e melhorar a disponibilidade de nutrientes.")
            elif ph_level > 7.5:
                recommendations.append("🧪 **Solo Alcalino**: Considere adicionar enxofre ou matéria orgânica para reduzir o pH.")
            
            # Análise de Temperatura
            if temperature < 15:
                recommendations.append("🌡️ **Temperatura Baixa**: Temperatura abaixo do ideal pode retardar o crescimento. Considere proteção térmica ou aguardar período mais quente.")
            elif temperature > 35:
                recommendations.append("🌡️ **Temperatura Alta**: Calor excessivo pode estressar as plantas. Aumente a irrigação e considere sombreamento.")
            
            # Análise de Chuva
            if rainfall < 75:
                recommendations.append("☔ **Precipitação Insuficiente**: Nível de chuva baixo. Implemente sistema de irrigação suplementar.")
            elif rainfall > 180:
                recommendations.append("🌧️ **Precipitação Excessiva**: Chuva em excesso pode causar lixiviação de nutrientes. Monitore drenagem e considere adubação de cobertura.")
            
            # Análise de Nitrogênio (N)
            if nitrogen < 30:
                recommendations.append("🌿 **Nitrogênio Baixo**: Aplique fertilizantes nitrogenados (ureia, sulfato de amônio) para promover crescimento vegetativo.")
            elif nitrogen > 80:
                recommendations.append("🌿 **Nitrogênio Alto**: Excesso de nitrogênio pode causar crescimento excessivo de folhas. Reduza aplicação.")
            
            # Análise de Fósforo (P)
            if phosphorus < 25:
                recommendations.append("🌾 **Fósforo Baixo**: Adicione superfosfato ou MAP para fortalecer raízes e melhorar floração.")
            elif phosphorus > 75:
                recommendations.append("🌾 **Fósforo Alto**: Níveis adequados. Mantenha monitoramento regular.")
            
            # Análise de Potássio (K)
            if potassium < 30:
                recommendations.append("🍃 **Potássio Baixo**: Aplique cloreto de potássio (KCl) para melhorar resistência a doenças e qualidade dos frutos.")
            elif potassium > 80:
                recommendations.append("🍃 **Potássio Alto**: Níveis adequados. Continue com manejo atual.")
            
            # Exibir recomendações
            if recommendations:
                for rec in recommendations:
                    st.info(rec)
            else:
                st.success("✅ **Condições Ideais**: Todos os parâmetros estão dentro da faixa ótima!")
            
            # Análise geral da produtividade
            st.subheader("Análise da Produtividade")
            if prediction < 100:
                st.warning(f"📉 **Produtividade Baixa** ({prediction:.2f}): Revise as recomendações acima e ajuste os parâmetros conforme necessário.")
            elif prediction < 150:
                st.info(f"📊 **Produtividade Moderada** ({prediction:.2f}): Boas condições, mas há espaço para otimização.")
            else:
                st.balloons()
                st.success(f"🚀 **Excelente Produtividade** ({prediction:.2f}): Condições ótimas para alta produtividade!")
    else:
        st.error("Modelo não encontrado. Por favor, treine o modelo primeiro.")

# Analytics
elif page == "Analytics":
    st.title("📈 Análise & Insights")
    
    st.subheader("Mapa de Calor de Correlação")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
    
    st.subheader("Produtividade vs Fatores")
    factor = st.selectbox("Selecione o Fator", df.columns.drop('crop_yield'))
    
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=df, x=factor, y='crop_yield', ax=ax2)
    st.pyplot(fig2)
