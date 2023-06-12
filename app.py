import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('relatorio-sisref-sad.csv')

st.sidebar.title("Configurações de Exibição")

mes = st.sidebar.radio("Selecione um mês", ['January', 'February'])

st.title("Atividade - SISREF")

st.subheader("Visualização dos dados")
st.dataframe(data)

#Primeiramente trazer alguns dados separados por mês
st.header("Dados por mês")

filtro = data[data['Mes_da_Refeicao'] == mes]

st.subheader("Refeições por curso")
contagem_cursos = filtro['Curso'].value_counts()
plt.figure(figsize=(10, 8))
plt.pie(contagem_cursos.values, labels=contagem_cursos.index, autopct='%1.1f%%')
plt.title("Contagem de cursos")
st.pyplot(plt)

st.subheader("Refeições por dia")
refeicoes_por_dia = filtro.groupby('Data_da_Refeicao')['Refeicao'].count().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x=refeicoes_por_dia['Data_da_Refeicao'], y=refeicoes_por_dia['Refeicao'])
plt.xlabel("Data da Refeição")
plt.ylabel("Contagem de Refeições")
plt.title("Contagem de refeições por dia")
plt.xticks(rotation=45)
st.pyplot(plt)


#Trazer dados gerais
st.header("Dados Gerais")

st.subheader("Refeições por mês")
refeicoes_por_mes = data['Mes_da_Refeicao'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=refeicoes_por_mes.index, y=refeicoes_por_mes.values)
plt.xlabel("Mês")
plt.ylabel("Número de refeições")
st.pyplot(plt)

st.subheader("Porcentagem de comparecimento")
comparecimento = data['Compareceu'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(comparecimento.values, labels=comparecimento.index, autopct='%1.1f%%')
plt.title("Comparecimento")
st.pyplot(plt)