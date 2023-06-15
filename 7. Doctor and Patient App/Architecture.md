The architecture follows a client-server model, where the frontend (client) interacts with the backend (server) via API requests.
The frontend captures user inputs, sends requests to the backend API endpoints, and updates the UI based on the server's 
responses. The Flask backend receives the requests, performs the required operations (e.g., registration), interacts 
with the database using SQLAlchemy, and sends back appropriate responses to the frontend.


Frontend Architecture:

HTML: The HTML code defines the structure and content of the web pages. It includes elements such as buttons, 
input fields, labels, and paragraphs to create the user interface.

CSS: The CSS code defines the styles and layout of the web pages. It includes selectors and properties to 
customize the appearance of HTML elements, such as setting background colors, font styles, and positioning.

JavaScript: The JavaScript code adds interactivity and functionality to the web pages. It includes event listeners,
AJAX requests, and DOM manipulation to handle form submissions, send HTTP requests to the backend, and update the UI 
based on the server's response.

Event Listeners: The JavaScript code attaches event listeners to elements such as the patient registration 
form and buttons. These listeners listen for specific events, such as form submission or button clicks, and
execute corresponding functions when triggered.

AJAX Requests: The JavaScript code uses the fetch() function to send asynchronous HTTP requests to the backend
API endpoints. It includes the URL, request method, headers, and request payload (data) in the request configuration.

DOM Manipulation: The JavaScript code interacts with the Document Object Model (DOM) to access and modify HTML 
elements dynamically. It retrieves input values, displays error messages, and updates the UI based on the server's response.

Backend Architecture (Flask):

The Flask backend handles the API requests sent from the frontend. It includes the following components:

Flask: Flask is a Python web framework used to build the backend of the application. It handles HTTP requests, 
defines API endpoints, and interacts with the database.

API Endpoints: The Flask app defines API endpoints using the @app.route() decorator. These endpoints are accessed
by the frontend to perform operations such as patient registration (/register/patient) and doctor registration.

SQLAlchemy: The SQLAlchemy library is used for database management. It provides an ORM (Object-Relational Mapping) 
interface to interact with the PostgreSQL database. The Doctor and Patient classes represent the database tables 
and define the table schema.

Database: The app uses a PostgreSQL database as specified in the SQLAlchemy configuration
(app.config['SQLALCHEMY_DATABASE_URI']). The database stores the registered doctors and patients' information.

![image](https://github.com/MBhargavi235/flask_tasks/assets/106804698/3593a2c0-6370-4b7f-9893-352507493d46)

![image](https://github.com/MBhargavi235/flask_tasks/assets/106804698/7499e65d-2ac0-47ea-8a01-e9c26afbe51f)

![image](https://github.com/MBhargavi235/flask_tasks/assets/106804698/7f3482e1-760e-4c34-b2df-6d6d263b0f9a)

![image](https://github.com/MBhargavi235/flask_tasks/assets/106804698/653b4fd0-e438-4b04-880d-bf6f93d3808f)

![image](https://github.com/MBhargavi235/flask_tasks/assets/106804698/930c7717-6365-4183-bbf2-6439dfa524d9)

![image](https://github.com/MBhargavi235/flask_tasks/assets/106804698/733b0f55-30fc-405a-b0ee-4b90927405d0)







