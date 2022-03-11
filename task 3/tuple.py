#iterators tuple
x=("apple","Banana","Pine","Peach","Orange")
print(x,"\n",type(x))
for i in range(len(x)):
  s=""
  for j in x[i]:
    s+=j
    print(s)


#indexing
print(x[:2])

#negitive indexing
print(x[-1:])


#join two tuples
y=(1,2,3,4,5)
y=y+x
print(y)

#multiply 
y= y*3
print(y)
