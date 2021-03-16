import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    #df.tail(15)

    # Create scatter plot
    x1 = df['Year']
    y1 = df['CSIRO Adjusted Sea Level']
    plt.scatter(x1, y1)
    #plt.show()

    # Create first line of best fit
    slope1, intercept1, rvalue1, pvalue1, stderr1 = linregress(x1, y1)
    #linregress(x1,y1)

    regress_x1 = pd.Series(range(1880, 2051))
    regress_y1 = pd.Series(range(0, 2051-1880)*slope1)
    plt.plot(regress_x1, regress_y1, color='r')

    # Create second line of best fit
    x2 = df['Year'].loc[2000-1880:]
    y2 = df['CSIRO Adjusted Sea Level'].loc[2000-1880:]

    slope2, intercept2, rvalue2, pvalue2, stderr2 = linregress(x2, y2)

    regress_x2 = pd.Series(range(2000, 2051))
    regress_y2 = (pd.Series(range(0, 2051-2000))*slope2)+df['CSIRO Adjusted Sea Level'].loc[2000-1880]
    linregress(x2,y2), regress_x2, regress_y2
    plt.plot(regress_x2, regress_y2, color='c')
    #plt.show()

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level(inches)')
    plt.title('Rise in Sea Level')
    #plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

x2 = df['Year'].loc[2000-1880:]
y2 = df['CSIRO Adjusted Sea Level'].loc[2000-1880:]

slope2, intercept2, rvalue2, pvalue2, stderr2 = linregress(x2, y2)

regress_x2 = pd.Series(range(2000, 2051))
regress_y2 = (pd.Series(range(0, 2051-2000))*slope2)+df['CSIRO Adjusted Sea Level'].loc[2000-1880]
linregress(x2,y2), regress_x2, regress_y2
plt.plot(regress_x2, regress_y2, color='c')
#plt.show()

plt.xlabel('Year')
plt.ylabel('Sea Level(inches)')
plt.title('Rise in Sea Level')
plt.show()

