## Usage

1. Clone the repo

1. Run the app in a local server:

        $ python manage.py runserver

1. Migrate the database schema

        $ python manage.py migrate

1. Go to http://127.0.0.1:8000/snippets in browser. Or run in terminal:

        $ http http://127.0.0.1:8000/snippets.json  # JSON suffix
        $ http http://127.0.0.1:8000/snippets.api   # Browsable API suffix

1. Run the test suite

        $ python manage.py test
