from enum import Enum

class ShoesForManSelector(Enum):
    MAIN_PAGE_PRODUCTS = 'div[data-cy="title-recipe"] > a'
    TITLE = "#productTitle"
    PRICE = '.a-price span[aria-hidden="true"]'
    STARS = "i[data-hook=average-star-rating]"
    RATING_COUNT = "#acrCustomerReviewText"
    SPARE_RATING_COUNT = '*[data-hook="total-review-count"]'
    DETAILS = "#productFactsDesktopExpander .a-nostyle li" # multiple