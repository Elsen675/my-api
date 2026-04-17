# My Movie API Project

## Task
The goal of this project is to create a high-performance, professionally documented REST API with a significant dataset (over 1,000 records). Key objectives include managing large-scale data, implementing caching via Redis, providing Full CRUD functionality, and integrating a GraphQL interface.

## Description
The project is built using Django Rest Framework (DRF) with a focus on scalability and modern API standards:

Data Significance (Question 2): Over 2,100 movie records are present in the database, generated via a custom `fill_data.py` script to ensure data depth.
Cloud Hosted (Question 1): Fully deployed and live on Render.
Authentication (Question 3 & 4):Supports User Registration and Token-based Authentication.
Redis Caching (Question 5): Integrated with `django-redis` to optimize performance for high-traffic endpoints.
OAuth Integration (Question 6): Structure prepared for OAuth2 protocol via `django-oauth-toolkit`.
Pagination (Question 8): Global pagination implemented (10-20 items per page) to handle large result sets efficiently.
Full CRUD (Question 9, 10, 11): Complete Resource management (Create, Read, Update, Delete) via DRF `ModelViewSet`.
GraphQL Interface (Question 12): Interactive **GraphiQL interface provided for flexible data querying.
Documentation: Fully interactive Swagger/OpenAPI documentation.

 🔗 Project Links
Live API & Swagger Docs: [https://my-api-fdpd.onrender.com/](https://my-api-fdpd.onrender.com/)
GraphQL Interface [https://my-api-fdpd.onrender.com/graphql/](https://my-api-fdpd.onrender.com/graphql/)
GitHub Repository: [https://github.com/Elsen675/my-api](https://github.com/Elsen675/my-api)

## Installation
Clone the repository:
    `git clone https://github.com/Elsen675/my-api.git`
Create a virtual environment:
    `python -m venv venv`
Activate venv:
    `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
Install dependencies:
    `pip install -r requirements.txt`
Run migrations:
    `python manage.py migrate`
Start the server:
    `python manage.py runserver`

## Usage
 Authentication
To obtain a token:
Endpoint: `POST /api-token-auth/`
Payload: `{"username": "your_user", "password": "your_password"}`

 Main API Endpoints
List Movies (Cached & Paginated): `GET /api/movies/`
Create Movie: `POST /api/movies/` (Token Required)
Update Movie: `PUT /api/movies/{id}/` (Token Required)
Delete Movie: `DELETE /api/movies/{id}/` (Token Required)
GraphQL UI: `GET /graphql/`

## The Core Team
**Elshan Ahmedov** - Software Engineering Student at Qwasar SV.

---
<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>