from typing import Any
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

shipments ={
    121:{
        "id": 121,
        "Content": "Wooden Table",
        "Status": "In transit",
        "Price": 1000,
        "Currency": "USD"
    },
    122: {
        "id": 122,
        "Content": "Leather Sofa",
        "Status": "Delivered",
        "Price": 2500,
        "Currency": "USD"
    },
    123: {
        "id": 123,
        "Content": "Gaming Laptop",
        "Status": "Processing",
        "Price": 1800,
        "Currency": "EUR"
    },
    124: {
        "id": 124,
        "Content": "Coffee Machine",
        "Status": "Shipped",
        "Price": 450,
        "Currency": "GBP"
    },
    125: {
        "id": 125,
        "Content": "Yoga Mat Set",
        "Status": "In transit",
        "Price": 89,
        "Currency": "USD"
    },
    126: {
        "id": 126,
        "Content": "Smartphone",
        "Status": "Cancelled",
        "Price": 999,
        "Currency": "CAD"
    },
    127: {
        "id": 127,
        "Content": "Kitchen Knife Set",
        "Status": "Delivered",
        "Price": 320,
        "Currency": "AUD"
    },
    128: {
        "id": 128,
        "Content": "Wireless Headphones",
        "Status": "Out for delivery",
        "Price": 250,
        "Currency": "USD"
    },
    129: {
        "id": 129,
        "Content": "Electric Bicycle",
        "Status": "Processing",
        "Price": 1200,
        "Currency": "EUR"
    },
    130: {
        "id": 130,
        "Content": "Art Canvas Set",
        "Status": "Shipped",
        "Price": 75,
        "Currency": "USD"
    },
    131: {
        "id": 131,
        "Content": "Standing Desk",
        "Status": "In transit",
        "Price": 650,
        "Currency": "JPY"
    },
}
@app.get("/shipment/latest")
def get_latest_shipment()->dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]



@app.get("/shipment/{id}")
def get_shipment(id: int)->dict[str, Any]:
    if id not in shipments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shipment not found")
    return shipments[id]

@app.get("/shipments")
def get_shipmentbyqueryparam(id: int | None = None)->dict[str, Any]:
    if not id:
        id = max(shipments.keys())
        return shipments[id]
    if id not in shipments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shipment not found")
    return shipments[id]

@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
        return get_scalar_api_reference(
            openapi_url=app.openapi_url,
            title="Scalar API Docs",
        )