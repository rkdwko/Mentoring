import numpy as np

#TODO
x = np.array([1,2,3])
print(  type( x) )
print(  x.dtype  )  #int32

x = np.array([1,2,3]  )  #TODO
print(  x.dtype  )

a =  #TODO
b = np.zeros( (2,3) )
c = np.zeros( (5,2) , dtype="f")

print (a)
print (b)
print (c)

d = np.zeros(5, dtype="U4")
d[0] = "abc"
d[1] = "abcd"
d[2] = "ABCDE"
d[3] = "ABCDEF"
d[4] = "ABCDEFG"
print( d) #['abc' 'abcd' 'ABCD' 'ABCD' 'ABCD']

a = np.ones( 5 )
b = np.ones( (2,3) )
c = np.ones( (5,2) , dtype="i" )
print(a)


a = np.arange(10)
print (a)

# TODO
print (a)

# TODO
print (n)

n = np.linspace(0,100, 250)
print (n)


a = np.arange( 12 )
print (a )

# TODO
print( b )


a = np.arange(12)

# TODO
print ( a.reshape(2,2,-1))
print ( a.reshape(2,-1,2))

x = np. arange(5)
print (x)
print(x.reshape(1,5))
print(x.reshape(5,1))

# TODO
print (a.ravel())

a1 = np.ones((2,3))
a2 = np.zeros((2,3))

print (a1)
print (a2)

print (np.vstack([a1,a2]))