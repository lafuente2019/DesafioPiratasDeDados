# Desafio Piratas de Dados
### Objetivo
Obtenha dados de pelo menos dois UFs. Quanto mais melhor; Colete todos os registros de cada UF; Cada registro deve conter no mínimo 3 campos: "localidade", "faixa de cep" e um "id" gerado. Não deixe registros duplicados em seu arquivo de saída; O formato de saída deve ser JSON
Use a URL https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm 


### Ferramentas utilizada

* Linguagem de programação Python
* Jupyter Notebook

### Requisitos para rodar o codigo
será necessario instalar algumas biblioteas e a URL para completar a case

* from bs4 import BeautifulSoup
* from urllib.parse import urlencode
* from urllib.request import Request, urlopen
* import json
*  https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm

Apos a import das bibliotecas  crie uma varialvel para guardar a url<br/>
url = 'https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'<br/>
Crie também  uma variavel de input para pesquisar o UF desejado.<br/>
uf_input = {'UF' : 'SP'}<br/>

com as variaveis criada é hora de fazer nossa querisição ao site WEB com os seguintes comandos:<br/>
request = Request(url, urlencode(uf_input).encode())<br/>
result = urlopen(request).read()<br/>
result = str(result)<br/>

caso queira visualizar o objeto que foi retornado basta fazer um print(result)<br/>
agora chegou a hora de começar a lapidar esses dados brutos até acharmos o tão esperado ouro <br/>

### Começar a lapidar os dados

vamos primeiro cuidart dos caracteres especiais com o seguinte comando:<br/>
result = bytes(result, 'utf-8').decode('unicode_escape')<br/>

após executar o comando vamos criar uma função para eliminar os espaços no objeto <br/>
def trata_dados(input):
    return " ".join(input.split()).replace('> <', '><')<br/>
