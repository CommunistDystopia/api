# Communist Dystopia [API]

## Requirements:

* Python 3.7+
* Django 3.1 + Django REST Framework
* PostgreSQL 12.3+

## Local [.env ENVIROMENT=LOCAL]

### Docker setup

* Run the container.

        $ docker-compose up
        
### Manual setup

* Install the dependencies for the pip packages.

        $ apt-get install -y python3-dev python3-venv build-essential libpq-dev
        
* Prepare the virtual enviroment.

        $ python3 -m venv env
        $ source env/bin/activate

* Clone the project.

        $ git clone https://github.com/CommunistDystopia/api.git

* Install the dependencies.

        $ pip install -r api/requirements.txt

* Config the local settings for the database. (The default settings are used for the Docker container)

        $ vim api/CD/settings/local.py
        $ nano api/CD/settings/local.py

* Run migrations, create a superuser and run the server.

        $ python api/manage.py migrate
        $ python api/manage.py createsuperuser
        $ python api/manage.py runserver

## Production [.env ENVIROMENT=PRODUCTION]

*Please, be aware that this is just an example guide to get your project running outside of the local enviroment.*

* Set the enviroment variables (can be done in the docker-compose file/.env/...)

```
ENVIROMENT=production
DJANGO_SECRET_KEY=${your key here}
ALLOWED_HOSTS=${your host here}
DATABASE_NAME=${your db name here}
DATABASE_USER=${your db user here}
DATABASE_PASSWORD=${your db password here}
DATABASE_HOST=${your db host here}
DATABASE_PORT=${your db port here}
REFRESH_TOKEN_EXPIRE_SECONDS=${your oauth refresh token lifetime here}
ACCESS_TOKEN_EXPIRE_SECONDS=${your oauth access token lifetime here}
```

* Create a docker-compose-deploy.yml

> It's recommended to build and host your images on a repository.

```
version: '3.8'

services:
  app:
    image: ${your built image based on the Dockerfile in the root of this project}
    volumes:
    - static_data:/vol/web

  proxy:
    image: ${your built image based on the Dockerfile in the proxy/ folder}
    volumes:
    - static_data:/vol/static
    ports:
      - '80:8080'
    depends_on:
      - app

volumes:
  static_data:
```

* Modify the files above based on your hosting provider. (You can use different ports/folders if you want)

* Install docker and docker-compose.

* Time to run!

        $ docker-compose -f docker-compose-deploy.yml build 

## Author

* **Antonio Garcia** -  [lantoniogc](https://github.com/lantoniogc/)
