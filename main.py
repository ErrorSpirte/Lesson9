from flask import Flask, render_template
import random 

app = Flask(__name__)

list_facts = []
with open('facts.txt','r',encoding='UTF-8') as f:
    list_facts = f.readlines()

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/random') 
def get_random_number():
    return str(random.randint(1,1000))

@app.route('/fact')
def facts():
   return render_template('fact.html',fact=random.choice(list_facts))

@app.route('/game')
def game():
    result = random.choice(['Орел', 'Решка'])
    return f"Результат броска монетки: {result}"

@app.route('/fact/<number>')
def facts_number(number):
   try:
      return render_template('fact.html',fact=list_facts[int(number)])
   except:
      return 'упс... что-то пошло не так'

app.run(debug=True)