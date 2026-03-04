from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# History to keep track of calculations
global history
history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    operation = request.json.get('operation')
    value1 = request.json.get('value1')
    value2 = request.json.get('value2')
    result = None

    if operation == 'add':
        result = value1 + value2
    elif operation == 'subtract':
        result = value1 - value2
    elif operation == 'multiply':
        result = value1 * value2
    elif operation == 'divide':
        if value2 != 0:
            result = value1 / value2
        else:
            return jsonify({'error': 'Cannot divide by zero'}), 400
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    history.append({'operation': operation, 'value1': value1, 'value2': value2, 'result': result})
    return jsonify({'result': result})

@app.route('/history')
def get_history():
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True)