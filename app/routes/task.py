from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app import db
from app.models import Task

tasks_bp = Blueprint('tasks', __name__)

# View all tasks
@tasks_bp.route('/')
def view_tasks():
    if 'user' not in session:
        flash('Please login first!', 'warning')
        return redirect(url_for('auth.login'))
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

# Add a new task
@tasks_bp.route('/add', methods=['POST'])
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status='pending')
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
    return redirect(url_for('tasks.view_tasks'))

# Toggle task status
@tasks_bp.route('/toggle/<int:task_id>', methods=["POST"])
def toggle_task(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.status == 'pending':
            task.status = 'working'
        elif task.status == 'working':
            task.status = 'completed'
        else:
            task.status = 'pending'
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

# Clear all tasks
@tasks_bp.route('/clear', methods=["POST"])
def clear_tasks():
    Task.query.delete()
    db.session.commit()
    flash('All tasks cleared!', 'info')
    return redirect(url_for('tasks.view_tasks'))
