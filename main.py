import pandas as pd

# Example DataFrame
df = pd.read_csv('merged_file.csv')  # Load your dataset

# Parameters
total_samples = 8000
samples_per_class = total_samples // 8  # You have 8 classes

# Create an empty DataFrame to store the balanced subset
balanced_df = pd.DataFrame()

# Define your classes based on 'age' and 'condition'
age = [23, 27, 53, 63]
case = [0, 1]

# Sample from each combination of age and condition
for person_age in age:
    for condition in case:
        class_subset = df[(df['Age'] == person_age) & (df['status'] == condition)]
        sampled_subset = class_subset.sample(n=samples_per_class, random_state=42)
        balanced_df = pd.concat([balanced_df, sampled_subset], ignore_index=True)

# save dataframe shuffled to csv file
balanced_df = balanced_df.sample(frac=1, random_state=42).reset_index(drop=True)
balanced_df.to_csv('balanced_dataset_m.csv', index=False)
