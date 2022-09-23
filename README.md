# 🔐User Authentication & Login using SQLite and Flask of Python

🌟A website where users need to login or register inorder to gain access to the information hidden behind the authentication layer. The authentication is implemented using
Flask login extension. The secret ingredient added for strong authentication is use of hashing function to hash & salt the user's password and then store it in the database.
This makes hacking into users data and consequetivley data leakage almost impossisible.

🌟The login generation and login management is done using the flask_login extension of Flask. The Hashing and Salting of the password is done using the werkzeug.security
package which converts it into a sha256 hash. All of this data is managed using the SQLite database. With HTML, CSS and Jinja for the fronted of website.

👉The final working of website is as follows: 

![Authentication Website](https://github.com/bellaryyash23/Authentication_Flask/blob/master/samples/site.gif?raw=true)

👆Final Authentication Website Working👆

👉In the 'main.py' file, first the User database in SQLite database is created. Next the Flask app is setup and also the Login Manager for the app is setup to track the
user's login access using the '.is_authenticated' method and is passed during rendering each page on route.

👉Now, the home route is used to render the 'index.html' which provides user options to either login or register to gain access to the website.

![Home Page of Website](https://github.com/bellaryyash23/Authentication_Flask/blob/master/samples/home.jpg?raw=true)

👆Home Page of Website👆

👉Next, the 'register' route is setup for new users to register to the website. Here, the user needs to enter their Name, email-id and password. After this the user gets
logged in and their data is added to the database. The hashing of password takes place in here and the hashed passsword converted to sha256 hash gets added to the database.

![Registration Page of Website](https://github.com/bellaryyash23/Authentication_Flask/blob/master/samples/register.jpg?raw=true)

👆Registration Page of Website👆

👉Once, the user has registered to the website now they can access the information by simplying loggin in to the website rather than registering again. The login authentication
is done using the email-id and password. The user needs to enter the email-id which is used to find the user in the database. Next, the password authenication is done
where the entered password and stored password is compared and if the credabilities match then, the user is successfully logged in.

👉Since re-hasing and finding the original password text is almost impossisible, the comparison happens by converting the entered password into hash and then checking
both their values.

![Login Page of Website](https://github.com/bellaryyash23/Authentication_Flask/blob/master/samples/login.jpg?raw=true)

👆Login Page of Website👆

👉Once, the user has successfully register or logged in to the website, then they are redirected to the secret inforamtion hidden under the authentication layer. 

![Welcome Page of Website](https://github.com/bellaryyash23/Authentication_Flask/blob/master/samples/welcome.jpg?raw=true)

👆Welcome Page with access to information of Website👆

👉After the user has accessed the information, they can logout of the website with the logout route and their login sesssion is terminated via the flask login manager.

![Logout Page of Website](https://github.com/bellaryyash23/Authentication_Flask/blob/master/samples/logout.jpg?raw=true)

👆Successfully Logged out of Website👆

👉In this way, the login authentication and management is carried out. We can view how the password after hashing is stored in the database as follows:

![Database for Website](https://github.com/bellaryyash23/Authentication_Flask/blob/master/samples/database.JPG?raw=true)

👆Database for the Website👆
