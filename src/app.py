from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'Welcome to the Toonchs Raspberry Pi web application!'
=======
  return 'Welcome to da the Raspberry Pi web application!'
