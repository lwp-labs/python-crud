# DevOps 3-Tier CRUD App (Flask + PostgreSQL + Redis)

This is a production-style 3-tier application designed to showcase:

- **Flask** (Web + Application Layer)
- **PostgreSQL** (Database Layer)
- **Redis** (Caching Layer)
- **SQLAlchemy ORM**
- **DevOps-ready structure** with `.env`, logging, modularity

---

## 📁 Project Structure

```
devops_crud_app/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── config.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── form.html
├── db/
│   └── init.sql
├── logs/
├── run.py
├── requirements.txt
├── .env
└── venv/
```

---

## ✅ Prerequisites

Make sure these are installed:

```bash
sudo apt update
sudo apt install -y python3-venv postgresql redis
```

Start services:

```bash
sudo systemctl start postgresql
sudo systemctl start redis
```

---

## 🚀 Setup Instructions

### 1. Clone the Repo & Create Virtual Environment

```bash
git clone https://github.com/YOUR_USERNAME/devops_crud_app.git
cd devops_crud_app
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 🛠️ PostgreSQL Setup

### 1. Create DB, User, and Table

```bash
sudo -u postgres psql -c "CREATE DATABASE devopsdb;"
sudo -u postgres psql -c "CREATE USER devuser WITH ENCRYPTED PASSWORD 'devpass123';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE devopsdb TO devuser;"
```

### 2. Initialize Table

```bash
sudo -u postgres psql -d devopsdb -f db/init.sql
```

### 3. Verify Table

```bash
PGPASSWORD=devpass123 psql -U devuser -h localhost -d devopsdb -c '\dt'
PGPASSWORD=devpass123 psql -U devuser -h localhost -d devopsdb -c 'SELECT * FROM tasks;'
```

---

## 📦 Environment Variables

Create a `.env` file at the root:

```env
DB_USER=devuser
DB_PASS=devpass123
DB_NAME=devopsdb
DB_HOST=localhost
DB_PORT=5432
REDIS_URL=redis://localhost:6379
```

---

## ▶️ Run the Flask App

```bash
source venv/bin/activate
python run.py
```

App will run on:  
📍 `http://localhost:5000`

---

## 🧪 Test the App

| URL                          | Function                    |
|-----------------------------|-----------------------------|
| http://localhost:5000       | View task list              |
| http://localhost:5000/add   | Add new task                |
| http://localhost:5000/clear | Clear Redis cache (optional) |

---

## 🗄️ Query DB from CLI

```bash
PGPASSWORD=devpass123 psql -U devuser -h localhost -d devopsdb -c 'SELECT * FROM tasks;'
```

---

## 🔥 Features to Showcase

- PostgreSQL queries via SQLAlchemy
- Redis caching with response-time difference
- CRUD via UI + CLI validation
- 3-tier application with clear separation
- DevOps-ready folder structure and `.env`

---

## 📌 Credits

Built for DevOps/Full Stack learning labs by [Prayag Sangode](https://github.com/prayagsangode)

---
