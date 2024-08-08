
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
   git clone https://github.com/your-username/fastapi-authentication-with-jwt.git
   cd fastapi-authentication-with-jwt
