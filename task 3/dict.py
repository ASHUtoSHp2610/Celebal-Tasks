x =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
x3 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(x)

a= x["model"]
print(a) #access an element

a= x.get("year")
print(a)

b= x.keys()  #add element
x["color"]="black"
print(x)


b= x.values() #get values
x['year'] = 2020
print(b)


b= x.items() #get items
x["brand"]="ford"
print(b)


#check if is exist or not
if "year" in x:
  print("yes")

else:
  print("no")


#update
x["year"]="1881"
print(x)


x.update({"year":"2000"})
print(x)


#add
x.update({"wheels":"5"})
print(x)


#remove
x.pop("wheels")
print(x)

#clear whole dict
x1= x.clear()
print(x1)

#copy
b = x3.copy()
print("copy",b)