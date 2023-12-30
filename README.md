# Testes de API com Playwright em Python

## Introdução
Este projeto demonstra como utilizar o Playwright em Python para a automação de teste de APIs. O foco está na criação de testes automatizados que validam o funcionamento de uma API simulada, verificando a integridade de suas respostas e o status dos códigos retornados.

## Pré-requisitos
Antes de começar, certifique-se de ter o Python instalado em seu sistema. Este projeto foi testado com Python versão 3.11.6. Outras dependências incluem:

* Playwright
* Pytest
* Pytest-html (para relatórios de testes)

## Instalação
Para configurar o ambiente do projeto, siga os passos abaixo:

1. Clone o repositório
````
git clone [URL do Repositório]
````

2. Navegue até o diretório do projeto:
````
cd [Nome do Diretório]
````

3. Instale as dependências:
````
pip install playwright pytest pytest-html
````

4. Instale o Playwright:
````
playwright install
````



## Estrutura do Projeto
A estrutura do projeto é a seguinte:
- projeto_zappts/
- pojos/
 - __init__.py
 - user.py
- tests/
 - __init__.py
 - test_user_creation.py
 - test_user_details.py
 - test_user_update.py
 - test_user_delete.py
 - test_user_listing.py
 - test_user_authentication.py
- utils/ (se necessário)
 - __init__.py

## Uso
Para executar todos os testes, utilize o seguinte comando:
````
pytest tests
````

Para gerar um relatório em HTML dos testes:
````
pytest tests --html=report.html
````

Para gerar um relatório em HTML dos testes com logs detalhados, execute:
````
pytest tests --html=report.html --log-cli-level=INFO
````
**OBS:**Este comando irá gerar um relatório HTML dos resultados dos testes  e incluirá logs detalhados no nível de informação, facilitando o diagnóstico de eventuais falhas no testes.

## Execução dos Testes
Os testes são escritos usando a biblioteca Playwright e podem ser executados com o Pytest. Os testes verificam várias funcionalidades da API, incluindo a criação, atualização, exclusão e listagem de usuários, bem como testes de autenticação.

## Geração de Relatórios
O plugin `pytest-html` é utilizado para gerar relatórios detalhados em HTML. Estes relatórios incluem informações sobre os testes executados, seus resultados, quaisquer falhas encontradas e logs capturados durante a execução dos testes.



