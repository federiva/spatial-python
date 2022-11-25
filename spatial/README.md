## Installing
Create a virtual environment
```
python3 -m venv env
source env/bin/activate
```
Install dependencies
```
pip install -r requirements.txt
```
Run migrations
```
python manage.py migrate
```
Run app
```
python manage.py runserver
```
### Data
Data from Movebank was downloaded from [Kaggle](https://www.kaggle.com/datasets/pulkit8595/movebank-animal-tracking/discussion/27618?resource=download)