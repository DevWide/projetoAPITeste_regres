import json
import logging
from playwright.sync_api import sync_playwright

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://reqres.in/api/"

def test_user_login():
    logger.info("Testando login com credenciais válidas.")
    with sync_playwright() as p:
        credentials = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        browser = p.request.new_context(base_url=BASE_URL)
        response = browser.post("/api/login", data=json.dumps(credentials), headers={"Content-Type": "application/json"})
        assert response.status == 200
        logger.info("Login bem-sucedido.")

def test_login_failure():
    logger.info("Testando login com credenciais inválidas.")
    with sync_playwright() as p:
        wrong_credentials = {"email": "eve.holt@reqres.in"}
        browser = p.request.new_context(base_url=BASE_URL)
        response = browser.post("/api/login", data=json.dumps(wrong_credentials), headers={"Content-Type": "application/json"})
        assert response.status == 400
        logger.info("Falha no login conforme esperado.")
