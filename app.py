from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pravinderreddy@localhost:5432/todo_db'
db = SQLAlchemy(app)

class Todo(db.Model):
     __tablename__ = 'todos'
     id = db.Column(db.Integer, primary_key=True)
     description = db.Column(db.String(), nullable=False)

def __repr__(self):
    return f'<Todo {self.id} {self.description}>'
db.create_all()

@app.route('/todos/create', methods= ["POST"])
def add_task():
    task = request.get_json()['description']
    #Create a new task desription in the Database
    todo = Todo(description=task)
    db.session.add(todo)
    db.session.commit()

    #redirect to root route('/')
    return jsonify({
        'description':todo.description
    })

@app.route('/')
def index():
    return render_template('index.html', data = Todo.query.all())
