import pandas as pd
from flask import Flask
from webargs import fields, validate
from webargs.flaskparser import use_kwargs
from database_handler import execute_query
from database_handler import count_tracks_duration

app = Flask(__name__)

@app.route('/')
@use_kwargs(
    {
        'genre': fields.Str(
            required=True,

        )
    },
    location='query'
)
def country_by_genre(genre):
    qurey = "SELECT  g.Name, i.BillingCountry, SUM(ii.Quantity) FROM genres g " \
            "JOIN tracks t on g.GenreId = t.GenreId JOIN invoice_items ii on t.TrackId = ii.TrackId " \
            "JOIN invoices i on i.InvoiceId = ii.InvoiceId WHERE g.Name = '{}' GROUP BY g.Name, i.BillingCountry "

    if not execute_query(qurey.format(genre)):
        return '<h1> Genre not found </h1>'
    record = execute_query(qurey.format(genre))
    max_listeners = [max(record, key=lambda q: int(q[2]))]
    df = pd.DataFrame(max_listeners, columns=['Genre', 'Country', 'Number of sales'])
    return f"{df.to_html(index=False)}"



app.run(port=5001, debug=True)
