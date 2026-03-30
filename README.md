# Readme - Documentação de Arquivos

# Documentação do Projeto
Este repositório contém as soluções desenvolvidas para o desafio técnico aplicado pela MXQ Insight, estruturado em três partes que abordam questões na linguagem Python, consultas SQL e consumo de API externa.

## Configuração
- Linguagem: Python 3.x
- Bibliotecas: requests e datetime
Obs: A biblioteca datetime é nativa do Python.

A biblioteca requests é necessário utilizar o comando:
- pip install requests

## Código

- `questao_1.py` - Script que contém a resolução do primeiro desafio da etapa 1 do teste
- `questao_2.py` - Script que contém a resolução do segundo desafio da etapa 1 do teste
- `questao_1` - Script que contém as queries desenvolvidas e testadas no SQLite da etapa 2
- `project_temperature.py` - Script que utiliza a biblioteca requests para buscar os dados climáticos da API do OpenMeteo e datetime para tratamento das informações de data

## Documentação
O projeto foi organizado conforme determinado as etapas específicas do teste, garantindo organização e legibilidade ao visualizar a estrutura dos códigos.

## Como executar
Para rodar qualquer arquivo do Python, utilize o terminal na raiz da pasta que o arquivo está, como exemplo:
- python `PARTE 1 - PYTHON/questao_1.py`

## Dicas
- Execução: Se certificar que está dentro da raíz do projeto para executar os scripts OU utilizar o caminho completo do arquivo
- Internet: O arquivo `project_temperature.py` requer conexão de internet ativa para realizar as requisições HTTP da API do OpenMeteo
- SQL: As queries da Parte 2 do teste foram utilizadas no SQLite
