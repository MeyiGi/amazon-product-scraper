from enum import Enum

class ShoesForManSelector(Enum):
    MAIN_PAGE_PRODUCTS = 'div[data-cy="title-recipe"] > a'
    TITLE = "#productTitle"
    PRICE = "#corePriceDisplay_desktop_feature_div .aok-offscreen"
    STARS = "#acrPopover .a-size-base.a-color-base"
    RATING_COUNT = "#acrCustomerReviewText"
    DETAILS = "#productFactsDesktopExpander .a-nostyle li" # multiple