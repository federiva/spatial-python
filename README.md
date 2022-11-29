## Introduction
This is a small example of integrating tracks data coming from this *Larus fuscus* [tracking database](https://www.kaggle.com/datasets/pulkit8595/movebank-animal-tracking) and using an [open source API](https://openskynetwork.github.io/opensky-api/index.html) to get the current flights passing through the bounding zone delimited by the animal tracks.

## Live development version
You can check a deployed development version of this small app [here](http://104.248.77.150:7000/)
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