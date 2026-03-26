import pyscreenshot
import time
import threading
from flask import Flask, send_file
import os
from datetime import datetime

app = Flask(__name__)

def take_screenshots():
    while True:
        image = pyscreenshot.grab()
        filename = datetime.now().strftime("%Y-%m-%d-%H.png")
        image.save(filename)
        time.sleep(20)

@app.route('/')
def get_screenshot():
    files = [f for f in os.listdir('.') if f.endswith('.png')]
    if not files:
        return "No screenshots yet", 404
    latest = max(files, key=lambda f: os.path.getmtime(f))
    return send_file(latest, mimetype='image/png')

if __name__ == "__main__":
    screenshot_thread = threading.Thread(target=take_screenshots)
    screenshot_thread.daemon = True
    screenshot_thread.start()
    app.run(host='0.0.0.0', port=5000)
