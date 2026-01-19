import math

def f(x):
    # La fonction demandée : valeur absolue de sin(x)
    return abs(math.sin(x))

def compute_integral(lower, upper, n):
    total_area = 0.0
    step = (upper - lower) / n  # Largeur de chaque rectangle
    
    # On boucle n fois pour sommer les aires
    for i in range(n):
        x = lower + i * step
        # Aire = Hauteur * Largeur
        total_area += f(x) * step
        
    return total_area

# Paramètres de l'exercice
lower_bound = 0
upper_bound = 3.14159
n_values = [10, 100, 1000, 10000, 100000, 1000000]

print(f"Calcul de l'intégrale de {lower_bound} à {upper_bound}")
print("-" * 40)

for n in n_values:
    result = compute_integral(lower_bound, upper_bound, n)
    # Affichage formaté pour voir la convergence
    print(f"N = {n:<7} | Resultat = {result:.6f}")