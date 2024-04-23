# QuantumBenchmarkingDB
## Setup Steps
1. Install project requirements (virtual environment suggested)
    ```bash
    pip install -r /requirements.txt
    ```
2. Create tables associated with benchmarking app in SQL database
    ```bash
    python3 /benchmarking_project/manage.py makemigrations benchmarks
    python3 /benchmarking_project/manage.py migrate
    ```
3. Create a superuser for Django App
    ```bash
    python3 /benchmarking_project/manage.py createsuperuser
    ```
    - Will ask for Username, Email, and Password
4. If desired to use an existing .sqlite3 file, place .sqlite3 file within `/benchmarking_project/` directory
5. Launch Django Server
    ```bash
    python3 benchmarking_project/manage.py runserver
    ```
## Django Admin Site
### Overview
Django automatically provides a way to manipulate table data through its admin interface. "It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site" ([DjangoProject](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/)). 

To make newly created models accessible within the admin interface, they must be registered to the admin site using the `admin.py` file within their project directory (for those unaware of how Django apps are structured, see [this guide](https://medium.com/django-unleashed/django-project-structure-a-comprehensive-guide-4b2ddbf2b6b8))
### Accessing Site
To login to the site, open the `/admin` URL and enter the credentials for your superuser. Once inside, you can manipulate the metadata associated with the models registered to be accessible within the admin site.