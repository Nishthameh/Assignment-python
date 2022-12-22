x = float(input("enter your gross income"))
y = int(input("enter number of dependents"))
z = round(x) - 10000 - y*3000
print( "tax is", z*0.2 )