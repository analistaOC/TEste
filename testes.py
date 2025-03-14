import streamlit as st
import plotly.express as px
import pandas as pd

# Criar um dataframe simples para o exemplo
df = pd.DataFrame({
    "Categoria": ["A", "B", "C", "D"],
    "Valor": [10, 20, 15, 30],
    "Mês": ["Jan", "Feb", "Mar", "Apr"]
})

# Função para criar o gráfico baseado na seleção
def criar_grafico(categoria):
    # Filtra os dados com base na categoria escolhida
    df_filtrado = df[df['Categoria'] == categoria]
    fig = px.bar(df_filtrado, x='Mês', y='Valor', title=f'Valores de {categoria}')
    return fig

# Adicionar título ao app Streamlit
st.title("Exemplo de Gráfico com Dropdown")

# Criar o dropdown para selecionar a categoria
opcao = st.selectbox("Escolha a Categoria", df['Categoria'].unique())

# Gerar o gráfico com base na categoria escolhida
fig = criar_grafi
