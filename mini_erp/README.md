# Mini ERP System - Django REST API

A comprehensive, production-ready Mini ERP backend built with Django and Django REST Framework. This project manages Products, Customers, Sales Orders, and automated Stock Movement logging with role-based access control (Admin/Sales).

## 🚀 Key Features

- **Authentication**: Secure JWT-based login and registration.
- **Role-Based Access Control**:
  - **Admin**: Full access to all modules and configurations.
  - **Sales User**: Restricted access (Create orders, view products, add/view customers).
- **Product Management**: Support for image uploads via a dedicated file service.
- **Stock Lifecycle Logic**: Automatic stock deduction on order confirmation and full restoration on cancellation.
- **Automated Stock Logging**: System-generated audit trail for every stock movement (Sale, Restock, Cancel).
- **Live Dashboard**: Real-time stats for total customers, daily sales totals, and low-stock alerts.
- **Advanced API Features**: Global pagination (10 per page), dynamic search, and multi-field filtering.
- **Interactive Documentation**: Full Swagger UI integration.

---

## 🛠 Tech Stack

- **Backend**: Django 4.2+ & Django REST Framework
- **Auth**: SimpleJWT
- **Documentation**: drf-spectacular (OpenAPI 3.0)
- **Database**: SQLite (Default)
- **Media**: Pillow for image processing

---

## ⚙️ Setup & Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install Pillow
   ```

2. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

---

## 🔑 Default Admin Account

An admin account is pre-seeded for immediate testing:
- **Username**: `admin`
- **Password**: `admin123`

---

## 📍 API Endpoints

### 1. Authentication (`/api/auth/`)
- `POST /register/`: New user signup.
- `POST /login/`: Obtain JWT tokens.
- `GET /me/`: Current user profile.

### 2. Products (`/api/products/`) - *Supports Multipart/Form-Data*
- `GET /`: List products (Search by name/SKU/category, Filter by category).
- `POST /`: Create with **image upload** (Admin only).
- `PATCH /{id}/`: Update details or image (Admin only).

### 3. Customers (`/api/customers/`)
- `GET /`: List customers (Search by name/phone/email).
- `POST /`: Add new customer.

### 4. Sales Orders (`/api/orders/`)
- `POST /`: Create order with nested items.
- `PATCH /{id}/`: Update status (`CONFIRMED` triggers stock reduction).

### 5. Inventory (`/api/inventory/`)
- `GET /`: View automated stock logs.
  - *Admin*: All logs.
  - *Sales*: Personal logs only.

### 6. Dashboard (`/api/dashboard/`)
- `GET /stats/`: View real-time business metrics.

---

## 📖 API Documentation

Access the Swagger UI for testing:
🔗 **[http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)**

---

## 📂 Architecture Note
This project uses a **Service-Oriented Architecture**. Business logic (like stock updates and file uploads) is decoupled from views into dedicated service files located in `apps/*/services/` and `core/services/` for maximum maintainability.
