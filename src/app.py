from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'Welcome to the Toonch\'s Raspberry Pi web application Container!'
=======
  return 'Welcome to da the Raspberry Pi web application!'
