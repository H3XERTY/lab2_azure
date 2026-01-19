import azure.functions as func
import logging
import math
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def compute_integral(lower, upper, n):
    total_area = 0.0
    step = (upper - lower) / n
    for i in range(n):
        x = lower + i * step
        total_area += abs(math.sin(x)) * step
    return total_area

@app.route(route="numericalintegralservice/{lower}/{upper}")
def numericalintegralservice(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Trigger function processed a request.')
    try:
        lower = float(req.route_params.get('lower'))
        upper = float(req.route_params.get('upper'))
    except:
        return func.HttpResponse("Erreur parametres", status_code=400)

    n_values = [10, 100, 1000, 10000, 100000, 1000000]
    results = []
    for n in n_values:
        results.append({"N": n, "result": compute_integral(lower, upper, n)})

    return func.HttpResponse(
        json.dumps({"meta": {"lower": lower, "upper": upper}, "computations": results}),
        mimetype="application/json",
        status_code=200
    )
