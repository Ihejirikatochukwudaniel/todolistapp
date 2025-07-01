# 📋 To-Do List CLI Application

A powerful command-line interface for managing your daily tasks with persistent storage and an intuitive user experience.

## 🚀 Features

- ✅ **Add Tasks** - Create tasks with titles and optional descriptions
- 📋 **View Tasks** - Display all tasks or filter by completion status
- ✏️ **Update Tasks** - Modify existing task titles and descriptions
- 🗑️ **Delete Tasks** - Remove tasks with confirmation prompts
- ✅ **Complete/Uncomplete** - Mark tasks as done or pending
- 💾 **Persistent Storage** - All tasks saved automatically to JSON file
- 📊 **Statistics** - View completion rates and task summaries
- 🎯 **Unique IDs** - Easy task management with auto-generated IDs
- 📅 **Timestamps** - Track creation and completion dates
- 🛡️ **Error Handling** - Robust input validation and file operation safety

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Setup
1. Clone this repository:
```bash
git clone https://github.com/yourusername/todo-cli-app.git
cd todo-cli-app
```

2. Run the application:
```bash
python todo_app.py
```

## 📖 Usage

### Main Menu Options
When you run the application, you'll see a menu with the following options:

1. **➕ Add Task** - Create a new task
2. **📋 View All Tasks** - Display all tasks (completed and pending)
3. **👀 View Pending Tasks** - Show only incomplete tasks
4. **✏️ Update Task** - Modify an existing task
5. **✅ Complete Task** - Mark a task as completed
6. **🔄 Uncomplete Task** - Mark a completed task as pending
7. **🗑️ Delete Task** - Remove a task permanently
8. **📊 View Statistics** - Display task completion statistics
9. **❌ Exit** - Close the application

### Example Usage

```bash
# Start the application
python todo_app.py

# Follow the interactive prompts to:
# - Add your first task
# - View your task list
# - Complete tasks as you finish them
# - Delete tasks you no longer need
```

### Sample Task Flow
```
1. Add Task: "Complete Python project"
   Description: "Finish the CLI todo application for portfolio"

2. View Tasks: See your task with ID, creation date, and status

3. Complete Task: Mark task as done when finished

4. View Statistics: Check your productivity metrics
```

## 📁 File Structure

```
todo-cli-app/
│
├── todo_app.py          # Main application file
├── tasks.json           # Auto-generated task storage (created on first run)
├── README.md            # This file
└── .gitignore           # Git ignore file (optional)
```

## 🔧 Technical Details

### Data Structure
Tasks are stored as JSON objects with the following structure:
```json
{
  "id": 1,
  "title": "Task title",
  "description": "Optional description",
  "completed": false,
  "created_at": "2025-07-01T10:30:00.123456",
  "completed_at": null
}
```

### Libraries Used
- `json` - Data serialization and file storage
- `os` - File system operations
- `datetime` - Timestamp management
- `typing` - Type hints for better code documentation

## 🎯 Skills Demonstrated

This project showcases proficiency in:

- **Data Structures** - Lists and dictionaries for task management
- **Functions** - Modular, reusable code organization
- **File I/O** - JSON file handling for persistent storage
- **Error Handling** - Comprehensive input validation and exception management
- **Object-Oriented Programming** - Class-based application structure
- **User Experience** - Intuitive CLI interface with clear feedback
- **Code Documentation** - Type hints and comprehensive comments

## 🚀 Future Enhancements

Potential features for future versions:
- [ ] Task categories and tags
- [ ] Due dates and reminders
- [ ] Task priority levels
- [ ] Search and filter functionality
- [ ] Export tasks to different formats
- [ ] Task scheduling and recurring tasks
- [ ] Multiple task lists/projects

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Your Name**
- GitHub: Ihejirikatochukwudaniel
- LinkedIn:(https://www.linkedin.com/in/tochukwu-ihejirika-daniel-902a51203/)
- Email: tochukwuihejirika3@gmail.com

## 🙏 Acknowledgments

- Built as part of Python development portfolio
- Inspired by the need for simple, effective task management
- Thanks to the Python community for excellent documentation

---

⭐ **Star this repository if you found it helpful!** ⭐
