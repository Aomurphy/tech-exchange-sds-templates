
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware",
 "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Indiana", "Kansas", "Kentucky", "Louisiana", 
 "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", 
 "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "New York", "Ohio", "Oklahoma", 
 "Oregon", "Pennsylvania", "South Carolina", "Tennessee", "Texas",
  "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
capital_dic={
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
} 
previous_correct=[]
app = Flask('app')
@app.route('/scorepage',methods=["POST","GET"])

def output():
  correctA=len(previous_correct)
  for state in state_names:
    if request.method=="POST":
        answer = request.form['capital']
           
        correct = answer == capital_dic[state]
        if(correct):
            previous_correct.append(answer)  
            correctA=len(previous_correct)
  return render_template("scorepage.html", previous_correct=previous_correct,correct=correctA)
  
@app.route('/')
def hello_world():
  return render_template("index.html",state_names=state_names,correctA=0)


app.run(host='0.0.0.0', port=8080)


# -- Routes section --
# @app.route('/')
# @app.route('/index')
# def index():
#     return "hello world"
