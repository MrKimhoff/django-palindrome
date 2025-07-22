# 🧠 Django Palindrome Checker

A clean and simple web app built with Django that allows users to check if a given string is a palindrome — and view a running history of their checks. Styled with Bootstrap 5 for a modern, responsive look.

![Screenshot](https://via.placeholder.com/800x400?text=Add+Your+Screenshot+Here)

---

## 🚀 Features

- ✅ Check if a string is a palindrome (ignoring case and punctuation)
- 📝 View recent palindrome check history
- 🗑️ Clear all historical entries with one click
- 🎨 Fully responsive design using Bootstrap 5
- 🧰 Built entirely in Python using the Django framework

---

## 📷 Demo

> _Insert a screenshot or link to a live version here if deployed_

---

## 🛠️ Tech Stack

- **Backend**: Django 4+
- **Frontend**: HTML5, Bootstrap 5
- **Database**: SQLite (default, easy to swap with PostgreSQL)
- **Python Version**: 3.10+

---

## 🧪 Palindrome Logic

The checker:
- Ignores punctuation, spaces, and letter casing
- Uses a clean Python utility function to determine palindrome status

```python
def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
```

---

## 🔧 Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/django-palindrome-checker.git
   cd django-palindrome-checker
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Visit in your browser:**

   ```
   http://localhost:8000/
   ```

---

## ✨ Bonus Features (Coming Soon?)

- [ ] User authentication
- [ ] Save history per user
- [ ] Search & filter history
- [ ] Deploy to the web with Render/Fly.io

---

## 📸 Screenshot

Feel free to take a screenshot of your running app and drop it into the repo (e.g., `screenshot.png`), then update the placeholder image above.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- Built with ❤️ by Taylor and Vera (your trusty coding assistant 😉)
- Powered by Django and Bootstrap
