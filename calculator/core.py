class Calculator:
  def add(self, x: int, y: int) -> int:
    return x + y
  
  def subtract(self, x: int, y: int) -> int:
    return x - y
  
  def multiply(self, x: int, y: int) -> int:
    return x * y
  
  def devide(self, x: int, y: int) -> int:
    if not y:
      return ValueError("Cannot make division by 0.")
    return x / y