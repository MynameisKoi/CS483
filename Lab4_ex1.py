# 1. Getting data from the Internet
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import matplotlib.dates as mdates
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    
def graph_data(stock):
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y-%m-%d')})
    # %Y = full year. 2015
    # %y = partial year 15
    # %m = number month
    # %d = number day
    # %H = hours
    # %M = minutes
    # %S = seconds
    # 12-06-2014
    # %m-%d-%Y
    plt.plot_date(date, closep,'-', label='Price')
 
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
plt.show()
graph_data('TSLA')

# 2. Converting data from the Internet
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import matplotlib.dates as mdates
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    
def graph_data(stock):
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y-%m-%d')})
# %Y = full year. 2015
# %y = partial year 15
# %m = number month
# %d = number day
# %H = hours
# %M = minutes
# %S = seconds
# 12-06-2014
# %m-%d-%Y
    plt.plot_date(date, closep,'-', label='Price')
# '-': connect each point in solid line on the plot
 
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()
graph_data('TSLA')

# 3. Basic customizations, rotating labels
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import matplotlib.dates as mdates
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    
def graph_data(stock):
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))
    # Check the follwing link for subplot2grid
#https://www.southampton.ac.uk/~fangohr/training/python/notebooks/Matplotlib.html
    
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y-%m-%d')})
# %Y = full year. 2015
# %y = partial year 15
# %m = number month
# %d = number day
# %H = hours
# %M = minutes
# %S = seconds
# 12-06-2014
# %m-%d-%Y
    
    ax1.plot_date(date, closep,'-', label='Price')
    ax1.grid(True, color='g', linestyle='--', linewidth=0.1)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
        
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.95, wspace=0.2, hspace=0)
    plt.show()
graph_data('TSLA')

# 4. More customization of colors and fills
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import matplotlib.dates as mdates
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    
def graph_data(stock):
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    fig = plt.figure(1) # Create figure 1 window
    ax1 = plt.subplot2grid((1,1),(0,0))
    
    
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y-%m-%d')})
    
    ax1.plot_date(date, closep,'-', label='Price')
    ax1.plot([], [], linewidth=5, label='loss', color='r', alpha=1)
    ax1.plot([], [], linewidth=5, label='gain', color='g', alpha=0.5)
    ax1.fill_between(date, closep, 250,where = (closep > 100), facecolor='g', alpha = 0.5)
    # alpha: softening color
    ax1.fill_between(date, closep, 250,where = (closep <= 100), facecolor='r', alpha = 0.5)
    ax1.grid(True, color='g', linestyle='--', linewidth=0.1)
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
    ax1.set_yticks([0,125,250,375, 475, 575])
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
        
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.95, wspace=0.2, hspace=0)
    # plot location in displaly window
    plt.show()
graph_data('TSLA')

# 5. Spines and horizontal lines
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import matplotlib.dates as mdates
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    
def graph_data(stock):
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    fig = plt.figure(1) # Create figure 1 window
    ax1 = plt.subplot2grid((1,1),(0,0))
    
    
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          converters={0: bytespdate2num('%Y-%m-%d')})
    
    ax1.plot_date(date, closep,'-', label='Price')
    ax1.plot([], [], linewidth=5, label='loss', color='r', alpha=1)
    ax1.plot([], [], linewidth=5, label='gain', color='g', alpha=0.5)
    ax1.axhline(closep[0], color='k', linewidth=5)
    # axhline: axis horizontal line
    ax1.fill_between(date, closep, 250,where = (closep > 100), facecolor='g', alpha = 0.5)
    ax1.fill_between(date, closep, 250,where = (closep <= 100), facecolor='r', alpha = 0.5)
    ax1.grid(True, color='g', linestyle='--', linewidth=0.1)
    # ax1.xaxis.label.set_color('c')
    # ax1.yaxis.label.set_color('r')
    ax1.set_yticks([0,125,250,375, 475, 575])
    
    ax1.spines['left'].set_color('r')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['left'].set_linewidth(5)
    
    ax1.tick_params(axis='x', colors='#f05215')    # Change label on x axis from https://www.color-hex.com/
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
        
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94,top=0.95, wspace=0.2, hspace=0)
    plt.show()
graph_data('TSLA')

# 6. Candlestick OHLC graphs
!pip install --upgrade mplfinance
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mplfinance.original_flavor import candlestick_ohlc
import numpy as np
import urllib.request
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    
def graph_data(stock):
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    fig = plt.figure(1) # Create figure 1 window
    ax1 = plt.subplot2grid((1,1),(0,0))
    
    
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y-%m-%d')})
    
    x = 0
    y = len(date)
    ohlc = []
    while x < y:
      append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
      ohlc.append(append_me)
      x+=1
    candlestick_ohlc(ax1,ohlc, width=0.4, colorup='g', colordown='r')  #Open-High-Low-Close Chart (OHLC Chart)
    for label in ax1.xaxis.get_ticklabels():
      label.set_rotation(45)    
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))  
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94,top=0.95, wspace=0.2, hspace=0)
    plt.show()
graph_data('TSLA')

# 7. Styles
!pip install --upgrade mplfinance
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mplfinance.original_flavor import candlestick_ohlc
import numpy as np
import urllib
from matplotlib import style
# style.use('ggplot')   # grey backgroud
# style.use('dark_background')  
style.use('bmh')        # Bayesian Methods for Hackers
print(plt.style.available)
print(plt.__file__)
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    
def graph_data(stock):
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    fig = plt.figure(1) # Create figure 1 window
    ax1 = plt.subplot2grid((1,1),(0,0))
    
    
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y-%m-%d')})
    
    x = 0
    y = len(date)
    ohlc = []
    while x < y:
      append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
      ohlc.append(append_me)
      x+=1
    ax1.plot(date,closep)
    ax1.plot(date,openp)
    for label in ax1.xaxis.get_ticklabels():
      label.set_rotation(45)    
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))  
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94,top=0.95, wspace=0.2, hspace=0)
    plt.show()
graph_data('TSLA')
