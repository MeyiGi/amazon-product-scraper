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

        for product_url in product_page_urls:
            print(product_url)
            page.goto(product_url)
            item = self.extract_product_detail(page)
            append_to_json(item, OUTPUT_FOLDER["mens-shoes"])
            products.append(item)

        return products
    
    def extract_product_detail(self, page):
        item = {}
        item["title"] = page.query_selector(get_selector(ShoesForManSelector, "TITLE")).text_content()
        item["price"] = page.query_selector(get_selector(ShoesForManSelector, "PRICE")).text_content()
        item["stars"] = page.query_selector(get_selector(ShoesForManSelector, "STARS")).text_content()
        rating_count = page.query_selector(get_selector(ShoesForManSelector, "RATING_COUNT"))
        if not rating_count:
            rating_count = page.query_selector(get_selector(ShoesForManSelector, "SPARE_RATING_COUNT"))
        item["rating_count"] = rating_count.text_content()
        item["details"] = [x.text_content() for x in page.query_selector_all(get_selector(ShoesForManSelector, "DETAILS"))]
        return item