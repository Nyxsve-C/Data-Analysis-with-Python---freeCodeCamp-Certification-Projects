# [Demographic Data Analyzer](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer)

You will be [working on this project with our Gitpod starter code](https://gitpod.io/?autostart=true#https://github.com/freeCodeCamp/boilerplate-demographic-data-analyzer/).

We are still developing the interactive instructional part of the Python curriculum. For now, here are some videos on the freeCodeCamp.org YouTube channel that will teach you everything you need to know to complete this project:

* [Python for Everybody Video Course](https://www.freecodecamp.org/news/python-for-everybody/) (14 hours)
* [How to Analyze Data with Python Pandas](https://www.freecodecamp.org/news/how-to-analyze-data-with-python-pandas/) (10 hours)

In this challenge you must analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database. Here is a sample of what the data looks like:

|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |

You must use Pandas to answer the following questions:

* How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (`race` column)
* What is the average age of men?
* What is the percentage of people who have a Bachelor's degree?
* What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
* What percentage of people without advanced education make more than 50K?
* What is the minimum number of hours a person works per week?
* What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
* What country has the highest percentage of people that earn >50K and what is that percentage?
* Identify the most popular occupation for those who earn >50K in India.

Use the starter code in the file `demographic_data_analyzer.py`. Update the code so all variables set to `None` are set to the appropriate calculation or code. Round all decimals to the nearest tenth.

## Development
Write your code in `demographic_data_analyzer.py`. For development, you can use `main.py` to test your code.

## Testing
The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience.

## Submitting
Copy your project's URL and submit it to freeCodeCamp.

## Dataset Source
Dua, D. and Graff, C. (2019). [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml). Irvine, CA: University of California, School of Information and Computer Science.

# Code
```python
import pandas as pd


def calculate_demographic_data(print_data=True):

    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()
    # df.groupby(['race'], sort=False)['race'].count()

    average_age_men = (df[df['sex'] == 'Male']['age'].mean()).round(1)

    percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100).round(1)

    higher_education_mask = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    rich_mask = df['salary'] == '>50K'

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education_rich = (df[(higher_education_mask) & (rich_mask)].shape[0] / df[higher_education_mask].shape[0] * 100).round(1)
    # What percentage of people without advanced education make more than 50K?
    lower_education_rich = (df[(~higher_education_mask) & (rich_mask), 'education'].shape[0] / df[~higher_education_mask].shape[0] * 100).round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    min_hours_mask = df['hours-per-week'] == min_work_hours

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich_percentage = df[(min_hours_mask) & (rich_mask)].shape[0] / df[min_hours_mask].shape[0] * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df[rich_mask]['native-country'].value_counts() / df['native-country'].value_counts() * 100).round(1).sort_values(ascending=False).index[0]
    highest_earning_country_percentage = (df[rich_mask]['native-country'].value_counts() / df['native-country'].value_counts() * 100).round(1).max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (df.loc[(rich_mask) & (df['native-country'] == 'India'), 'occupation']).value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
```

## Test Result Screenshot
![Test result screenshot](https://github.com/user-attachments/assets/9745975a-bd3e-49e3-8b40-2858cba1584b)
