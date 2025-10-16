# Pytrack
Basic python project from https://roadmap.sh/projects/task-tracker

A command-line tool to manage your daily tasks directly from the terminal.

## How to Use

To use this tool, run the python script followed by a command. Make sure the script is executable or call it with `python pytrack.py`.

### Commands

**1. Add a Task**
```bash
pytrack add "your task description here"
# Example: pytrack add "buy groceries"
```

**2. List Task**
```bash
# List all tasks
pytrack list

# List tasks by status (todo, progress, done)
pytrack list done
```

**3. Update a Task**
```bash
pytrack update <task_id> "new task description"
# Example: pytrack update 1 "buy fresh vegetables"
```

**4. Mark Task Status**
```bash
pytrack mark <task_id> <status>
# Example: pytrack mark 1 in-progress
# Example: pytrack mark 2 done
```

**5. Delete a Task**
```bash
pytrack delete <task_id>
# Example: pytrack delete 3
```

