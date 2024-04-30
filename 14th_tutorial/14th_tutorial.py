import numpy as np



# print(np.random.random())
# print(np.random.choice([1,2,3,4]))


# for i in range(10):
#     print(np.random.random())


# for i in range(10):
#     print(np.random.choice([1,2,3,4]))
    
    
# # Monte Carlo Simulation
# A_win = []
# for i in range(10000):
#     if np.random.random() <= 0.7:
#         A_win.append(1)
# print(sum(A_win))




# import matplotlib.pyplot as plt
# x = np.linspace(-1,1,100)

# def function(x):
#     return (x-0.5)*x*(x+0.5)

# y = function(x)

# plt.plot(x,y,label='f')
# plt.plot(x,y,'o-',label='g')
# plt.legend()
# plt.grid()
# plt.show()


import csv
rows = []
with open('tutorial.csv', 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
 
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)