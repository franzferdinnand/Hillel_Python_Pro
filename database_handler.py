import sqlite3
import datetime
from datetime import time
import time


def execute_query(query):
    with sqlite3.connect('chinook.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        records = cursor.fetchall()
    return records


def count_tracks_duration():
    query = 'SELECT SUM(Milliseconds) FROM tracks'
    data = execute_query(query)
    millis = int(data[0][0])
    seconds = (millis / 1000) % 60
    minutes = (millis / (1000 * 60)) % 60
    hours = (millis / (1000 * 60 * 60))
    return "%d:%d:%d" % (hours, minutes, seconds)


