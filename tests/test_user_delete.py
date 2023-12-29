from playwright.sync_api import sync_playwright

BASE_URL = "https://reqres.in/api/"

def test_delete_user():
    with sync_playwright() as p:
        user_id = 2
        browser = p.request.new_context(base_url=BASE_URL)
        response = browser.delete(f"users/{user_id}")
        assert response.status == 204
