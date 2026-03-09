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
    Subtracts the second number from the first number.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result of a - b
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
    Divides the first number by the second number.
    
    Parameters:
    - a: Numerator
    - b: Denominator
    
    Returns:
    - JSON object with the result of a / b

    Raises:
    - HTTPException (400): If the denominator 'b' is zero.
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

@app.get("/quad/{a}/{b}/{c}", status_code=status.HTTP_200_OK)
def quad(a: float, b: float, c: float):
    """
    Calculates the real roots of a quadratic equation (ax^2 + bx + c = 0).

    Parameters:
    - a: Coefficient of x^2
    - b: Coefficient of x
    - c: Constant term

    Returns:
    - JSON object with the real roots, 'root1' and 'root2'.

    Raises:
    - HTTPException (400): If 'a' is zero.
    - HTTPException (400): If the discriminant is negative (no real roots).
    """
    if a == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Coefficient 'a' cannot be zero for a quadratic equation."
        )

    discriminant = (b**2) - (4*a*c)

    if discriminant < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Discriminant is negative, roots are not real."
        )
    
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    return {"root1": root1, "root2": root2}

@app.get("/compound/{p}/{r}/{n}/{t}", status_code=status.HTTP_200_OK)
def compound(p: float, r: float, n: int, t: float):
    """
    Calculates compound interest. A = P(1 + r/n)^(nt)
    
    Parameters:
    - p: Principal amount
    - r: Annual interest rate (as a decimal, e.g., 0.05 for 5%)
    - n: Number of times interest is compounded per year
    - t: Number of years

    Returns:
    - JSON object with the final amount after interest.
    """
    amount = p * (1 + r / n)**(n * t)
    return {"result": amount}
