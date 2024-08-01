import math

def find_angle(opposite, adjacent):
  """
  This function calculates the angle (in degrees) in a right triangle
  given the lengths of the opposite and adjacent sides.

  Args:
      opposite: The length of the opposite side (unsigned integer).
      adjacent: The length of the adjacent side (unsigned integer).

  Returns:
      The angle in degrees (float).
  """
  # Ensure positive values for sides
  opposite = abs(opposite)
  adjacent = abs(adjacent)

  # Calculate the tangent
  tangent = opposite / adjacent

  # Use arctangent function to find the angle in radians
  angle_radians = math.atan(tangent)

  # Convert radians to degrees
  angle_degrees = math.degrees(angle_radians)

  return angle_degrees

def main():
  """
  This function takes user input for the opposite and adjacent sides,
  calls the find_angle function, and displays the angle in degrees and radians.
  """
  while True:
    try:
      opposite = int(input("Enter the length of the opposite side (positive integer): "))
      adjacent = int(input("Enter the length of the adjacent side (positive integer): "))
      if opposite <= 0 or adjacent <= 0:
        raise ValueError("Sides must be positive integers")
      break
    except ValueError:
      print("Invalid input. Please enter positive integers for the sides.")

  # Find the angle
  angle = find_angle(opposite, adjacent)

    # Calculate the angle in radians based on the returned degrees
  angle_radians = math.radians(angle)

  # Convert pi to a constant
  pi = math.pi

  # Display the angle in degrees and radians
  print(f"The angle is: {angle:.2f} degrees")





  
  print(f"The angle in radians is: {angle_radians:.2f} (pi = {pi:.4f})")

if __name__ == "__main__":
  main()
