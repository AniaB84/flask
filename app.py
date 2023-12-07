from flask import Flask, render_template, request, redirect
import json
import csv
import requests




app = Flask(__name__)

codes = ["USD", "AUD","CAD", "EUR", "HUF", "CHF", "GBP", "JPY", "CZK", "DKK", "NOK", "SEK", "XDR"]  

def get_rates():

    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    rates = data[0]["rates"]

    return rates
    

@app.route("/save_rates", methods=["GET", "POST"])
def save_rates():
    rates = get_rates()

    header=rates[0].keys()
    print(header)
    
    with open('rates.csv', "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(rates)
        
    return "Zapisano poprawnie"   

@app.route('/exchange', methods=["GET", "POST"])
def calculator():
    result = None
    rates = get_rates()
    
    if request.method == "POST":
        amount = request.form["amount"]
        for rate in rates:
            if rate["code"] == request.form["currency"]:
                result = round((float(rate["ask"]) * float(amount)), 2)
    return render_template("data.html", rates=rates, result=result)
