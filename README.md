# PizzaOrderWebsite

This repository contains my first Django project. The website is a food ordering website. It`s main product is Pizza,
but it contains a few more products.

<h2>Features</h2>
<ul>
<li>User authentication and registration</li>
<li>Browse trough the available menu that is offered on the website</li>
<li>Add products in the shopping cart</li>
<li>Finish order</li>
<li>Choose how to complete the order, paying by cash or Credit card</li>
<li>Repeat previous orders from the order history</li>
<li>Upload photo in your profile</li>
<li>Change password from the profile</li>
<li>Forgotten password feature</li>
<li>Repeat order feature</li>
<li>Email confirmation on registration, successful order and on new password request</li>
</ul>

<h2>Technologies</h2>

<ul>
<li>Django(4.2.3)</li>
<li>Djangorestframework(3.14.0)</li>
<li>Stripe(5.5.0)</li>
<li>HTML, CSS</li>
<li>JavaScript</li>
<li>Postgresql</li>
</ul>


<h2>Installation</h2>
<ol>
<li>Clone repository:<br>
git clone https://github.com/kristiyanradoslavov/PizzaOrderWebsite.git
</li>

<li>Install dependencies:<br>
pip install -r requirements.txt 
</li>

<li>
Set up environment variables
</li>

<li>Apply database migrations: <br>
python manage.py makemigrations <br>
python manage.py migrate
</li>

<li>
In order to see the full functionality of the website you need to import the data for the products which is in data.json.
In order to do this run command: <br>
python manage.py loaddata data.json
</li>

<li>
Run the server <br>
python manage.py runserver
</li>
</ol>
