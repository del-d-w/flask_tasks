"""# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

data_list = ["Item 1", "Item 2", "Item 3"]

@app.route('/')
def home():
    return render_template('home.html', data_list=data_list)

@app.route('/create', methods=['POST'])
def create():
    item = request.form['item']
    data_list.append(item)
    return redirect(url_for('home'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        if 'item' in request.form:
            updated_item = request.form['item']
            data_list[index] = updated_item
            return redirect(url_for('home'))
        else:
            print('Error: "item" key not found in request.form')
    return render_template('edit.html', index=index, item=data_list[index])
    
@app.route('/delete/<int:index>', methods=['GET','POST'])
def delete(index):
    del data_list[index]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
"""

# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

data_list = []

@app.route('/')
def home():
    return render_template('home.html', data_list=data_list)

@app.route('/create', methods=['POST'])
def create():
    hobby=request.form.getlist('hobbies')
    hobbies=",".join(map(str,hobby))
    item = {
        "id": len(data_list) + 1,
        "firstname":request.form['firstname'],
        "lastname":request.form['lastname'],
        "email":request.form['email'],
        "password":request.form['password'],
        "gender":request.form.get("gender"),
        "hobbies":hobbies,
        "country":request.form['country']
    }
    data_list.append(item)
    return redirect(url_for('home'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
            hobby=request.form.getlist('hobbies')
            hobbies=",".join(map(str,hobby))
            updated_item = {
                "id": data_list[index]["id"],
                "firstname":request.form['firstname'],
                "lastname":request.form['lastname'],
                "email":request.form['email'],
                "password":request.form['password'],
                "gender":request.form.get("gender"),
                "hobbies":hobbies,
                "country":request.form['country']
            }
            data_list[index] = updated_item
            return redirect(url_for('home'))
    return render_template('edit.html', index=index, user=data_list[index])
    
@app.route('/delete/<int:index>', methods=['GET','POST'])
def delete(index):
    del data_list[index]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
