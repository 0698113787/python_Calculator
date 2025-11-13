# Calculator Web Application

A modern responsive calculator web application built with **Flask** and deployed on **Vercel**. Features smooth AJAX interactions and dark/light mode toggle.

## Features

- Basic arithmetic operations (`+`, `-`, `×`, `÷`)
- Advanced functions (square `x²`, square root `√`, percentage `%`, parentheses)
- Dark/Light mode with **Font Awesome** icons
- AJAX-powered (no page reloads)
- Fully responsive design

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (AJAX)
- **Icons**: Font Awesome 6.4.0
- **Deployment**: Vercel (Serverless)

## Project Structure

```
calculator/
├── app.py                 # Flask backend application
├── vercel.json           # Vercel deployment configuration
├── requirements.txt      # Python dependencies
├── templates/
│   └── calculator.html   # Frontend with AJAX functionality
└── static/
    └── calculator.css    # Stylesheet with light/dark mode
```

## Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Local Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/calculator.git
cd calculator
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the application**

```bash
python -m flask run / python app.py
```

4. **Open your browser**

Navigate to `http://localhost:5000`

## Deployment

### Deploy to Vercel


### `vercel.json`


### `requirements.txt`

```
Flask==3.0.0
```

## Usage

- **Numbers**: Click `0-9` to input numbers
- **Operations**: Click `+`, `-`, `×`, `÷` for basic operations
- **Calculate**: Click `=` to get result
- **Clear**: Click `AC` to clear all
- **Delete**: Click `⌫` to delete last character
- **Square**: Click `x²` to square current number
- **Square Root**: Click `√` to get square root
- **Percentage**: Click `%` for percentage calculations
- **Sign Toggle**: Click `+/−` to change sign
- **Parentheses**: Use `(` and `)` for complex expressions
- **Mode Toggle**: Click mode button to switch between light/dark themes



## Author

**Andile Ntshangase**
## EMAIL
**vuyiswaandile176@gmail.com**

---

**Live Demo**: https://python-calculator-tau.vercel.app/

**Thank You For Viewing my Repo** ⭐ 
