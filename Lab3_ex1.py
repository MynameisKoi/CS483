# 1. Introduction & Line Plot
import matplotlib.pyplot as plt # Data visualization library
plt.plot([1,2,3],[5,7,4]) # [1,2,3] -> x; [5,7,4] -> y;
plt.show() # move plot to the foregr

# 2. Legends, Titles, and Labels
import matplotlib.pyplot as plt
x = [1,2,3]
y = [5,7,4]
plt.plot(x,y)
plt.xlabel('Plot Number')
plt.ylabel('Important Var')
plt.title('Interesting Graph\nCheck it out')
plt.show()
 
import matplotlib. pyplot as plt
x = [1,2,3]
y = [5,7,4]
x2 = [1,2,3]
y2 = [10,14,12]
plt.plot(x, y, label = 'First Line')
plt.plot(x2, y2, label = 'Second Line')
plt.xlabel('Plot Number')
plt.ylabel('Important Var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

# 3. Bar Charts and Histograms
import matplotlib.pyplot as plt
x = [2,4,6,8,10] # width of bar < 1
y = [6,7,8,2,4]
x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]
plt.bar(x,y, label='Bars1', color = 'r')
plt.bar(x2,y2, label='Bars2', color = 'c') # c -> cyan
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
 
import matplotlib.pyplot as plt
population_ages = [22,55,62,45, 21, 22,34, 
42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
ids =[x for x in range(len(population_ages))]
plt.bar(ids, population_ages, label='bars')
# bins =[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
# plt.hist(population_ages, bins, label='bars',histtype = 'bar', rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

# 4. Scatter Plots
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8]
y= [5,2,4,7,6,9,3,1]
plt.scatter(x,y, label='skitscat', color='k', marker='o', s=100) # k-black
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

# 5. Stack Plots
import matplotlib.pyplot as plt
days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]
plt.plot([],[],color='m', label='sleeping', linewidth=5)
plt.plot([],[],color='c', label='eating', linewidth=5)
plt.plot([],[],color='r', label='working', linewidth=5)
plt.plot([],[],color='k', label='playing', linewidth=5)
plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','k'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

# 6. Pie Charts
import matplotlib.pyplot as plt
slices = [7,2,2,13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c','m','r','b']
plt.pie(slices, labels = activities, colors=cols, startangle=90, 
shadow = True, explode=[0, 0.1,0,0], autopct='%1.1f%%')
# explode - pull out; autopct - change to percentage 
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

# 7. Loading Dataset from Files
# Example 1
from google.colab import drive
drive.mount('/content/drive')         
# mount '/content/drive' to virtual machine directory for google colab user
#below where the file is in gdrive, change with your
data_path = "/content/drive/My Drive/Colab Notebooks/"
import numpy as np
data = np.loadtxt(data_path + 'data_decision_trees.txt', delimiter=',')
X, y = data[:, :-1], data[:, -1]
print(X)
%cd /content/drive/My Drive/Colab Notebooks
%pwd

# Example 2
from google.colab import drive
drive.mount('/content/drive')         
# mount '/content/drive' to virtual machine directory for google colab user
#below where the file is in gdrive, change with your
data_path = "/content/drive/My Drive/Colab Notebooks/"
import numpy as np
import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open(data_path + 'example.txt', 'r') as csvfile:
  plots = csv.reader(csvfile, delimiter=',')
  for row in plots:
    x.append(row[0])
    y.append(row[1])
plt. scatter(x,y, label='Loaded from the file')
# x, y = np.loadtxt(data_path + 'example.txt', delimiter=',', unpack=True)
# plt.plot(x,y, label='Loaded from the file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
