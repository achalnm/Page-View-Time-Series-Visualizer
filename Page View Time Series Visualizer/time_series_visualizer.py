import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def draw_line_plot():
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['value'], color='r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.show()

def draw_bar_plot():
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    
    monthly_data = df.groupby(['year', 'month'])['value'].mean().unstack()
    
    plt.figure(figsize=(12, 6))
    monthly_data.plot(kind='bar', legend=True)
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.show()

def draw_box_plot():
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    
    plt.figure(figsize=(14, 7))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df, order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    
    plt.tight_layout()
    plt.savefig('box_plot.png')
    plt.show()
