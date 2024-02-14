def divide(a, b):
  assert b != 0, "Cannot divide by zero"
  return a / b

result1 = divide(10, 2)  # No error
# result2 = divide(10, 0)  # Raises assertion error with message

print(result1)
# print(result2)