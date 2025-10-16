import argparse
import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(args, tasks):
    now = datetime.now().strftime("%d %b %Y, %H:%M")
    new_id = tasks[-1]['id'] + 1 if tasks else 1
    new_task = {
        'id': new_id,
        'description': args.description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }
    tasks.append(new_task)
    print(f"new task added with id {new_id}: '{args.description}'")

def update_task(args, tasks):
    for task in tasks:
        if task['id'] == args.id:
            task['description'] = args.new_description
            
            task['updatedAt'] = datetime.now().strftime("%d %b %Y, %H:%M")
            
            print(f"task id {args.id} updated to: '{args.new_description}'")
            return
    print(f"error: task with id {args.id} not found.")

def delete_task(args, tasks):
    task_to_delete = None
    for task in tasks:
        if task['id'] == args.id:
            task_to_delete = task
            break
    
    if task_to_delete:
        tasks.remove(task_to_delete)
        print(f"task id {args.id} ('{task_to_delete['description']}') has been deleted.")
    else:
        print(f"error: task with id {args.id} not found.")

def mark_task(args, tasks):
    for task in tasks:
        if task['id'] == args.id:
            task['status'] = args.status
            task['updatedAt'] = datetime.now().strftime("%d %b %Y, %H:%M")
            
            print(f"task id {args.id} status changed to '{args.status}'.")
            return
    print(f"error: task with id {args.id} not found.")

def list_tasks(args, tasks):
    print("--- task list ---")
    
    filtered_tasks = []
    if args.status:
        for task in tasks:
            if task['status'] == args.status:
                filtered_tasks.append(task)
    else:
        filtered_tasks = tasks

    if not filtered_tasks:
        print("no tasks match the filter." if args.status else "the task list is empty.")
        return

    for task in filtered_tasks:
        print(f"  [{task['id']}] {task['description']}  ({task['status']})")
        print(f"      created: {task['createdAt']}, updated: {task['updatedAt']}")

def main():
    parser = argparse.ArgumentParser(description="a simple command-line tracker.")
    
    subparsers = parser.add_subparsers(dest='command', required=True, metavar='command')
    
    parser_add = subparsers.add_parser('add', help='add a new task')
    parser_add.add_argument('description', type=str, help='description of the task')

    parser_update = subparsers.add_parser('update', help='update an existing task')
    parser_update.add_argument('id', type=int, help='the id of the task to update') 
    parser_update.add_argument('new_description', type=str, help='the new description for the task')

    parser_delete = subparsers.add_parser('delete', help='delete an existing task')
    parser_delete.add_argument('id', type=int, help = 'the id of the task to delete')

    parser_mark = subparsers.add_parser('mark', help='mark a task as done, todo, or in progress')
    parser_mark.add_argument('id', type=int, help='the id of the task to update status')
    parser_mark.add_argument('status', choices=['done', 'todo', 'progress'], help='new status for the task', metavar='done|todo|progress')

    parser_list = subparsers.add_parser('list', help='list all tasks')
    parser_list.add_argument('status', nargs='?', default=None, choices=['done', 'todo', 'progress'], help='filter task by status (optional)', metavar='done|todo|progress')
    
    args = parser.parse_args()
    tasks = load_tasks()

    if args.command == 'add':
        add_task(args, tasks)
    elif args.command == 'update':
        update_task(args, tasks)
    elif args.command == 'delete':
        delete_task(args, tasks)
    elif args.command == 'mark':
        mark_task(args, tasks)
    elif args.command == 'list':
        list_tasks(args, tasks)
    
    save_tasks(tasks)

if __name__ == "__main__":
    main()