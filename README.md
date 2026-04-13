# Welcome to My Movie API
***

## Task
Bu layihənin məqsədi 1000-dən çox film datasına malik olan, performanslı və sənədləşdirilmiş bir REST API yaratmaq idi. Əsas çətinlik böyük həcmli datanı SQLite-a sürətli köçürmək, Redis vasitəsilə keşləmək və Swagger (OpenAPI) sənədləşməsini qurmaq idi.

## Description
Problem Django Rest Framework (DRF) istifadə edilərək həll olunub:
- **Data:** 1000 film datası xüsusi script vasitəsilə bazaya yüklənib.
- **Cache:** Performansı artırmaq üçün Redis keşləmə sistemi tətbiq olunub.
- **Security:** API-yə giriş Token Authentication ilə qorunur.
- **Documentation:** Bütün endpointlər drf-yasg (Swagger) vasitəsilə avtomatik sənədləşdirilib.
- **Deployment:** Layihə Render platformasında canlıya (Live) çıxarılıb.

## Project Links
- **Live API & Swagger:** [https://my-api-fdpd.onrender.com/swagger/](https://my-api-fdpd.onrender.com/swagger/)
- **GitHub Repository:** [https://github.com/Elsen675/my-api](https://github.com/Elsen675/my-api)

## Installation
Layihəni lokalda işə salmaq üçün:
1. Virtual mühiti yaradın və aktivləşdirin: `python -m venv venv`
2. Kitabxanaları yükləyin: `pip install -r requirements.txt`
3. Miqrasiyaları edin: `python manage.py migrate`
4. Serveri başladın: `python manage.py runserver`

## Usage
API-nin canlı versiyasına və Swagger sənədləşməsinə buradan baxa bilərsiniz:
`https://my-api-fdpd.onrender.com/swagger/`

Token almaq üçün:
`POST /api-token-auth/` (username və password ilə)

Filmləri siyahılamaq:
`GET /api/movies/`

### The Core Team
**Elshan Ahmedov** - Software Engineering Student at Qwasar SV.

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>