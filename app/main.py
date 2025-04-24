from app.browser_handler import BrowserHandlerForMenShoes
from app.parsers.parser_man_shoes import ParserShoesForMen
from app.interfaces import BrowserHandlerProtocol

def main() -> None:
    browser_handler: BrowserHandlerProtocol = BrowserHandlerForMenShoes()
    page, browser = browser_handler.start_browser()
    
    shoes_parser = ParserShoesForMen()
    shoes_parser.extract_products_info(page=page)


    # ----------------------------
    browser_handler.close_browser



if __name__ == "__main__":
    main()