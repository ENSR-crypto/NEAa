from flask import Flask, request, render_template
import random as r
import time as t 


app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        return f"Hello {name}, POST request received"
    return render_template('login.html')

@app.route('/home')
def main():
    return render_template('mainMenu.html')
    
@app.route('/new', methods=['GET'])
def main2():
    return render_template('newGameMenu.html')
    
@app.route('/game', methods=['GET','POST'])
def main3():
    return render_template('mainGame.html')
    
if __name__ == '__main__':
    app.run(debug=True)