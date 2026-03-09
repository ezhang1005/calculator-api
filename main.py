import math
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Handles validation errors for path parameters, returning a 422
    status code with a custom, human-readable error message.
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "All arguments must be valid numbers."},
    )

@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.get("/add/{a}/{b}", status_code=status.HTTP_200_OK)
def add(a: float, b: float):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    return {"result": a + b}


@app.get("/subtract/{a}/{b}", status_code=status.HTTP_200_OK)
def subtract(a: float, b: float):
    """
    Subtract two numbers from each other.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    return {"result": a - b}


@app.get("/multiply/{a}/{b}", status_code=status.HTTP_200_OK)
def multiply(a: float, b: float):
    """
    Multiply two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    return {"result": a * b}

@app.get("/divide/{a}/{b}", status_code=status.HTTP_200_OK)
def divide(a: float, b: float):
    """
    Divide two numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    if b == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Division by zero is not allowed.")
    return {"result": a / b}

@app.get("/hypotenuse/{a}/{b}", status_code=status.HTTP_200_OK)
def hypotenuse(a: float, b: float):
    """
    Calculates the hypotenuse of a right triangle given the other two sides.

    Parameters:
    - a: Length of the first side
    - b: Length of the second side

    Returns:
    - JSON object with the length of the hypotenuse
    """
    hypot = math.sqrt(a**2 + b**2)
    return {"result": hypot}