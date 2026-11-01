def calculate_tax(price, rate):
	"""Calculate sales tax using a decimal tax rate."""
	return price * rate


tax_1 = calculate_tax(100, 0.07)
tax_2 = calculate_tax(250, 0.08)

print("--- Exercise 1 ---")
print(f"Tax on $100 at 7%: ${tax_1:.2f}")
print(f"Tax on $250 at 8%: ${tax_2:.2f}")
print()


def apply_discount(price, tier):
	"""Apply the tier discount, or no discount for an unknown tier."""
	if tier == "gold":
		discount = 0.15
	elif tier == "silver":
		discount = 0.10
	elif tier == "bronze":
		discount = 0.05
	else:
		discount = 0.0
	return price * (1 - discount)


test_price = 200
print("--- Exercise 2 ---")
print(f"gold:   ${apply_discount(test_price, 'gold'):.2f}")
print(f"silver: ${apply_discount(test_price, 'silver'):.2f}")
print(f"bronze: ${apply_discount(test_price, 'bronze'):.2f}")
print(f"none:   ${apply_discount(test_price, 'none'):.2f}")
print()


def final_price(price, tier, tax_rate):
	"""Apply the discount first, then tax the discounted price."""
	discounted = apply_discount(price, tier)
	return discounted + calculate_tax(discounted, tax_rate)


print("--- Exercise 3 ---")
gold_discounted = apply_discount(200, "gold")
print(f"After gold discount: ${gold_discounted:.2f}")
after_tax = gold_discounted + calculate_tax(gold_discounted, 0.07)
print(f"After tax: ${after_tax:.2f}")
composed_total = final_price(200, "gold", 0.07)
print(f'final_price(200, "gold", 0.07) = ${composed_total:.2f}')
print()


orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
print("--- Exercise 4 ---")
for price, tier in orders:
	total = final_price(price, tier, 0.07)
	print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")
print()


def process_sales_batch(orders_list, tax_rate=0.07):
	"""Print each processed order and return the grand total."""
	grand_total = 0.0
	for order_price, order_tier in orders_list:
		order_final = final_price(order_price, order_tier, tax_rate)
		grand_total += order_final
		print(f"Processed order ({order_tier}): ${order_final:.2f}")
	return grand_total


print("--- Exercise 5 (Fixed broken_sales) ---")
batch_total = process_sales_batch(orders, 0.07)
print(f"Batch Total: ${batch_total:.2f}")
print()


x = 100


def double_it():
	x = 999
	return x * 2


print("--- Exercise 6 ---")
print(x)           # 100: accesses global x
print(double_it()) # 1998: uses local x
print(x)           # 100: the global x is unchanged
