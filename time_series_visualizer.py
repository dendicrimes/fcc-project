import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 1. Загрузка и подготовка данных
url = 'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/main/fcc-forum-pageviews.csv'
df = pd.read_csv(url, parse_dates=['date'], index_col='date')

# 2. Очистка данных (удаляем топ 2.5% и нижние 2.5%)
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # Создаем копию
    df_line = df.copy()
    
    # Рисуем линейный график
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_line.index, df_line['value'], color='red', linewidth=1)
    
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Сохраняем
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Подготовка данных для бара
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    # Группируем по году и месяцу, считаем среднее
    df_pivot = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Сортируем месяцы правильно
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_pivot = df_pivot[months]

    # Рисуем
    fig = df_pivot.plot(kind='bar', figsize=(10, 8), xlabel='Years', ylabel='Average Page Views').get_figure()
    plt.legend(title='Months')

    # Сохраняем
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Подготовка данных для Box Plot
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Рисуем два графика рядом
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

    # Годовой (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    # Месячный (Seasonality)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2, order=month_order)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Сохраняем
    fig.savefig('box_plot.png')
    return fig
