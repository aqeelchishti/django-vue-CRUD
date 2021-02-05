# Django Vue CRUD App

## Project setup on local server

### Django Backend API
```
cd django-vue-CRUD/
```

#### Setup Virtual Environment
```
pip install pipenv
pipenv --python 3.9 shell
pipenv install -r requirements.txt
```

#### Database Migration & Run Backend Server
```
python manage.py migrate
python manage.py runserver
```

### Vue Frontend App
```
cd frontend/
npm install
```

#### Compile for Development
```
npm run serve
```

#### Compile for Production
```
npm run build
```

#### Customize configuration
See [Vue js Configuration](https://cli.vuejs.org/config/).
