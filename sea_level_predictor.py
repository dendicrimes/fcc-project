import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # 1. Импорт данных
    url = 'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/main/epa-sea-level.csv'
    df = pd.read_csv(url)

    # 2. Создаем scatter plot (точечный график)
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10, label='Original Data')

    # 3. Первая линия наилучшего соответствия (все данные)
    # Получаем наклон и перехват
    reg1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Создаем массив лет до 2050 года
    years_extended = np.arange(df['Year'].min(), 2051)
    # Формула прямой: y = mx + b
    line1 = reg1.slope * years_extended + reg1.intercept
    plt.plot(years_extended, line1, 'r', label='Best Fit Line 1 (1880-2050)')

    # 4. Вторая линия наилучшего соответствия (с 2000 года)
    df_recent = df[df['Year'] >= 2000]
    reg2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    years_recent = np.arange(2000, 2051)
    line2 = reg2.slope * years_recent + reg2.intercept
    plt.plot(years_recent, line2, 'green', label='Best Fit Line 2 (2000-2050)')

    # 5. Оформление графика
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # 6. Сохранение
    plt.savefig('sea_level_plot.png')
    return plt.gca()
