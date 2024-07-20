<h1 align="center">
  <img
    width="400"
    alt="django"
    src="https://live.staticflickr.com/65535/53869010241_7f0b71e672_n.jpg">
</h1>

---

<h3 align="center">
  <strong>
 ✈️ Django Aribnb ✈️

  </strong>
</h3>

---

## Django Airbnb - Django REST API (DRF)
### Description

DjangoAirbnb is a robust backend application designed to power a platform similar to Airbnb, providing comprehensive features for property listings, user authentication, real-time chat, and review management. Built with Django and Django Channels, the application ensures scalability, security, and performance. Below is a detailed overview of its features and configuration.

---

## Features

1. **Property Listings**

- Create, Read, Update, Delete (CRUD) Operations: Allows users to manage property listings with ease.
- Media Management: Efficiently handles images and other media files associated with properties.

2. **User Authentication and Authorization**

- Custom User Model: Utilizes a custom user model (useraccount.User) to support email-based authentication.
- JWT Authentication: Implements JSON Web Token (JWT) for secure user authentication.
- Django Allauth: Integrates with Django Allauth for robust user registration and authentication workflows.

3. **Real-time Chat**

- WebSocket Support: Leverages Django Channels to provide real-time chat functionality between users.
- Token Authentication Middleware: Ensures secure WebSocket connections using token authentication.

4. **Review Management**

- User Reviews: Allows users to leave reviews for properties, enhancing trust and credibility.
Security and Configurations

5. **Payment Integration**

- Stripe Integration: Secure payment processing for reservations using Stripe.

6. **Security and Configurations**

- Environment Variables: Utilizes environment variables for sensitive configurations such as SECRET_KEY, DEBUG, DATABASE credentials, and STRIPE_SECRET_KEY.
- Content Security Policy (CSP): Implements CSP headers to protect against cross-site scripting (XSS) and other attacks.
- CORS Configuration: Configured to allow cross-origin requests from specified origins.

7.  **Middleware and Security**

- Django Middleware: Includes essential middleware for security, session management, and cross-origin resource sharing (CORS).
- CSP Middleware: Enhances security by restricting resource loading to trusted sources.

---

## Technologies Used

### Backend

- **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework (DRF):** A powerful and flexible toolkit for building Web APIs in Django.
- **Django Channels:** Extends Django to handle WebSockets, enabling real-time support in the application.
- **PostgreSQL:** A powerful, open source object-relational database system.
- **Daphne:** A HTTP, HTTP2, and WebSocket protocol server for ASGI and ASGI-HTTP, used to serve Django Channels applications.
- **psycopg2:** A PostgreSQL adapter for Python, used to connect Django with PostgreSQL.
- **Stripe API:** Integration for handling secure payment processing.

### Authentication and Authorization
- **Django Allauth:** Integrated set of Django applications addressing authentication, registration, account management, and third-party (social) account authentication.
- **Django Rest Auth:** Provides a set of REST API endpoints for user registration, login/logout, password change/reset, social auth, and more.
- **Django Rest Framework SimpleJWT:** A JSON Web Token authentication backend for the Django REST Framework.
- **WebSockets:** For enabling real-time, two-way interactive communication between the user's browser and the server.

### Security
- **Content Security Policy (CSP):** A security feature that helps to prevent various attacks including Cross-Site Scripting (XSS) and data injection attacks.
- **JSON Web Tokens (JWT):** For secure user authentication and session management.

### DevOps and Deployment
- **Docker:** A platform for developing, shipping, and running applications inside lightweight containers.
- **Docker Compose:** A tool for defining and running multi-container Docker applications.

### Middleware
- **CORS Headers:** Django middleware for handling Cross-Origin Resource Sharing (CORS), making cross-origin AJAX possible.
- **CSRF Middleware:** Protects the application from Cross-Site Request Forgery (CSRF) attacks.

### Miscellaneous
- **Pillow:** A Python Imaging Library (PIL) fork that adds image processing capabilities to your Python interpreter.
- **uuid:** For generating universally unique identifiers (UUIDs) for user and reservation primary keys.

### Project Management
- **Git:** Version control system for tracking changes in the source code during software development.
- **GitHub:** Hosting service for version control using Git, facilitating collaboration and project management.

 <p align="left">
  <img src="https://img.shields.io/badge/django-00008B?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/django rest framework-acace6?style=for-the-badge&logo=DRF&logoColor=white"/>
  <img src="https://img.shields.io/badge/postgresql-800000?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/stripe-85EA2D?style=for-the-badge&logo=stripe&logoColor=white"/>
  <img src="https://img.shields.io/badge/WebSockets-ffa500?style=for-the-badge&logo=pyjwt&logoColor=white"/>
  <img src="https://img.shields.io/badge/simplejwt-ff0000?style=for-the-badge&logo=&logoColor=white"/>
  <img src="https://img.shields.io/badge/daphne-FF7F50?style=for-the-badge&logo=&logoColor=white"/>
  <img src="https://img.shields.io/badge/docker-0000FF?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/docker compose-4682B4?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/git-ffff00?style=for-the-badge&logo=git&logoColor=white"/>
  <img src="https://img.shields.io/badge/github-bf00ff?style=for-the-badge&logo=github&logoColor=white"/>

</p>

---

## API Endpoints
### Property

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/api/properties/``` | _Retrieve list of all properties_| _All users_|
| *GET* | ```/api/properties/<uuid:property_id>/``` | _Retrieve details of a specific property_|_All users_|
| *POST* | ```/api/properties/create/``` | _Create a new property_|_Authenticated users_|
| *PUT* | ```/api/properties/<uuid:property_id>/update/``` | _Update details of a specific property_|_Authenticated users_|
| *DELETE*  | ```/api/properties/<uuid:property_id>/delete/``` | _Delete a specific property_ |_Authenticated users_|

### User

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/api/auth/<uuid:pk>/``` | _Retrieve details of a specific user (landlord)_| _All users_|
| *GET* | ```/api/auth/myreservations/``` | _Retrieve list of all reservations for the logged-in user_|_Authenticated users_|
| *GET* | ```/api/auth/<uuid:pk>/reservation/``` | _Retrieve details of a specific reservation_|_Authenticated users_|
| *POST* | ```/api/auth/<uuid:pk>/upload-profile/``` | _Upload profile photo for a specific user_|_All users_|
| *PUT*  | ```/api/auth/<uuid:pk>/profile/``` | _Update details of a specific user_ |_Authenticated users_|
| *DELETE*  | ```/api/auth/<uuid:pk>/delete/``` | _Delete a specific user_ |_Authenticated users_|

### Review

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/api/reviews/<uuid:property_id>/reviews/``` | _Retrieve list of all reviews for a specific property_| _All users_|
| *POST* | ```/api/reviews/<uuid:property_id>/create/``` | _Create a new review for a specific property_|_Authenticated users_|
| *DELETE* | ```/api/reviews/<uuid:review_id>/delete/``` | _Delete a specific review_|_Authenticated users_|

### Chat

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/api/chat/rooms/``` | _Retrieve list of all chat rooms_| _Authenticated users_|
| *GET* | ```/api/chat/rooms/<uuid:room_id>/``` | _Retrieve details of a specific chat room_|_Authenticated users_|
| *POST* | ```/api/chat/rooms/create/``` | _Create a new chat room_|_Authenticated users_|
| *POST* | ```/api/chat/messages/`` | _Send a message to a chat room_|_Authenticated users_|
| *GET*  | ```/api/chat/messages/<uuid:room_id>/``` | _Retrieve list of all messages in a specific chat room_ |_Authenticated users_|

---

## Installation
### Prerequisites

- **Docker:** Ensure Docker is installed on your machine.
- **Python 3.12:** The app is built using Python 3.12.


