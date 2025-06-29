class Calculator:
  def add(self, x: float, y: float) -> float:
    return x + y
  
  def subtract(self, x: float, y: float) -> float:
    return x - y
  
  def multiply(self, x: float, y: float) -> float:
    return x * y
  
  def divide(self, x: float, y: float) -> float:
    if not y:
      return ValueError("Cannot make division by 0.")
    return x / y