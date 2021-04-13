# FlipOn
Projeto vaga de estágio

## Usuário Linux
## Criar um diretório para o projeto e instalar um ambiente virtual pyhton dentro:
```
mkdir project
cd project
python3 -m venv venv
source venv/bin/activate
```


## Criar um diretório raiz e clonar o repositório:
```
mkdir src
cd src
git clone https://github.com/RaphaelLima123/FlipOn.git .
```

## Instalar as dependências:
```
pip install -r requirements/local.txt
```

## Rodar as migrações e em seguida o server:
```
python manage.py migrate
python manage.py runserver
```

## Usuário Windows
## Criar um diretório para o projeto e instalar um ambiente virtual pyhton dentro:
```
mkdir project
cd project
python -m venv venv
cd venv/scripts/
./activate
cd ../..
```
## Clonar o repositório:
```
git clone https://github.com/RaphaelLima123/FlipOn.git
```

## Instalar as dependências:
```
cd FlipOn
pip install -r requirements/local.txt
```

## Rodar as migrações e em seguida o server:
```
python manage.py migrate
python manage.py runserver
```
