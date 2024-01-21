def index(data, index):
  """
  Retrieves an element from a data structure based on an index.

  Args:
    data: The data structure (list, tuple, etc.) to access.
    index: The index of the element to retrieve.

  Returns:
    The element at the specified index.

  Raises:
    IndexError: If the provided index is out of range.
  """

  try:
    result = data[index]  # Access the element using square brackets
    print(f"Result: {result}")
  except IndexError:
    print("Error: Index out of range.")

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]

# Get index from user (ensure it's an integer)
index = int(input("Input the index: "))

# Call the function
index(nums, index)
