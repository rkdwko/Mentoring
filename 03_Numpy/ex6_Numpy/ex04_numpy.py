import numpy as np

x = np.array([ 18, 5, 10, 23, 19, -8, 10, 0, 0 ,5,2,15, 8,
               2, 5, 4, 15, -1, 4, -7 , -24, 7, 9, -6, 23, -13])

# TODO
# TODO
# TODO
# TODO
# TODO
print(x.sum(), np.sum(x))
print(x.mean(), np.mean(x))
print(np.median(x))
print(x.min(),  np.min(x))
print(x.max(),  np.max(x))
# TODO
# TODO

x = np.array( [[ 1,1],
                [2,2] ])
print(" 전체 합 ", x.sum())
print(  x.sum( axis= 0 ))  #열 합
print(  x.sum( axis= 1 ))  #행 합계

# TODO
# TODO
# TODO
print(np.percentile(x, 0 ))
print(np.percentile(x, 25 ))
print(np.percentile(x, 50 ))
print(np.percentile(x, 75 )) # 3/4
print(np.percentile(x, 100 )) # 최대값


