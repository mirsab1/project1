import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Task 1a: Load the CSV file into a DataFrame
def load_data(file_path):
    return pd.read_csv(file_path)

# Task 1b: Clean the data
def clean_data(df):
    # Check for missing values and handle them (e.g., fill or drop)
    df = df.dropna()
    
    # Ensure appropriate data types
    df['PetID'] = df['PetID'].astype(str)
    df['Name'] = df['Name'].astype(str)
    df['Birthdate'] = pd.to_datetime(df['Birthdate'], format='%m/%d/%Y')
    df['Price'] = df['Price'].astype(float)
    df['Species'] = df['Species'].astype(str)
    df['SpecialFeatures'] = df['SpecialFeatures'].astype(str)
    
    return df

# Task 2a: Calculate the average price of pets in a specified species
def calculate_average_price(df, species):
    species_df = df[df['Species'] == species]
    return species_df['Price'].mean()

# Task 2b: Find pets with a specific special feature
def find_pets_with_feature(df, feature):
    return df[df['SpecialFeatures'] == feature]['Name'].tolist()

# Task 3a: Get species statistics
def get_species_statistics(df):
    stats = {}
    species_groups = df.groupby('Species')
    
    for species, group in species_groups:
        avg_price = group['Price'].mean()
        avg_age = (pd.Timestamp.now() - group['Birthdate']).mean().days / 365.25
        stats[species] = {'Average Price': avg_price, 'Average Age': avg_age}
    
    return stats

# Task 4a: Plot price distribution
def plot_price_distribution(df):
    plt.hist(df['Price'], bins=20, edgecolor='k')
    plt.title('Price Distribution')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.savefig('price_distribution.png')
    plt.show()

# Task 4c: Plot average price by species
def plot_average_price_by_species(df):
    species_avg_price = df.groupby('Species')['Price'].mean()
    species_avg_price.plot(kind='bar', color='skyblue')
    plt.title('Average Price by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Price')
    plt.savefig('average_price_by_species.png')
    plt.show()

# Task 5a: Plot price vs. age
def plot_price_vs_age(df):
    df['Age'] = (pd.Timestamp.now() - df['Birthdate']).dt.days / 365.25
    sns.scatterplot(data=df, x='Age', y='Price')
    plt.title('Price vs. Age')
    plt.xlabel('Age (years)')
    plt.ylabel('Price')
    plt.savefig('price_vs_age.png')
    plt.show()

# Task 5d: Plot age distribution by species
def plot_age_distribution_by_species(df):
    df['Age'] = (pd.Timestamp.now() - df['Birthdate']).dt.days / 365.25
    fig = px.box(df, x='Species', y='Age', title='Age Distribution by Species')
    fig.write_image('age_distribution_by_species.png')
    fig.show()
