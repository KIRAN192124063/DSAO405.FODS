item_prices = [10, 20, 15]       
item_quantities = [2, 1, 3]       
discount_rate = 10                 
tax_rate = 5                      

subtotal = 0
for i in range(len(item_prices)):
    subtotal += item_prices[i] * item_quantities[i]

discount_amount = subtotal * (discount_rate / 100)
subtotal_after_discount = subtotal - discount_amount

tax_amount = subtotal_after_discount * (tax_rate / 100)

total_cost = subtotal_after_discount + tax_amount

print("Total cost for customer:", total_cost)
