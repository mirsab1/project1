import pet_analysis as pa

# Load and clean data
df = pa.load_data('pets.csv')
df = pa.clean_data(df)

# Perform calculations
average_price_dog = pa.calculate_average_price(df, 'Dog')
print(f'Average price of dogs: {average_price_dog:.2f}')

pets_with_feature = pa.find_pets_with_feature(df, 'Foxhound')
print(f'Pets with the specified feature: {pets_with_feature}')

species_stats = pa.get_species_statistics(df)
print(f'Species statistics:')
for species, stats in species_stats.items():
    print(f'{species}: Average Price - {stats["Average Price"]:.2f}, Average Age - {stats["Average Age"]:.2f} years')

# Create visualizations
pa.plot_price_distribution(df)
pa.plot_average_price_by_species(df)
pa.plot_price_vs_age(df)
pa.plot_age_distribution_by_species(df)
