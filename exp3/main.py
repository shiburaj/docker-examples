# # Simple interest calculator
import sys

def calculate_simple_interest(principal, rate, time):
  """Calculates the simple interest and total amount.

  Args:
    principal: The initial amount of money.
    rate: The annual interest rate (as a percentage).
    time: The time period in years.

  Returns:
    A tuple containing the simple interest and the total amount,
    or (None, None) if inputs are invalid.
  """
  if principal < 0 or rate < 0 or time < 0:
    print("Error: Principal, rate, and time cannot be negative.")
    return None, None
  
  interest = (principal * rate * time) / 100
  total_amount = principal + interest
  return interest, total_amount

def main():
  """Gets user input and displays the simple interest calculation."""
  print("Simple Interest Calculator")
  print("--------------------------")

  try:
    principal_amount = float(sys.argv[1])
    annual_rate = float(sys.argv[2])
    time_years = float(sys.argv[3])

    simple_interest, final_amount = calculate_simple_interest(principal_amount, annual_rate, time_years)

    if simple_interest is not None:
      print("\n--- Results ---")
      # Using f-strings for formatted output
      print(f"Principal Amount: Rs. {principal_amount:,.2f}")
      print(f"Annual Interest Rate: {annual_rate:.2f}%")
      print(f"Time Period: {time_years:.2f} years")
      print(f"Simple Interest Earned: Rs. {simple_interest:,.2f}")
      print(f"Total Amount after {time_years} years: Rs. {final_amount:,.2f}")

  except ValueError:
    print("\nError: Invalid input. Please enter numeric values for amount, rate, and time.")
  except Exception as e:
      print(f"\nAn unexpected error occurred: {e}")

# Run the main function when the script is executed
if __name__ == "__main__":
  main()

