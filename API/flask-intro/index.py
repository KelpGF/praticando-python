from flask import Flask, render_template

from data import persons 

app = Flask(__name__)

print(persons)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/persons')
def listPersons():
  personsList = map(lambda person: person.showContent(), persons)

  return render_template('index.html', persons = " - ".join(list(personsList)))

if __name__ == '__main__':
  app.run()