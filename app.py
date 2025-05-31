import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from graficos import grafico_map_estado, grafico_rec_mensal, grafico_rec_estado, grafico_rec_categoria, grafico_rec_vendedores, grafico_vendas_vendedores


#defininndo a pagina como wide para ficar mais alongada

st.set_page_config(layout='wide')

#titulo

st.title("Dasheboard de vendas :shopping_trolley:")

#Filtros de analises

st.sidebar.title('Filtro de Vendedores')

filtro_vendedor = st.sidebar.multiselect(
    'vendedores',
    df['Vendedor'].unique()
)

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]



#criando abas with trazendo os dados do arquivo json formatando preço com dados importados de utils

aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
with aba1:
    st.dataframe(df)
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
        #criando o grafico mapa receita por estado no app
        st.plotly_chart(grafico_map_estado, use_container_width=True)
        st.plotly_chart(grafico_rec_estado, use_container_width=True)

    with coluna2:
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))
        #criando o grafico de receita mensal
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)
        #criando grafico receita categoria
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)

# grafico de vendedores
with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_rec_vendedores)
    with coluna2:
        st.plotly_chart(grafico_vendas_vendedores)



