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

