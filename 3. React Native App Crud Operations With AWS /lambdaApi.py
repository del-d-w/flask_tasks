import json
import psycopg2

def lambda_handler(event, context):
    DB_HOST = "4.6.44.290"
    DB_NAME = "postgres"
    DB_USER = "postgres"
    DB_PASS = "yourpassword"
    
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cursor = conn.cursor()

    try:
        http_method = event['httpMethod']
        
        if http_method == 'GET':
            # Perform READ operation
            cursor.execute("SELECT * FROM todouser")
            rows = cursor.fetchall()

            # Process and format the retrieved data
            data = []
            for row in rows:
                data.append({
                    'id': row[0],
                    'title': row[1],
                    'completed': row[2]
                })

            return {
                'statusCode': 200,
                'body': json.dumps(data)
            }
        
        elif http_method == 'POST':
            # Parse the request body
            body = json.loads(event['body'])

            # Extract the values from the request body
            id = body['id']
            title = body['title']
            completed = bool(body['completed'])  # Convert to boolean

            # Perform CREATE operation
            cursor.execute("INSERT INTO todouser (id, title, completed) VALUES (%s, %s, %s)",
                           (id, title, completed))

            # Commit the changes
            conn.commit()

            return {
                'statusCode': 200,
                'body': json.dumps('Record inserted successfully.')
            }
        
        elif http_method == 'PUT':
            # Extract the path parameter
            id = event['queryStringParameters']['id']

            # Parse the request body
            body = json.loads(event['body'])

            # Extract the values from the request body
            completed = bool(body['completed'])  # Convert to boolean

            # Perform UPDATE operation
            cursor.execute("UPDATE todouser SET completed = %s WHERE id = %s", (completed, id))

            # Commit the changes
            conn.commit()

            return {
                'statusCode': 200,
                'body': json.dumps('Record updated successfully.')
            }
        
        elif http_method == 'DELETE':
            # Extract the path parameter
            id = event['queryStringParameters']['id']

            # Perform DELETE operation
            cursor.execute("DELETE FROM todouser WHERE id = %s", (id,))

            # Commit the changes
            conn.commit()

            return {
                'statusCode': 200,
                'body': json.dumps('Record deleted successfully.')
            }
        
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid HTTP method.')
            }
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('An error occurred.')
        }
    
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
