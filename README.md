# ☄️ TaskOrbit — IT Task Management System

**TaskOrbit** is a custom-built task management solution tailored for IT teams. It combines robust project tracking functionality with a cutting-edge **Glassmorphism** interface. Designed for teams who have outgrown generic tools and want a futuristic, clean workspace to manage their development lifecycle.

👉 **[Live Demo — Explore TaskOrbit](https://it-task-manager-4458.onrender.com)**

---

## 🚀 Key Features
* **Task Management:** Create, update, and track development tasks from inception to completion.
* **Team Collaboration:** Assign tasks to multiple team members and track their progress.
* **Role-Based Structure:** Organize your team by positions such as Developer, QA, Project Manager, or Designer.
* **Prioritization:** Built-in deadline tracking and urgency levels (Urgent, High, Medium, Low).
* **Modern UX/UI:** A fully responsive interface powered by the **Quartz** theme and custom glassmorphism CSS effects.

---

## 🏗️ Database Architecture
The project is built on a structured relational database model to ensure data integrity and scalability:

* **Worker:** An extended user model (`AbstractUser`) linked to specific professional positions.
* **Position:** Defines team roles (e.g., DevOps, Designer, QA).
* **Task:** The core entity containing descriptions, deadlines, priority levels, and task types.
* **TaskType:** Categories for organizing work (e.g., Bug, New Feature, Refactoring).

---

## 🎨 Design Philosophy
TaskOrbit moves away from the "standard" look of enterprise software, focusing on:
* **Glassmorphism:** UI panels with backdrop-blur effects for a modern, layered feel.
* **Interactive Elements:** Smooth transitions and neon hover glows for better engagement.
* **Visual Hierarchy:** A clean, distraction-free environment with a focus on typography and readability.
* **Mobile Ready:** A custom offcanvas navigation system ensures the app works perfectly on small screens.

---

## 🛠️ Technology Stack
* **Framework:** Django 6.0 (Class-Based Views)
* **Database:** PostgreSQL (Hosted on Neon)
* **Deployment:** Render (Web Service architecture)
* **Frontend:** Bootstrap 5, Bootswatch (Quartz theme), FontAwesome 6
* **CSS Customization:** Advanced CSS for glass effects and global UI normalization.
* **Testing:** Django TestCase for model logic and view accessibility.

---

## ⚙️ Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/DenysHalytskyi/it-task-manager.git](https://github.com/DenysHalytskyi/it-task-manager.git)
   cd it-task-manager
   ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
   
3. **Install dependencies:**
    ```bash
      pip install -r requirements.txt
    ```

4. **Environment Variables:**
   
   Create a ``` .env``` file in the root directory and add your secret key and database configuration variables.

5. **Launch the project:**
    ```bash
      python manage.py migrate
      python manage.py runserver
    ```

---

## 🧪 Testing

The application includes a suite of tests to verify model behavior and page availability:

```bash
   python manage.py test
```
