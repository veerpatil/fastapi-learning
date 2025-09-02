from typing import Any
from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

@app.get(f"/shipment/{id}")
def get_shipment(id: int)->dict[str, Any]:
    return {
        "id": id,
        "Content": "Wooden Table",
        "Status": "In transit",
        "Price": 1000,
        "Currency": "USD"
    }

@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
        return get_scalar_api_reference(
            openapi_url=app.openapi_url,
            title="Scalar API Docs",
        )