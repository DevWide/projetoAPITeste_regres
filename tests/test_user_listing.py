from playwright.sync_api import sync_playwright

BASE_URL = "https://reqres.in/api/"

def test_list_users():
    with sync_playwright() as p:
        browser = p.request.new_context(base_url=BASE_URL)
        response = browser.get("users?page=2")
        assert response.status == 200
        users = response.json()["data"]
        assert len(users) > 0
