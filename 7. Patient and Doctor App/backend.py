from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# pip install flask-cors
# pip install Flask-SQLAlchemy
# pip install flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/employees'
db = SQLAlchemy(app)
CORS(app)

# Define the Doctor model
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    # Add other fields as required

# Define the Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    # Add other fields as required

# Doctor Registration Endpoint
@app.route('/register/doctor', methods=['POST'])
def register_doctor():
    data = request.get_json()
    new_doctor = Doctor(
        first_name=data['first_name'],
        last_name=data['last_name'],
        dob=data['dob'],
        username=data['username'],
        password=data['password'],
        address=data['address'],
        specialization=data['specialization'],
        phone_number=data['phone_number'],
        email=data['email']
    )
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify({'message': 'Doctor registered successfully!'}), 200

# Patient Registration Endpoint
@app.route('/register/patient', methods=['POST'])
def register_patient():
    data = request.get_json()
    new_patient = Patient(
        first_name=data['first_name'],
        last_name=data['last_name'],
        dob=data['dob'],
        username=data['username'],
        password=data['password'],
        address=data['address'],
        phone_number=data['phone_number'],
        email=data['email']
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'Patient registered successfully!'}), 200

# Login Endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    username = data['username']
    password = data['password']

    # Check if the user is a doctor
    doctor = Doctor.query.filter_by(username=username, password=password).first()
    if doctor:
        return jsonify({'message': f'Doctor {username} login successful!'}), 200

    # Check if the user is a patient
    patient = Patient.query.filter_by(username=username, password=password).first()
    if patient:
        return jsonify({'message': f'Patient {username} login successful!'}), 200

    return jsonify({'message': 'Invalid credentials!'}), 401

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

"""
from flask import Flask, request, jsonify
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database connection details
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    database='practice',
    user='postgres',
    password='c98xa5'
)

# Doctor Registration Endpoint
@app.route('/register/doctor', methods=['POST'])
def register_doctor():
    data = request.get_json()
    cursor = conn.cursor()

    # Extract data from the request
    first_name = data['first_name']
    last_name = data['last_name']
    dob = data['dob']
    phone_number = data['phone_number']
    password = data['password']
    address = data['address']
    doctor_id = data['doctor_id']
    specialization = data['specialization']
    user_name = data['user_name']
    email_id = data['email_id']

    # Check if the username already exists in the patient or doctor table
    cursor.execute(
        "SELECT * FROM information.doctor_registration WHERE user_name = %s",
        (user_name,)
    )
    existing_doctor = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM information.patient_registration WHERE user_name = %s",
        (user_name,)
    )
    existing_patient = cursor.fetchone()

    if existing_doctor or existing_patient:
        cursor.close()
        return jsonify({'message': 'Username already exists!'}), 200

    # Execute the SQL query to insert a new doctor
    cursor.execute(
        "INSERT INTO information.doctor_registration (first_name, last_name, dob, phone_number, password, address, doctor_id, specialization, user_name, email_id) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (first_name, last_name, dob, phone_number, password, address, doctor_id, specialization, user_name, email_id)
    )
    conn.commit()
    cursor.close()

    return jsonify({'message': 'Doctor registered successfully!'}), 200

# Patient Registration Endpoint
@app.route('/register/patient', methods=['POST'])
def register_patient():
    data = request.get_json()
    cursor = conn.cursor()

    # Extract data from the request
    first_name = data['first_name']
    last_name = data['last_name']
    dob = data['dob']
    phone_number = data['phone_number']
    password = data['password']
    address = data['address']
    user_name = data['user_name']
    email_id = data['email_id']

    # Check if the username already exists in the patient or doctor table
    cursor.execute(
        "SELECT * FROM information.doctor_registration WHERE user_name = %s",
        (user_name,)
    )
    existing_doctor = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM information.patient_registration WHERE user_name = %s",
        (user_name,)
    )
    existing_patient = cursor.fetchone()

    if existing_doctor or existing_patient:
        cursor.close()
        return jsonify({'message': 'Username already exists!'}), 409

    # Execute the SQL query to insert a new patient
    cursor.execute(
        "INSERT INTO information.patient_registration (first_name, last_name, dob, phone_number, password, address, user_name, email_id) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (first_name, last_name, dob, phone_number, password, address, user_name, email_id)
    )
    conn.commit()
    cursor.close()

    return jsonify({'message': 'Patient registered successfully!'}), 200


# Login Endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    cursor = conn.cursor()

    # Extract data from the request
    user_name = data['user_name']
    password = data['password']

    # Execute the SQL query to check login credentials for a doctor
    cursor.execute(
        "SELECT * FROM information.doctor_registration WHERE user_name = %s AND password = %s",
        (user_name, password)
    )
    doctor = cursor.fetchone()

    if doctor:
        cursor.close()
        return jsonify({'message': f'Doctor {user_name} login successful!'}), 200
    
    # Execute the SQL query to check login credentials for a patient
    cursor.execute(
        "SELECT * FROM information.patient_registration WHERE user_name = %s AND password = %s",
        (user_name, password)
    )
    patient = cursor.fetchone()
    if patient:
        cursor.close()
        return jsonify({'message': f'Patient {user_name} login successful!'}), 200

    cursor.close()
    return jsonify({'message': 'Invalid credentials!'}), 401


if __name__ == '__main__':
    app.run(debug=True)

"""
