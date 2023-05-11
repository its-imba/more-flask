from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="POST" action="/greet">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="user_name" required>
            <button type="submit">Submit</button>
        </form>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    user_name = request.form['user_name']
    return f'Hello, {user_name}!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
