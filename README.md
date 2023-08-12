Clone the repository.
Create a virtual environment and activate it.
Install the required dependencies using pip install -r requirements.txt.
Configure the database settings in gas_utility/settings.py.
Apply migrations using python manage.py migrate.
Create a superuser for the admin panel using python manage.py createsuperuser.
Run the development server using python manage.py runserver.
Usage:

Access the admin panel at http://localhost:8000/admin/ to manage service requests and customer accounts. 
username - san
pass.- san
Customers can submit service requests and track their status at http://localhost:8000/service-requests/.
Customers can view and update their account information at http://localhost:8000/customer-accounts/.