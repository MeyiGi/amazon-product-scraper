from typing import Protocol
from abc import abstractmethod
from playwright.sync_api import Page


class ProductParserProtocol(Protocol):
    @abstractmethod
    def extract_products_info(self, page: Page) -> list[dict]:
        """Extract all informations about products"""
        pass

    @abstractmethod
    def extract_product_detail(self, page: Page) -> dict:
        """Extract all fields from detail page about product"""
        pass