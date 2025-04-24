from app.interfaces import ProductParserProtocol
from app.utils import get_selector
from app.selectors import ShoesForManSelector
from meyigi_scripts import append_to_json
from urllib.parse import urljoin
from config import BASE_URL, OUTPUT_FOLDER

class ParserShoesForMen(ProductParserProtocol):
    """Parser for extracting all informations about shoes for men"""
    def extract_products_info(self, page):
        products = []
        selector = get_selector(ShoesForManSelector, "MAIN_PAGE_PRODUCTS")
        hrefs = [
            href for link in page.query_selector_all(selector)
            if (href := link.get_attribute("href"))
        ]
                
        product_page_urls = [urljoin(BASE_URL, href) for href in hrefs]
        print(product_page_urls)

        for product_url in product_page_urls:
            page.goto(product_url)
            item = self.extract_product_detail(page)
            append_to_json(item, OUTPUT_FOLDER["mens-shoes"])
            products.append(item)

        return products
    
    def extract_product_detail(self, page):
        return super().extract_product_detail(page)
    