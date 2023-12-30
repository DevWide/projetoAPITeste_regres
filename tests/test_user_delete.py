import logging
from playwright.sync_api import sync_playwright

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

BASE_URL = "https://reqres.in/api/"

def test_delete_user():
    logger.info("Iniciando teste de exclusão de usuário.")
    with sync_playwright() as p:
        user_id = 2
        browser = p.request.new_context(base_url=BASE_URL)
        response = browser.delete(f"users/{user_id}")
        assert response.status == 204
        logger.info(f"Usuário com ID {user_id} excluído com sucesso.")

