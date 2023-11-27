# Django Hacker News Parser

This is a Django project that parses top 30 stories from Hacker News and stores them in a PostgreSQL database.

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

## Getting Started

### 1. Clone the repository:

    ```git clone https://github.com/IgChern/ParseDjango```

### 2. Build and run the Docker containers:

    ```docker-compose --build```

    ```docker-compose up -d```

### 4. Access the Django development server at:  
1. [http://127.0.0.1:8000/posts/](http://127.0.0.1:8000/posts/) - Parse Hacker News Website, stored 30 items in DataBase and returns 5  
2. [http://127.0.0.1:8000/posts/?offset=0&limit=10](http://127.0.0.1:8000/posts/?order=&offset=0&limit=10) - Returns data with options (offset, limit)  
3. [http://127.0.0.1:8000/posts?order=title](http://127.0.0.1:8000/posts?order=title) - Returns data with order (e.x. order=title, order=-title)  
4. [http://localhost:8000/posts/?order=-created&offset=0&limit=10](http://localhost:8000/posts/?order=-created&offset=0&limit=10) - Returns sorted data with offset/limit  

### 5. Check celery tasks:
    ```docker-compose logs celery-worker```
    ```docker-compose logs celery-beat```

### 6. Check DataBase locally with password 'postgres':

    ```psql -h localhost -U postgres -d postgres -p 5432```

### 7. Stop Docker containers:

    ```docker-compose down```



## Developer Information

Feel free to contact me for any questions or issues.

<a href="https://t.me/Igareokay" >
<img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
</a>
<a href="mailto:igchern95@gmail.com" >
<img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>