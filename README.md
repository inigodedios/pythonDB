# Stock Portfolio Management App

This Flask-based application allows users to register, login, and manage their stock portfolios by adding, updating, or removing stocks. It utilizes an Oracle database to store user information and stock portfolios. The application also integrates with the Alpha Vantage API to fetch current stock prices.

## Features

- User authentication (register, login, logout)
- Portfolio management (add, update, remove stocks)
- Fetching current stock prices from Alpha Vantage API

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/inigodedios/pythonDB
    cd pythonDB
    ```

2. **Install Dependencies**

    Ensure you have `pip` installed and then run:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the application, execute:

```bash
python3 main.py
```
## Usage

- **Register**: Send a POST request to `/register` with a JSON body containing `username` and `password`.
- **Login**: Send a POST request to `/login` with a JSON body containing `username` and `password`.
- **Logout**: Access `/logout` via GET request.
- **Add Stock**: After logging in, use the `/modifyPortfolio/` endpoint with `operation` set to `ADD`.
- **Remove Stock**: Use the `/modifyPortfolio/` endpoint with `operation` set to `REMOVE`.
- **Update Portfolio**: Send appropriate requests to `/modifyPortfolio/` to update stock quantities.
- **View Portfolio**: Access `/overview` via GET request to see the current portfolio.

## Contributing

Feel free to fork the repository and submit pull requests.
