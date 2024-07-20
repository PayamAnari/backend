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

## Property Management

The Property section of PropertyBnB provides comprehensive tools for managing property listings, ensuring both property owners and renters have a seamless experience. This section encompasses various functionalities, from creating and updating listings to viewing detailed property information and managing user favorites.

### Key Features

**Create, Read, Update, Delete (CRUD) Operations**

- **Create Property:** Property owners can easily create new property listings, providing all necessary details such as title, description, price per night, number of bedrooms, bathrooms, and guest capacity.
- **Update Property:** Owners can update existing listings to reflect changes in availability, pricing, or property details.
- **Delete Property:** Listings can be removed when no longer available, ensuring the platform remains up-to-date.
- **View Properties:** Users can browse through available properties, with detailed information presented for each listing.
Detailed Property Information

- **Property Details:** Each property listing includes a comprehensive set of details, such as the number of bedrooms, bathrooms, guest capacity, and amenities.
- **Location Information:** Listings include location details like country, city, and specific address, helping users find properties in their desired areas.
- **Categorization:** Properties can be categorized by type, such as apartments, houses, or villas, allowing users to filter based on their preferences.
Media Handling

- **Image Uploads:** Property owners can upload images to showcase their properties, enhancing the visual appeal and providing potential renters with a clear view of the property.
- **Image Management:** Easy management of property images, including updating and removing outdated pictures.
Favorites

- **Favorite Properties:** Users can mark properties as favorites, making it easier to find and revisit preferred listings.
- **Favorite Management:** Simple toggle functionality to add or remove properties from a user's favorites list.
Property Filtering and Search

- **Advanced Search:** Users can search for properties based on various criteria such as location, price, number of bedrooms, and availability dates.
- **Filter by Attributes:** Properties can be filtered by specific attributes like number of guests, amenities, and category, helping users find properties that meet their exact needs.
Reservation Integration

- **Availability Checking:** Automatically check property availability based on existing reservations to prevent double bookings.
- **Reservation Management:** Integration with the reservation system to display available dates and manage bookings directly from the property listing.
  
### User Experience

- **Responsive Design:** The property section is designed to be responsive, ensuring a smooth browsing experience on both desktop and mobile devices.
- **User-friendly Interface:** Intuitive interfaces for both property owners and renters, simplifying the process of listing, updating, and searching for properties.

---

## User Management

The User section of PropertyBnB is designed to handle all aspects of user account management, including user registration, authentication, profile updates, and reservation management. This section ensures a secure and user-friendly experience, enabling users to manage their accounts and interactions with the platform efficiently.

### Key Features

**User Registration and Authentication**

- **Registration:** New users can register an account on the platform, providing necessary details like name and email. Upon registration, users can start exploring and interacting with the platform.
- **Login/Logout:** Users can securely log in and log out of their accounts. The login system uses email and password for authentication, ensuring that only authorized users can access their accounts.
- **Token Management:** The system uses JWT (JSON Web Tokens) for managing user sessions, allowing users to refresh their tokens to stay logged in without having to re-enter their credentials frequently.

### User Profile Management

- **View Profile:** Users can view their profile details, including personal information, contact details, and profile picture. This information is displayed in a structured and easy-to-read format.
- **Update Profile:** Users can update their profile information, including their name, email, telephone, address, birthday, work details, favorite song, and a personal bio. This feature ensures that users can keep their information up-to-date.
- **Upload Profile Picture:** Users can upload a profile picture, personalizing their account and enhancing their profile
visibility. The profile picture can be easily updated or changed.

### Reservation Management

- **View Reservations:** Users can view a list of their reservations, allowing them to keep track of their booking history. This list includes detailed information about each reservation.
- **Reservation Details:** Users can view specific details about individual reservations, providing them with all necessary information about their stays in one place.

### Administrative Controls

- **Update User Information:** Admins or users themselves can update their profile information, ensuring data accuracy and relevance.
- **Delete Account:** Users can delete their accounts if they decide to leave the platform. This feature ensures users have full control over their data and can choose to remove it if necessary.

### User Experience

- **Responsive Design:** The user management section is designed to be responsive, providing a seamless experience across different devices, including desktops, tablets, and smartphones.
- **User-friendly Interface:** The interface is intuitive and easy to navigate, making it simple for users to manage their accounts and reservations without needing technical assistance.

### Security

- **Authentication:** Secure authentication mechanisms ensure that user data is protected, and only authorized users can access their accounts.
- **Permissions:** Different permission levels ensure that users can only perform actions they are authorized for, enhancing overall security and integrity of the platform.

### Integration with Other Sections

- **Seamless Integration:** The user management section is integrated with other sections like property listings and reviews, providing a cohesive and interconnected user experience.
- **Profile Information in Reviews:** User profile information can be displayed alongside their reviews, adding credibility and context to the feedback provided.

### Enhancing Trust and Engagement

- **Community Building:** By allowing users to personalize their profiles and share information, the platform fosters a sense of community and trust among users.
- **Informed Decisions:** Detailed user profiles and review histories help potential renters make informed decisions based on real user feedback and experiences.

---

## Review Management

The Review section of PropertyBnB provides users with the ability to leave feedback on properties, enhancing the overall user experience by offering insights into property quality and user satisfaction. This section includes functionalities for creating, viewing, and deleting reviews, as well as calculating average ratings for properties.

### Key Features

**Create, Read, Delete (CRD) Operations**

- **Create Review:** Users can submit reviews for properties they have stayed at, sharing their experiences and rating the property on a scale. This helps other potential renters make informed decisions based on past experiences.
- **View Reviews:** Potential renters can view reviews left by other users for a specific property. Reviews include ratings, comments, and details about the reviewer, providing a comprehensive understanding of the property’s quality.
- **Delete Review:** Users can delete their reviews if they wish to remove their feedback. This ensures users have control over the content they contribute to the platform.

### Average Rating Calculation

- **Average Rating:** The system calculates the average rating for each property based on user reviews. This average rating is displayed alongside the reviews, giving potential renters a quick overview of the property’s overall rating.

### Detailed Review Information

- **Review Details:** Each review includes detailed information such as the rating, comment, user who submitted the review, and timestamps for when the review was created and last updated.
- **User Information:** Reviews display details about the reviewer, helping to build trust and transparency in the feedback provided.

### User Experience

- **Responsive Design:** The review section is designed to be responsive, ensuring a smooth experience on both desktop and mobile devices.
- **User-friendly Interface:** Intuitive forms and interfaces make it easy for users to submit and manage their reviews, contributing to the community and helping others make informed decisions.

### Administrative Controls

- **Moderation:** Admins have the ability to moderate reviews, ensuring that all content complies with the platform’s guidelines and maintaining a positive and constructive environment.

### Integration with Property Listings

- **Seamless Integration:** The review section is seamlessly integrated with property listings, allowing users to view reviews directly on the property detail page. This integration ensures that all relevant information is readily accessible.

### Enhancing Trust and Transparency

- **Community Feedback:*** Reviews provide a platform for community feedback, helping to build trust and transparency within the PropertyBnB ecosystem.
- **Informed Decisions:** By reading reviews and seeing average ratings, potential renters can make more informed decisions, leading to higher satisfaction and fewer surprises.

---

## Chat

The Chat section of PropertyBnB is designed to facilitate real-time communication between users, enhancing interaction and support within the platform. This section enables users to engage in conversations, view chat history, and manage their messaging experiences seamlessly.

### Key Features
**Real-Time Communication**

- **Live Chat:** Users can engage in real-time conversations with others through WebSocket connections. This feature ensures instant messaging and dynamic interaction, providing a responsive and interactive user experience.
- **Conversation Creation:** Users can start new conversations with other platform members or retrieve existing chat threads, allowing for both new and ongoing discussions.
- **Message Notifications:** Real-time notifications for incoming messages ensure that users are promptly informed of new interactions, enhancing responsiveness and engagement.
Conversation Management
View Conversations: Users can view a list of their active and past conversations. This overview includes essential details such as participants and timestamps, helping users keep track of their interactions.
Conversation Details: Users can access specific conversations to view message history and other relevant details, allowing for a comprehensive understanding of the context and content of their discussions.
Message Handling
Send and Receive Messages: Users can send and receive messages within their conversations. The messaging system supports text-based communication and ensures that messages are delivered and displayed in real time.
Message Storage: Messages are stored in the database, ensuring that users can access their chat history even after their WebSocket connection is closed. This feature provides continuity and reference for past interactions.
Administrative Controls
Manage Conversations: Users have the ability to manage their conversations, including starting new chats and accessing previous ones. This control ensures that users can effectively organize and review their communication history.
Delete Conversations: Users can delete specific conversations if desired, allowing for the removal of outdated or unnecessary chat threads and maintaining a clean and relevant chat history.
User Experience
Real-Time Interaction: The chat system is designed to offer a seamless real-time interaction experience, making it easy for users to communicate instantly without delays or interruptions.
Intuitive Interface: The chat interface is user-friendly and straightforward, providing an easy-to-navigate environment for managing conversations and messages.
Security
Secure Messaging: All messages are transmitted over secure WebSocket connections, ensuring that user communications are protected from unauthorized access.
Authentication: The chat system integrates with the platform’s authentication mechanisms to ensure that only authorized users can participate in conversations and access message data.
Integration with Other Sections
Profile Integration: The chat system integrates with user profiles, displaying relevant profile information alongside conversations. This integration provides context and enhances the user experience by linking chat interactions with user details.
Reservation Coordination: The chat feature can be used to coordinate reservations and property-related discussions, streamlining communication related to booking and property management.
Enhancing User Interaction
Community Engagement: By facilitating direct communication between users, the chat section fosters community building and engagement, allowing for more personal and interactive experiences.
Support and Assistance: The real-time chat feature enables users to seek support and assistance promptly, improving overall customer service and satisfaction.

---



## Installation
### Prerequisites

- **Docker:** Ensure Docker is installed on your machine.
- **Python 3.12:** The app is built using Python 3.12.

### Steps

1- **Clone the Repository:**
```
git clone https://github.com/PayamAnari/backend.git
cd backend
```

2- **Environment Setup:** Create a .env.dev file in the root directory with the following variables:

Make file
```
SECRET_KEY=your_secret_key
DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=airbnb
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432
STRIPE_SECRET_KEY=your_stripe_secret_key
```

3- **Build and Run Docker Containers:**

```
docker-compose up --build

```

4- **Run Migrations:**

```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

5- **Access the Application**

```
Open your web browser and go to http://localhost:3000 to access the application.
```

6- **Admin Panel**

Access the Django admin panel at http://localhost:8000/admin to manage users, properties, and reviews.


---

