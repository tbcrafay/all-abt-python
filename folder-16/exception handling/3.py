# def Interest(cost, month, rate):

#  if rate > 100:
#    raise ValueError(rate)
#    interest1 = (cost * month * rate) / 100
#    print('The Interest is', interest1)
#    return interest1
# print('Case 1')
# Interest(650, 2, 6)
# print('Case 2')
# Interest(880, 2, 900)


def Interest(cost, month, rate):
    """Calculates the interest for a given cost, month, and rate.

    Args:
        cost: The initial cost of the loan.
        month: The number of months for the loan.
        rate: The annual interest rate (as a percentage).

    Raises:
        ValueError: If the interest rate is greater than 100%.

    Returns:
        The calculated interest amount.
    """

    if rate > 100:
        raise ValueError("Interest rate cannot be greater than 100%.")  # Added a more informative error message

    interest = (cost * month * rate) / 100
    print(f"The Interest is: {interest:.2f}")  # Formatted interest with 2 decimal places
    return interest

print('Case 1')
Interest(650, 2, 6)
print('Case 2')
Interest(880, 2, 9)  # Corrected rate to 9%
print('case 3')
Interest(800,2,120)