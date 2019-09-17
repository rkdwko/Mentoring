import numpy as np

x = np.arange(1, 10001 )
y = np.arange(10001, 20001 )

z = 3*x + y
print(z)

a = np.array([1,2,3,4])
# TODO


a = np.array([ 1,2,3,4 ])
b = np.array([ 4,2,3,4 ])

print ( (a>=b) & (a==4) )
print ( (a>=b) | (a==b) )

# TODO

# TODO

print (np.exp (a ))
print (np.log (a + 1 ))

a = np.array ([ [ 4,3,5,7],
                 [ 1,12,11,9],
                 [2,15,1,14] ]
               )

# TODO
print ( np.sort(a, axis=1) ) #행정렬
print ( np.sort(a, axis=0) ) #열정렬

a = np.array ([ 42, 38, 12, 25])
# TODO
print ( j )
print ( a [ j ])









