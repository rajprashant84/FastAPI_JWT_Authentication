# FastAPI Authentication with JWT

This project demonstrates how to implement authentication in a FastAPI application using JWT tokens. The project includes user creation, token generation, and protected routes.

## Project Structure



## Description

### Authentication Flow

1. **User Creation**:
   - Endpoint: `POST /users/`
   - Description: Creates a new user with a unique username and email. The password is hashed before storing in the database.

2. **Token Generation**:
   - Endpoint: `POST /token`
   - Description: Generates a JWT token for authenticated users. Requires `username` and `password`.

3. **Protected Route**:
   - Endpoint: `GET /users/me/`
   - Description: Retrieves details of the current authenticated user. Requires a valid JWT token.

### JWT Authentication

- **JWTBearer**: A custom dependency class that verifies the JWT token in the `Authorization` header of incoming requests.
- **Token Handling**: Functions to create and decode JWT tokens, and verify passwords.

### Database Models

- **User**: A model representing a user with fields for `id`, `username`, `hashed_password`, and `email`.
- **Post**: A model representing a post with fields for `id`, `title`, `content`, and `owner_id`.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rajprashant84/FastAPI_JWT_Authentication.git
   cd fFastAPI_JWT_Authentication



### Create and activate a virtual environment:

python -m venv venv

source venv/bin/activate # On macOS/Linux:
venv\Scripts\activate  # On Windows:


## Install the dependencies:
pip install -r requirements.txt
psql -U postgres -h localhost -d postgres -f sql/create_tables.sql

## Configure the environment variables:

Create a .env file in the root directory of your project and add the following content. Make sure to replace your_password and your_secret_key with your actual PostgreSQL password and a secret key for JWT encoding.

## Run the application:
uvicorn main:app --reload
