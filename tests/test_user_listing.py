import logging
from playwright.sync_api import sync_playwright

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

BASE_URL = "https://reqres.in/api/"

def test_list_users():
    logger.info("Iniciando teste de listagem de usuários.")
    with sync_playwright() as p:
        browser = p.request.new_context(base_url=BASE_URL)
        response = browser.get("users?page=2")
        assert response.status == 200

        users = response.json()["data"]
        assert len(users) > 0
        logger.info(f"Número de usuários encontrados na página 2: {len(users)}")

