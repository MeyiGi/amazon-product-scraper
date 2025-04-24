from playwright.sync_api import sync_playwright, Page, Browser
from typing import Iterable
from app.interfaces.browser_handler import BrowserHandlerProtocol
from app.utils.randomizer import random_delay, random_proxy
from config import MIN_DELAY, MAX_DELAY, SCRAPE_URLS


class BrowserHandlerForMenShoes(BrowserHandlerProtocol):
    """ https://www.amazon.com/s?i=fashion-mens-shoes&s=popularity-rank """
    def __init__(self, proxies: Iterable[str] = None) -> None:
        self.proxies = proxies
        self.playwright = sync_playwright().start()
        self.browser = None
        self.context = None
        self.page = None

    def _setup_browser(self) -> None:
        proxy = random_proxy(self.proxies)
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context(
            proxy={"server": proxy} if proxy else None
        )
        self.page = self.context.new_page()

    def start_browser(self) -> tuple[Page, Browser]:
        self._setup_browser()
        random_delay(MIN_DELAY, MAX_DELAY)
        self.page.goto(
            SCRAPE_URLS["mens-shoes"]
        )
        return self.page, self.browser