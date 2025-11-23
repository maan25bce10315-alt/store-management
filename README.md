# store-management
📦 Store Management System (Python + CSV/Excel)
A lightweight console application built with Python for efficiently managing a retail store's inventory, products, and sales records. Data is persisted in CSV format for easy viewing, editing, and analysis using Microsoft Excel or any spreadsheet software.
## 📖 Table of Contents
 - Overview
 - Key Features
 - Tech Stack
 - Installation
 - Usage
 - Project Structure
 - License
# Overview
This Store Management System is designed for small business owners and managers who need a simple, portable, and non-database solution for tracking their stock. All inventory and transaction data are stored in human-readable CSV files.
Target Audience: Store Managers, Retail Clerks, and Inventory Controllers.
  - Key Features
# Python Core Logic
 - Product Management: Add new products (Name, SKU, Price, Stock Quantity).
 - Inventory Update: Modify existing product details and stock levels.
 - Sales Logging: Record transactions by product SKU and quantity sold, automatically updating stock.
 - Search Functionality: Quickly find products by SKU or name.
 - Reporting: View low-stock alerts and total sales history.
# Excel & CSV Integration
 - Auto-Save: All changes are automatically saved to the respective .csv files.
 - Excel Compatible: Data is formatted for direct readability by Microsoft Excel.
 - Data Segregation: Separate files for Products (inventory.csv) and Transactions (sales.csv).
#  Tech Stack
Language:
 - Python 3.x
# Libraries & Modules:
 - csv (Standard library for handling data persistence)
 - os (For file path handling)
Data Storage:
 - .csv (Comma Separated Values)
--  Installation
Prerequisites
 - Python 3.x installed on your machine.
Steps
 - Clone the repository
   git clone [https://github.com/maan25bce10315-alt/store-management](https://github.com/maan25bce10315-alt/store-management)
cd store-management

 - Run the Application Execute the main Python script:
   python src/main.py

# Usage
 - Run the Application: Execute the main Python script using the command above.
 - Interact with the Menu: Follow the on-screen prompts in your terminal/command prompt to Add, Update, Remove, or Process Sales.
 - View Data in Excel: The data is saved in the data/ folder as inventory.csv and sales.csv. You can open these files directly in Excel for analysis.
--  Project Structure
store-management-system/
├── src/
│   ├── main.py             # Main entry point and menu handler


│   ├── product_manager.py  # Product class, inventory logic, and sales processing


│   └── file_handler.py     # CSV reading/writing functions


├── data/
│   ├── inventory.csv       # Persistent data file for products and stock


│   └── sales.csv           # Persistent data file for recorded transactions


├── requirements.txt      # Python dependencies (minimal, mainly 'csv')


└── README.md

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
