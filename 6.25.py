'''
quote = "It's all over."
print(quote)
first = 'Iris'
last = 'Wang'
print(first + ' ' + last)
word = 'Python'
print(len(word))
print(word[0])
print(word[-1])
print(word[0:3])
messy = '   Hello World   '
print(messy.strip())
print(messy.upper())
print(messy.lower())
name = 'Iris'
age = 17
print(f"I'm {name}  , {age} years old now")
word = input('please write down a word:')
print(len(word))
print(word.upper())


first_name = input('please write down your first name:')
last_name = input('please write down your last name:')
birth_year = input('when were you born:')
city = input('please write down where do you live:')
print('===== ACCOUNT INFO =====')
print(f'username: {first_name[0].lower()}{last_name.lower()}')
print(f'Initials:+{first_name[0].upper()}.{last_name[0].upper()}')
print(f'age:{2026 - int(birth_year)}')
print(f'name length:{len(first_name)+len(last_name)} letter')
print(f'city:{city}')
'''

customer = input('please write down your name:')
product = input("product's name:")
price = input('how much:')
quantity = input('how many:')

subtotal = float(price)*float(quantity)
tax = float(subtotal)*0.05
total = subtotal+tax
order_id = product[0:3].upper()+quantity
item = (f'{product} x{quantity}')

print(f"""
===== RECIPT =====
Customer:{customer}
Order ID:{order_id}
Item:{item}
Subtotal:${subtotal:.2f}
Tax(5%):${tax:.2f}
Total:${total:.2f}
==================
""")
