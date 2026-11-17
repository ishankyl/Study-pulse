# Study Pulse — Task and Deadline Prioritizer

## Project Overview
Study Pulse is a Python-based task management system designed to help students organize academic tasks and prioritize them according to deadlines and importance.

## Objectives
- Organize academic tasks in one place.
- Calculate the number of days remaining until each deadline.
- Assign priority scores based on urgency and importance.
- Store task information using CSV files.

## Features
1. **Add New Task:** Add tasks with a title, due date, and importance level.
2. **View Prioritized Tasks:** Display tasks sorted by their calculated priority scores.
3. **Automatic Data Storage:** Save tasks in a CSV file.
4. **Input Validation:** Validate task titles, date formats, and importance levels.
5. **Overdue Detection:** Assign maximum priority to overdue tasks.

## Technologies Used
- Python
- CSV module
- Datetime module

## Priority Calculation

The project uses the following formula:

`Priority Score = (Importance × 20) / (Days Left + 1)`

- Importance ranges from 1 to 5.
- Higher scores indicate greater priority.
- Overdue tasks receive a priority score of 100.

## Project Structure

```text
Study-Pulse/
│
├── study_pulse.py
├── study_pulse_tasks.csv
└── README.md
```

## How to Run

1. Install Python.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run the following command:

```bash
python study_pulse.py
```

## Data Storage

Task information is stored locally in `study_pulse_tasks.csv` using the following fields:

- Title
- Due Date
- Importance
- Completion Status

## Future Improvements
- Mark tasks as completed.
- Edit or delete existing tasks.
- Add subject-wise task categorization.
- Generate task summary reports.

## Conclusion
Study Pulse demonstrates the practical application of Python programming concepts, including functions, loops, conditional statements, dictionaries, CSV file handling, and computational logic.