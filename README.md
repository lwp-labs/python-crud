
# DevOps 3-Tier CRUD App (Flask + PostgreSQL + Redis)

This project is a production-style **3-tier CRUD application** to demonstrate:

* **Flask** – Web + App Layer
* **PostgreSQL** – Database Layer
* **Redis** – Caching Layer
* **SQLAlchemy ORM** – DB Abstraction
* **DevOps-ready structure** – Modular, `.env`-driven, logs, CLI + UI support

---

##  Project Structure

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

##  Prerequisites

```bash
sudo apt update
sudo apt install -y python3-venv postgresql redis
sudo systemctl start postgresql
sudo systemctl start redis
```

---

##  Setup Instructions

### 1. Clone & Setup Python Virtual Environment

```bash
git clone https://github.com/YOUR_USERNAME/python-crud.git
cd python-crud
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

##  PostgreSQL Setup

### 1. Set Password for Postgres User

```bash
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'devpass123';"
```

### 2. Create Database and Schema (Table + Sample Data)

```bash
cat > db/init.sql <<EOF
DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO tasks (title, description) VALUES
('Initial Setup', 'App + DB + Redis up and running!');
EOF
```

```bash
sudo -u postgres psql -c "CREATE DATABASE devopsdb;"
sudo -u postgres psql -d devopsdb -f db/init.sql
```

---

##  Environment Variables

Create a `.env` file at project root:

```env
DB_USER=postgres
DB_PASS=devpass123
DB_NAME=devopsdb
DB_HOST=localhost
DB_PORT=5432
REDIS_URL=redis://localhost:6379
```

---

##  Run the Flask App

```bash
source venv/bin/activate
python run.py
```

App will run on:
 `http://localhost:5000`

---

##  Test the App

| URL                           | Description       |
| ----------------------------- | ----------------- |
| `http://localhost:5000`       | View task list    |
| `http://localhost:5000/add`   | Add a new task    |
| `http://localhost:5000/clear` | Clear Redis cache |

Each task created via the UI is stored in **PostgreSQL** and cached in **Redis**. Repeated access will show faster response times from cache.

---

##  Check Database from CLI

```bash
PGPASSWORD=devpass123 psql -U postgres -h localhost -d devopsdb -c '\dt'
PGPASSWORD=devpass123 psql -U postgres -h localhost -d devopsdb -c 'SELECT * FROM tasks;'
```

---

##  Redis Testing from CLI

Check if Redis is caching the content:

```bash
redis-cli
> KEYS *
> GET task_cache_all
```

Clear cache:

```bash
> DEL task_cache_all
```

---

##  Key Concepts You’ll Demonstrate

* Fast vs slow load times (Redis vs PostgreSQL)
* Caching logic in code (Jinja + Redis)
* Environment-based config using `.env`
* Python packaging + `venv`
* DevOps-style separation of concerns

---

##  Credits

Created by [Prayag Sangode](https://github.com/prayagsangode) for real-world DevOps showcase labs and training.

---


