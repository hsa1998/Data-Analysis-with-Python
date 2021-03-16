import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', header = 0, index_col = 0)
df.index = pd.to_datetime(df.index)

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig1 = plt.figure(figsize=(15,5))
    axes1 = fig1.add_axes([0, 0, 1, 1])

    axes1.set_xlabel('Date')
    axes1.set_ylabel('Page Views')

    axes1.xaxis.set_major_locator(MultipleLocator(180))
    axes1.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    plt.plot(df.index, df['value'], color = 'r', linewidth=1)




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig2 = df_bar.plot(kind='bar', legend=True, figsize=(15,15)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title = 'Months', labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.show()




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2)

    fig.set_figwidth(20)
    fig.set_figheight(6)

    ax1 = sns.boxplot(x=df_box['year'], y=df_box['value'], ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')

    ax2 = sns.boxplot(x=df_box['month'], y=df_box['value'], ax=ax2)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
