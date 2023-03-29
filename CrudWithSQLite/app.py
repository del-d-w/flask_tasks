"""
sqlite3 kpi.db
.database
creating tables
.tables
.mode column
SELECT * FROM employee;
.headers on
SELECT * FROM employee;
"""

from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 
import re 

app=Flask(__name__)

app.secret_key = "cairocoders-ednalan"
 


@app.route('/')
def home():
    return render_template('home.html')

@app.route("/details")
def get_details():
    conn =sqlite3.connect("kpi.db") 
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    s = "SELECT * FROM registers"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    print(list_users)
    return render_template("details.html",users=list_users)

@app.route('/create',methods=['POST'])
def create():
    conn =sqlite3.connect("kpi.db") 
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    if request.method=='POST':
        hobby=request.form.getlist('hobbies')
        hobbies=",".join(map(str,hobby))
        firstname=request.form['firstname']
        print(firstname)
        lastname=request.form['lastname']
        email=request.form['email']
        password=request.form['password']
        gender=request.form.get("gender")
        hobbies=hobbies
        country=request.form['country']
        ##
        cur.execute('SELECT * FROM registers WHERE email = ?', (email,))
        account = cur.fetchone()
        print(account)
        # If account exists show error and validation checks
        if account:
            flash('user already exists!')
            return redirect(url_for('home'))
        ##
        elif firstname=="" or lastname=="" or email=="" or password=="" or gender=="" or  hobbies=="":
            flash("Please fill all the details")
            return redirect(url_for('home'))
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!')
            return redirect(url_for('home'))
        elif not (len(password) >= 8 and
        re.search(r'\d+', password) and
        re.search(r'[a-z]+', password) and
        re.search(r'[A-Z]+', password) and
        re.search(r'\W+', password) and not
        re.search(r'\s+', password)):
            
            flash("Password should be combination of alphabets, special characters, digits and length of password is greater than 8")
            return redirect(url_for('home'))
        else:
            cur.execute("INSERT INTO registers (firstname, lastname, email,password,gender,hobbies,country) VALUES (?,?,?,?,?,?,?)", (firstname, 
            lastname, email,password,gender,hobbies,country))
            conn.commit()
            flash('User Registered successfully')
            return redirect(url_for('get_details'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):
    conn =sqlite3.connect("kpi.db") 
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM registers WHERE id = ?', (id,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', user = data[0])
 
@app.route('/update/<int:id>', methods=['POST'])
def update_student(id):
    if request.method == 'POST':
        hobby=request.form.getlist('hobbies')
        hobbies=",".join(map(str,hobby))
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        email=request.form['email']
        password=request.form['password']
        gender=request.form['gender']
        hobbies=hobbies
        country=request.form['country'] 
        conn =sqlite3.connect("kpi.db")
        conn.row_factory = sqlite3.Row         
        cur = conn.cursor()
        cur.execute("""
            UPDATE registers
            SET firstname = ?,
                lastname = ?,
                email = ?,
                password=?,
                gender=?,
                hobbies=?,
                country=?
            WHERE id = ?
        """, (firstname, lastname, email,password,gender,hobbies,country,id))
        flash('User Updated Successfully')
        conn.commit()
        return redirect(url_for('get_details'))
 
@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete_student(id):
    conn =sqlite3.connect("kpi.db") 
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('DELETE FROM registers WHERE id =?',(id,))
    conn.commit()
    flash('User Removed Successfully')
    return redirect(url_for('get_details'))
 
if __name__=='__main__':
    app.run(debug=True)
  
  
  """
from flask import Flask,render_template,request,redirect,url_for,flash,g
import sqlite3 
import re 

app=Flask(__name__)

app.secret_key = "cairocoders-ednalan"
 
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("kpi.db")
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/details")
def get_details():
    db = get_db()
    cur = db.cursor()
    s = "SELECT * FROM registers"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    print(list_users)
    return render_template("details.html",users=list_users)

@app.route('/create',methods=['POST'])
def create():
    db = get_db()
    cur = db.cursor()
    if request.method=='POST':
        hobby=request.form.getlist('hobbies')
        hobbies=",".join(map(str,hobby))
        firstname=request.form['firstname']
        print(firstname)
        lastname=request.form['lastname']
        email=request.form['email']
        password=request.form['password']
        gender=request.form.get("gender")
        hobbies=hobbies
        country=request.form['country']
        ##
        cur.execute('SELECT * FROM registers WHERE email = ?', (email,))
        account = cur.fetchone()
        print(account)
        # If account exists show error and validation checks
        if account:
            flash('user already exists!')
            return redirect(url_for('home'))
        ##
        elif firstname=="" or lastname=="" or email=="" or password=="" or gender=="" or  hobbies=="":
            flash("Please fill all the details")
            return redirect(url_for('home'))
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!')
            return redirect(url_for('home'))
        elif not (len(password) >= 8 and
        re.search(r'\d+', password) and
        re.search(r'[a-z]+', password) and
        re.search(r'[A-Z]+', password) and
        re.search(r'\W+', password) and not
        re.search(r'\s+', password)):
            
            flash("Password should be combination of alphabets, special characters, digits and length of password is greater than 8")
            return redirect(url_for('home'))
        else:
            cur.execute("INSERT INTO registers (firstname, lastname, email,password,gender,hobbies,country) VALUES (?,?,?,?,?,?,?)", (firstname, 
            lastname, email,password,gender,hobbies,country))
            db.commit()
            flash('User Registered successfully')
            return redirect(url_for('get_details'))


@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):

    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM registers WHERE id = ?', (id,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', user = data[0])
 
@app.route('/update/<int:id>', methods=['POST'])
def update_student(id):
    if request.method == 'POST':
        hobby=request.form.getlist('hobbies')
        hobbies=",".join(map(str,hobby))
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        email=request.form['email']
        password=request.form['password']
        gender=request.form['gender']
        hobbies=hobbies
        country=request.form['country']         
        db = get_db()
        cur = db.cursor()
        cur.execute("""
            UPDATE registers
            SET firstname = ?,
                lastname = ?,
                email = ?,
                password=?,
                gender=?,
                hobbies=?,
                country=?
            WHERE id = ?
        """, (firstname, lastname, email,password,gender,hobbies,country,id))
        flash('User Updated Successfully')
        db.commit()
        return redirect(url_for('get_details'))
 
@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete_student(id):
    db = get_db()
    cur = db.cursor()
    cur.execute('DELETE FROM registers WHERE id =?',(id,))
    db.commit()
    flash('User Removed Successfully')
    return redirect(url_for('get_details'))
 
if __name__=='__main__':
    app.run(debug=True)
  """
