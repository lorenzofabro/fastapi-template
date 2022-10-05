from config.main import app
from fastapi.testclient import TestClient

client = TestClient(app)
