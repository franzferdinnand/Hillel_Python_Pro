import pandas as pd
from database_handler import execute_query
from database_handler import count_tracks_duration
from flask import Flask
from webargs import fields, validate
from webargs.flaskparser import use_kwargs


app = Flask(__name__)


@app.route('/')
def main():
    return "<h1>Welcome to homework number 3</h1>" \
           "<hr>" \
           "<a>To see a database of sales </a><a href=http://127.0.0.1:5100/order-price>click here</a><br>" \
           "<br>" \
           "<a>To see all tracks info and duration </a><a href=http://127.0.0.1:5100/tracks-info>click here</a><br>"


@app.route('/order-price')
@use_kwargs(
    {
        'country': fields.Str(
            required=False,
            missing=None,
            validate=[validate.Regexp("^[a-zA-Z]+")]

        )
    },
    location='query'
)
def order_price(country):
    query = "SELECT (SAL.UnitPrice * SUM(SAL.Quantity)) AS SALES, CUS.BillingCountry  " \
            "FROM invoice_items AS SAL JOIN invoices AS CUS " \
            "ON CUS.InvoiceId = SAL.InvoiceId "

    if country:
        query += f"WHERE CUS.BillingCountry = '{country}'"
    else:
        query += f"GROUP BY CUS.BillingCountry "

    records = execute_query(query=query)
    df = pd.DataFrame(records, columns=['Sales', 'Country'])
    return f"{df.to_html(index=False)}"


@app.route('/tracks-info')
@use_kwargs(
    {
        'track_id': fields.Int(
            required=False,
            missing=None
        )
    },
    location='query'
)
def get_all_info_about_track(track_id):
    query = "SELECT t.TrackId, t.Name AS Track, a2.Name AS Artist, a.Title AS Album, t.Composer,g.Name AS Genre, " \
            "GROUP_CONCAT(pl.Name) AS Playlist, t.Milliseconds, mt.Name AS MediaType,t.UnitPrice, SUM(ii.Quantity) AS Sales " \
            "FROM tracks AS t JOIN albums AS a ON t.AlbumId = a.AlbumId  " \
            "JOIN artists AS a2 ON a2.ArtistId = a.ArtistId JOIN genres AS g ON g.GenreId = t.GenreId " \
            "JOIN media_types AS mt ON mt.MediaTypeId = t.MediaTypeId " \
            "LEFT JOIN invoice_items AS ii ON t.TrackId = ii.TrackId " \
            "JOIN playlist_track AS pt ON t.TrackId = pt.TrackId " \
            "JOIN playlists AS pl ON pt.PlaylistId = pl.PlaylistId "
    if track_id:
        query += f"WHERE t.TrackId = {int(track_id)}"
    else:
        query += f"GROUP BY t.TrackId"

    records = execute_query(query=query)
    df = pd.DataFrame(records, columns=['Track_Id', 'Track', 'Artist', 'Album', 'Composer', 'Genre',
                                        'Playlist', 'Duration(ms)', 'Type', 'Price', 'Sales'])
    return f"<h1>All tracks duration is {str(count_tracks_duration())}" \
           f"<hr>" \
           f"<a href=http://127.0.0.1:5100/> back </a>" \
           f"<br>" \
           f"{df.to_html(index=False)}"


app.run(port=5100, debug=True)
