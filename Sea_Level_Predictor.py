import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  
  # Read data from file
  df = pd.read_csv("epa-sea-level.csv")

  # Create scatter plot
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

  # Create first line of best fit
  slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
  X1 = list(range(1880,2051))
  Y1 = []
  for year in X1:
    Y1.append(intercept + slope*year)
  plt.plot( X1, Y1, label = "Best Fit Line 1")

  # Create second line of best fit
  df2 = df[ df["Year"] >= 2000]
  slope, intercept, r_value, p_value, std_err = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
  X2 = list(range(2000,2051))
  Y2 = []
  for year in X2:
    Y2.append(intercept + slope*year)
  plt.plot( X2, Y2, label = "Best Fit Line 2")

  # Add labels and title
  plt.legend()
  plt.title("Rise in Sea Level")
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()