from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:c98xa5@localhost/practice'
db = SQLAlchemy(app)
CORS(app)

class Doctor(db.Model):
    __tablename__ = 'doctor_registration'
    __table_args__ = {'schema': 'information'}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    doctor_id = db.Column(db.String(20), nullable=False, unique=True)
    specialization = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(100), nullable=False, unique=True)
    email_id = db.Column(db.String(100), nullable=False)

class Patient(db.Model):
    __tablename__ = 'patient_registration'
    __table_args__ = {'schema': 'information'}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(100), nullable=False, unique=True)
    email_id = db.Column(db.String(100), nullable=False)

@app.route('/register/doctor', methods=['POST'])
def register_doctor():
    data = request.get_json()

    # Check if the username already exists in the patient or doctor table
    existing_doctor = Doctor.query.filter_by(user_name=data['user_name']).first()
    existing_patient = Patient.query.filter_by(user_name=data['user_name']).first()

    if existing_doctor or existing_patient:
        return jsonify({'message': 'Username already exists!'}), 409

    # Create a new doctor object
    new_doctor = Doctor(
        first_name=data['first_name'],
        last_name=data['last_name'],
        dob=data['dob'],
        phone_number=data['phone_number'],
        password=data['password'],
        address=data['address'],
        doctor_id=data['doctor_id'],
        specialization=data['specialization'],
        user_name=data['user_name'],
        email_id=data['email_id']
    )

    # Add the doctor to the database
    db.session.add(new_doctor)
    db.session.commit()

    return jsonify({'message': 'Doctor registered successfully!'}), 200

# Patient Registration Endpoint
@app.route('/register/patient', methods=['POST'])
def register_patient():
    data = request.get_json()

    # Check if the username already exists in the patient or doctor table
    existing_doctor = Doctor.query.filter_by(user_name=data['user_name']).first()
    existing_patient = Patient.query.filter_by(user_name=data['user_name']).first()

    if existing_doctor or existing_patient:
        return jsonify({'message': 'Username already exists!'}), 409

    # Create a new paient object
    new_patient = Patient(
        first_name=data['first_name'],
        last_name=data['last_name'],
        dob=data['dob'],
        phone_number=data['phone_number'],
        password=data['password'],
        address=data['address'],
        user_name=data['user_name'],
        email_id=data['email_id']
    )

    # Add the patient to the database
    db.session.add(new_patient)
    db.session.commit()

    return jsonify({'message': 'Patient registered successfully!'}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    user_name = data['user_name']
    password = data['password']

    # Check if the user is a doctor
    doctor = Doctor.query.filter_by(user_name=user_name, password=password).first()
    if doctor:
        return jsonify({'message': f'Doctor {user_name} login successful!'}), 200

    # Check if the user is a patient
    patient = Patient.query.filter_by(user_name=user_name, password=password).first()
    if patient:
        return jsonify({'message': f'Patient {user_name} login successful!'}), 200

    return jsonify({'message': 'Invalid credentials!'}), 401


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
