from ast import Return
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return 'Rodando'

@app.route('/ola')
@app.route('/ola/<nome>')
def ola(nome = 'mundo'): 
  return render_template('teste.html', nome = nome)

if __name__ == '__main__':
  app.run()