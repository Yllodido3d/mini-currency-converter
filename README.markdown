# Currency Converter Mini-Project

## Overview
This is a simple Python script that fetches real-time exchange rates from the ExchangeRate-API and converts amounts between currencies. It includes a basic interactive menu and saves conversion history to a CSV file for tracking. The project is designed for learning purposes and can be extended with additional features.

## Features
- Fetch exchange rates for any supported currency pair.
- Convert amounts with two decimal precision.
- Save conversion history to `conversion_history.csv`.
- User-friendly command-line interface.

## Requirements
- Python 3.x
- `requests` library (install with `pip install requests`)
- `pandas` library (install with `pip install pandas`)

## Installation
1. Clone or download this repository.
   ```bash
   git clone https://github.com/Yllodido3d/mini-currency-converter.git
2. Install the required libraries by running:
   ```bash
   pip install requests pandas
   ```
3. Run the script with:
   ```bash
   python conversormoedaENG.py
   ```

## Usage
- Enter the base currency (e.g., `BRL`).
- Enter the target currency (e.g., `USD`).
- Input the amount to convert.
- View the result and decide if you want to convert another amount.
- Check `conversion_history.csv` for past conversions.

## Code and Comments
The code and comments have been translated into English by an AI (Grok, created by xAI) to enhance readability and accessibility for a broader audience. Original logic and structure remain intact, with translations aimed at making the script easier to understand for non-Portuguese speakers.

## License
This project is open-source and available under the MIT License. Feel free to modify and distribute it as needed.

## Acknowledgments
- ExchangeRate-API for providing free exchange rate data.
- xAI's Grok for assisting with code translation and documentation.
