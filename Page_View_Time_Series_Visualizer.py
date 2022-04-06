import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = "date", parse_dates = True)

# Clean data
df = df[ (df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975)) ]


def draw_line_plot():
    # Draw line plot

    fig, axes = plt.subplots(figsize=(12, 6))

    axes.plot(df)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month
    df_bar = df_bar.groupby(["year","month"]).mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
      
    fig = df_bar.plot(kind = "bar").figure
    plt.legend(title = "Months", labels = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")


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

    fig, axs = plt.subplots(1, 2, figsize=(12,6))
  
    sns.boxplot(x =  "year", y = "value", data = df_box, ax=axs[0]).set(title="Year-wise Box Plot (Trend)",xlabel="Year",ylabel="Page Views")
    
    sns.boxplot(x =  "month", y = "value", data = df_box, ax=axs[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']).set(title="Month-wise Box Plot (Seasonality)",xlabel="Month",ylabel="Page Views")
    

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig