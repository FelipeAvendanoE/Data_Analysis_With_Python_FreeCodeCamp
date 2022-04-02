import pandas as pd
import numpy as np

# Read data from file
df = pd.read_csv("adult.data.csv")

# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = df["race"].value_counts()

# What is the average age of men?
average_age_men = df.loc[df["sex"] == "Male", "age"].mean().round(1)

# What is the percentage of people who have a Bachelor's degree?
bachelors = df.loc[df["education"] == "Bachelors", ].count()[0]
total = df.count()[0]
percentage_bachelors = ((bachelors/total)*100).round(1)

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
# What percentage of people without advanced education make more than 50K?
# with and without `Bachelors`, `Masters`, or `Doctorate`
higher_education = df.loc[((df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate"))].count()[0]
lower_education = df.loc[~((df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate"))].count()[0]
HE_rich = df.loc[((df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")) & (df["salary"] == ">50K")].count()[0]
LE_rich = df.loc[~((df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")) & (df["salary"] == ">50K")].count()[0]
# percentage with salary >50K
higher_education_rich = (HE_rich / higher_education * 100).round(1)
lower_education_rich = (LE_rich / lower_education * 100).round(1)

# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df["hours-per-week"].min()

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = df.loc[df["hours-per-week"] == 1].count()[0]
rich_min_worker = df.loc[(df["hours-per-week"] == 1) & (df["salary"] == ">50K")].count()[0]
rich_percentage = (rich_min_worker/num_min_workers*100).round(1)

# What country has the highest percentage of people that earn >50K?
country_earning = df.loc[df["salary"] == ">50K"].groupby("native-country").count()
country_pop = df.groupby("native-country").count()
highest_earning_country = (country_earning/country_pop).idxmax()[0]
highest_earning_country_percentage = (country_earning / country_pop * 100).max().round(1)[0]

# Identify the most popular occupation for those who earn >50K in India.
India = df.loc[(df["native-country"] == "India") & (df["salary"] == ">50K")]
top_IN_occupation = India.occupation.mode()[0]
