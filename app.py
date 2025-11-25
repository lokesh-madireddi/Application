import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from sqlalchemy.orm import declarative_base


# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/products_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Product model
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

# Create database tables
Base.metadata.create_all(bind=engine)

# FastAPI app instance
app = FastAPI() 

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for product input
class ProductCreate(BaseModel):
    name: str
    description: str

# API to list products
@app.get("/products/")
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

# API to create a product
@app.post("/products/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(name=product.name, description=product.description)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# Fixture for sample products
def init_db():
    db = SessionLocal()
    sample_products = [
        Product(name="Laptop", description="A powerful laptop"),
        Product(name="Smartphone", description="Latest model smartphone"),
        Product(name="Tablet", description="Portable and efficient tablet")
    ]
    db.add_all(sample_products)
    db.commit()
    db.close()

if __name__ == "__main__":
    init_db()
