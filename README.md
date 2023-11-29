# Django Hacker News Parser on REST Framework

This is a Django REST Framework project that parses with Celery top 30 stories from Hacker News and stores them in a PostgreSQL database.

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

## Getting Started

### 1. Clone the repository:

    git clone https://github.com/IgChern/ParseDjango/tree/rest

### 2. Change directory:

    cd ParseDjango

### 3. Make .env file with your own settings (or you can use it locally without .env):

    POSTGRES_ENGINE=<your_settings>
    POSTGRES_NAME=<your_settings>
    POSTGRES_USER=<your_settings>
    POSTGRES_PASSWORD=<your_settings>
    POSTGRES_HOST=<your_settings>
    POSTGRES_PORT=<your_settings>
    CELERY_BROKER_URL=<your_settings>
    CELERY_RESULT_BACKEND=<your_settings>

### 4. Build and run the Docker containers:

    docker-compose build

    docker-compose up

### 5. Access the Django development server at:  
1. [http://127.0.0.1:8000/api/posts/](http://127.0.0.1:8000/api/posts/) - Returns last 5 stories from database 
2. [http://127.0.0.1:8000/api/posts/?offset=0&limit=10](http://127.0.0.1:8000/api/posts/?order=&offset=0&limit=10) - Returns stories with options (offset, limit)  
3. [http://127.0.0.1:8000/api/posts?order=title](http://127.0.0.1:8000/api/posts?order=title) - Returns stories with order (e.x. order=title, order=-title)  
4. [http://127.0.0.1:8000/api/posts/?order=-created&offset=0&limit=10](http://127.0.0.1:8000/api/posts/?order=-created&offset=0&limit=10) - Returns sorted stories with order, offset and limit  

### 6. Check celery tasks:

    docker-compose logs celery-worker
    
    docker-compose logs celery-beat

### 7. Check DataBase locally with password 'postgres':

    psql -h localhost -U postgres -d postgres -p 5432

### 8. Stop Docker containers:

    docker-compose down



## Developer Information

Feel free to contact me for any questions or issues.

<a href="https://t.me/Igareokay" >
<img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
</a>
<a href="mailto:igchern95@gmail.com" >
<img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>