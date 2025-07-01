#!/usr/bin/env python3
"""
To-Do List CLI Application
A command-line interface for managing tasks with persistent storage.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional

class TodoApp:
    def __init__(self, filename: str = "tasks.json"):
        """Initialize the TodoApp with a filename for persistent storage."""
        self.filename = filename
        self.tasks = self.load_tasks()
        self.next_id = self._get_next_id()
    
    def _get_next_id(self) -> int:
        """Get the next available task ID."""
        if not self.tasks:
            return 1
        return max(task['id'] for task in self.tasks) + 1
    
    def load_tasks(self) -> List[Dict]:
        """Load tasks from JSON file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as file:
                    return json.load(file)
            return []
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading tasks: {e}")
            return []
    
    def save_tasks(self) -> bool:
        """Save tasks to JSON file."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.tasks, file, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False
    
    def add_task(self, title: str, description: str = "") -> bool:
        """Add a new task to the list."""
        if not title.strip():
            print("Error: Task title cannot be empty!")
            return False
        
        task = {
            'id': self.next_id,
            'title': title.strip(),
            'description': description.strip(),
            'completed': False,
            'created_at': datetime.now().isoformat(),
            'completed_at': None
        }
        
        self.tasks.append(task)
        self.next_id += 1
        
        if self.save_tasks():
            print(f"✅ Task '{title}' added successfully! (ID: {task['id']})")
            return True
        else:
            self.tasks.pop()  # Remove the task if save failed
            self.next_id -= 1
            return False
    
    def view_tasks(self, show_completed: bool = True) -> None:
        """Display all tasks or filter by completion status."""
        if not self.tasks:
            print("📝 No tasks found! Add some tasks to get started.")
            return
        
        # Filter tasks based on completion status
        filtered_tasks = self.tasks if show_completed else [t for t in self.tasks if not t['completed']]
        
        if not filtered_tasks:
            status = "completed" if not show_completed else "pending"
            print(f"📝 No {status} tasks found!")
            return
        
        print("\n" + "="*60)
        print("📋 YOUR TO-DO LIST")
        print("="*60)
        
        for task in filtered_tasks:
            status_icon = "✅" if task['completed'] else "⏳"
            print(f"\n{status_icon} ID: {task['id']} | {task['title']}")
            
            if task['description']:
                print(f"   📄 Description: {task['description']}")
            
            # Format and display dates
            created_date = datetime.fromisoformat(task['created_at']).strftime("%Y-%m-%d %H:%M")
            print(f"   📅 Created: {created_date}")
            
            if task['completed'] and task['completed_at']:
                completed_date = datetime.fromisoformat(task['completed_at']).strftime("%Y-%m-%d %H:%M")
                print(f"   ✅ Completed: {completed_date}")
        
        print("\n" + "="*60)
    
    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        """Update an existing task's title or description."""
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"❌ Task with ID {task_id} not found!")
            return False
        
        # Update fields if provided
        if title is not None:
            if not title.strip():
                print("Error: Task title cannot be empty!")
                return False
            task['title'] = title.strip()
        
        if description is not None:
            task['description'] = description.strip()
        
        if self.save_tasks():
            print(f"✅ Task {task_id} updated successfully!")
            return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID."""
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"❌ Task with ID {task_id} not found!")
            return False
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete '{task['title']}'? (y/N): ").lower()
        if confirm != 'y':
            print("❌ Task deletion cancelled.")
            return False
        
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        
        if self.save_tasks():
            print(f"🗑️ Task '{task['title']}' deleted successfully!")
            return True
        return False
    
    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed."""
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"❌ Task with ID {task_id} not found!")
            return False
        
        if task['completed']:
            print(f"ℹ️ Task '{task['title']}' is already completed!")
            return True
        
        task['completed'] = True
        task['completed_at'] = datetime.now().isoformat()
        
        if self.save_tasks():
            print(f"🎉 Task '{task['title']}' marked as completed!")
            return True
        return False
    
    def uncomplete_task(self, task_id: int) -> bool:
        """Mark a task as not completed."""
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"❌ Task with ID {task_id} not found!")
            return False
        
        if not task['completed']:
            print(f"ℹ️ Task '{task['title']}' is already pending!")
            return True
        
        task['completed'] = False
        task['completed_at'] = None
        
        if self.save_tasks():
            print(f"🔄 Task '{task['title']}' marked as pending!")
            return True
        return False
    
    def find_task_by_id(self, task_id: int) -> Optional[Dict]:
        """Find and return a task by its ID."""
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def get_task_stats(self) -> Dict[str, int]:
        """Get statistics about tasks."""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task['completed'])
        pending = total - completed
        return {'total': total, 'completed': completed, 'pending': pending}

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("🚀 TO-DO LIST MANAGER")
    print("="*50)
    print("1. ➕ Add Task")
    print("2. 📋 View All Tasks")
    print("3. 👀 View Pending Tasks")
    print("4. ✏️  Update Task")
    print("5. ✅ Complete Task")
    print("6. 🔄 Uncomplete Task")
    print("7. 🗑️  Delete Task")
    print("8. 📊 View Statistics")
    print("9. ❌ Exit")
    print("="*50)

def get_user_input(prompt: str, input_type: type = str, allow_empty: bool = False):
    """Get user input with error handling."""
    while True:
        try:
            user_input = input(prompt).strip()
            
            if not allow_empty and not user_input:
                print("❌ This field cannot be empty. Please try again.")
                continue
            
            if input_type == int:
                return int(user_input) if user_input else None
            
            return user_input if user_input else None
            
        except ValueError:
            print("❌ Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            exit(0)

def main():
    """Main application loop."""
    print("🎯 Welcome to Your Personal To-Do List Manager!")
    
    # Initialize the TodoApp
    app = TodoApp()
    
    while True:
        try:
            display_menu()
            
            choice = get_user_input("Choose an option (1-9): ", int)
            
            if choice == 1:  # Add Task
                print("\n➕ ADD NEW TASK")
                title = get_user_input("Enter task title: ")
                if title:
                    description = get_user_input("Enter task description (optional): ", allow_empty=True)
                    app.add_task(title, description or "")
            
            elif choice == 2:  # View All Tasks
                app.view_tasks(show_completed=True)
            
            elif choice == 3:  # View Pending Tasks
                app.view_tasks(show_completed=False)
            
            elif choice == 4:  # Update Task
                print("\n✏️ UPDATE TASK")
                app.view_tasks(show_completed=False)  # Show pending tasks for reference
                task_id = get_user_input("Enter task ID to update: ", int)
                if task_id:
                    title = get_user_input("Enter new title (press Enter to keep current): ", allow_empty=True)
                    description = get_user_input("Enter new description (press Enter to keep current): ", allow_empty=True)
                    app.update_task(task_id, title, description)
            
            elif choice == 5:  # Complete Task
                print("\n✅ COMPLETE TASK")
                app.view_tasks(show_completed=False)  # Show pending tasks
                task_id = get_user_input("Enter task ID to complete: ", int)
                if task_id:
                    app.complete_task(task_id)
            
            elif choice == 6:  # Uncomplete Task
                print("\n🔄 UNCOMPLETE TASK")
                completed_tasks = [t for t in app.tasks if t['completed']]
                if completed_tasks:
                    print("\nCompleted Tasks:")
                    for task in completed_tasks:
                        print(f"✅ ID: {task['id']} | {task['title']}")
                    task_id = get_user_input("Enter task ID to mark as pending: ", int)
                    if task_id:
                        app.uncomplete_task(task_id)
                else:
                    print("📝 No completed tasks found!")
            
            elif choice == 7:  # Delete Task
                print("\n🗑️ DELETE TASK")
                app.view_tasks()
                task_id = get_user_input("Enter task ID to delete: ", int)
                if task_id:
                    app.delete_task(task_id)
            
            elif choice == 8:  # View Statistics
                stats = app.get_task_stats()
                print("\n📊 TASK STATISTICS")
                print("="*30)
                print(f"📋 Total Tasks: {stats['total']}")
                print(f"✅ Completed: {stats['completed']}")
                print(f"⏳ Pending: {stats['pending']}")
                if stats['total'] > 0:
                    completion_rate = (stats['completed'] / stats['total']) * 100
                    print(f"🎯 Completion Rate: {completion_rate:.1f}%")
                print("="*30)
            
            elif choice == 9:  # Exit
                print("\n👋 Thank you for using To-Do List Manager!")
                print("💾 All your tasks have been saved automatically.")
                break
            
            else:
                print("❌ Invalid option! Please choose a number between 1-9.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()