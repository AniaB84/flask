from flask import Flask, render_template, request, redirect
import json
import csv
app = Flask(__name__)
import requests

@app.route("/save_rates", methods=["GET", "POST"])
def save_rates():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    print(data)
    if request.method == 'GET':
       rates = [{"currency":"dolar amerykański","code":"USD","bid":4.1098,"ask":4.1928},{"currency":"dolar australijski","code":"AUD","bid":2.6426,"ask":2.6960},{"currency":"dolar kanadyjski","code":"CAD","bid":2.9818,"ask":3.0420},{"currency":"euro","code":"EUR","bid":4.3938,"ask":4.4826},{"currency":"forint (Węgry)","code":"HUF","bid":0.0116,"ask":0.011834},{"currency":"frank szwajcarski","code":"CHF","bid":4.5704,"ask":4.6628},{"currency":"funt szterling","code":"GBP","bid":5.0474,"ask":5.1494},{"currency":"jen (Japonia)","code":"JPY","bid":0.027246,"ask":0.027796},{"currency":"korona czeska","code":"CZK","bid":0.1785,"ask":0.1821},{"currency":"korona duńska","code":"DKK","bid":0.5891,"ask":0.6011},{"currency":"korona norweska","code":"NOK","bid":0.3673,"ask":0.3747},{"currency":"korona szwedzka","code":"SEK","bid":0.3766,"ask":0.3842},{"currency":"SDR (MFW)","code":"XDR","bid":5.4142,"ask":5.5236}]
       return rates
    with open('rates.csv', newline='') as csvfile:
           reader = csv.DictReader(csvfile)
           for row in reader:
               return (row['currency'], row['code'], row['bid'], row['row'])
codes = []    

@app.route('/exchange', methods=["GET", "POST"])
def calculator():
    result = None
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    print(data)
    
    if request.method == "POST":
        amount = request.form["amount"]
        for rate in rates:
            if rate["code"] == request.form["codes"]:
                result = round((float(rate["ask"]) * float(amount)), 2)
    return render_tamplate("data.html", codes=codes, date=date, result=result)