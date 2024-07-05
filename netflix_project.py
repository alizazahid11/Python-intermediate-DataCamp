# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
year = netflix_df.loc[:, 'release_year']

# Filter the DataFrame for years between 1990 and 1999
filtered_years = netflix_df[(year >= 1990) & (year <= 1999)]
print(filtered_years)

dur = filtered_years.loc[:, 'duration']
val=dur.value_counts()
duration=dur.mode().iloc[0]

genre=netflix_df['genre']
dr=filtered_years['duration']<90
short_movies = filtered_years[(filtered_years['genre'] == 'Action') & dr]
short_movie_count=short_movies.shape[0]