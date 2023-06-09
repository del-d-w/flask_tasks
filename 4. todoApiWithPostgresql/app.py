from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

DB_HOST = "localhost"
DB_NAME = "practice"
DB_USER = "postgres"
DB_PASS = "c98xa5"

def get_db_connection():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/todos', methods=['GET'])
def get_todos():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM information.todouser")
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
def get_todos_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM information.todouser WHERE id = %s", (id,))
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
def create_todo():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        body = request.get_json()

        id = body['id']
        title = body['title']
        completed = bool(body['completed'])

        cursor.execute("INSERT INTO information.todouser (id, title, completed) VALUES (%s, %s, %s)",
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
def update_todo(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        body = request.get_json()

        completed = bool(body['completed'])

        cursor.execute("UPDATE information.todouser SET completed = %s WHERE id = %s", (completed, id))

        conn.commit()

        return jsonify({'message': 'Record updated successfully.'}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'message': 'An error occurred.'}), 500

    finally:
        cursor.close()
        conn.close()

@app.route('/todos/<id>', methods=['DELETE'])
def delete_todo(id):
    conn =get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM information.todouser WHERE id = %s", (id,))

        conn.commit()

        return jsonify({'message': 'Record deleted successfully.'}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'message': 'An error occurred.'}), 500

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run()
