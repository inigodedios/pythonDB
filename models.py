from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy to handle database operations
db = SQLAlchemy()

class User(db.Model):
    """
    User model representing the USERS table in the database.
    - USERID: Primary key, unique identifier for the user.
    - USERNAME: User's username, must be unique and is used for login.
    - PASSWORD: User's password, stored securely and used for authentication.
    Stocks relationship: Establishes a one-to-many relationship with the UserStock model,
    indicating that a single user can own multiple stocks.
    """
    __tablename__ = 'USERS'
    USERID = db.Column(db.Integer, primary_key=True)
    USERNAME = db.Column(db.String(255), nullable=False)
    PASSWORD = db.Column(db.String(255), nullable=False)
    stocks = db.relationship('UserStock', backref='user', lazy=True)

class UserStock(db.Model):
    """
    UserStock model representing the USER_STOCKS table in the database.
    Maps the association between a user and their stock holdings.
    - USERID: Foreign key linked to the User model's USERID.
    - STOCKSYMBOL: The stock symbol, part of the primary key to uniquely identify stock entries.
    - QUANTITY: The number of shares the user owns of the given stock.
    """
    __tablename__ = 'USER_STOCKS'
    USERID = db.Column(db.Integer, db.ForeignKey('USERS.USERID'), primary_key=True)
    STOCKSYMBOL = db.Column(db.String(255), primary_key=True)
    QUANTITY = db.Column(db.Integer, nullable=False)

def add_stock(user_id, stock_symbol, quantity):
    """
    Adds stock to a user's portfolio or updates the quantity if the stock already exists.
    - user_id: The ID of the user to whom the stock will be added.
    - stock_symbol: The symbol of the stock to add.
    - quantity: The number of shares to add.
    """
    user_stock = UserStock.query.filter_by(user_id=user_id, stock_symbol=stock_symbol).first()
    if user_stock:
        # Stock already exists, so we update the quantity.
        user_stock.quantity += quantity
    else:
        # Stock does not exist, so we add a new record.
        user_stock = UserStock(user_id=user_id, stock_symbol=stock_symbol, quantity=quantity)
        db.session.add(user_stock)
    db.session.commit()

def update_stock(user_id, stock_symbol, quantity):
    """
    Updates the quantity of a specific stock for a user.
    - user_id: The ID of the user whose stock will be updated.
    - stock_symbol: The symbol of the stock to update.
    - quantity: The new quantity of the stock.
    """
    user_stock = UserStock.query.filter_by(user_id=user_id, stock_symbol=stock_symbol).first()
    if user_stock:
        user_stock.quantity = quantity
        db.session.commit()
    else:
        print("Stock does not exist for the user.")

def remove_stock(user_id, stock_symbol):
    """
    Removes a stock from a user's portfolio.
    - user_id: The ID of the user from whom the stock will be removed.
    - stock_symbol: The symbol of the stock to remove.
    """
    UserStock.query.filter_by(user_id=user_id, stock_symbol=stock_symbol).delete()
    db.session.commit()
