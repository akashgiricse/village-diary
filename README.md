# Village diary


## Current Featur

*TODO*
- Add Template for Login, Register
- Data Retrival
- Search Feature

## Getting started with development
Dependencies:
- Python 3.6.x
- Django 1.11.x
- Ubuntu 17.04 or later or Linux Mint 18.2 or later

### 1. Clone this repository
```bash
git clone https://github.com/akashgiricse/village-diary.git
# in the cloned directory goto village_diary directory i.e.
cd village_diary
```

### 2. Install the [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)
Follow [instructions on official documentation page](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

### 3. Create the virtualenv
```bash
## run following command from `village_diary` directory
mkvirtualenv village_diary -a "$(pwd)" -p python3.6
```

### 4. Install python packages
```bash
## Activate the virtualenv which you created on the last step (should be automatically activated)
workon village_diary
cd ..
pip install -r requirements.txt
```

### 5. Setup the database
*TODO - Add instructions for this when I start using MySQL/Postgre database.*

### 6. Run database migrations
```bash
cd village_diary
python manage.py migrate
```

### 7. Create superuser
```bash
python manage.py createsuperuser
```

### 8. Run development server
```bash
python manage.py runserver
```
