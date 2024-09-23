from selenium.webdriver import Firefox

from modules.browser_object import PanelUi, TabBar


def test_about_login_navigation_from_password_hamburger_menu(driver: Firefox):
    """
    C2241082 - Verify that clicking the Password option in Hamburger Menu opens about:login page in a new tab
    """

    panel_ui = PanelUi(driver)
    tabs = TabBar(driver)

    panel_ui.open_panel_menu()
    panel_ui.redirect_to_about_logins_page()
    tabs.wait_for_num_tabs(2)
    tabs.title_contains("Passwords")
