import matplotlib.pyplot as plt
days = ["Monday", "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"]
temperatures = [22 , 24 , 19 , 23 , 25 , 27 , 29]
plt.plot(days , temperatures , marker = 'o' , linesstyle = '-' , color = 'b')
plt.title("Temperature Variation Over a Week")
plt.xlabel("Days of the Week")
plt.ylabel("Temperature(C)")
plt.grid(True)
plt.show()