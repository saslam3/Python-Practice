my_age = 21
half_my_age = my_age/2
greeting = "hello"
name = "Saimah"
greeting_with_name = greeting + name

print(" SSS  L")
print("S   S L")
print("S     L")
print(" SSS  L")
print("    S L")
print("S   S L")
print(" SSS  LLLLL")

#Saimah
#Premed and Enginnering major

print("""
 SSS        A
S   S      A A
S         A   A
 SSS     AAAAAAA
    S   A       A
S   S  A         A
 SSS  A           A
""")


lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""

lovely_loveseat_price = 254.00

stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""

stylish_settee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""

luxurious_lamp_price = 52.15

customer_one_total = 0

customer_one_itemization = ""

customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price

customer_one_itemization +=  luxurious_lamp_description

sales_tax = 0.08

customer_one_tax = customer_one_total * sales_tax

print("Customer One Items: ")
print(customer_one_itemization)

print("Customer One Total: ") 
print(customer_one_total)


