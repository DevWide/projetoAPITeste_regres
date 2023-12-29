import json
from playwright.sync_api import sync_playwright

BASE_URL = "https://reqres.in/api/"

def test_user_login():
    with sync_playwright() as p:
        credentials = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        browser = p.request.new_context(base_url=BASE_URL)
        response = browser.post("/api/login", data=json.dumps(credentials), headers={"Content-Type": "application/json"})
        assert response.status == 200


def test_login_failure():
    with sync_playwright() as p:
        wrong_credentials = {"email": "eve.holt@reqres.in"}
        browser = p.request.new_context(base_url=BASE_URL)
        response = browser.post("/api/login", data=json.dumps(wrong_credentials), headers={"Content-Type": "application/json"})
        assert response.status == 400

