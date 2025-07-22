# 📝 Blogging Platform API (RESTful)
https://roadmap.sh/projects/blogging-platform-api
A REST API for managing blog articles with full CRUD functionality, built with Flask and MySQL.

## ✨ Features
- **Full CRUD Operations**:
  - Create, Read, Update, and Delete blog articles
  - Partial updates supported
- **RESTful Design**:
  - Proper HTTP methods and status codes
  - JSON request/response format
- **MySQL Backend**:
  - Persistent data storage
  - Efficient querying

## 🚀 API Endpoints

| Method | Endpoint          | Description                          | Required Fields                     |
|--------|-------------------|--------------------------------------|-------------------------------------|
| GET    | `/posts`          | List all articles                    | -                                   |
| POST   | `/posts`          | Create new article                   | `title`, `content`, `category`, `tags` |
| GET    | `/posts/<int:id>` | Get specific article                 | -                                   |
| PUT    | `/posts/<int:id>` | Full article update                  | All fields                          |
| PATCH  | `/posts/<int:id>` | Partial article update               | Any field(s)                        |
| DELETE | `/posts/<int:id>` | Delete article                       | -                                   |

## 🛠️ Tech Stack

### Backend
- **Python** (3.13)
- **Flask** (Web framework)
- **SQLAlchemy** (ORM)
- **Flask-RESTful** (API extensions)

### Database
- **MySQL** (Relational database)

### Development Tools
- **Git** (Version control)
- **Pip** (Package management)

## 🏗️ Project Structure

```
blogging-platform/
├── api/                   # Core application
│   ├── __init__.py        # App factory
│   ├── blog.py            # API routes/controllers
│   ├── database_access.py # DB operations
│   ├── extensions.py      # Flask extensions
│   ├── models.py          # Database models
├── requirements.txt       # Dependencies
├── README.md              # This file
```

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.13
- MySQL Server
- Git (optional)

### Setup Instructions

1. **Clone repository**:
   ```bash
   git clone https://github.com/pantacrazy/Blogging-Platform-API
   cd blogging-platform
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database configuration**:
   - Create MySQL database:
     ```sql
     CREATE DATABASE blog_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
     ```
   - Update connection settings in `api/__init__.py`:
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost:3306/blog_db'
     ```

5. **Run the application**:
   ```bash
   flask run
   ```

## 🚦 Usage Examples

### Create Article
```bash
curl -X POST http://localhost:5000/posts \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Getting Started with Flask",
    "content": "Flask is a micro web framework...",
    "category": "Programming",
    "tags": ["python", "web"]
  }'
```

### Get All Articles
```bash
curl http://localhost:5000/posts
```

### Update Article (Partial)
```bash
curl -X PATCH http://localhost:5000/posts/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Title"}'
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| MySQL Connection Error | Verify credentials in config |
| 500 Server Error | Check Flask debug logs |
