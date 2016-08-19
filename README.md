# Tote Tiroler 

**Tote Tiroler** is a django-based web application for publishing data about Tyroleans who were killed during the [Tyrolean uprise in 1809](https://en.wikipedia.org/wiki/Tyrolean_Rebellion). The data driving this web application was first published by Hans Kramer [Die Gefallenen Tirols 1796-1813 (Schlern-Schriften 47), Innsbruck 1949](http://search.obvsg.at/UIB:Blended:UIB_aleph_acc000119944) and republished in a more normalized way by Peter Andorfer [Totetiroler, Innsbruck 2009](http://search.obvsg.at/UIB:Blended:UIB_aleph_acc001586080). With this web application, this data is online available. 

## Install
The application was build with Python 3.4.

1. clone the repo
2. create a virtual environment and run install the required packages `pip install > requirements`
3. makemigrations and migrate `python manage.py makemigrations --settings=totetiroler.settings.dev`and `python manage.py migrate --settings=totetiroler.settings.dev`
4. start the dev-server `python manage.py runserver`
5. browse to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Upload the data
To upload the dataset stored in this repo you have to exectue the ipython script `import_data.ipynb`.

1. Start a new iypthon session `python manage.py shell_plus --notebook --settings=totetiroler.settings.dev`.
2. Open `import_data.ipynb`.
3. Execute the script cell by cell. 