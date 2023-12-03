"""
testing connectivity on vercel
"""

from http.server import BaseHTTPRequestHandler
import psycopg2
import os


class handler(BaseHTTPRequestHandler):

    def db_connection():
        return psycopg2.connect(
            host=os.environ.get('POSTGRES_HOST'),
            dbname=os.environ.get('POSTGRES_DATABASE'),
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get('POSTGRES_PASSWORD'),
            # port=os.environ.get('PORT'),
        )

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<h1>Hello, world! Test3<h1>'.encode('utf-8'))

        conn = self.db_connection()
        cursor = conn.cursor()
        cursor.execute("select * from comercio.tickers_daily order by ticker")
        values_array = list(cursor.fetchall())
        self.wfile.write(f"Found {} rows".format(len(values_array)))

        return
