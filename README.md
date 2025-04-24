Here's a simple template for your GitHub README based on the project structure you've provided:

```markdown
# Amazon Product Scraper

A Python-based scraper for Amazon products, designed to scrape, clean, and store product data efficiently.

## Project Structure

```
.
├── app                      # Main application files
│   ├── browser_handler.py   # Handles browser automation
│   ├── interfaces           # Contains interfaces for handling product data
│   ├── main.py              # Main entry point for running the scraper
│   ├── parsers              # Parsing logic for different product categories
│   ├── pipelines            # Data cleaning and transformation
│   ├── selectors            # Defines selectors for scraping specific product data
│   └── utils                # Utility functions and helpers
├── config                   # Configuration files
│   ├── settings.py          # Configuration settings
├── data                     # Data storage for raw and cleaned data
├── main.py                  # Main script to run the application
├── pyproject.toml           # Python project configuration
├── README.md                # Project documentation
└── uv.lock                  # Dependencies lock file
```

## Features

- **Amazon Product Scraping**: Scrape product details like price, description, and availability.
- **Product Data Cleaning**: Clean and format the scraped data into a structured format.
- **Data Storage**: Store raw and cleaned data in JSON files.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/amazon_product_scraper.git
   cd amazon_product_scraper
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install the project dependencies:

   ```bash
   pip install -e .
   ```

## Configuration

You can customize your scraping settings in the `config/settings.py` file. Modify the settings as per your requirements.

## Usage

To start scraping Amazon products, run the following command:

```bash
python app/main.py
```

The scraper will begin running and store the results in the `data` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. Ensure that you follow the project's coding conventions and write tests for any new functionality.

## Acknowledgments

- Thanks to the open-source community for their contributions.
```

You can adjust the details and any additional instructions specific to your project as needed!