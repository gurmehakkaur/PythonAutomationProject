import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print('\n\n\n*******Data Representation Updating********\n\n')

# Adjust the separator based on your CSV file format
df = pd.read_csv('data.csv', sep=';')  # Use ',' or ';' based on your actual data

# Create a folder for saving graphs and text files
output_folder = 'analysis_results'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Textual analysis
text_analysis = []

# Age Distribution Analysis (Textual)
text_analysis.append("Age Distribution Analysis:")
text_analysis.append(f"The average age of bank customers is {df['age'].mean():.2f} years.")
text_analysis.append(f"Minimum age: {df['age'].min()}, Maximum age: {df['age'].max()}.\n")

# Job Type Distribution Analysis (Textual)
text_analysis.append("Job Type Distribution Analysis:")
text_analysis.append(df['job'].value_counts().to_string())
text_analysis.append("\nThis shows the count of customers per job type.\n")

# Balance by Marital Status Analysis (Textual)
text_analysis.append("Balance by Marital Status Analysis:")
text_analysis.append(df.groupby('marital')['balance'].mean().to_string())
text_analysis.append("\nThis shows the average balance of customers based on their marital status.\n")

# Campaign Success Rate Analysis (Textual)
text_analysis.append("Campaign Success Rate Analysis:")
text_analysis.append(df['y'].value_counts().to_string())
text_analysis.append("\nThis shows the number of successful and unsuccessful campaign outcomes.\n")

# Save textual analysis to a text file
with open(os.path.join(output_folder, 'textual_analysis.txt'), 'w') as file:
    file.write("\n".join(text_analysis))

# Visual Analysis

# 1. Histogram of Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=20, color='blue', kde=True)
plt.title('Age Distribution of Bank Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig(os.path.join(output_folder, 'age_distribution.png'))
plt.close()

# 2. Bar Plot representing Job Type Distribution
plt.figure(figsize=(12, 6))
sns.countplot(x='job', data=df, palette='viridis')
plt.title('Job Type Distribution')
plt.xlabel('Job Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.savefig(os.path.join(output_folder, 'job_type_distribution.png'))
plt.close()

# 3. Box Plot representing Balance by Marital Status
plt.figure(figsize=(10, 6))
sns.boxplot(x='marital', y='balance', data=df, palette='pastel')
plt.title('Customer Balance by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Balance')
plt.savefig(os.path.join(output_folder, 'balance_by_marital_status.png'))
plt.close()

# 4. Representation for Campaign Success Rate ('y' column)
plt.figure(figsize=(6, 6))
sns.countplot(x='y', data=df, palette='coolwarm')
plt.title('Campaign Success Rate')
plt.xlabel('Campaign Outcome')
plt.ylabel('Count')
plt.savefig(os.path.join(output_folder, 'campaign_success_rate.png'))
plt.close()

print(f"All analysis has been saved in the '{output_folder}' folder.")
