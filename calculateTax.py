
item_Price = 75.34
tax = 0.0725

sales_tax = item_Price * tax 
total = item_Price + sales_tax 

print(f'The item cost ${item_Price}')
print(f'Sales Tax is ${sales_tax:,.2f}.')
print(f'The total is ${total:,.2f}.')

