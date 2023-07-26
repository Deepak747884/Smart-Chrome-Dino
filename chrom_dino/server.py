from flask import Flask, render_template
from run import run_dino

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('start.html')

@app.route('/index.html')
def other_page():
    # Add code to handle "index.html" here if needed
    return render_template('index.html')

@app.route('/my-link/')
def my_link():
  run_dino()

if __name__ == '__main__':
  app.run(debug=True)