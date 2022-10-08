# User_Login_System-Django

This is a simple User login system build with django's default user model

## Run Locally
You will need to install Python on  you system. Head over to https://www.python.org/downloads/ to download python.
(Dont Forget to Tick Add to Path while installing Python)

Once you have downloaded Python on your system, 
run the following command inside your terminal

```bash
  git clone https://github.com/milan-sony/User_Login_System-Django.git
```

Then go to the project folder

```bash
  cd User-Login_System-Django
```

(This is optional, but strongly recommended) Make a virtual environment

```bash
  python -m venv venv
```

Activate the virtual environment

```bash
  venv/Scripts/activate
```

If error occurs when activating virtual environment, run the following command

```bash
  Set-ExecutionPolicy Unrestricted
```

Install the dependencies needed for this project

```bash
  pip install -r requirement.txt
```

Now minimize the terminal and make a database on MySQL named authentication

Once you have created the database, open the project folder inside a code editor (if you don't have a code editor install one). Then open the file named .env.example and do as per mentioned  on that file

After creating the .env file, head back to the terminal and make migrations

```bash
  python manage.py makemigrations
```

This will create all the migration files (database migrations) required to run this project

Now apply this migrations

```bash
  python manage.py migrate
```

Then run the server

```bash
  python manage.py runserver
```

Once the server is hosted click on the link http://127.0.0.1:8000/
