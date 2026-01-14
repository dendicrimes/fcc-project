import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Импорт данных
# Используем прямую ссылку, чтобы не мучиться с загрузкой файла
url = 'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/main/medical_examination.csv'
df = pd.read_csv(url)

# 2. Добавляем колонку 'overweight' (избыточный вес)
# BMI = weight / (height/100)^2. Если > 25, то 1, иначе 0.
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Нормализация данных
# 0 - хорошо, 1 - плохо. Если cholesterol/gluc > 1, ставим 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Функция для отрисовки категориального графика
def draw_cat_plot():
    # 5. Создаем DataFrame для графика через pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Группируем данные для подсчета
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7. Рисуем график с помощью sns.catplot
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig

    # 10. Сохраняем
    fig.savefig('catplot.png')
    return fig

# 11. Функция для отрисовки тепловой карты (Heat Map)
def draw_heat_map():
    # 12. Очистка данных
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 13. Матрица корреляции
    corr = df_heat.corr()

    # 14. Маска для верхнего треугольника (чтобы скрыть дубликаты)
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 15. Настройка фигуры matplotlib
    fig, ax = plt.subplots(figsize=(12, 12))

    # 16. Рисуем тепловую карту
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, square=True, linewidths=.5, cbar_kws={'shrink': .5})

    # 19. Сохраняем
    fig.savefig('heatmap.png')
    return fig
