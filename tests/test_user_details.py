import logging
from playwright.sync_api import sync_playwright

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

BASE_URL = "https://reqres.in/api/"

def test_get_user_details():
    logger.info("Iniciando teste de obtenção de detalhes do usuário.")
    with sync_playwright() as p:
        user_id = 2
        browser = p.request.new_context(base_url=BASE_URL)
        response = browser.get(f"users/{user_id}")
        assert response.status == 200
        user_details = response.json()["data"]
        assert user_details["id"] == user_id
        logger.info(f"Detalhes do usuário com ID {user_id} obtidos com sucesso.")

