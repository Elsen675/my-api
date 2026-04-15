## Welcome to My Movie API
## Task
Bu layihənin məqsədi 1000-dən çox film datasına malik olan, yüksək performanslı və peşəkar sənədləşdirilmiş bir REST API yaratmaqdır. Layihədə əsas hədəf böyük həcmli datanı (1,000+ records) idarə etmək, Redis vasitəsilə keşləmə tətbiq etmək və Full CRUD funksionallığını təmin etməkdir.

## Description
Problem Django Rest Framework (DRF) istifadə edilərək kompleks şəkildə həll olunub:

Data Significance (Question 2): 1,000-dən çox film datası xüsusi fill_data.py scripti vasitəsilə bazaya yüklənmişdir.

Redis Caching (Question 5): Performansı optimallaşdırmaq üçün django-redis inteqrasiya olunub. GET /api/movies/ endpointi 15 dəqiqəlik keşlənir.

Authentication & OAuth (Question 3, 4, 6): Sistem həm Token Authentication, həm də social auth (OAuth) strukturuna uyğun quraşdırılıb.

Pagination (Question 8): Böyük datanı idarə etmək üçün qlobal Pagination (hər səhifədə 20 element) tətbiq olunub.

Full CRUD (Question 9, 10, 11): ModelViewSet vasitəsilə resursların yaradılması (POST), yenilənməsi (UPDATE) və silinməsi (DESTROY) tam dəstəklənir.

Documentation (Question 12): Bütün endpointlər və interfeys drf-yasg (Swagger/OpenAPI) vasitəsilə interaktiv şəkildə sənədləşdirilib.

Deployment (Question 1): Layihə Render platformasında canlıya çıxarılıb və Cloud mühitində işləyir.

Project Links
Live API & Swagger Docs: https://my-api-fdpd.onrender.com/swagger/

GitHub Repository: https://github.com/Elsen675/my-api

## Installation
Virtual mühiti yaradın: python -m venv venv

Kitabxanaları yükləyin: pip install -r requirements.txt

Verilənlər bazasını hazırlayın: python manage.py migrate

Data Generatoru işlədin: python fill_data.py (1000+ data üçün)

Serveri başladın: python manage.py runserver

## Usage
Authentication
Token almaq üçün:
POST /api-token-auth/ (Body: username, password)

API Endpoints
List Movies (Cached & Paginated): GET /api/movies/

Create Movie: POST /api/movies/ (Auth Required)

Update Movie: PUT /api/movies/{id}/ (Auth Required)

Delete Movie: DELETE /api/movies/{id}/ (Auth Required)

## The Core Team
Elshan Ahmedov - Software Engineering Student at Qwasar SV.

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>