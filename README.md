# Weather App with OpenWeatherMap API

## install project
You can create the project as if you would do any django based project.
fork this repo.

```git
git clone https://github.com/Botir/openweather.git
```
Create your virtual environment

```git
python3.8 -m venv
source env/bin/activate
```
##### Install packages
```git
pip install -r requirements.txt
```

##### Create database
```sql
CREATE USER USER_NAME WITH PASSWORD 'USER_PASSWORD';
CREATE DATABASE DB_NAME OWNER USER_NAME;
```
##### Migrations 
```git
python manage.py migrate
```

Once done run this command to run the server.
```git
python manage.py runserver
```

##### Run Celery and Beat
 ```git
celery -A openweathermap beat --loglevel=info
celery -A openweathermap worker --loglevel=info
```


**Requirementes**

You will need an API of OpenWeatherMap. You can go on the site and sign up for the API and then can use it.


