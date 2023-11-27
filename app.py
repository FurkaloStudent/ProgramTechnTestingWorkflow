from flask import Flask, request, jsonify
import program as pr
app = Flask(__name__)
collection = {}

@app.route('/')
def home():
  return "Home Page."

@app.route('/test')
def test_route():
  return "Test Route 2: Extra Testing"  

@app.route('/add_item', methods=['POST'])
def add_item_route():
  data = request.get_json()
  item_id = data['item_id']
  name = data['name']
  description = data['description']
  value = data['value']
  date = data['date']    
  pr.add_item(collection, item_id, name, description, value, date)  
  return jsonify({"message": "Item added successfully"})
  
@app.route('/get_item/<item_id>', methods=['GET'])
def get_item_route(item_id):
    try:
        item = pr.get_item(collection, item_id)
        return jsonify(item)
    except ValueError:
        return jsonify({"message": "Item not found"})

@app.route('/update_item/<item_id>', methods=['PUT'])
def update_item_route(item_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    value = data.get('value')
    date = data.get('date')

    if value is not None:
        value = float(value)

    pr.update_item(collection, item_id, name, description, value, date)

    return jsonify({"message": "Item updated successfully"})

@app.route('/delete_item/<item_id>', methods=['DELETE'])
def delete_item_route(item_id):
    try:
        pr.delete_item(collection, item_id)
        return jsonify({"message": "Item deleted successfully"})
    except KeyError:
        return jsonify({"message": "Item not found"})

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

