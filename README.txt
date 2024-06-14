# MyPetStore Data Analysis Project

This project analyzes data from a pet store, performing various calculations and visualizations.

## Files

- `main.py`: The main script to run the project.
- `pet_analysis.py`: A module containing functions for data analysis and visualization.
- `pets.csv`: The dataset containing pet information.

## How to Run

1. Ensure you have Python installed on your machine.
2. Install the required libraries by running:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the main script:
    ```sh
    python main.py
    ```

## Functions

### pet_analysis.py

- `load_data(file_path)`: Loads the CSV file into a DataFrame.
- `clean_data(df)`: Cleans the DataFrame by handling missing values and ensuring appropriate data types.
- `calculate_average_price(df, species)`: Calculates the average price of pets in a specified species.
- `find_pets_with_feature(df, feature)`: Finds pets with a specific special feature.
- `get_species_statistics(df)`: Returns statistics (average price and age) for each species.
- `plot_price_distribution(df)`: Plots the distribution of pet prices.
- `plot_average_price_by_species(df)`: Plots the average price by species.
- `plot_price_vs_age(df)`: Plots price vs. age of pets.
- `plot_age_distribution_by_species(df)`: Plots the age distribution by species.

### main.py

- Loads and cleans the pet data.
- Performs various analyses and prints the results.
- Generates and saves plots.
