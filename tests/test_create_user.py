# test_user_creation.py
import json
from playwright.sync_api import sync_playwright
from pojos.user import User

BASE_URL = "https://reqres.in/api/"

def test_create_user():
    with sync_playwright() as p:
        user = User("morpheus", "leader")
        browser = p.request.new_context(base_url=BASE_URL)
        user_data = json.dumps(user.__dict__)
        response = browser.post("users", data=user_data, headers={"Content-Type": "application/json"})
        assert response.status == 201
        json_response = response.json()
        assert "id" in json_response
        assert json_response["name"] == user.name
        assert json_response["job"] == user.job
