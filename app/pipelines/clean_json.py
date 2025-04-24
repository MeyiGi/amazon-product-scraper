import re
import json
from config import OUTPUT_FOLDER
from meyigi_scripts import append_to_json, clean_string

class ProductDataCleaner:
    def __init__(self):
        pass
    
    def clean_data(self, raw_data):
        cleaned_products = []
        for product in raw_data:
            cleaned_product = {
                "title": self.clean_title(product["title"]),
                "price": self.clean_price(product["price"]),
                "stars": self.clean_stars(product["stars"]),
                "rating_count": self.clean_rating_count(product["rating_count"]),
                "details": self.clean_details(product["details"]),
            }
            cleaned_products.append(cleaned_product)
        return cleaned_products
    
    def clean_title(self, title):
        """
        Очистка названия продукта от лишних пробелов.
        """
        return title.strip()

    def clean_price(self, price):
        # Если цена уже является числом (float), возвращаем его без изменений
        if isinstance(price, float):
            return price
        # В противном случае обрабатываем строковое значение
        return float(price.replace("$", "").strip())

    def clean_stars(self, stars):
        # Преобразуем в строку, если stars является числом (float)
        if isinstance(stars, float):
            stars = str(stars)
        
        match = re.search(r"(\d+(\.\d+)?)", stars)
        if match:
            return float(match.group(1))
        return None  # или другое значение по умолчанию, если звезды не найдены

    def clean_rating_count(self, rating_count):
        # Преобразуем в строку, если rating_count является числом (int)
        if isinstance(rating_count, int):
            rating_count = str(rating_count)
        
        match = re.search(r"(\d{1,3}(?:,\d{3})*)", rating_count)
        if match:
            return int(match.group(1).replace(",", ""))  # Убираем запятые, если они есть
        return None  # или другое значение по умолчанию, если рейтинг не найден

    def clean_details(self, details):
        """
        Очистка деталей продукта. Удаление всех пробелов и символов новой строки.
        """
        cleaned_details = []
        for detail in details:
            # Убираем все символы новой строки и пробелы
            cleaned_detail = re.sub(r'\s+', ' ', detail).strip()
            cleaned_details.append(cleaned_detail)
        
        return cleaned_details
        

if __name__ == "__main__":
    folder = OUTPUT_FOLDER["mens-shoes"]
    with open(folder, "r") as file:
        raw_data = json.load(file)

    cleaner = ProductDataCleaner()
    cleaned_data = cleaner.clean_data(raw_data)
    append_to_json(cleaned_data, OUTPUT_FOLDER["cleaned-mens-shoes"])