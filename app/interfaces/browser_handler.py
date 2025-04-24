from typing import Protocol
from playwright.sync_api import Page, Browser
from abc import abstractmethod

class BrowserHandlerProtocol(Protocol):
    """Protocol for handling browser setup, defines methods."""
    @abstractmethod
    def start_browser(self) -> tuple[Page, Browser]:
        """Start the browser and returns the page and browser objects"""
        pass
    
    def close_browser(self) -> None:
        """Закрытие браузера после завершения работы."""
        if self.browser:
            self.browser.close()