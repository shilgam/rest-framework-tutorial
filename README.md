# rest-framework-tutorial

[![Codeship Status for shilgam/rest-framework-tutorial](https://app.codeship.com/projects/a995cb20-f548-0136-e8d2-7e4b83070a34/status?branch=master)](/projects/320832)

## Usage

1. Clone the repo

1. Build the app:

        $ docker-compose up --build

1. Migrate the database schema

        $ docker-compose exec web python manage.py migrate

1. Run the app in a local server:

        $ python manage.py runserver

1. Go to http://127.0.0.1:8000/snippets in browser. Or run in terminal:

        $ docker-compose exec web http GET http://127.0.0.1:8000/snippets/2.json  # JSON format
        $ docker-compose exec web http GET http://127.0.0.1:8000/snippets/2.api  # API format
        $ docker-compose exec web http POST http://127.0.0.1:8000/snippets.json code="print('hello!')"  # create new snippet

1. Run the test suite

        $ docker-compose exec web python manage.py test
