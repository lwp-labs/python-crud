
# DevOps 3-Tier CRUD App (Flask + PostgreSQL + Redis)

This is a production-style **3-tier application** designed to showcase:

*  **Flask** (Web + Application Layer)
*  **PostgreSQL** (Database Layer)
*  **Redis** (Caching Layer)
*  **SQLAlchemy ORM**
*  **DevOps-style structure** with `.env`, logging, modularity

---

##  Project Structure

```
python-crud/
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

Install required packages:

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

##  Setup Instructions

### 1. Clone Repo & Set Up Python Environment

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

###  1. Set Password for postgres (optional)

```bash
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'devpass123';"
```

###  2. Create DB, User & Grant permissions

```bash
sudo -u postgres psql -c "CREATE DATABASE devopsdb;"
sudo -u postgres psql -c "CREATE USER devuser WITH ENCRYPTED PASSWORD 'devpass123';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE devopsdb TO devuser;"
sudo -u postgres psql -d devopsdb -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO devuser;"
sudo -u postgres psql -d devopsdb -c "GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO devuser;"
```

###  3. Apply SQL Schema

Use /tmp workaround**

```bash
cp db/init.sql /tmp/init.sql
sudo -u postgres psql -d devopsdb -f /tmp/init.sql
```

###  4. Verify from CLI

```bash
PGPASSWORD=devpass123 psql -U devuser -h localhost -d devopsdb -c '\dt'
PGPASSWORD=devpass123 psql -U devuser -h localhost -d devopsdb -c 'SELECT * FROM tasks;'
```

---

##  Environment Variables

Create `.env` in the root:

```env
DB_USER=devuser
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

App runs on:
 `http://localhost:5000`

---

##  Test the App

| URL                                                        | Function                     |
| ---------------------------------------------------------- | ---------------------------- |
| [http://localhost:5000](http://localhost:5000)             | View task list               |
| [http://localhost:5000/add](http://localhost:5000/add)     | Add new task                 |

---

##  Query DB from CLI

```bash
PGPASSWORD=devpass123 psql -U devuser -h localhost -d devopsdb -c 'SELECT * FROM task;'
```

---

##  Features to Showcase

* PostgreSQL queries via SQLAlchemy ORM
* Redis caching with visible performance boost
* Web-based CRUD operations
* CLI verification of database state
* Clean DevOps-style file structure

---

## Cleanup (optional)

```bash
sudo -u postgres psql -c "DROP DATABASE devopsdb;"
sudo -u postgres psql -c "DROP USER devuser;"
rm -rf ~/python-crud
```

---

## Credits

Built for **DevOps Full Stack Lab** by [Prayag Sangode](https://github.com/prayagsangode)


