import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col="date")

# Clean data
df = df[
(df["value"]>=df["value"].quantile(0.025))&
(df["value"]<=df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, axes = plt.subplots(figsize=(10,5))
    axes.plot(df.index, df["value"],"r", linewidth=1)
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    axes.set_xlabel("Date")
    axes.set_ylabel("Page Views")




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df["month"]=df.index.month
    df["year"]=df.index.year
    df_bar = df.groupby(["year","month"])["value"].mean()
    df_bar = df_bar.unstack()
   
    # Draw bar plot
    df_bar.columns=["January","February","March","April","May","June","July","August","September","October","November","December"]
    fig = df_bar.plot(kind="bar", legend=True, figsize=(15,8)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.legend(title="Months")


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
    df_box["month_num"]=df_box["date"].dt.month
    df_box=df_box.sort_values("month_num")
    fig, (ax1,ax2)=plt.subplots(1,2, figsize=(16,9))
    sns.boxplot(ax=ax1,x="year",y="value",data=df_box)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

    sns.boxplot(ax=ax2,x="month",y="value",data=df_box)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
draw_line_plot()
draw_bar_plot()
draw_box_plot()