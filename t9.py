import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    maximo = 100

    a = 1
    cont = 1
    valor = 3
    
    primos = "2, "


    while cont < maximo:
        primo = 1
        for p in range(2, valor):
            if valor % p == 0:
                primo = 0
                break
        if(primo):
            primos = primos + str(valor) + ","
            cont += 1
            if(cont % 10 == 0):
                primos = primos + "<br>"
        valor+=1

    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
