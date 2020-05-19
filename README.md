# VulnerableApp
#### Vulnerable Flask-App

###### _Vulnerabilities_

1. ...

###### SETUP ON UBUNTU
- cloning and virtualenv setup
```bash
git clone https/github.com/MeresaG/vulnerableApp
cd vulnerableApp
python3 -m venv venv
source /venv/bin/activate 
# make sure its activated by running `which python` and `which pip`
cd vulnerableApp
```

- make sure to set environment variable before `flask run`
```bash
export FLASK_APP=main.py 
# if you want debug mode `export FLASK_ENV=development`
pip install -r requirements.txt
python3 python3 -m pip install mysql-connector
flask run
```

- Mysql Setup
   just follow the mysql doc


