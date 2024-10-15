# analyze-audio

## Key Features

### 1. **Audio Analysis and Prompt Generation**
   - The system is designed to handle audio input, break it down into prompts, and store those prompts in a PostgreSQL database.
   - It supports integrations with various APIs or local models for processing audio, allowing flexibility in how audio is transcribed into text prompts.
   - Prompts are stored alongside task metadata, including the audio file reference, task name, and user ownership.

### 2. **Task Management (CRUD)**
   - **GET**: Retrieve task details based on the task ID.
   - **POST**: Create a new task, including the name and prompts.
   - **PUT**: Update an existing task’s name or prompts using batch updates.
   - **DELETE**: Remove a task by its ID, supporting batch deletion for efficiency.
   - Each task is linked to a user, ensuring multi-tenancy and data isolation per user.

### 3. **User Authentication**
   - Implements a secure authentication mechanism using JWT tokens.
   - Endpoints include user registration, login, and logout.
   - Protected routes for task management are accessible only to authenticated users, ensuring data security.

### 4. **Modern, Scalable Architecture**
   - Built with **FastAPI**, providing fast, asynchronous support for high-performance needs.
   - Uses **PostgreSQL** for relational data management, ensuring reliable storage.
   - Designed with modularity and extensibility in mind, enabling future expansion without sacrificing performance or maintainability.

### 5. **Dockerized for Portability**
   - Complete Docker support, including a `docker-compose.yml` configuration to quickly spin up the application and its dependencies.
   - Application and database run as separate services, ensuring clean separation of concerns and making the project easy to scale and deploy.

## Getting Started

### Prerequisites

- **Docker**: Ensure that Docker and Docker Compose are installed on your machine.
- **Python 3.9+**: If running locally without Docker.
- **PostgreSQL**: If running locally without Docker, ensure that PostgreSQL is installed and running.

### Installation and Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Environment Configuration**:
   - The database connection URL and other environment variables can be adjusted in the `docker-compose.yml` file and the application’s `database.py` configuration.

3. **Build and run the application with Docker**:

   ```bash
   docker-compose up --build
   ```

   This will spin up both the FastAPI application and the PostgreSQL database. The API will be available at `http://localhost:8000`.

4. **Access API Documentation**:

   You can access the auto-generated API documentation provided by FastAPI via:

   - **Swagger UI**: `http://localhost:8000/docs`
   - **ReDoc**: `http://localhost:8000/redoc`

### Running Locally Without Docker

1. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up the Database**:

   Ensure that PostgreSQL is installed and running, and create a database for the application. Update the connection string in `app/database.py`.

3. **Run the Application**:

   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

### Authentication Endpoints

- **POST /register**: Register a new user by providing a username, password, and email.
- **POST /login**: Authenticate the user and receive a JWT token for subsequent requests.
- **GET /user**: Retrieve the authenticated user's profile.
- **POST /logout**: Log out the user (handled on the client side by discarding the token).

### Task Endpoints

- **POST /tasks**: Create a new task with prompts.
- **GET /tasks/{task_id}**: Retrieve task details by ID.
- **PUT /tasks/{task_id}**: Update a task’s name or prompts.
- **DELETE /tasks/{task_id}**: Delete a task by ID.

### Database Structure

The application uses PostgreSQL to store:
- **Users**: Authenticated users with secure hashed passwords.
- **Tasks**: Tasks linked to users, containing audio links and prompt data.

## Project Structure

```
├── app/
│   ├── main.py            # Main FastAPI application
│   ├── models.py          # SQLAlchemy models for users and tasks
│   ├── schemas.py         # Pydantic schemas for request/response validation
│   ├── crud.py            # Database operations for tasks and users
│   ├── auth.py            # Authentication-related logic (JWT, password hashing)
│   ├── database.py        # Database connection setup
├── Dockerfile             # Dockerfile for FastAPI app
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

## Testing

- Unit and integration tests should be added for all major components, including the authentication system and task management.
- FastAPI's built-in testing framework (based on **pytest**) can be used for writing and running tests.

## Future Improvements

1. **Audio Processing Enhancements**:
   - Implement more sophisticated models for audio transcription.
   - Add support for various audio formats and asynchronous processing for larger files.

2. **Task Management**:
   - Implement tagging and categorization for tasks.
   - Add support for task history and version control.

3. **Authentication & Security**:
   - Implement multi-factor authentication (MFA).
   - Add role-based access control (RBAC) for more granular permission management.

4. **Deployment**:
   - Provide a CI/CD pipeline for automated deployment to cloud environments.

