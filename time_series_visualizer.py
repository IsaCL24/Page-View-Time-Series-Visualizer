import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

# Import data (Make Copy)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
df.index = pd.to_datetime(df.index)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & 
        (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    df_copy = df.copy()
    ax.plot(df_copy.index, df_copy['value'], color='red', linewidth=1)
    
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    fig.tight_layout()
    
    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and prepare data for monthly average
    df_copy = df.copy()
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month
    
    # Calculate average page views per month per year
    df_bar = df_copy.groupby(['year', 'month'])['value'].mean().unstack()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    df_bar.plot(kind='bar', ax=ax)
    
    ax.set_title('Average Daily Page Views - Each Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    
    fig.tight_layout()
    
    # Save image and return fig (don't change this part)
    plt.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_copy = df.copy()
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month

    # Prepare data for box plots (this part is done!)
    df_copy['year'] = df_copy['year'].astype(str)
    df_copy['month_name'] = df_copy['month'].apply(lambda x: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                                                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][x-1])

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Year-wise box plot
    sns.boxplot(data=df_copy, x='year', y='value', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise box plot
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_copy, x='month_name', y='value', order=month_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    fig.tight_layout()
    
    # Save image and return fig (don't change this part)
    plt.savefig('box_plot.png')
    return fig
