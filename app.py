from flask import Flask, flash, request, redirect, url_for, send_from_directory
from time import sleep

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def counteverytwo():
    if request.method == 'POST':
        for i in range(1, 10):
            sleep(5)
            print("serving requester # " + str(request.form['user']) + " with response " + str(i))
    return '''
    <!doctype html>
    <h1>Click</h1>
    <form method=post>
      <input type=text name='user'>
      <input type=submit value=click>
    </form>
    '''
