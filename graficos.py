import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

#criando grafico e mapa de receitas por estado 

grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat = 'lat',
    lon = 'lon',
    scope = 'south america',
    size = 'Preço',
    template = 'seaborn',
    hover_name = 'Local da compra',
    hover_data = {'lat': False, 'lon': False},
    title = 'Receita por Estado'
)

grafico_rec_mensal = px.line(
    df_rec_mensal,
    x = 'Mes',
    y = 'Preço',
    markers = True,
    range_y = (0, df_rec_mensal.max()),
    color = 'Ano',
    line_dash= 'Ano',
    title = 'Receita Mensal'  
)

#atualizando o nome do grafico de receita mensal

grafico_rec_mensal.update_layout(yaxis_title = 'Receita') 

#grafico top receita por estado filtrando pelo 5 primeieros 

grafico_rec_estado = px.bar(
    df_rec_estado.head(5),
    x = 'Local da compra',
    y = 'Preço',
    text_auto = True,
    title = 'Top Rceita por Estado'
)
#top categorias com maior receira
grafico_rec_categoria = px.bar(
    df_rec_categoria.head(5),
    text_auto = True,
    title = 'Top Categorias com Maior Receita'
)

#grafico de vendedores
grafico_rec_vendedores = px.bar(
    df_vendedores[['sum']].sort_values('sum', ascending=False).head(5),
    x = 'sum',
    y = df_vendedores[['sum']].sort_values('sum', ascending=False).head(5).index,
    text_auto = True,
    title = 'Top 5 Vendedores'
)

grafico_vendas_vendedores = px.bar(
    df_vendedores[['count']].sort_values('count' , ascending=False).head(5),
    x = 'count',
    y = df_vendedores[['count']].sort_values('count' , ascending=False).head(5).index,
    text_auto = True,
    title = 'Top Cinco vendedores por venda'
)
