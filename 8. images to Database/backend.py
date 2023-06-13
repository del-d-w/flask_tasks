from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import base64


# pip install flask-cors
# pip install Flask-SQLAlchemy
# pip install flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:c98xa5@localhost/practice'
db = SQLAlchemy(app)
CORS(app)

class Image(db.Model):
    __tablename__ = 'images'
    __table_args__ = {'schema': 'information'}
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.LargeBinary, nullable=False)

@app.route('/images', methods=['POST'])
def upload_image():
    # Read the uploaded file from the form data
    image = request.files['image']

    # Convert the image file to binary data
    image_data = image.read()

    # Create a new Image object
    new_image = Image(data=image_data)

    # Add the image object to the database session
    db.session.add(new_image)
    # Commit the session to persist the changes
    db.session.commit()

    return 'Image uploaded successfully'

@app.route('/image', methods=['GET'])
def get_images():
    images = Image.query.all()
    image_list = []
    for image in images:
        image_data = base64.b64encode(image.data).decode('utf-8')
        image_list.append(image_data)

    return jsonify(image_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
