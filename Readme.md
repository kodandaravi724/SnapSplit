# SnapSplit

SnapSplit is a Python application that integrates OCR (using Tesseract) and the Splitwise API to simplify expense splitting. The tool allows users to upload an image of a receipt, automatically extracts items and their costs, and then assists in assigning and logging each item as an expense in a Splitwise group. Additionally, SnapSplit can generate monthly expense reports to keep track of spending.

## Features

- **Receipt Scanning**: Upload a picture of a receipt and use OCR (via pytesseract) to extract item names and costs.
- **Expense Splitting**: Assign each extracted item to group members using the Splitwise API.
- **Monthly Reporting**: Generate basic reports summarizing monthly expenses.
- **Modular Design**: Separate modules for OCR processing and Splitwise API interaction make the project easy to extend and maintain.

## Getting Started

### Prerequisites

- **Python 3.6+**
- **Tesseract OCR**:  
  - [Installation Instructions](https://github.com/tesseract-ocr/tesseract)
- **Splitwise Developer Account**:  
  - Obtain your Consumer Key and Consumer Secret from [Splitwise Dev](https://dev.splitwise.com/)
- **Pip** (Python package installer)
