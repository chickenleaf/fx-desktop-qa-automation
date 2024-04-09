import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from modules.browser_object import Navigation

sites = ["Google", "Amazon", "Bing", "DuckDuckGo", "eBay"]


@pytest.mark.parametrize("site", sites)
def test_search_modes_for_sites(driver: Firefox, site: str):
    # C2234690
    # C1365213 (potentially)
    nav = Navigation(driver).open()
    (
        nav.search("soccer", mode=site)
        .expect_in_content(EC.url_contains(site.lower()))
        .clear_awesome_bar()
    )
