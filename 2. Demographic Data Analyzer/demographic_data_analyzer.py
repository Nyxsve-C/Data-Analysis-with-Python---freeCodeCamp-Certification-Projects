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