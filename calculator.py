"""A simple command-line calculator."""


def calculate(first: float, operator: str, second: float) -> float:
	"""Return the result of applying operator to the two numbers."""
	if operator == "+":
		return first + second
	if operator == "-":
		return first - second
	if operator == "*":
		return first * second
	if operator == "/":
		if second == 0:
			raise ValueError("Cannot divide by zero.")
		return first / second
	if operator == "**":
		return first**second
	raise ValueError("Choose one of: +, -, *, /, **.")


def main() -> None:
	print("Calculator: enter expressions like 12 * 3 (or q to quit).")
	while True:
		expression = input("> ").strip()
		if expression.lower() in {"q", "quit", "exit"}:
			return

		parts = expression.split()
		if len(parts) != 3:
			print("Please enter two numbers and an operator, separated by spaces.")
			continue

		try:
			result = calculate(float(parts[0]), parts[1], float(parts[2]))
		except ValueError as error:
			print(f"Error: {error}")
		else:
			print(result)


if __name__ == "__main__":
	main()
