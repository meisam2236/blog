First you need to install python virtual environmnet:
```
pip install virtualenv==20.7.2
```
Now you should make one:
```
virtualenv venv
```
Activate the virtual environment on Windows:
```
cd venv/Scripts
acitvate.bat
```
Activate the virtual environment on other OS:
```
source venv/bin/activate
```
Now we install the requirements:
```
pip install -r requirements.txt
```
Create a .env file like this in the root directory:
```
POSTGRES_USER=admin
POSTGRES_PASSWORD=2Cq8tohQUvhYfh
POSTGRES_DB=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```
After installing docker on your machine, create volume and network and use docker-compose file:
```
docker volume create blog_postgresql
docker network create blog_network
docker-compose up -d
```
You can see your docker container using `docker ps -a`.

Also know that you can run sql commands in postgresql shell:
```
docker exec -it blog_postgresql psql -U admin -W postgres
```
Then enter the password from .env file.

To migrate apps:
```
python manage.py makemigrations website
python manage.py migrate
```
And to create an admin for the website:
```
python manage.py createsuperuser
```
Finally run the project:
```
python manage.py runserver
```
Visit the website in [localhost:8000](localhost:8000)


