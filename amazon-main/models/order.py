from utils.db import db

class Order(db.Model):
    __tablename__ = 'orders'  # This specifies the table name

    # Define the columns for the Order table
    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    product_name = db.Column(db.String(100), nullable=False)  # Product name
    quantity = db.Column(db.Integer, nullable=False)  # Quantity of products
    price_per_unit = db.Column(db.Float, nullable=False)  # Price per unit
    total_price = db.Column(db.Float, nullable=False)  # Total price (calculated field)
    customer_name = db.Column(db.String(100), nullable=False)  # Customer's name
    order_date = db.Column(db.String(100), nullable=False)  # Date of the order

    def __repr__(self):
        return f"<Order {self.product_name} by {self.customer_name}>"