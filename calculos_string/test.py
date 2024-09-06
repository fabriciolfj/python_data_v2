val =  "a,b, guido"

result = val.split(",")
print(result)
print(len(result))

result = "::".join(result)
print(result)

print("guido" in val)
print(val.find(","))
print(val.index(","))
print(val.count(","))
print(val.replace(",", ";"))
