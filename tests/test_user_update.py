import logging
import json
from playwright.sync_api import sync_playwright

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

BASE_URL = "https://reqres.in/api/"

def test_update_user():
    logger.info("Iniciando teste de atualização de usuário.")
    with sync_playwright() as p:
        user_id = 2
        updated_data = {"name": "morpheus", "job": "zion resident"}
        browser = p.request.new_context(base_url=BASE_URL)
        response = browser.put(f"users/{user_id}", data=json.dumps(updated_data), headers={"Content-Type": "application/json"})

        assert response.status == 200
        updated_user = response.json()
        assert updated_user["name"] == updated_data["name"]
        assert updated_user["job"] == updated_data["job"]
        logger.info(f"Usuário com ID {user_id} atualizado com sucesso.")

