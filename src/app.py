from flask import Flask
from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
    ]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text,200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos),201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # request_body = request.get_json(force=True)
    print("This is the position to delete:", position)
    del todos[position]
    return jsonify(todos),204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)