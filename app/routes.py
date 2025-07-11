from flask import Blueprint, render_template, request, redirect, url_for
from app import db, r
from app.models import Task
import time
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    start = time.time()
    cache_key = 'tasks_list'

    if r.exists(cache_key):
        tasks = json.loads(r.get(cache_key))
        source = "Redis Cache"
    else:
        tasks = [
            {"id": t.id, "title": t.title, "description": t.description}
            for t in Task.query.order_by(Task.created_at.desc()).all()
        ]
        r.set(cache_key, json.dumps(tasks))
        source = "PostgreSQL DB"

    response_time = round((time.time() - start) * 1000, 2)
    return render_template("index.html", tasks=tasks, source=source, response_time=response_time)

@main.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        r.delete('tasks_list')
        return redirect(url_for('main.index'))
    return render_template('form.html', action='Add')

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        db.session.commit()
        r.delete('tasks_list')
        return redirect(url_for('main.index'))
    return render_template('form.html', action='Edit', task=task)

@main.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    r.delete('tasks_list')
    return redirect(url_for('main.index'))
from flask import Blueprint, render_template, request, redirect, url_for
from app import db, r
from app.models import Task
import time
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    start = time.time()
    cache_key = 'tasks_list'

    if r.exists(cache_key):
        tasks = json.loads(r.get(cache_key))
        source = "Redis Cache"
    else:
        tasks = [
            {"id": t.id, "title": t.title, "description": t.description}
            for t in Task.query.order_by(Task.created_at.desc()).all()
        ]
        r.set(cache_key, json.dumps(tasks))
        source = "PostgreSQL DB"

    response_time = round((time.time() - start) * 1000, 2)
    return render_template("index.html", tasks=tasks, source=source, response_time=response_time)

@main.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        r.delete('tasks_list')
        return redirect(url_for('main.index'))
    return render_template('form.html', action='Add')

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        db.session.commit()
        r.delete('tasks_list')
        return redirect(url_for('main.index'))
    return render_template('form.html', action='Edit', task=task)

@main.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    r.delete('tasks_list')
    return redirect(url_for('main.index'))
