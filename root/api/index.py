"""
testing connectivity on vercel
"""

from http.server import BaseHTTPRequestHandler
import os
import psycopg2


class handler(BaseHTTPRequestHandler):

    def db_connection(self):
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
        num_rows = len(values_array)
        self.wfile.write(f"Found {num_rows} rows")

        return
