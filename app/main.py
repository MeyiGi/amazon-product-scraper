from playwright.sync_api import sync_playwright, Page, Browser
from playwright_stealth import stealth_sync
from typing import Iterable
from utils.randomizer import random_delay, random_proxy
from config import MIN_DELAY, MAX_DELAY

def start_playwright(proxies: Iterable[str] = None) -> tuple[Page, Browser]:
    with sync_playwright() as p:
        proxy = random_proxy(proxies)

        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            proxy={"server" : proxy} if proxy else None 
        )
        page = context.new_page()
        stealth_sync(page)

        random_delay(MIN_DELAY, MAX_DELAY)

        return page, browser