#iterators list
x= ["apple","Banana","Pine","Peach","Orange"]
y= ["hoi","helo","hi"]
print(x,"\n",type(x))


print(x[1])
#slicing
#negative slicing
print(x[-1:])
#range of index
print(x[3:5]) 
print(x[:3])


#update
x[1]="hi"
print(x)

#change in range
x[0:2]='banana','mongo'
print(x)

#append
x.append('pea')
print(x)

#insert 
x.insert(1,'kelus')
print(x)

#extend
x.extend(y)
print(x)

#remove
x.remove("banana")
print(x)

#pop
y.pop(2)
print(y)

#delete
del x[2]
print(x)

#clear
y.clear()
print(y)


#sort
x.sort()
print(x)

#revese sort
x.sort(reverse= True)
print(x)

#copy
z=x.copy()
print(z)

z=list(x)
print(z)

y=['1','2','3','4','5']
a="_"
a=a.join(y)
print(a)