# FlipOn
Projeto vaga de estágio

## Criar um diretório para o projeto e instalar um ambiente virtual pyhton dentro:

1. mkdir project
2. cd project
3. python3 -m venv venv
4. source venv/bin/activate

## Criar um diretório raiz e clonar o repositório:
1. mkdir src
2. cd src
3. git clone https://github.com/RaphaelLima123/FlipOn.git

## Instalar as dependências:
1. pip install -r requirements/local.txt

## Rodar as migrações e em seguida o server:
1. python manage.py migrate
2. python manage.py runserver
