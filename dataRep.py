import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv', sep=';')

def display_textual_analysis(option):
    """Function to display textual summaries based on user choice."""
    if option == 1:
        print("\nAge Distribution Analysis:")
        print(f"The average age of bank customers is {df['age'].mean():.2f} years.")
        print(f"Minimum age: {df['age'].min()}, Maximum age: {df['age'].max()}.\n")
    elif option == 2:
        print("\nJob Type Distribution Analysis:")
        print(df['job'].value_counts().to_string())
        print("\nThis shows the count of customers per job type.\n")
    elif option == 3:
        print("\nBalance by Marital Status Analysis:")
        print(df.groupby('marital')['balance'].mean().to_string())
        print("\nThis shows the average balance of customers based on their marital status.\n")
    elif option == 4:
        print("\nCampaign Success Rate Analysis:")
        print(df['y'].value_counts().to_string())
        print("\nThis shows the number of successful and unsuccessful campaign outcomes.\n")

def display_visual_analysis(option):
    """Function to display visualizations based on user choice."""
    if option == 1:
        # Histogram of Age Distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(df['age'], bins=20, color='blue', kde=True)
        plt.title('Age Distribution of Bank Customers')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.show()
        
    elif option == 2:
        # Bar Plot representing Job Type Distribution
        plt.figure(figsize=(12, 6))
        sns.countplot(x='job', data=df, palette='viridis')
        plt.title('Job Type Distribution')
        plt.xlabel('Job Type')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.show()

    elif option == 3:
        # Box Plot representing Balance by Marital Status
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='marital', y='balance', data=df, palette='pastel')
        plt.title('Customer Balance by Marital Status')
        plt.xlabel('Marital Status')
        plt.ylabel('Balance')
        plt.show()

    elif option == 4:
        # Represetnation for Campaign Success Rate ('y' column)
        plt.figure(figsize=(6, 6))
        sns.countplot(x='y', data=df, palette='coolwarm')
        plt.title('Campaign Success Rate')
        plt.xlabel('Campaign Outcome')
        plt.ylabel('Count')
        plt.show()

def main_menu():
    """Main menu to choose between different options."""
    while True:
        print("\nMenu:")
        print("1. Age Distribution Analysis")
        print("2. Job Type Distribution Analysis")
        print("3. Balance by Marital Status Analysis")
        print("4. Campaign Success Rate Analysis")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice in ['1', '2', '3', '4']:
            analysis_type = input("Choose Analysis Type - Textual (T) or Visual (V): ").upper()
            if analysis_type == 'T':
                display_textual_analysis(int(choice))
            elif analysis_type == 'V':
                display_visual_analysis(int(choice))
            else:
                print("Invalid analysis type. Please choose 'T' or 'V'.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main_menu()
