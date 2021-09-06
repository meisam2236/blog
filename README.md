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
To migrate apps:
```
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