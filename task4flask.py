from flask import Flask
import pandas as pd
import random

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
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*']
    password_list = []
    num_of_chars = random.randint(10, 20)

    for char in range(1, num_of_chars - 3):
        password_list.append(random.choice(letters))

    for char in range(1, num_of_chars - 5):
        password_list.append(random.choice(numbers))

    for char in range(1, num_of_chars - 7):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password_result = ''.join(password_list)

    return '<title>PASSWORD GENERATOR</title>' \
           '<h1>PASSWORD GENERATOR</h1>' \
           '<hr>' \
           f'<p>Your password is: {password_result[:num_of_chars+1]}</p>' \
           '<a href=http://127.0.0.1:5001/password>Generate a new password</a><br>' \
           '<br>' \
           '<a href=http://127.0.0.1:5001>back to main page</a>'

@app.route('/average')
def average_params():
    """Provide the right path to your hw.csv instead of /users/brian/Downloads/hw.csv"""
    data = pd.read_csv('/users/brian/Downloads/hw.csv')
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

