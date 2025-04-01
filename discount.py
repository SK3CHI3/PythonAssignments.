def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if it's 20% or higher.
    :param price: Original price of the item.
    :param discount_percent: Discount percentage.
    :return: Final price after discount or original price if discount is below 20%.
    """
    if discount_percent >= 20:
        return price - (price * (discount_percent / 100))
    return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percentage)

# Display result
print(f"Final price after discount: ${final_price:.2f}")
