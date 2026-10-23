# 📝 Flask To-Do Web Application

A modern, responsive, and robust **To-Do Web Application** built using Python's Flask framework, Flask-SQLAlchemy (SQLite database), and Bootstrap CSS. This project features full CRUD operations along with an advanced search mechanism to manage and organize daily tasks efficiently.

## 🚀 Features

- **Full CRUD Operations:** Seamlessly Create, Read, Update, and Delete your daily tasks.
- **Advanced Search Engine:** Uses SQLAlchemy's `or_` and `ilike` operators to perform real-time, case-insensitive keyword searches across task titles and descriptions.
- **Data Persistence:** Integrated with a secure, lightweight local `SQLite` database managed via SQLAlchemy.
- **Responsive UI:** Styled beautifully using Bootstrap 5 to ensure a perfect look on both desktop and mobile screens.
- **Auto Timestamps:** Automatically records the exact time of creation for each task using `datetime.utcnow`.

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask
- **Database:** Flask-SQLAlchemy (SQLite)
- **Frontend:** HTML5, CSS3, Bootstrap 5

## 💻 Installation & Setup Instructions

Follow these simple steps to get this project running on your local machine:

### 1. Navigate to Project Folder
Open your terminal or command prompt and move into the project directory:
```bash
cd your-todo-project-folder
```

### 2. Install Required Dependencies
Run the following command to install Flask and the SQLAlchemy database library:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the Flask local development server by executing your main Python file:
```bash
python app.py
```

### 4. Access in Browser
Once the server starts, open your favorite web browser and navigate to:
```text
http://127.0.0
```

## 📂 Project Structure

```text
├── app.py               # Main Flask application file containing all routes
├── instance/
│   └── todo.db          # Auto-generated SQLite database file
└── templates/           # Folder containing all frontend HTML views
    ├── index.html       # Home Dashboard (Lists all active To-Dos)
    ├── update.html      # Form view to modify existing tasks
    ├── search.html      # Dynamic view displaying query search results
    ├── about.html       # About page for the application
    └── contact.html     # Contact page for user queries
```

## 🛑 Important Note on Future Upgrades
In newer versions of Python/SQLAlchemy, it is recommended to replace `datetime.utcnow` with `datetime.now(datetime.timezone.utc)` for better, timezone-aware timestamp management.

---

## 👨‍💻 Author & Project Credits

This project was envisioned, logically designed, and self-coded by:
* **Rahul Rayjada** 🚀

*Built with consistency, continuous logic-building, and self-taught Python expertise.*
