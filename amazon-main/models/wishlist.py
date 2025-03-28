from utils.db import db

class Wishlist(db.Model):
    __tablename__ = 'wishlist'  # This specifies the table name

    # Define the columns for the Wishlist table
    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    product_name = db.Column(db.String(100), nullable=False)  # Product name
    customer_name = db.Column(db.String(100), nullable=False)  # Customer's name
    price = db.Column(db.Float, nullable=False)  # Price of the item in wishlist

    def __repr__(self):
        return f"<Wishlist {self.product_name} for {self.customer_name}>"