# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Ask the user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Get the final price
final_price = calculate_discount(price, discount_percent)

# Display the result
print("The final price is:", final_price)
