from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

def do_the_login():
    # Mendapatkan data yang dikirimkan oleh pengguna melalui POST request
    username = request.form['username']
    password = request.form['password']
    
    # Contoh validasi sederhana - biasanya Anda akan memeriksa kredensial dalam basis data atau sistem autentikasi lainnya
    if username == 'admin' and password == 'password':
        # Kredensial valid, bisa lakukan tindakan lanjutan seperti mengizinkan akses atau menyimpan sesi login
        return 'Login successful!'
    else:
        # Kredensial tidak valid, kembalikan pesan kesalahan
        return 'Invalid username or password!'

def show_the_login_form():
    # Tampilkan formulir login
    return 'This is the login form.'

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/logina', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

app.run(debug=True)