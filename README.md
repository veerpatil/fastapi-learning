# FastAPI Backend Project

A simple FastAPI backend service for managing shipment data.

## Features

- RESTful API endpoint for shipment information
- Interactive API documentation with Scalar
- Fast and modern Python web framework

## API Endpoints

### GET /shipment
Returns shipment information including content and status.

**Response:**
```json
{
    "Content": "wooden tabel",
    "Status": "In transit"
}
```

### GET /scalar
Interactive API documentation interface.

## Setup and Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/veerpatil/fastapi-learning.git
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # On macOS/Linux
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install fastapi scalar-fastapi
   ```

## Running the Application

Start the development server:
```bash
fastapi dev 
```

The API will be available at:
- **Main API**: http://localhost:8000
- **Shipment endpoint**: http://localhost:8000/shipment
- **API Documentation**: http://localhost:8000/scalar

## Development

The main application code is located in `app/main.py`. The project uses:
- **FastAPI** for the web framework
- **Uvicorn** as the ASGI server
- **Scalar** for API documentation

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   └── main.py
├── venv/
├── .gitignore
└── README.md
```
