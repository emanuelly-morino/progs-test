from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Numeric,
    CheckConstraint
)
from sqlalchemy.orm import declarative_base, Session

# Base class for model definitions
Base = declarative_base()

# Define the Products model
class Product(Base):
    __tablename__ = "Products"

    ProductID = Column(Integer, primary_key=True)
    ProductName = Column(String(255), nullable=False)
    Price = Column(Numeric(10, 2), nullable=False)

    # CHECK constraint (Price > 0)
    __table_args__ = (
        CheckConstraint("Price > 0", name="check_price_positive"),
    )

    def __repr__(self):
        return f"<Product(id={self.ProductID}, name='{self.ProductName}', price={self.Price})>"

# --- Database setup ---
engine = create_engine("sqlite:///products.db", echo=True)
Base.metadata.create_all(engine)

# --- Example usage ---
with Session(engine) as session:
    product1 = Product(ProductID=1, ProductName="Laptop", Price=999.99)
    session.add(product1)
    session.commit()

    # Query the table
    for p in session.query(Product).all():
        print(p)

