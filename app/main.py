from fastapi import FastAPI

from .routers import orders, payments, products, users

app = FastAPI(title="Ecommerce API")


@app.get("/")
def read_root():
    return {"message": "Ecommerce API is running"}


app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(payments.router)


