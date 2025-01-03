from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import requests
from InzhurScraper import InzhurScraper

app = Flask(__name__)
data = {}
scrapper = InzhurScraper()
def fetch_data():
    global data
    data = scrapper.scrape()

scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_data, trigger="interval", minutes=1)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

@app.route('/getdata', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    fetch_data()  # Initial fetch
    app.run(debug=True)