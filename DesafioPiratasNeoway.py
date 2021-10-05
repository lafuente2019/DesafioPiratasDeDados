#!/usr/bin/env python
# coding: utf-8

# # Desafio Piratas de Dados

# ### Nesta tarefa, você deve coletar dados de um site da Web e, em seguida, gravar os resultados em um arquivo

# Use a URL https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm ;
# Obtenha dados de pelo menos dois UFs. Quanto mais melhor;
# Colete todos os registros de cada UF;
# Cada registro deve conter no mínimo 3 campos: "localidade", "faixa de cep" e um "id" gerado. Não deixe registros duplicados em seu arquivo de saída;
# O formato de saída deve ser JSON

# In[108]:


#Primeiramente vamos importar as bibliotecas para fazer a requisição ao site dos correio.
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json


# In[109]:


#url de busca por UF dos correios
url = 'https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'

# criando variavel de input para pesquisar o UF desejado.
uf_input = {'UF': 'CE'}
    
# Agora que temos todos os requisitos necessarios já podemos fazer a requisição ao site WEB
request = Request(url, urlencode(uf_input).encode())
result = urlopen(request).read()
result = str(result)

#Caso queira visualizar os dados da requisição descomente o codigo abaixo 
#print(result)


# ## Começar a lapidar os dados

# In[110]:


#Tratando os caracteres especiais
result = bytes(result, 'utf-8').decode('unicode_escape')


# In[111]:


#criado uma função tirar os espaços 
def trata_dados(input):
    return " ".join(input.split()).replace('> <', '><')


# In[112]:


#Passando a pagina web na função de tratamento
result = trata_dados(result)

#Caso queira visualizar apos o tratamento descomente o codigo abaixo 
#result


# ## Agora vamos Utilizar o objeto BeautifulSoup para interpretar o HTML 
# 

# In[113]:


# Obs caso não tenha a biblioteca será necessario instalar com o seguinte comando: pip3 install beautifulsoup4
from bs4 import BeautifulSoup

soup =  BeautifulSoup(result, 'lxml')


# In[114]:


# vamos usar o comando prettify() para ficar melhor de visualizar as informaçoes e tags
print(soup.prettify())


# ### acessando o conteudo das tags

# In[115]:


#capiturando as informações da TAG td onde width é igual a 100
infos = soup.findAll('td', {'width': '100'})


# In[116]:


info_list = []

#adicionando as informações na lista onde getText() for diferente de 'Não codificada por logradouros'
for info in infos:
    if info.getText() != 'Não codificada por logradouros' and info.getText() != 'Codificado por logradouros' and info.getText() != 'Codificada por logradouros':
            info_list.append(info.getText())


# In[117]:


#lista com as localidade
info_list


# In[118]:


#capiturando as informações da TAG td onde width é igual a 80
faixa = soup.findAll('td', {'width': '80'})


# In[119]:


faixas = []
#adicionando as informaões na lista eliminando os espaços no começo e no fim 
for item in faixa:
    faixas.append(item.getText().strip())


# In[120]:


#lista com a faixas de CEP
faixas


# In[121]:


json_struct = {}
json_array = []

#percorrendo a lista faixa e adicionando as informaçoes em no dicionario e criando o ID 
for i in range(0, len(faixas)):
    json_struct['id'] = str(i+1)
    json_struct['faixa_de_cep'] = faixas[i]
    json_struct['localidade'] = info_list[i]

    #adicionando o dicionario a lista
    json_array.append(json_struct)

    json_struct = {}


# In[122]:


#Visualizando o dicionario criado com as informações.
json_array


# In[123]:


#Criando Arquivo JSON
with open("uf_CE.json", "a", encoding='utf8') as file:
    for j in json_array:
        file.write(json.dumps(j, ensure_ascii=False)+'\n')

