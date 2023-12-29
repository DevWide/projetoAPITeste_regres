import json
from playwright.sync_api import sync_playwright
from pojos.user import User

BASE_URL = "https://reqres.in/api/"

def test_create_user():
    with sync_playwright() as p:
        user = User("morpheus", "leader")
        browser = p.request.new_context(base_url=BASE_URL)

        # Convertendo o objeto user para JSON
        user_data = json.dumps(user.__dict__)

        # Enviando os dados como JSON para o endpoint correto
        response = browser.post("users", data=user_data, headers={"Content-Type": "application/json"})

        # Verificando o status da resposta
        assert response.status == 201, f"Unexpected status code: {response.status}"
        json_response = response.json()
        assert "id" in json_response, "Response does not contain 'id'"
        assert json_response["name"] == user.name, f"Expected name to be {user.name}, but got {json_response['name']}"
