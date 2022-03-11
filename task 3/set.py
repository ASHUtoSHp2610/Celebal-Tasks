#iterators set
x={"apple", "banana", "cherry", "apple"}
y = {"hi","h","hello"}

print(x)
print(type(x)) #type
print(len(x)) #length

x.add("mango") #add
print(x)


y.update(x)#update
print(y)

x.remove("apple") #remove
print(x)

#pop
x1= x.pop()
print(x1)
print(x)

#discard
y.discard("")
print(y)

for x in y:
  print(x)


#union
y=y.union(x) 
print(y)