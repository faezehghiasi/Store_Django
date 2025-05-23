# 💎 LUXE – Django E-commerce Website

LUXE is a stylish online jewelry store built with Django. It includes a full shopping experience from product browsing to checkout and payment integration using Zarinpal.

## 🌟 Features

- ✅ User registration with email verification
- 🔐 Secure login/logout system
- 🛒 Product browsing and shopping cart
- 💳 Checkout process with Zarinpal payment gateway
- 📦 Order confirmation and invoice
- 📧 Email notifications for verification and order confirmation
- 🎨 Responsive frontend design

## 🛠️ Tech Stack

- **Backend**: Django 5+
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: SQLite (development)
- **Payment Gateway**: [Zarinpal](https://www.zarinpal.com)
- **Email**: Django email backend (SMTP)

## 🧾 Project Structure

```
store/
├── account/           # Handles user registration, login, email verification
├── core/              # Main e-commerce logic: products, cart, checkout
├── media/             # Uploaded images (e.g. product covers)
├── templates/         # HTML templates for all views
└── store/             # Django project settings
```

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/faezehghiasi/luxe-Store-Django.git
cd luxe-Store-Django
```

### 2. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure .env (optional)

Set up your environment variables (email backend, secret key, Zarinpal config).

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Run the server

```bash
python manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 💸 Zarinpal Integration

The project is integrated with Zarinpal sandbox for payment. You can configure the merchant ID and environment in settings.

## 📬 Email Verification

Users must verify their email before logging in. Make sure you have a working email backend set in `settings.py` for this to work.

## 📷 Screenshots
![Screenshot from 2025-05-14 16-53-50](https://github.com/user-attachments/assets/5945c1b7-0f65-482a-b2ee-f85dee10fdc6)
![Screenshot from 2025-05-14 16-53-02](https://github.com/user-attachments/assets/dea494f1-90fa-4da9-a2e5-57033b73f230)
![Screenshot from 2025-05-14 16-53-50](https://github.com/user-attachments/assets/08be0348-7713-4f4b-909e-41ac79b27286)
![Screenshot from 2025-05-14 16-54-10](https://github.com/user-attachments/assets/232b2168-d3f6-4d3a-8597-6edfe9c43910)
![Screenshot from 2025-05-14 16-54-21](https://github.com/user-attachments/assets/a5a66437-2176-497c-b9e2-b3f8a6cb57f8)
![Screenshot from 2025-05-14 16-58-13](https://github.com/user-attachments/assets/34da2270-bbeb-44cc-8a29-3c62358dcdf3)

## 👤 Author

- Faezeh Ghiasi – [GitHub](https://github.com/faezehghiasi)

