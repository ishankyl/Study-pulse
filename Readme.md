# Study Pulse – Task and Deadline Prioritizer

A command-line task and deadline prioritization tool built in Python by a five-member student team. Study Pulse calculates a dynamic priority score for each task based on its deadline urgency and importance rating, ranks tasks clearly in the terminal, and saves progress locally in `study_pulse_tasks.csv`.

## Key Features

- **Add New Tasks:** Enter a task title, due date (`YYYY-MM-DD`), and importance level (`1` to `5`) with input validation.
- **Dynamic Priority Scoring:** Computes priority scores using urgency (`days_left`) and importance (`1`–`5`) so urgent, high-importance tasks surface first.
- **View, Filter, Sort & Search:**
  - View all tasks ranked by priority score.
  - Filter tasks by `Pending`, `Completed`, or `All`, and sort by `Priority Level` or `Status`.
  - Search tasks by keyword in the title.
- **Manage Task Lifecycle:** Quickly toggle `Pending` / `Completed` status, edit individual or all fields of an existing task, or delete a task with confirmation.
- **Persistent CSV Storage:** Automatically loads tasks on startup and saves changes to `study_pulse_tasks.csv`.

## Priority Scoring Logic

- **Days Remaining:** Calculated by subtracting today's date from the task's due date (`due_date - today`).
- **Priority Formula:**
  $$\text{Priority Score} = \frac{\text{Importance} \times 20}{\text{Days Remaining} + 1}$$
  - Overdue tasks (`days_left < 0`) receive a score of `100.0`.
  - Scores are capped at `100.0` and rounded to two decimal places.
  - Adding `+ 1` in the denominator prevents division by zero when a task is due today.

## Project Structure

```text
├── 1.py                  # Main Python application (menu loop, navigation, scoring, CSV logic)
├── study_pulse_tasks.csv # Local CSV file storing saved tasks (created/updated automatically)
└── README.md             # Project documentation
