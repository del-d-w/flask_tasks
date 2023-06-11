from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token,jwt_required
import psycopg2
from flask_bcrypt import Bcrypt
from flask_cors import CORS

#pip install flask
#pip install flask-jwt-extended
#pip install psycopg2
#pip install bcrypt
#pip install flask-cors


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

DB_HOST = "localhost"
DB_NAME = "employees"
DB_USER = "postgres"
DB_PASS = "12345"

def get_db_connection():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


@app.route('/register', methods=['POST'])
def register():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        body = request.get_json()

        username = body['username']
        password = body['password']
        password_hash=password.encode('utf-8')
        # Check if the username is already registered
        cursor.execute("SELECT * FROM registered_users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            return jsonify({'message': 'Username already exists'}), 400

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password_hash).decode('utf-8')

        # Register the new user
        cursor.execute("INSERT INTO registered_users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()

        return jsonify({'message': 'Registration successful'}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'message': 'An error occurred.'}), 500

    finally:
        cursor.close()
        conn.close()

@app.route('/login', methods=['POST'])
def login():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        body = request.get_json()

        username = body['username']
        password = body['password']

        # Retrieve user from the database
        cursor.execute("SELECT * FROM registered_users WHERE username = %s", (username,))
        user = cursor.fetchone()
        print(user[2])
        print(bcrypt.check_password_hash(user[2], password))
        if bcrypt.check_password_hash(user[2], password):

            # Create access and refresh tokens
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)

            return jsonify({'access_token': access_token, 'refresh_token': refresh_token}), 200
        else:
            return jsonify({'message': 'Invalid username or password'}), 401

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'message': 'An error occurred.'}), 500

    finally:
        cursor.close()
        conn.close()



@app.route('/todos', methods=['GET'])
@jwt_required()
def get_todos():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM todouser")
        rows = cursor.fetchall()

        data = []
        for row in rows:
            data.append({
                'id': row[0],
                'title': row[1],
                'completed': row[2]
            })

        return jsonify(data), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'message': 'An error occurred.'}), 500

    finally:
        cursor.close()
        conn.close()

@app.route('/todos/<id>', methods=['GET'])
@jwt_required()
def get_todos_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM todouser WHERE id = %s", (id,))
        rows = cursor.fetchall()

        data = []
        for row in rows:
            data.append({
                'id': row[0],
                'title': row[1],
                'completed': row[2]
            })

        if data:
            return jsonify(data), 200
        else:
            return jsonify({'message': 'Todo not found'}), 404

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'message': 'An error occurred.'}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/todos', methods=['POST'])
@jwt_required()
def create_todo():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        body = request.get_json()

        id = body['id']
        title = body['title']
        completed = bool(body['completed'])

        cursor.execute("INSERT INTO todouser (id, title, completed) VALUES (%s, %s, %s)",
                       (id, title, completed))

        conn.commit()

        return jsonify({'message': 'Record inserted successfully.'}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'message': 'An error occurred.'}), 500

    finally:
        cursor.close()
        conn.close()

@app.route('/todos/<id>', methods=['PUT'])
@jwt_required()
def update_todo(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        body = request.get_json()

        completed = bool(body['completed'])

        cursor.execute("UPDATE todouser SET completed = %s WHERE id = %s", (completed, id))

        conn.commit()

        return jsonify({'message': 'Record updated successfully.'}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'message': 'An error occurred.'}), 500

    finally:
        cursor.close()
        conn.close()

@app.route('/todos/<id>', methods=['DELETE'])
@jwt_required()
def delete_todo(id):
    conn =get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM todouser WHERE id = %s", (id,))

        conn.commit()

        return jsonify({'message': 'Record deleted successfully.'}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'message': 'An error occurred.'}), 500

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
