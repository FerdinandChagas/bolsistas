Para rodar o projeto é necessário instalar o Python. 
Após instalar crie o ambiente virtual:

python -m venv venv

Logo em seguida instale as bibliotecas necessárias:

pip install django
pip install djangorestframework
pip install drf-extensions

A credeciais do super usuário: admin/admin

Após realizar alterações nos modelos para registrar as atualizações 
no banco execute o comando:

python manage.py makemigrations

Para aplicar as mudanças:

python manage.py migrate

Para rodar o servidor da aplicação:

python manage.py runserver