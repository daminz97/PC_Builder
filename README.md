# PC_Builder
Assist users to choose their ideal PC build
<br />
<br />
<br />
## Claim
**All sample datasets should not be used for any commercial purposes.**
<br />
<br />
<br />
### Features
1. Boards:
  - CPU, GPU, Motherboard, RAM, SSD, HDD
2. Accounts:
  - Create account and change password
  - Must login before create a PC build
<br />
<br />
<br />
### How to run
<br />
- Download the app to local and navigate to the directory. (Python environment installed)
<br />
- Run `python manage.py migrate` to setup database (Sqlite used, can be changed in setting, supported databases can be found at 
[Django website](https://docs.djangoproject.com/en/3.0/intro/tutorial02/)
<br />
- Run `python manage.py makemigrations` to create model tables
<br />
- Run `python manage.py sqlmigrate boards 0001`
<br />
- Run `python manage.py migrate` again to create model tables in database
<br />
- Run `python manage.py runserver` to start the web app
<br />
- Open browser and go to `127.0.0.1:8000/index`
<br />
<br />
<br />
### How to import data<br />
Sample CPU, Ram, SSD, HDD datasets were provided in json type file.<br />
- Run `python manage.py createsuperuser` to create admin (Follow the screen instructions)<br />
- Run `python manage.py loaddata *filename*` to import data into database<br />
- Open browser and go to `127.0.0.1:8000/admin` and login as admin<br />
<br />
<br />
<br />
### Future updates<br />
1. Pagination for each components<br />
2. Sample dataset for Motherboard and GPU<br />
3. Auto-calculated TDP for a PC build<br />
4. User portfolio page<br />
5. Votes for PC build<br />
