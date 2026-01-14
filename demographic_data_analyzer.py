import pandas as pd

def calculate_demographic_data(print_data=True):
    # Чтение данных
    df = pd.read_csv('adult.data.csv')

    # 1. Расы
    race_count = df['race'].value_counts()

    # 2. Средний возраст мужчин
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Процент бакалавров
    percentage_bachelors = round(len(df[df['education'] == 'Bachelors']) / len(df) * 100, 1)

    # 4. Образование и зарплата
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education) * 100, 1)
    lower_education_rich = round(len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education) * 100, 1)

    # 6. Мин. часы
    min_work_hours = df['hours-per-week'].min()

    # 7. Процент богатых при мин. часах
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers) * 100, 1)

    # 8. Страна с макс. процентом богатых
    country_stats = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)

    # 9. Профессия в Индии
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

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
