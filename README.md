# FastAPI User Authentication System

A robust user authentication system built with FastAPI and MongoDB, featuring JWT-based authentication and role-based access control (RBAC).

## ✅ Features Implemented

### Must Have Requirements
- [x] Login and logout endpoints with JWT token support
- [x] Secure endpoints for user CRUD operations
- [x] Clean, readable, and well-documented code
- [x] Direct MongoDB integration (No ODM)
- [x] User creation script for initialization

### Good to Have Requirements
- [x] Comprehensive logging across all API endpoints using Loguru
- [x] Predefined Pydantic models for:
  - User management
  - Token handling
  - Request/Response validation
- [x] MongoDB Atlas support for cloud database
- [x] Scalable code structure with separate modules for:
  - Routes
  - Models
  - Core functionality
  - Configuration

### Added Bonus
- [x] Role-Based Access Control (RBAC) with admin and user roles
- [x] Ready for deployment on serverless platforms

## 🛠️ Technology Stack

- **FastAPI**: Modern web framework for building APIs
- **MongoDB**: NoSQL database for data storage
- **JWT**: JSON Web Tokens for secure authentication
- **Pydantic**: Data validation using Python type annotations
- **Motor**: Async MongoDB driver
- **Loguru**: Logging made simple and effective

## 📋 Prerequisites

- Python 3.8+
- MongoDB (local or Atlas URL)
- pip (Python package manager)

## ⚙️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update the following variables:
```env
MONGODB_URL=your_mongodb_url
JWT_SECRET=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🚀 Getting Started

1. Start the application:
```bash
uvicorn main:app --reload
```

2. Create initial admin user:
```bash
python scripts/create_user.py
```

3. Access the API documentation:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## 🔐 API Endpoints

### Authentication
- `POST /auth/login`: User login
  - Request body: `{"email": "string", "password": "string"}`
  - Returns JWT token

- `POST /auth/logout`: User logout
  - Requires JWT token

### User Management
- `GET /users/`: Get all users (Admin only)
- `GET /users/{user_id}`: Get specific user
- `POST /users/`: Create new user
- `PUT /users/{user_id}`: Update user
- `DELETE /users/{user_id}`: Delete user

## 🔑 Role-Based Access

The system implements two roles:
- **Admin**: Full access to all endpoints
- **User**: Limited access to user-specific endpoints

## 📁 Project Structure

```
.
├── README.md
├── requirements.txt
├── main.py
├── .env
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   ├── routes/
│   ├── core/
│   └── schemas/
└── scripts/
    └── create_user.py
```

## 🔒 Security Features

- Password hashing using bcrypt
- JWT token-based authentication
- Role-based access control
- Secure password storage
- Request validation using Pydantic
- Protected routes using dependencies

## 📝 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| MONGODB_URL | MongoDB connection URL | - |
| JWT_SECRET | Secret key for JWT | - |
| JWT_ALGORITHM | Algorithm for JWT | HS256 |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token expiration time | 30 |

## 🧪 Testing

To run the tests:
```bash
pytest
```

## 📈 Logging

Logs are stored in:
- Console output
- `logs/app.log` file

## 🚀 Deployment

The application is designed to be deployed on any serverless platform that supports Python/FastAPI.

Common deployment platforms:
- AWS Lambda
- Google Cloud Functions
- Azure Functions
- Heroku
- Digital Ocean

## 📌 Future Improvements

Potential enhancements:
1. Refresh token implementation
2. Rate limiting
3. OAuth2 integration
4. Email verification
5. Password reset functionality

## 👥 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
