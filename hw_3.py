import pandas as pd
import requests
from faker import Faker
from flask import Flask, jsonify, Response
from http import HTTPStatus
from webargs import fields, validate
from webargs.flaskparser import use_kwargs

app = Flask(__name__)

URL = 'https://bitpay.com/api/rates/{}'
CURRENCY_INFO = 'https://bitpay.com/currencies'


@app.errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
@app.errorhandler(HTTPStatus.BAD_REQUEST)
def error_handler(error):
    headers = error.data.get('headers', None)
    messages = error.data.get('messages', ["Invalid request."])

    if headers:
        return jsonify(
            {
                'errors': messages
            },
            error.code,
            headers
        )
    else:
        return jsonify(
            {
                'errors': messages
            },
            error.code,
        )


@app.route('/')
def main_page():
    return "<h1>Welcome to homework number 3</h1>" \
           "<hr>" \
           "<a>To see a database of students </a><a href=http://127.0.0.1:5001/generate_students>click here</a><br>" \
           "<br>" \
           "<a>To see a Bitcoin rates </a><a href=http://127.0.0.1:5001/bitcoin_value>click here</a><br>"


@app.route('/generate_students')
@use_kwargs(
    {
        'count': fields.Int(
            missing=100,
            validate=[validate.Range(min=1, max=1000)]

        )
    },
    location='query'
)
def generate_students(count):
    data = []
    for _ in range(count):
        student = Faker('UK')
        students_data = []
        students_data.append(student.first_name())
        students_data.append(student.last_name())
        students_data.append(student.email())
        students_data.append(student.password(length=15))
        students_data.append(Faker().profile()['birthdate'])
        data.append(students_data)
    df = pd.DataFrame(data, columns=['first_name', 'last_name', 'email', 'password', 'birth_date'])
    df.to_csv('students.csv', mode='w', index=False)

    result = pd.read_csv('students.csv')
    return f"<h1>STUDENTS</h1>" \
           f"<hr>" \
           f"<a href=http://127.0.0.1:5001>back</a><br>" \
           f"{result.to_html(index=False)}" \
           f"<br><a href=http://127.0.0.1:5001>back</a>"


@app.route('/bitcoin_value')
@use_kwargs(
    {
        'currency': fields.Str(
            missing='USD',
            validate=validate.Regexp(regex='[A-Z]{3}', error='ERROR: wrong currency format')
        ),
        'count': fields.Int(
            missing=50
        )
    },
    location='query'
)
def get_bitcoin_value(currency, count):
    bitcoin_sign = '\U000020BF'
    response = requests.get(URL.format(currency))
    currency_data = requests.get(CURRENCY_INFO)
    if response.status_code not in (HTTPStatus.OK,) or currency_data.status_code not in (HTTPStatus.OK,):
        return Response(
            "ERROR: Something went wrong",
            status=response.status_code
        )
    rates_data = response.json()
    currency_response = currency_data.json()
    symbols = currency_response['data']
    for search in symbols:
        if currency == search['code']:
            symbol = search['symbol']

    summary = int(rates_data['rate']) * count

    return f'<h1>{bitcoin_sign}itcoin exchange rates with {symbol} {rates_data["name"]}</h1>' \
           f'<hr>' \
           f'<p>Rate of {bitcoin_sign}1 = {symbol} {int(rates_data["rate"]):,}</p>' \
           f'<p>{bitcoin_sign}{count}  = {symbol}{summary:,} </p>' \
           f'<a href=http://127.0.0.1:5001>back</a>'


if __name__ == '__main__':
    app.run(port=5001, debug=True)
