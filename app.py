import streamlit as st
import pandas as pd
import numpy as np

# Configurando o título do dashboard
st.title('Exemplo de Dashboard com Duas Colunas e Galeria de Gráficos')

# Dados de exemplo
data = pd.DataFrame({
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valores': [4, 7, 1, 8]
})

# Layout de duas colunas
col1, col2 = st.columns(2)

# Primeira coluna
with col1:
    st.header('Coluna 1')
    st.subheader('Gráfico de Barras')
    
    st.bar_chart(data.set_index('Categoria'))

    st.subheader('Gráfico de Linhas')
    
    st.line_chart(data.set_index('Categoria'))

# Segunda coluna
with col2:
    st.header('Coluna 2')
    st.subheader('Gráfico de Dispersão')
    
    st.write("**Simulação de gráfico de dispersão**")
    st.write(data)

    st.subheader('Gráfico de Pizza')
    
    st.write("**Simulação de gráfico de pizza**")
    st.write(data)

# Seção de Galeria de Gráficos
st.header('Galeria de Gráficos')

gallery_col1, gallery_col2 = st.columns(2)

# Primeiro gráfico da galeria
with gallery_col1:
    st.subheader('Histograma')
    
    hist_data = np.random.randn(1000)
    st.hist(hist_data)

# Segundo gráfico da galeria
with gallery_col2:
    st.subheader('Box Plot')

    box_data = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])
    st.box_chart(box_data)
