# Gerenciamento de Palestras

## Tecnologias Utilizadas:
- Python 3.6.9
- Flask 1.1.1

## Instalação:

### Ambiente Linux: 
Para podermos rodar o projeto, precisamos primeiro criar um ambiente virtual para instalar todas as dependências e para isso utiliaremos o virtualenv.

Utilize o seguinte comando para instalar o virtualenv caso não o tenha instalado:

```sudo apt install virtualenv -y```

Com o virtualenv instalado, podemos criar o ambiente virtual e instalar os pacotes. No diretório do projeto utilize o seguinte comando:

```virtualenv -p python3 --clear venv```

Utilize os seguintes comandos para entrar e sair do ambiente virtual:

```
source venv/bin/activate # ativar o ambiente virtual
deactivate 				 # desativar o ambiente virtual

```

Com o ambiente virtual ativo, utilize o comando abaixo para installar as dependencias:

``` pip install -r requirements.txt```

## Uso:

Para iniciar o servidor, da pasta raiz do projeto, podemos acessar a pasta 'src' e usar o seguinte comando:

```flask run```

Caso este comando não funcione, podemos inicia-lo através do próprio python:

```python app.py```

Desta forma o servidor estará funcionando e disponível para acesso no link: http://127.0.0.1:5000/
## Endpoints

Basta enviar o payload via POST para o endpoit: 

- http://127.0.0.1:5000/api/v1/lecture_manager

Para testar a aplicação sem a necessidade de instalação, utilize o postman ou insomnia para fazer a requisição neste endpoint:

- https://lecture-manager.herokuapp.com/api/v1/lecture_manager

### Exemplo de Payload:
```json
{
    "data":[
        "Writing Fast Tests Against Enterprise Rails 60min",
        "Overdoing it in Python 45min",
        "Lua for the Masses 30min",
        "Ruby Errors from Mismatched Gem Versions 45min",
        "Common Ruby Errors 45min",
        "Rails for Python Developers lightning",
        "Communicating Over Distance 60min",
        "Accounting-Driven Development 45min",
        "Woah 30min",
        "Sit Down and Write 30min",
        "Pair Programming vs Noise 45min",
        "Rails Magic 60min",
        "Ruby on Rails: Why We Should Move On 60min",
        "Clojure Ate Scala (on my project) 45min",
        "Programming in the Boondocks of Seattle 30min",
        "Ruby vs. Clojure for Back-End Development 30min",
        "Ruby on Rails Legacy App Maintenance 60min",
        "A World Without HackerNews 30min",
        "User Interface CSS in Rails Apps 30min"
    ]
}
```

## Testes

Os testes foram criados sob o framework 'pytest'. Para roda-los basta entrar na pasta 'tests' e utilizar o comando `pytest` no terminal.

## Autores:

- [Luiz Henrique Longo](https://www.linkedin.com/in/luizhenriquelongo/)
