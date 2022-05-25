mport numpy as np 
import matplotlib.pyplot as plt 
 
np.random.seed(4500) # Create the same group number of random number 
for each time running  
 
mean=150 
sd=10 
N=1000 
 
heights=np.random.normal(mean, sd, N) 
 #np.random.normal -> create random number based on mean/st/N 
 
density=False  # Switch between regular histogram and pdf 
hist,bin_edges=np.histogram(heights, bins=50, density=density) 
   # np.histogram -> put elem in heights array into 50 bins 
 
cum_hist=np.cumsum(hist) # add all elem in hist together 
 
# Normalized histogram 
norm_hist = hist/N 
 
# Cumulative Normalized histogram 
norm_cum_hist = np.cumsum(norm_hist) 
 
bin_width=bin_edges[2]-bin_edges[1] 
print('Bin Width',bin_width) 
 
plt.figure()  # create a new figure 
# plt.plot(bin_edges[:-1], hist, color='green', label='heights histogram') 
 # bin_edges[:-1] from 1st elem to last 2nd elem 
plt.plot(bin_edges[:-1], cum_hist, color='green', label='heights histogram') 
 
# plt.plot(bin_edges[:-1], norm_hist, color='green', label='heights histogram') 
 
# plt.plot(bin_edges[:-1], norm_cum_hist, color='green', label='heights 
histogram') 
plt.xlabel('Heights') 
plt.ylabel('Frequency') 
plt.grid() 
plt.legend() 
plt.title('Histogram/Density Function of Heights of college students') 
plt.show 
