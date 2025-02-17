# Jurin1 Task Management Backend

## Project Description

This is the backend API for a task management application. It's built using Django and Django REST Framework and provides functionalities for:

- **User Authentication:** Registration and login using email and password.
- **Contact Management:** Creating, reading, updating, and deleting contacts.
- **Task Management:** Creating, reading, updating, and deleting tasks, including features like status, priority, due dates, categories, and subtasks (stored as JSON).
- **Urgent Task Listing:**  Retrieving a list of urgent and upcoming tasks.

you need the [frontend](https://github.com/jurin1/join_frontend) project to work.

## Technologies Used

- **Python:** Programming language
- **Django:**  High-level Python web framework
- **Django REST Framework:** Powerful toolkit for building Web APIs
- **SQLite:** Database (default for development, PostgreSQL recommended for production)
- **Docker & Docker Compose:** For containerization and easier development setup

## Setup Instructions

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)
- Docker and Docker Compose (for Docker setup)

### Development Setup (Without Docker)

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:jurin1/join_backend.git
    cd join_backend
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```
    The backend will be accessible at `http://localhost:8000` or `http://127.0.0.1:8000`.

5.  **Creat a super user:**
    ```bash
    python manage.py createsuperuser
    ```
    This creates a super user who can log in at http://localhost:8000/admin.

6.  ** (Optional) Creat a guest user:**
    ```bash
    python manage.py shell
    ```

    ```bash
    from django.contrib.auth.models import User
    User.objects.create_user(username='guest', email='guest@test.de', password='Test123!', first_name='Gast')
    ```

    ```bash
    exit()
    ```
    



### Docker Setup

1.  **Ensure Docker and Docker Compose are installed.**

2.  **Navigate to the project directory:**
    ```bash
    cd join_backend
    ```

3.  **Build and run the Docker containers:**
    ```bash
    docker-compose up --build
    ```
    The backend will be accessible at `http://localhost:8888`.

## API Endpoints

The API endpoints are located under the `/api/` path.

**User Authentication:**

-   **`POST /api/register/`**: Register a new user.
    -   Request body:
        ```json
        {
            "username": "your_username",
            "email": "your_email@example.com",
            "password": "your_password",
            "first_name": "Your First Name"
        }
        ```
-   **`POST /api/login/`**: Log in an existing user.
    -   Request body:
        ```json
        {
            "username": "your_email@example.com",  // Use email as username
            "password": "your_password"
        }
        ```
    -   Response: Returns a token for authentication and user information.
        ```json
        {
            "token": "your_auth_token",
            "name": "Your First Name",
            "userID": 1
        }
        ```
-   **`GET/PUT/PATCH /api/user/profile/`**: Get or update the logged-in user's profile.
    -   Requires authentication token in headers (`Authorization: Token your_auth_token`).

**Contacts:**

-   **`GET/POST /api/contacts/`**: List all contacts for the logged-in user or create a new contact.
    -   Requires authentication.
-   **`GET/PUT/PATCH/DELETE /api/contacts/{id}/`**: Retrieve, update, or delete a specific contact.
    -   Requires authentication.

**Tasks:**

-   **`GET/POST /api/tasks/`**: List all tasks for the logged-in user or create a new task.
    -   Requires authentication.
-   **`GET/PUT/PATCH/DELETE /api/tasks/{id}/`**: Retrieve, update, or delete a specific task.
    -   Requires authentication.
-   **`GET /api/urgent_tasks/`**: Get a list of urgent and upcoming tasks (excluding "done" tasks), ordered by due date.
    -   Requires authentication.

**Health Check:**

-   **`GET /api/healthcheck/`**:  Check if the backend is running. Returns a 200 OK status.

## Authentication

This backend uses Token-based authentication. After successful login, you receive an authentication token. You need to include this token in the `Authorization` header of your requests to access protected endpoints (contacts, tasks, user profile).

Example header: `Authorization: Token <your_auth_token>`

## Further Improvements

-   **Testing:** Implement unit and integration tests to ensure code reliability.
-   **API Documentation:** Generate more detailed API documentation using tools like Swagger or OpenAPI for better discoverability and usage.
-   **Database:** Consider using PostgreSQL for production environments for better performance and scalability compared to SQLite.
-   **Error Handling and Logging:** Enhance error handling and implement robust logging for debugging and monitoring.
-   **Input Validation:** Add more comprehensive input validation to serializers to handle edge cases and improve data integrity.
-   **Security:** Review security best practices and implement necessary measures, especially for production deployment.

---

This README provides a basic overview of the Jurin1 Task Management Backend. For more detailed information, please refer to the code and comments within the project.
