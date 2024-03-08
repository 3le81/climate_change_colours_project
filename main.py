# =================================== IMPLEMENTATION with years displayed =================================
# 1 import libraries and give them aliases to call them later
import pandas as pd
import matplotlib.pyplot as plt

# # 2 loads the data
data = pd.read_csv('data.csv')

# # 3 set up the plot, a container with an adjustable canvas inside it
plt.figure(figsize=(8, 5))

plt.gca().set_aspect('equal', adjustable='box')

# # uncomment the line below to see just the picture without the graph
# plt.axis('off')

# # 4 create the bar chart
bars = data.shape[0]
barWidth = 800/bars
barHeight = 500
# # for loop iterating through each row of the DataFrame
for i in range(bars):
    x = i * barWidth
    y = 0
    # # going always to the 2nd column in each row for getting the global data
    d = data.iloc[i, 1]
    if d > 0:
        col = plt.cm.Reds(d)
    else:
        col = plt.cm.Blues(-d)

# # creating a function
    plt.bar(x, barHeight, width=barWidth, bottom=y, color=col)

# # Adding the year "1980" in the middle of the horizontal axis
plt.text(bars * barWidth / 2, -20, '1980',
         fontsize=10, fontweight='bold', ha='center')

# Adjusting the font properties for the x-axis ticks (1880 and 2022)
plt.xticks([0, bars * barWidth], ['1880', '2022'],
           fontsize=10, fontweight='bold')

plt.show()


# ===================================== WORKSHOP VERSION =====================================
# Comment out the code above and uncomment the following code to see the original work!

# # 1 import libraries and give them aliases to call them later
# import pandas as pd
# import matplotlib.pyplot as plt

# # 2 loads the data
# data = pd.read_csv('data.csv')

# # 3 set up the plot, a container with an adjustable canvas inside it
# plt.figure(figsize=(8, 5))

# plt.gca().set_aspect('equal', adjustable='box')

# # uncomment the line below to see just the picture without the graph
# plt.axis('off')

# # 4 create the bar chart
# bars = data.shape[0]
# barWidth = 800/bars
# barHeight = 500
# # for loop iterating through each row of the DataFrame
# for i in range(bars):
#     x = i * barWidth
#     y = 0
#     # going always to the 2nd column in each row for getting the global data
#     d = data.iloc[i, 1]
#     if d > 0:
#         col = plt.cm.Reds(d)
#     else:
#         col = plt.cm.Blues(-d)

# # creating a function
#     plt.bar(x, barHeight, width=barWidth, bottom=y, color=col)

# plt.show()
