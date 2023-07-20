from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:c98xa5@localhost:5432/practice'
app.app_context().push()
db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'<Item id={self.id} name={self.name}>'

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    name = data.get('name')
    if name:
        item = Item(name=name)
        db.session.add(item)
        db.session.commit()
        return jsonify({'message': 'Item created successfully'})
    else:
        return jsonify({'error': 'Invalid data'})


@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get(item_id)
    if item:
        return jsonify({'item_id': item.id, 'name': item.name})
    else:
        return jsonify({'error': 'Item not found'})

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    name = data.get('name')
    item = Item.query.get(item_id)
    if item and name:
        item.name = name
        db.session.commit()
        return jsonify({'message': 'Item updated successfully'})
    else:
        return jsonify({'error': 'Item not found or invalid data'})

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted successfully'})
    else:
        return jsonify({'error': 'Item not found'})

if __name__ == '__main__':
    app.run()
