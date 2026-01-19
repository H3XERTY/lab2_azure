import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    # Temps d'attente entre chaque requête (optionnel, ici entre 1 et 5 secondes)
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        # ATTENTION : J'ai mis votre route réelle ici (/numericalintegralservice/...)
        # au lieu de celle de l'image (/integral/...) qui ne marcherait pas.
        self.client.get("/numericalintegralservice/0.0/3.14159")
