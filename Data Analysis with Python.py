#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa do varejo e tem milhares de clientes diferentes.
# 
# Com o objetivo de aumentar o faturamento e o lucro da sua empresa, a diretoria quer conseguir identificar quem é o cliente ideal para seus produtos, baseado no histórico de compras dos clientes.
# 
# Para isso, ela fez um trabalho de classificar os clientes com uma nota de 1 a 100. Só que agora, sobrou para você conseguir, a partir dessa nota, descobrir qual o perfil de cliente ideal da empresa.
# 
# Qual a profissão? Qual a idade? Qual a faixa de renda? E todas as informações que você puder analisar para dizer qual o cliente ideal da empresa.
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=share_link

# In[25]:


#passo a passo
# passo 1- importar a base de clientes

import pandas as pd
tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";") 

#procurar falhas na base de dados
#excluir coluna inútil
tabela = tabela.drop("Unnamed: 8",axis=1)
#para deletar mais de uma coluna por vez faça ["nome da coluna","nome da coluna",axis=valor]
    
# passo 2- visualizar a base de dados
    #entender as informações disponíveis -> (foram entendidas quando eu vi)
display(tabela) 


# In[45]:


#passo 3- tratamento de dados

#acertar informações reconhecidas de forma errada
tabela["Salário Anual (R$)"]= pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
                                         
#corrigir informações vazias
tabela=tabela.dropna()
print(tabela.info())     


# In[71]:


# passo 4- análise inicial -> entender as notas dos clientes
display(tabela.describe())


# passo 5- análise completa -> entender como cada caracteristicas impacta na nota
#cria gráficos
import plotly.express as px
for coluna in tabela.columns:
    grafico= px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg",text_auto="true",nbins=20)
    #exibe gráfico
    grafico.show()




# In[ ]:


# salario pouco afeta
# abaixo de 15 anos a media da nota é ruim
# areas de trabalho e artista tem a melhor performance e construção o pior
# 10 e 15 anos de experiencia obteve a melhor nota
# com familias não muito grandes ate 7 pessoas

