import json
import logging
from playwright.sync_api import sync_playwright
from pojos.user import User

# Obter uma instância do logger
logger = logging.getLogger(__name__)

BASE_URL = "https://reqres.in/api/"

def test_create_user():
    logger.info("Iniciando o teste de criação de usuário.")
    with sync_playwright() as p:
        user = User("morpheus", "leader")
        browser = p.request.new_context(base_url=BASE_URL)

        user_data = json.dumps(user.__dict__)
        response = browser.post("users", data=user_data, headers={"Content-Type": "application/json"})
        json_response = response.json()

        logger.info(f"Status code da resposta: {response.status}")
        logger.info(f"Usuário criado: Nome: {json_response.get('name', 'Não disponível')}, "
                    f"Trabalho: {json_response.get('job', 'Não disponível')}, "
                    f"ID: {json_response.get('id', 'Não disponível')}")

        assert response.status == 201, "Expected status code to be 201 Created"
        assert "id" in json_response, "Response does not contain 'id'"
        assert json_response["name"] == user.name, f"Expected name to be {user.name}, but got {json_response['name']}"
        assert json_response["job"] == user.job, f"Expected job to be {user.job}, but got {json_response['job']}"

        logger.info("Teste de criação de usuário concluído com sucesso.")
