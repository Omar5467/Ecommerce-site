# Django Advanced E-Commerce Platform 🛒🚀

Welcome to the **Django E-Commerce Platform**, a production-ready, highly secure, and optimized backend system built for modern digital commerce. This project demonstrates enterprise-level development practices using Python and Django, focusing on database optimization, secure checkout flows, and scalable API architecture.

---

## 🛠️ Tech Stack & Key Features

* **Backend Framework:** Python 3.x & Django Web Framework.
* **Database Management:** PostgreSQL / SQLite (with production-ready index optimizations).
* **Security First:** Custom Authentication, JWT/Session tokens, and protection against CSRF/XSS.
* **Asynchronous Tasks:** Configured for background task execution (e.g., Order confirmations, transactional emails).

---

## 🏗️ System Architecture & Database Design

The platform architecture splits responsibilities cleanly between modular Django apps to handle high concurrent traffic seamlessly:

* **Product Catalog:** Optimized using database indexing on search fields (slugs, categories) and customized querying (`select_related` and `prefetch_related`) to eliminate the **N+1 query problem**.
* **Cart & Order Flow:** Atomic database transactions (`transaction.atomic`) to ensure accurate stock updates during checkout and prevent race conditions.
* **User Management:** Custom user models supporting secure role-based access control (RBAC).

---

## 🚀 Installation & Local Setup

Follow these structured steps to set up and run the development server locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/Omar5467/Ecommerce-site.git](https://github.com/Omar5467/Ecommerce-site.git)
cd Ecommerce-site


# Create environment
python -m venv venv

# Activate environment (Linux/macOS)
source venv/bin/activate

# Activate environment (Windows)
venv\Scripts\activate

#Install Dependencies
pip install -r requirements.txt

#Database Migrations & Superuser
python manage.py makemigrations
python manage.py migrate

# Create administrative account
python manage.py createsuperuser

#Run the Server
python manage.py runserver

Navigate to
http://127.0.0.1:8000/
in your browser.
