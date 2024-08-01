def factorial(n):
  """
  This function calculates the factorial of a non-negative integer.

  Args:
      n: The non-negative integer for which to calculate the factorial.

  Returns:
      The factorial of n (long integer).
  """
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

def calculate_x(n, r):
  """
  This function calculates the value of X(n, r) based on the formula.

  Args:
      n: The first integer (non-negative).
      r: The second integer (non-negative and less than or equal to n).

  Returns:
      The value of X(n, r).
  """
  if n < 0 or r < 0:
    raise ValueError("n and r must be non-negative integers")
  elif r > n:
    raise ValueError("r must be less than or equal to n")

  n_factorial = factorial(n)
  r_factorial = factorial(r)
  nr_factorial = factorial(n - r)

  result = n_factorial * r_factorial * nr_factorial / (n**0.5 * r**0.5)
  return result

def main():
  """
  This function takes user input for n and r, validates them, calls the calculate_x function, and displays the result.
  """
  while True:
    try:
      n = int(input("Enter a non-negative integer for n: "))
      r = int(input("Enter a non-negative integer for r (less than or equal to n): "))
      if n < 0 or r < 0:
        raise ValueError("n and r must be non-negative integers")
      elif r > n:
        raise ValueError("r must be less than or equal to n")
      break
    except ValueError as e:
      print(f"Invalid input: {e}")

  # Calculate and display X(n, r)
  result = calculate_x(n, r)
  print(f"X({n}, {r}) = {result:.2f}")

if __name__ == "__main__":
  main()
