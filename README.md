# Mini ERP System

A production-ready, modular Mini ERP backend built with Django and Django REST Framework. This project manages Products, Customers, Sales Orders, and automated Stock Movement logging with role-based access control.

## 🚀 Features

- **Authentication**: Secure JWT-based login and registration.
- **Role-Based Access Control**:
  - **Admin**: Full access (CRUD) to all modules.
  - **Sales User**: Can view products/customers, create orders, and add customers (No Delete/Edit rights for products).
- **Stock Management**: Automatic deduction on order confirmation and restoration on cancellation.
- **Audit Logs**: Full inventory movement tracking for every transaction.
- **Live Dashboard**: Real-time stats for total customers, daily sales, and low-stock alerts.
- **API Docs**: Integrated Swagger UI.

---

## 🛠 Tech Stack

- **Backend**: Django 4.2+ & Django REST Framework
- **Auth**: SimpleJWT
- **Database**: SQLite
- **Documentation**: drf-spectacular (OpenAPI 3.0)

---

## ⚙️ How to Run the Project

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Setup & Installation
Open your terminal and navigate to the project directory:

```bash
cd mini_erp
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run Migrations
Prepare the database:
```bash
python manage.py migrate
```

### 4. Start the Development Server
```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000/`

---

## 🔑 Default Credentials

For immediate testing, use the pre-seeded admin account:
- **Username**: `admin`
- **Password**: `admin123`

---

## 📍 API Documentation

Explore and test the API endpoints using the interactive Swagger UI:
🔗 **[http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)**

### Main Endpoints:
- `POST /api/auth/login/` - Get Access Token
- `GET /api/products/` - List/Search Products
- `POST /api/orders/` - Create Sales Order
- `GET /api/dashboard/stats/` - View Business Analytics
- `GET /api/inventory/` - View Stock Logs
