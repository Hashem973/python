import numpy as np
A = np.array([10 , 20 , 30 , 40 , 50])
B = np.array([5 , 4 , 3 , 2 , 1])
add_result = A + B
sub_result = A - B
mul_result = A * B
div_result = A / B
mean_A = np.mean(A)
max_A = np.max(A)
min_A = np.min(A)
dot_product = np.dot(A , B)
reshaped_A = A.reshape(5 , 1)
print(add_result)
print(sub_result)
print(mul_result)
print(div_result)
print(mean_A)
print(max_A)
print(min_A)
print(dot_product)
print(reshaped_A)