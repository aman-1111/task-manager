# ✅ Task Manager App using Python

A simple and user-friendly task management application built using Python. It helps users add, update, delete, and track their daily tasks with persistent storage.

## ✨ Features

- ➕ Add new tasks with title and optional description
- ✅ Mark tasks as completed
- 🗑️ Delete tasks
- 📝 Edit/update existing tasks
- 💾 Save and load tasks using JSON or CSV
- 🖥️ Optional GUI interface using Tkinter
- 📋 View all pending and completed tasks
- ⏳ Time-based sorting (optional)

## 🛠️ Technologies Used

- Python 3
- `json` or `csv` for storage
- `tkinter` for GUI (optional)
- `datetime` for timestamps
- `os` and `sys` for system-level operations

## 📁 Project Structure

task-manager/
│
├── task_manager.py # CLI version of the app
├── gui.py # Optional GUI version using Tkinter
├── storage_handler.py # Handles saving/loading tasks
├── tasks.json # JSON file with saved tasks
├── requirements.txt # Dependencies
└── README.md # Project documentation


## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/task-manager-python.git
cd task-manager-python

2. (Optional) Create a Virtual Environment

python -m venv venv
source venv/bin/activate        # For Linux/Mac
venv\Scripts\activate           # For Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run the Application

python task_manager.py          # Run CLI version
python gui.py                   # Run GUI version (optional)

📊 Example Use (CLI)

    Add a Task:

Title: Complete Python Assignment
Description: Finish by tonight
Status: Pending

Mark as Done:

    Task ID: 3
    ✅ Task marked as completed.

📄 License

This project is open-source and available under the MIT License.
🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
🔗 Connect with Me

Aman Chaurasia
📧 amanchaurasia687@gmail.com
