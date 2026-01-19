from flask import Flask, jsonify
import math

app = Flask(__name__)

# --- Logique métier (identique à votre script précédent) ---

def f(x):
    return abs(math.sin(x))

def compute_integral(lower, upper, n):
    total_area = 0.0
    step = (upper - lower) / n
    for i in range(n):
        x = lower + i * step
        total_area += f(x) * step
    return total_area

# --- Définition de la route (Endpoint) ---

@app.route('/numericalintegralservice/<float:lower>/<float:upper>')
def integral_service(lower, upper):
    # Les valeurs de N à tester
    n_values = [10, 100, 1000, 10000, 100000, 1000000]
    results = []

    # On boucle sur chaque N et on stocke le résultat
    for n in n_values:
        res = compute_integral(lower, upper, n)
        results.append({
            "N": n,
            "result": res
        })

    # On renvoie la réponse au format JSON (standard pour les microservices)
    return jsonify({
        "meta": {
            "lower": lower,
            "upper": upper
        },
        "computations": results
    })

if __name__ == '__main__':
    # On écoute sur toutes les interfaces (0.0.0.0) sur le port 5000
    app.run(host='0.0.0.0', port=5000)