# Django Hacker News Parser

This is a Django project that parses top stories from Hacker News and stores them in a PostgreSQL database.

## Setup

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

### Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

3. Access the Django development server at [http://localhost:8000/posts/],[http://127.0.0.1:8000/posts/].
http://localhost:8000/posts/?order=-created&offset=0&limit=10

## Project Structure

- **api_news:** Django project directory.
- **parse_app:** Django app responsible for parsing data.
- **parse_def.py:** Python script containing the parsing logic.
- **celery.py:** Configuration for Celery tasks.
- **Dockerfile:** Docker configuration.
- **docker-compose.yml:** Docker Compose configuration.
