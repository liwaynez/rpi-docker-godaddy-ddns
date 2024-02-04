from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
<<<<<<< HEAD
  return 'Welcome to the Toonchs Raspberry Pi web application!'
=======
  return 'Welcome to da the Raspberry Pi web application!'
>>>>>>> 82f7f68 (removed jupyter)
