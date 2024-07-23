
print("jp yen to usd")
jpYen = int(input("Japanese Yen: "))
usDur = jpYen * .0062
usD = round(usDur, 2)
print(f"US Dollars: {usD}")

print("meters to miles")
m = int(input("Meters: "))
mi = m / 1609.34 
print(f"Miles: {mi}")

print("kg to lb")
kg = int(input("Kilograms: "))
lb = kg * 2.2046226218
print(f"Pounds: {lb}")

if(lb <= 50):  
    print("You will fly without additional fees.")
else:
    print("Your baggage is overweight! You will incur additional fees :(")

# time for a little fun >:)
# https://www.omnicalculator.com/conversion/weird-units

print("usd to cans of coke (considering a pack of coke from Walmart is $8.26 / $1.84 ea can)")
usd = int(input("How much money ya got?: "))
cans = usd / 1.84
usd = round(usdur, 2)
left = usdur % 1.84
print(f"You will purchase {cans} cans of coke and have {left} dollars left. HAHA, ur broke!")

print("Hi, fellow cat lover! Have you ever wondered how many cats could make up you? Well, you should! (weight of cat is ~4.5kg)")
weightlb = int(input("Weight in Pounds: "))
cats = weightlb / 2.2046226218 / 4.5
print(f"If you disappeared tomorrow, {cats} cats could take your place!")

print("Thanks for using this unit converter :D")
