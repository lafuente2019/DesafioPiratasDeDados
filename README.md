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

Apos a import das bibliotecas  crie uma varialvel para guardar a url\ 
url = 'https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'\
