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
def trata_dados(input):<br/>
    return " ".join(input.split()).replace('> <', '><')<br/>
com a função criada passe o objeto pela função com o seguinte comando:<br/>    

result = trata_dados(result)<br/>

caso queira ver o resultado do tratamento é só fazer um prit(result)

com os tratamento finalizado é hora de criar o objeto BeautifulSoup para interpretar o HTML com o seguinte comando<br/>

soup =  BeautifulSoup(result, 'lxml')<br/>
#### OBS caso o comando acima não funcione execute o proximo comando
soup = BeautifulSoup(result, "result.parser")<br/>

com o obejto criado podemos executar o seguinte comando para organizar as TAGS HTMl<br/>
print(soup.prettify())<br/>

agora ficara mais facil identificar os dados que iremos coletar da pagina WEB<br/>
nessa etapa voce terá que encontrar os dados e verificar se oo mesmo tem um identificador único que ajudara a localiza-lo<br/>
por exemplo, o comando a segui irá trazer todos os dados da TAB td onde {'width': '100'}<br/>

infos = soup.findAll('td', {'width': '100'})<br/>

Após executar o comando acima a variavel "infos" está com os dados armazenados. agora iremos criar uma lista onde iremos armazezar os dados coletados separadamente. Para isso iremos percorrer a variavel com o laço FOR com o seguinte comando:<br/>

for info in infos:<br/>
    if info.getText() != 'Não codificada por logradouros':<br/>
        info_list.append(info.getText())<br/>

#### atenção a identação do código

caso queira visualizar a list façã o seguinte comando :<br/>
info_list
![capituraLista](https://user-images.githubusercontent.com/48107412/135949847-ef246aca-6f46-46a4-94b0-1ba9a1d7a3ac.png)
