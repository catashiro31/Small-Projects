import requests
import selectorlib
import ssl
import time
import os
import smtplib
import psycopg2

URL = "http://programmer100.pythonanywhere.com/tours/"
def scrape(url):
    response = requests.get(url)
    src = response.text
    return src

def extract(src):
    extractor = selectorlib.Extractor.from_yaml_file(r"F:\App\Practise\Web Scrape Music Events\extract.yaml")
    data = extractor.extract(src)['tours']
    return data

def send_email(data):
    host = 'smtp.gmail.com'
    port = 465
    sender_email = 'user'
    receiver_email = 'user'
    password = os.getenv('EMAIL_PASS')
    subject = 'New Tour'
    body = f'New music event found:\n{data}'
    message = f'Subject: {subject}\n\n{body}'
    context = ssl._create_unverified_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print('Email sent successfully!')

conn = psycopg2.connect(
    database="data_1",
    user="postgres",
    password=os.getenv('POSTGRES_PASS'),
    host="localhost",
    port="5432"       
)
cur = conn.cursor()

def query(data):
    row = data.split(',')
    row = [item.strip() for item in row]
    band, city, date = row[0], row[1], row[2]
    cur.execute('SELECT * FROM events WHERE band = %s AND city = %s AND date = %s', (band, city, date))
    result = cur.fetchall()
    return result
    
def write(data):
    row = data.split(',')
    row = [item.strip() for item in row]
    band, city, date = row[0], row[1], row[2]
    cur.execute('INSERT INTO events (band, city, date) VALUES (%s, %s, %s)', (band, city, date))
    conn.commit()


if __name__ == "__main__":
    while True:
        src = scrape(URL)
        data = extract(src)
        if data != 'No upcoming tours':
            row = query(data)
            if not row:
                write(data)
                send_email(data)
        time.sleep(5)