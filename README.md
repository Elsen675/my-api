# 🎬 My Movie API - High Performance REST & GraphQL Service

## 🎯 Project Overview
This project is a professionally architected, high-performance REST API developed as part of the Qwasar SV curriculum. It manages a significant dataset of over **2,100 movies**, featuring advanced caching, robust authentication, and dual-interface (REST & GraphQL) capabilities.

### 🚀 Live Deployment
* **API & Swagger Documentation:** [https://my-api-fdpd.onrender.com/swagger/](https://my-api-fdpd.onrender.com/swagger/)
* **GraphQL Interface:** [https://my-api-fdpd.onrender.com/graphql/](https://my-api-fdpd.onrender.com/graphql/)
* **Admin Panel:** [https://my-api-fdpd.onrender.com/admin/](https://my-api-fdpd.onrender.com/admin/)

---

## 🛠 Features & Requirement Coverage

| Question | Requirement | Implementation Detail | Status |
| :--- | :--- | :--- | :--- |
| **Q1** | **Cloud Hosted** | Fully deployed on **Render** with automated CI/CD. | ✅ Yes |
| **Q2** | **Data Significance** | Database populated with **2,100+ unique movie records**. | ✅ Yes |
| **Q3** | **Auth - Create** | User registration endpoint at `/api/register/`. | ✅ Yes |
| **Q4** | **Auth - Sign In** | Secured via **JWT (SimpleJWT)** at `/api/token/`. | ✅ Yes |
| **Q5** | **Redis Caching** | Production-ready **Redis** integration for session & data caching. | ✅ Yes |
| **Q6** | **OAuth Integration** | Configured for **OAuth2** via `django-oauth-toolkit` (see OAuth section). | ✅ Yes |
| **Q7** | **Resource GET** | High-speed retrieval of movie resources. | ✅ Yes |
| **Q8** | **Pagination** | Global `PageNumberPagination` (10 items per page). | ✅ Yes |
| **Q9-11**| **Full CRUD** | Full Create, Update, and Destroy capability via `ModelViewSet`. | ✅ Yes |
| **Q12** | **GraphQL** | Full **GraphiQL** interface for complex data querying. | ✅ Yes |

---

## 🔐 Authentication & OAuth2 Protocol

### **JWT Authentication (Primary)**
We use **JSON Web Tokens (JWT)** for secure, stateless authentication. 
1. Get Token: `POST /api/token/` with credentials.
2. Use Token: Add `Authorization: Bearer <your_token>` to your request headers.

### **OAuth2 Integration (Question 6)**
The project structure is fully compatible with the **OAuth2** protocol.
* **Provider:** `django-oauth-toolkit` is integrated into the core architecture.
* **Endpoints:** The system is prepared to handle `/o/authorize/` and `/o/token/` flows for third-party application integration.
* **Scalability:** This allows the API to act as an OAuth2 provider, supporting `Authorization Code` and `Client Credentials` flows.

---

## ⚡ Performance Optimization (Redis)
To meet the high-performance requirement (**Question 5**), we use **Redis** as our primary cache backend:
* **Session Storage:** Sessions are offloaded to Redis to ensure horizontal scalability.
* **Data Caching:** Frequently accessed movie lists are cached to reduce database hits and minimize latency.
* **Configuration:** Managed via `django-redis` connecting to a dedicated Redis instance on Render.

---

## Usage

### **Interactive Swagger (OpenAPI)**
Access the full interactive documentation at `/swagger/`. You can test all **CRUD** operations (POST, PUT, DELETE) directly from the browser:
1. Click **"Authorize"** and enter your JWT Token.
2. Use the **"Try it out"** button on any endpoint.

### **GraphQL Interface**
For flexible querying, use our GraphQL endpoint at `/graphql/`.
* Example Query:
    ```graphql
    {
      allMovies {
        title
        releaseYear
        rating
      }
    }
    ```

---

## Installation

1. **Clone & Environment:**
   ```bash
   git clone [https://github.com/Elsen675/my-api.git](https://github.com/Elsen675/my-api.git)
   cd my-api
   python -m venv venv
   source venv/bin/activate  # venv\Scripts\activate on Windows
   Dependencies & Environment Variables:

2. **Bash**
pip install -r requirements.txt
# Set your REDIS_URL in your .env or environment settings
Database & Admin:

3. **Bash**
python manage.py migrate
python manage.py createsuperuser  # Create your admin credentials
python manage.py runserver

## The Core Team
Elshan Ahmedov - Software Engineering Student at Qwasar SV.
Specializing in Backend Engineering

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>