# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from tabulate import tabulate
file = pd.read_csv(r"C:\Users\emani\Documents\my_files\projects\datasets\wow_battlegrounds\wowbgs2.csv")
file = file.fillna(0)
file_win = file[file['Win'] == 1]
print(file.head())
stats = file.describe()
print("\033[1m",'Basic Statistics for WoW Battlegrounds',"\033[0m")
print(tabulate(stats[['DD','HD','D']], ['DD','HD','D'], tablefmt="fancy_grid"))

import matplotlib.pyplot as plt
import seaborn as sns
# Creating distributions plots for battleground outcomes in DD, HD, and D
# Define the variables for subplots
variables = ['DD', 'HD', 'D']
titles_horde = ['Horde DD Distribution', 'Horde HD Distribution', 'Horde D Distribution']
titles_alliance = ['Alliance DD Distribution', 'Alliance HD Distribution', 'Alliance D Distribution']
titles_horde_win = ['DD', 'Horde Distributions for Wins HD', 'D']
titles_alliance_win = ['DD', 'Alliance Distributions for Wins HD', 'D']

fig, axes = plt.subplots(nrows=4, ncols=len(variables), figsize=(12, 16))

# Iterate over variables and create histplot for Horde
for i, var in enumerate(variables):
    sns.histplot(np.array(file[file['Faction'] == 'Horde'][var]), ax=axes[0, i], kde=True)
    axes[0, i].set_xlabel(var)
    axes[0, i].set_ylabel('Count')
    axes[0, i].set_title(titles_horde[i])

# Iterate over variables and create histplot for Alliance
for i, var in enumerate(variables):
    sns.histplot(np.array(file[file['Faction'] == 'Alliance'][var]), ax=axes[1, i], kde=True)
    axes[1, i].set_xlabel(var)
    axes[1, i].set_ylabel('Count')
    axes[1, i].set_title(titles_alliance[i])
    
for i, var in enumerate(variables):
    sns.histplot(np.array(file_win[file_win['Faction'] == 'Horde'][var]), ax=axes[2, i], kde=True)
    axes[2, i].set_xlabel(var)
    axes[2, i].set_ylabel('Count')
    axes[2, i].set_title(titles_horde_win[i])

# Iterate over variables and create histplot for Alliance
for i, var in enumerate(variables):
    sns.histplot(np.array(file_win[file_win['Faction'] == 'Alliance'][var]), ax=axes[3, i], kde=True)
    axes[3, i].set_xlabel(var)
    axes[3, i].set_ylabel('Count')
    axes[3, i].set_title(titles_alliance_win[i])

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()

#display Shapiro-Wilk test results
import scipy.stats as stats

datasets = [file_win[file_win['Faction'] == 'Horde']['DD'], file_win[file_win['Faction'] == 'Horde']['HD'], file_win[file_win['Faction'] == 'Horde']['D'], 
            file_win[file_win['Faction'] == 'Alliance']['DD'], file_win[file_win['Faction'] == 'Alliance']['HD'], file_win[file_win['Faction'] == 'Alliance']['D']]

dataset_names = ['Horde DD', 'Horde HD', 'Horde D', 'Alliance DD', 'Alliance HD', 'Alliance D']

results = []

for name, data in zip(dataset_names, datasets):
    statistic, p_value = stats.shapiro(data)
    result = [name, statistic, p_value]
    results.append(result)

# Define the table headers
headers = ["Dataset", "Statistic", "p-value"]

# Print the table using tabulate
print("\033[1m",'Shapiro-Wilk test fesults for DD, HD, and D, divided by Horde and Alliance, respectively',"\033[0m")
print(tabulate(results, headers, tablefmt="fancy_grid"))

plots = [
    {'data': file_win[file_win['Faction'] == 'Horde'], 'x': 'DD', 'hue': 'Rol', 'title': 'DD Distribution for Horde Controlling for Role'},
    {'data': file_win[file_win['Faction'] == 'Alliance'], 'x': 'DD', 'hue': 'Rol', 'title': 'DD Distribution for Alliance Controlling for Role'},
    {'data': file_win[file_win['Faction'] == 'Horde'], 'x': 'D', 'title': 'Horde D Distribution Controlling for Win'},
    {'data': file_win[file_win['Faction'] == 'Alliance'], 'x': 'D', 'title': 'Alliance D Distribution Controlling for Win'}
]

#perform mann-whitney U and student's t to examine differences in Horde and Alliance data

alliance_data = file.loc[file['Faction'] == 'Alliance']
horde_data = file.loc[file['Faction'] == 'Horde']

titles = ['Damage Done', 'Healing Done', 'Deaths']
results = []

for var, title in zip(variables, titles):
    alliance_var = alliance_data[var].values
    horde_var = horde_data[var].values

    U, p = stats.mannwhitneyu(alliance_var, horde_var)
    result = {'Variable': title, "Statistic": 'Mann-Whitney U statistic', "Value": U, "P-value": p}
    results.append(result)

for var, title in zip(variables, titles):
    alliance_var = alliance_data[var].values
    horde_var = horde_data[var].values

    T, p = stats.ttest_ind(alliance_var, horde_var)
    result = {'Variable': title, "Statistic": "Student's T-statistic", "Value": T, "P-value": p}
    results.append(result)

# Create a DataFrame from the results
result_df = pd.DataFrame(results)

# Print the resulting table
print("\033[1m", "Student's T and Mann-Whitney U for DD, HD, and D", "\033[0m")
print(tabulate(result_df, headers=result_df.columns, tablefmt='fancy_grid'))

for var, title in zip(variables, titles):
    # Calculate and plot median
    median_values = sns.pointplot(data=file, x='Faction', y=var, estimator=np.median, ci=None, color='red', markers='d', capsize=0.1, linestyles='')

    # Calculate and plot mean
    mean_values = sns.pointplot(data=file, x='Faction', y=var, estimator=np.mean, ci=95, color='blue', markers='s', capsize=0.1, linestyles='')

    # Set legend labels
    median_values.set_label('Median')
    mean_values.set_label('Mean')

    # Set title and labels
    plt.title(f'Differences in Median and Mean for {title}')
    plt.xlabel('Faction')
    plt.ylabel(title)

    # Add legend
    handles, labels = median_values.get_legend_handles_labels()
    plt.legend(handles, labels)

    plt.show()

#make a pivot table which is the contingency table for wins and losses
pivot = pd.pivot_table(file, values=['Win','Lose'], columns='Faction', aggfunc='sum')
print("\033[1m{}\033[0m".format('Contingency Table of Alliance and Horde Wins and Losses'))
print(tabulate(pivot, headers = ['Outcome','Alliance','Horde'], tablefmt="fancy_grid"))

#derive the ratio of wins to losses
wins = file.groupby('Faction')['Win'].agg('sum')
ratio = wins.loc['Horde']/wins.loc['Alliance']
print('The ratio of Horde Wins to Alliance Wins is:',ratio)

stat, p, dof, expected = stats.chi2_contingency(pivot)
chi2_statlist = [stat,p,dof]
chi2_table = pd.DataFrame(data=chi2_statlist, index=['Chi-squared','p-value','Degrees of Freedom'])
print("\033[1m",'Chi-squared test results for Alliance vs. Horde Wins and Losses',"\033[0m")
print(tabulate(chi2_table, tablefmt='fancy_grid'))

#calculate and display Kendall's Tau
columns = ['DD', 'HD', 'HK', 'D','Win']
results = []

# Calculate Kendall's tau and p-value for each pair of columns
for i in range(len(columns)):
    for j in range(i+1, len(columns)):
        col1 = columns[i]
        col2 = columns[j]
        tau, p_value = stats.kendalltau(file[col1], file[col2])
        result = {'Column 1': col1, 'Column 2': col2, 'Kendall\'s tau': tau, 'p-value': p_value}
        results.append(result)

# Create a DataFrame from the results
result_df = pd.DataFrame(results)
headings = ['Index','Variable1','Variable2',"Kendall's Tau",'p-value']

# Print the resulting table
print("Kendall's Tau for DD, HD, D, and HK")
print(tabulate(result_df, headings, tablefmt='fancy_grid'))