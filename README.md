# Desafio Piratas de Dados

### Objetivo
Nesta tarefa, precisarei coletar dados de um site da Web e, em seguida, gravar os resultados em um arquivo.

- Use a URL https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm
- Obtenha dados de pelo menos dois UFs. Quanto mais melhor.
- Colete todos os registros de cada UF.
- Cada registro deve conter no mínimo 3 campos: "localidade", "faixa de cep" e um "id" gerado.
- Não deixe registros duplicados em seu arquivo de saída.
- O formato de saída deve ser JSON.

### Ferramentas utilizadas
- Linguagem de programação Python
- Visual studio code

### Requisitos para rodar o código
- Bibliotecas: BeautifulSoup, urlencode, Request, urlopen, json
- URL: https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm

### Instruções
1. Importe as bibliotecas necessárias:
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json


2. Defina a URL para a busca dos dados:
url = 'https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'

3. Crie um arquivo txt (uf.txt) com os UFs que você deseja pesquisar, separados por vírgula (por exemplo: SP, RJ, CE).

4. Execute o código abaixo para coletar os dados:

def trata_dados(input):
    return " ".join(input.split()).replace('> <', '><')

arquivos='arquivo/uf.txt'
ufs = []
with open(arquivos, 'r') as arquivo:
     uf = arquivo.readlines()

      # Percorre cada linha
     for linha in uf:
        # Remove os espaços em branco e quebra a linha em itens separados por vírgulas
        itens = linha.strip().split(",")
        
        # Adiciona os itens à lista de resultados
        ufs.extend(itens)


for resultado in ufs:
    #url de busca por UF dos correios
    url = 'https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
    # criando variavel de input para pesquisar o UF desejado.
    data = {'uf':resultado}
    # Agora que temos todos os requisitos necessarios já podemos fazer a requisição ao site WEB
    request = Request(url, urlencode(data).encode())
    result = urlopen(request).read()
    result = str(result)
    
    #Tratando os caracteres especiais
    result = bytes(result, 'utf-8').decode('unicode_escape')
    
    #Passando a pagina web na função de tratamento
    result = trata_dados(result)
    
    # Obs caso não tenha a biblioteca será necessario instalar com o seguinte comando: pip3 install beautifulsoup4
    soup = BeautifulSoup(result, 'html.parser')
        
    #acessando o conteudo das tags
    
    #capiturando as informações da TAG td onde width é igual a 100
    infos = soup.findAll('td', {'width': '100'})
    
    info_list = []
    
    #adicionando as informações na lista onde getText() for diferente de 'Não codificada por logradouros'
    for info in infos:
        if info.getText() != 'Não codificada por logradouros' and info.getText() != 'Codificado por logradouros' and info.getText() != 'Codificada por logradouros':
                info_list.append(info.getText())
    
    #capiturando as informações da TAG td onde width é igual a 80
    faixa = soup.findAll('td', {'width': '80'})
    
    faixas = []
    #adicionando as informaões na lista eliminando os espaços no começo e no fim 
    for item in faixa:
        faixas.append(item.getText().strip())
    
    
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
    
        UF = data['uf']

    #Criando Arquivo JSON
    with open(f"arquivo/{UF}.json", "w", encoding='utf8') as file:
        file.write(json.dumps(json_array, ensure_ascii=False)+'\n')
