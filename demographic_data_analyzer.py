import pandas as pd

def calculate_demographic_data(print_data=True):
    # Читаем данные напрямую по ссылке, чтобы тесты сошлись на 100%
    url = 'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/main/adult.data.csv'
    df = pd.read_csv(url)

    # 1. Сколько людей каждой расы?
    race_count = df['race'].value_counts()

    # 2. Средний возраст мужчин
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Процент людей с образованием Bachelors
    percentage_bachelors = round(len(df[df['education'] == 'Bachelors']) / len(df) * 100, 1)

    # 4. Процент людей с высшим образованием (Bachelors, Masters, Doctorate) с доходом >50K
    # 5. Процент людей без высшего образования с доходом >50K
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education) * 100, 1)
    lower_education_rich = round(len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education) * 100, 1)

    # 6. Минимальное количество рабочих часов в неделю
    min_work_hours = df['hours-per-week'].min()

    # 7. Процент людей, работающих мин. часы и имеющих зарплату >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers) * 100, 1)

    # 8. Страна с самым высоким процентом богатых (>50K)
    # Считаем процент богатых для каждой страны
    rich_per_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100)
    highest_earning_country = rich_per_country.idxmax()
    highest_earning_country_percentage = round(rich_per_country.max(), 1)

    # 9. Самая популярная профессия для тех, кто зарабатывает >50K в Индии
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
