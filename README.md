# restaurant-app

API's to check 
1- http://localhost/restaurant/bookings/
2- http://localhost/restaurant/bookings/{booking-id}

3- http://localhost/restaurant/menus/
4- http://localhost/restaurant/menus/{booking-id}

to run/check the tests run the command 
python manage.py test or view the tests.py file inside the app folder

to check registration run the following request "http://localhost/api-token-auth/" with the username "adminfortest" and password "safadi112" or create a superuser by running the command python3 manage.py createsuperuser to create new user and password for testing the API.

to check login, send request to this API "http://localhost/auth/token/login/" with the username and password you used before. you will get a Token.
to check logout, send a request to this API "http://localhost/auth/token/logout/" + include in the header the token you got while you logged in, add it like "Authorization" in the tag name and in the value add "Token <token-value>". without ""
