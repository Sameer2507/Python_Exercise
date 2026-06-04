subtotal, gratuity_rate = eval(input("Enter the subtotal and a gratuity rate: "))
gratuity = subtotal * (gratuity_rate / 100)
total = subtotal + gratuity
print(f"The gratuity is {round(gratuity, 2)} and the total is {round(total, 2)}")