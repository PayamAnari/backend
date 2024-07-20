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
Security
Content Security Policy (CSP): A security feature that helps to prevent various attacks including Cross-Site Scripting (XSS) and data injection attacks.
JSON Web Tokens (JWT): For secure user authentication and session management.
DevOps and Deployment
Docker: A platform for developing, shipping, and running applications inside lightweight containers.
Docker Compose: A tool for defining and running multi-container Docker applications.
nginx: (Not mentioned in the code, but often used in deployment) A high-performance web server that can also be used as a reverse proxy, load balancer, mail proxy, and HTTP cache.
Middleware
CORS Headers: Django middleware for handling Cross-Origin Resource Sharing (CORS), making cross-origin AJAX possible.
CSRF Middleware: Protects the application from Cross-Site Request Forgery (CSRF) attacks.
Miscellaneous
Pillow: A Python Imaging Library (PIL) fork that adds image processing capabilities to your Python interpreter.
uuid: For generating universally unique identifiers (UUIDs) for user and reservation primary keys.
Project Management
Git: Version control system for tracking changes in the source code during software development.
GitHub: Hosting service for version control using Git, facilitating collaboration and project management.
