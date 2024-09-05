from flask import Flask, request, jsonify
app = Flask(__name__)
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    operation = data.get('operation')
    if not num1 or not num2 or not operation:
        return jsonify({"error": "Please provide num1, num2, and operation"}), 400
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 400
    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        return jsonify({"error": "Invalid operation"}), 400
    return jsonify({"result": result})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)