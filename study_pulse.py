
import csv
from datetime import datetime

# Local file where tasks will be saved automatically
FILENAME = "study_pulse_tasks.csv"
FIELDNAMES = ["title", "due_date", "importance", "completed"]


def calculate_days_left(due_date_str):
    """Calculates days remaining from today to the due date."""
    today = datetime.now().date()
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    return (due_date - today).days


def calculate_priority_score(days_left, importance):
    """
    Computes priority score based on urgency and importance.
    Formula: (Importance * 20) / (Days Left + 1)
    """
    if days_left < 0:
        return 100.0

    score = (importance * 20) / (days_left + 1)
    return round(min(score, 100.0), 2)


def load_tasks():
    """Reads saved tasks from the CSV file."""
    tasks = []
    try:
        with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append({
                    "title": row["title"],
                    "due_date": row["due_date"],
                    "importance": int(row["importance"]),
                    "completed": row["completed"] == "True"
                })
    except FileNotFoundError:
        pass

    return tasks


def save_tasks(tasks):
    """Saves the tasks list to the CSV file."""
    try:
        with open(FILENAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            for task in tasks:
                writer.writerow(task)
    except Exception as e:
        print(f"Error saving data to CSV: {e}")


def add_task(tasks):
    """Adds a new task with basic input validation."""
    print("\n--- ADD NEW TASK ---")

    title = input("Enter Task Title: ").strip()
    if not title:
        print("Error: Task title cannot be empty.")
        return

    while True:
        date_str = input("Enter Due Date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format! Use YYYY-MM-DD (e.g., 2026-11-20).")

    while True:
        try:
            importance = int(input("Enter Importance Level (1 = Low, 5 = High): "))
            if 1 <= importance <= 5:
                break
            print("Please enter a whole number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    new_task = {
        "title": title,
        "due_date": date_str,
        "importance": importance,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' saved successfully!")


def view_tasks(tasks):
    """Calculates dynamic priority scores and prints a sorted table."""
    if not tasks:
        print("\nNo tasks registered yet. Choose Option 1 to add a task!")
        return

    # Create separate dictionaries for displaying tasks.
    sorted_tasks = []

    for task in tasks:
        days = calculate_days_left(task["due_date"])

        display_task = task.copy()
        display_task["days_left"] = days
        display_task["priority_score"] = calculate_priority_score(
            days, task["importance"]
        )

        sorted_tasks.append(display_task)

    # Sort tasks by priority score (highest first).
    sorted_tasks = sorted(
        sorted_tasks,
        key=lambda t: t["priority_score"],
        reverse=True
    )

    print("\n" + "=" * 68)
    print(f"{'No.':<4} {'Status':<8} {'Title':<20} {'Due Date':<12} {'Days Left':<10} {'Priority':<8}")
    print("=" * 68)

    for idx, task in enumerate(sorted_tasks, 1):
        status = "[DONE]" if task["completed"] else "[PENDING]"
        days_str = "OVERDUE" if task["days_left"] < 0 else str(task["days_left"])

        print(
            f"{idx:<4} {status:<8} {task['title'][:18]:<20} "
            f"{task['due_date']:<12} {days_str:<10} "
            f"{task['priority_score']:<8}"
        )

    print("=" * 68)


def main():
    tasks = load_tasks()

    while True:
        print("\n==============================")
        print("    STUDY PULSE - MAIN MENU   ")
        print("==============================")
        print("1. Add New Task")
        print("2. View Prioritized Tasks")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Exiting Study Pulse. Good luck with your studies!")
            break
        else:
            print("Invalid choice! Please type 1, 2, or 3.")


if __name__ == "__main__":
    main()
