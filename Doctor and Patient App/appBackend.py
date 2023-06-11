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
    username = data['username']
    password = data['password']

    # Check if the user is a doctor
    doctor = Doctor.query.filter_by(username=username, password=password).first()
    if doctor:
        return jsonify({'message': 'Doctor login successful!'}), 200

    # Check if the user is a patient
    patient = Patient.query.filter_by(username=username, password=password).first()
    if patient:
        return jsonify({'message': 'Patient login successful!'}), 200

    return jsonify({'message': 'Invalid credentials!'}), 401

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
