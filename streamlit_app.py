
import altair as alt
import pandas as pd
import streamlit as st

# Google Sheets URL
SHEET_ID = "1pjBBicoDfechmzgbQecFGCvEgnIN3yHSaEoLzYungug"
SHEET_NAME = "Лист1"
URL = f"https://docs.google.com/spreadsheets/d/e/2PACX-1vTxrNdMwRnWz4lu_YYK85LpRAPEgn0Sd_VsXHeg0la0MZl60CpMsJLf7k0XlwbwQdmic7m8e8egHouu/pub?gid=0&single=true&output=csv"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

try:
    df = load_data(URL)
    st.title("Книги по культуре Востока: Китай, Корея, Япония")

    st.dataframe(df)

    # Фильтр по стране
    st.subheader("Фильтрация по стране")
    country_filter = st.multiselect("Выберите страну", df['Страна'].unique())
    if country_filter:
        filtered_df = df[df['Страна'].isin(country_filter)]
    else:
        filtered_df = df

    st.dataframe(filtered_df)

    # График 1: Количество книг по годам выпуска
    st.subheader("Количество книг, выпущенных в определённый год")
    if 'Год' in filtered_df.columns:
        year_counts = filtered_df.groupby('Год').size().reset_index(name='Количество книг')
        chart_year = alt.Chart(year_counts).mark_bar().encode(
            x=alt.X('Год:O', title='Год выпуска'),
            y=alt.Y('Количество книг:Q', title='Количество книг'),
            tooltip=['Год', 'Количество книг'],
            color=alt.Color('Год:O', legend=None)
        ).properties(
            width=700,
            height=400
        )
        st.altair_chart(chart_year)
    else:
        st.info("В данных отсутствует столбец 'Год' для построения графика по годам.")

    # График 2: Количество книг по странам
    st.subheader("Количество книг по странам")
    country_counts = filtered_df.groupby('Страна').size().reset_index(name='Количество книг')
    chart_country = alt.Chart(country_counts).mark_bar().encode(
        x=alt.X('Страна:N', sort='-y', title='Страна'),
        y=alt.Y('Количество книг:Q', title='Количество книг'),
        tooltip=['Страна', 'Количество книг'],
        color=alt.Color('Страна:N', legend=None)
    ).properties(
        width=700,
        height=400
    )
    st.altair_chart(chart_country)

except Exception as e:
    st.error(f"Ошибка при загрузке данных: {e}")
    st.info("Убедитесь, что доступ к Google Sheets открыт для всех, у кого есть ссылка (File -> Share -> Publish to web).")

