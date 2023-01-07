from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = [{'id':1, 'title':'수학숙제하기', 'is_completed':False}]

class Todo():
    id = 1
    title = ''
    is_completed = False

    def __init__(self, id, title, is_completed=False):
        self.id = id
        self.title = title
        self.is_completed = is_completed

    def __str__(self):
        return f'id:{self.id}, title:{self.title}, is_completed:{self.is_completed}'

next_id = 1
todos_title = ['수학숙제하기', '코딩숙제하기', '배드민턴 치기']
for title in todos_title:
    todos.append(Todo(next_id, '배드민턴 치기'))
    next_id += 1

@app.route('/')
def index():
    return render_template('index.html',todos=todos)

@app.route('/add', methods=['POST'])
def add():
    global next_id
    title = request.form.get('title')
    new_todo = Todo(next_id, title)
    todos.append(new_todo)
    next_id += 1
    return redirect('/')

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            break
    return redirect('/')

@app.route('/change_state/<int:todo_id>')
def change_state(todo_id):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            # not Ture => False
            # not False => True
            todos[index].is_completed = not todos[index].is_completed
            break
    return redirect('/')


# if __name__ == "__main__":
#     app.run(debug=True)

app.run(host='0.0.0.0', port=81)
