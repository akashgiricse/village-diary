# Village diary


## Current Featur

*TODO*


## Getting started with development
Dependencies:
- Python 3.6.x
- Django 1.11.x
- Ubuntu 17.04 or later or Linux Mint 18.2 or later

### 1. Clone this repository
```bash
git clone https://github.com/akashgiricse/village-diary.git
cd lets_quiz
```

### 2. Install the [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)
Follow [instructions on official documentation page](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

### 3. Create the virtualenv
```bash
## run following command from `lets_quiz` directory
mkvirtualenv lets_quiz -a "$(pwd)" -p python3.6
```

### 4. Install python packages
```bash
## Activate the virtualenv which you created on the last step
workon lets_quiz
cd ..
pip install -r requirements.txt
```

### 5. Setup the database
*TODO - Add instructions for this when I start using MySQL database.*

### 6. Run database migrations
```bash
cd lets_quiz
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

## Contribute

- Issue Tracker: [Issues](https://github.com/akashgiricse/lets-quiz/issues)
- Source Code: [Download zip: Release v1.0.1](https://github.com/akashgiricse/lets-quiz/archive/1.0.1.zip)

## Contributors

* [Akash Giri](https://github.com/akashgiricse)

## Support

* If you are having issues, please let me know.<gr>
I have a mailing list located at: buggyrango@gmail.com

## License
MIT License

Copyright (c) 2018 Akash Giri.
