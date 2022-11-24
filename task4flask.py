from flask import Flask, escape
import pandas as pd
import random
import string

app = Flask(__name__)


@app.route('/')
def main_page():
    return '<title>Turchyn\'s main page</title>' \
           '<h1>Turchyn\'s main page for homework#2</h1>' \
           '<hr>' \
           '<a>If you want to generate password, </a><a href=http://127.0.0.1:5001/password>click here</a><br>' \
           '<br>' \
           '<a>If you want to see the average parameters of students, </a>' \
           '<a href=http://127.0.0.1:5001/average>click here</a>'


@app.route('/password')
def generate_password():
    letters_up = string.ascii_uppercase
    letters_low = string.ascii_lowercase
    digits = string.digits
    spec_sym = string.punctuation
    length = random.randint(10, 20)
    password = []

    for _ in range(length):
        password.append(random.choice(letters_up))
        password.append(random.choice(letters_low))
        password.append(random.choice(digits))
        password.append(random.choice(spec_sym))

    password_result = ''.join(password)

    return '<title>PASSWORD GENERATOR</title>' \
           '<h1>PASSWORD GENERATOR</h1>' \
           '<hr>' \
           f'<p>Your password is: {escape(password_result[:length])}</p>' \
           '<a href=http://127.0.0.1:5001/password>Generate a new password</a><br>' \
           '<br>' \
           '<a href=http://127.0.0.1:5001>back to main page</a>'


@app.route('/average')
def average_params():
    data = pd.read_csv('hw.csv')
    df = pd.DataFrame(data, columns=[' Height(Inches)', ' Weight(Pounds)'])
    height_average = df[' Height(Inches)'].mean()
    weight_average = df[' Weight(Pounds)'].mean()

    return '<title>AVERAGE PARAMETERS OF STUDENTS</title>' \
           '<h1>AVERAGE PARAMETERS OF STUDENTS</h1>' \
           '<hr>' \
           f'<p>The average height of students is {format(height_average, ".2f")} inches</p>' \
           f'<p>The average weight of students is {format(weight_average, ".2f")} pounds</p>' \
           '<br>' \
           '<a href=http://127.0.0.1:5001>back to main page</a>'


app.run(port=5001, debug=True)
