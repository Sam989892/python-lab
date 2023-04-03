x = 10
print(x)
print(id(x))
print(type(x))

#float
y = 7.65
print(y)
print(id(y))
print(type(y))

#str
z = 'SAM' 
print(z)
print(id(z))
print(type(z))

#boolean
a = True
print(a)
print(id(a))
print(type(a))

#complex
b = 4 + 2j
print(b)
print(id(b))
print(type(b))

print('<','-' * 45,'>')

x = 10
y = 10
abc = 10
print(id(x))
print(id(y))
print(id(abc))

print('<','-' * 45,'>')
c = [12,14,True,"python",12.55]
print(c)
print(id(c))
print(type(c))
print('<','-' * 45,'>')
d = (12,14,True,"python",12.55)
print(d)
print(id(d))
print(type(d))
print('<','-' * 45,'>')
e = {12,14,True,"python",12.55}
print(e)
print(id(e))
print(type(e))
print('<','-' * 45,'>')
f = {1:12,2:14,55:True,23:"python",99:12.55}
print(f)
print(id(f))
print(type(f))