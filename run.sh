pip install virtualenv
python virtualenv venv
source venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate