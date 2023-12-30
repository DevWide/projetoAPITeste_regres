import json
import logging
from playwright.sync_api import sync_playwright
from pojos.user import User

BASE_URL = "https://reqres.in/api/"

def test_create_user():
    logging.info("Iniciando o teste de criação de usuário.")
    with sync_playwright() as p:
        user = User("morpheus", "leader")
        browser = p.request.new_context(base_url=BASE_URL)

        user_data = json.dumps(user.__dict__)
        response = browser.post("users", data=user_data, headers={"Content-Type": "application/json"})
        logging.info(f"Status code da resposta: {response.status}")

        json_response = response.json()
        assert "id" in json_response, "Response does not contain 'id'"
        assert json_response["name"] == user.name, f"Expected name to be {user.name}, but got {json_response['name']}"
        assert json_response["job"] == user.job, f"Expected job to be {user.job}, but got {json_response['job']}"

        assert isinstance(int(json_response["id"]), int), "ID should be an integer"
        assert isinstance(json_response["name"], str), "Name should be a string"
        assert isinstance(json_response["job"], str), "Job should be a string"
        logging.info("Teste de criação de usuário concluído com sucesso.")
