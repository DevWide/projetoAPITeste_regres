from playwright.sync_api import sync_playwright

BASE_URL = "https://reqres.in/api/"

def test_get_user_details():
    with sync_playwright() as p:
        user_id = 2
        browser = p.request.new_context(base_url=BASE_URL)
        response = browser.get(f"users/{user_id}")
        assert response.status == 200
        user_details = response.json()["data"]
        assert user_details["id"] == user_id
