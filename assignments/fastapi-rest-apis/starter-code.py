from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Products API")


class Product(BaseModel):
    id: int
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    in_stock: bool


products: list[Product] = []


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/products", response_model=list[Product])
def list_products():
    return products


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", response_model=Product, status_code=201)
def create_product(product: Product):
    for existing in products:
        if existing.id == product.id:
            raise HTTPException(status_code=400, detail="Product with this ID already exists")

    products.append(product)
    return product


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    for idx, product in enumerate(products):
        if product.id == product_id:
            products[idx] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for idx, product in enumerate(products):
        if product.id == product_id:
            del products[idx]
            return {"message": "Product removed"}
    raise HTTPException(status_code=404, detail="Product not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
