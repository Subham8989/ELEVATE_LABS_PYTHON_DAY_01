# 🧮 Calculator CLI App

A clean and interactive command-line calculator supporting basic arithmetic operations.

## ✅ Features

- Addition, Subtraction, Multiplication, Division
- Input validation
- Looping until user exits
- Graceful error handling (e.g., divide-by-zero)

## 📦 Project Structure

- `classes/` – Core logic with a `Calculator` class
- `calculator.py` – Entry point of CLI
- `pyproject.toml` – For dependency management with `uv`

## 🚀 Usage

Run in terminal:

```bash
# 1. Create a virtual environment using uv
uv venv

# 2. Activate the virtual environment
source .venv/bin/activate   # On Linux/macOS
# OR
.venv\Scripts\activate      # On Windows

# 3. Run the calculator
python calculator.py
```
