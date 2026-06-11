from locust import HttpUser, task, between

class UsuarioAPI(HttpUser):
    wait_time = between(1, 3)
    host = "http://127.0.0.1:8000"

    @task(3)
    def listar_productos(self):
        self.client.get("/api/productos/")

    @task(2)
    def inicio(self):
        self.client.get("/")

    @task(1)
    def comunidades(self):
        self.client.get("/comunidades/")