from calculator import Calculator

def get_number(prompt: str) -> float:
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Invalid Input. Please enter a valid number.")

def get_choice() -> int:
  print("\nChoose an operation: ")
  print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
  return int(input("Enter Choice (1 - 5): "))

def main() -> None:
  calc = Calculator()
  print("\nWelcome to Calculator CLI!")

  while True:
    try:
      choice = get_choice()
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 5.")
      continue
    if choice == 5:
      print("Exiting the CLI.")
      break

    if choice not in {1, 2, 3, 4}:
      print("Please enter a valid choice.")
      continue

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    match choice:
      case 1:
        result = calc.add(num1, num2)
        symbol = "+"
      case 2:
        result = calc.subtract(num1, num2)
        symbol = "-"
      case 3:
        result = calc.multiply(num1, num2)
        symbol = "*"
      case 4:
        result = calc.divide(num1, num2)
        symbol = "/"
    
    print(f"{num1} {symbol} {num2} = {result}") if isinstance(result, float) else print(f"{result}")

if __name__ == "__main__":
  main()