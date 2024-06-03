from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !!!!!</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')  #commentaire23
def exercices():
    return render_template('exercices.html')

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
  res = val_user * val_user
  if val_user % 2 == 0:
    return f"<h2>Le carré de votre valeur est : {res}</h2><h3>Nombre pair</h3>"
  else:
    return f"<h2>Le carré de votre valeur est : {res}</h2><h3>Nombre impair</h3>"

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(val1,val2):
  res = val1 + val2
  if res % 2 == 0:
    return f"<h2>Le resulat de la somme de {val1} + {valeur2} est : {resultat}</h2><h3>Nombre pair</h3>"
  else:
    return f"<h2>Le resulat de la somme de {val1} + {valeur2} est : {resultat}</h2><h3>Nombre impair</h3>"



                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
