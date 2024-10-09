from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  


@app.route('/')
def hello_world():
    return render_template('hello.html')



@app.route("/contact/")
def mapagecontact():
    return render_template('contact.html')




@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)




@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")




@app.route("/histogramme/")
def monhistogramme():
    return render_template("histogramme.html")



@app.route("/camembert/")
def moncamambert():
    return render_template("camembert.html")



@app.route('/commits/')
def commits():
    return render_template('commits.html')

@app.route('/extract-minutes/<date_string>')
def extract_minutes(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
    minutes = date_object.minute
    return jsonify({'minutes': minutes})

def fetch_commits():
    url = 'https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits'
    response = requests.get(url)
    return response.json()






API_KEY = '8ee609855bac79e1c36c3766701dcf90622d68855d687bfb6def45f46396d812'

# URL de l'API SerpAPI pour Google Flights
url = 'https://serpapi.com/search.json'

# Fonction pour obtenir les vols
def get_flights():
    params = {
        'engine': 'google_flights',
        'departure_id': 'CDG',  # ID d'aéroport pour CDG
        'arrival_id': 'LAX',  # Exemple d'aéroport d'arrivée (Los Angeles)
        'outbound_date': '2024-10-09',  # Date de départ
        'type': '0',  # 0 pour aller simple
        'api_key': API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('flights_results', [])
    else:
        print(f"Erreur: {response.status_code}, {response.text}")
        return []

@app.route('/vacance/')
def vacance():
    flights = get_flights()  # Obtient les résultats des vols
    return render_template("index.html", flights=flights)





  
if __name__ == "__main__":
  app.run(debug=True)
