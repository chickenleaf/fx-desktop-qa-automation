import pytest
from selenium.webdriver import Firefox

from modules.page_object_about_pages import AboutLogins
from modules.page_object_autofill import LoginAutofill


@pytest.fixture()
def test_case():
    return "2241089"


@pytest.fixture()
def set_prefs():
    """Set prefs"""
    return [("signon.rememberSignons", True), ("signon.autofillForms", True)]


def test_saved_hyperlink_redirects_to_corresponding_page(driver: Firefox):
    """
    C2241089 - Verify that a saved hyperlink redirects to the corresponding page
    """
    about_logins = AboutLogins(driver).open()
    login_autofill = LoginAutofill(driver)

    # Add a new login
    about_logins.click_add_login_button()
    about_logins.create_new_login(
        {
            "origin": "https://mozilla.github.io/",
            "username": "username",
            "password": "password",
        }
    )

    # Click on the hyperlink website
    about_logins.get_element("website-address").click()
    about_logins.switch_to_new_tab()
    about_logins.url_contains("mozilla.github")

    # Verify that the saved login is recognized
    login_autofill.open()

    # Verify the username field has the saved value
    username_element = login_autofill.get_element("username-login-field")
    assert username_element.get_attribute("value") == "username"

    # Verify the password field is filled with a value that match the length of the saved password
    password_element = login_autofill.get_element("password-login-field")
    masked_password_value = password_element.get_attribute("value")
    assert len(masked_password_value) == 8
