# PC_Builder
Assist users to choose their ideal PC build

## Claim
**All sample datasets should not be used for any commercial purposes.**

### Features
1. Boards:
  - CPU, GPU, Motherboard, RAM, SSD, HDD
2. Accounts:
  - Create account and change password
  - Must login before create a PC build

### How to run
- Download the app to local and navigate to the directory. (Python environment installed)
- Run `python manage.py migrate` to setup database (Sqlite used, can be changed in setting, supported databases can be found at 
[Django website](https://docs.djangoproject.com/en/3.0/intro/tutorial02/)
- Run `python manage.py makemigrations` to create model tables
- Run `python manage.py sqlmigrate boards 0001`
- Run `python manage.py migrate` again to create model tables in database
- Run `python manage.py runserver` to start the web app
- Open browser and go to `127.0.0.1:8000/index`

### How to import data
Sample CPU, Ram, SSD, HDD datasets were provided in json type file.
- Run `python manage.py createsuperuser` to create admin (Follow the screen instructions)
- Run `python manage.py loaddata *filename*` to import data into database
- Open browser and go to `127.0.0.1:8000/admin` and login as admin

### Future updates
1. Pagination for each components
2. Sample dataset for Motherboard and GPU
3. Auto-calculated TDP for a PC build
4. User portfolio page
5. Votes for PC build