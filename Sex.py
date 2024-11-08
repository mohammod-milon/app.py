app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form action="/login" method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return f'Username: {username}, Password: {password}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
