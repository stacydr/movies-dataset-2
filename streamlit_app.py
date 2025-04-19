
import altair as alt
import pandas as pd
import streamlit as st
import streamlit as st
import pandas as pd
# Google Sheets URL
SHEET_ID = "1pjBBicoDfechmzgbQecFGCvEgnIN3yHSaEoLzYungug"
SHEET_NAME = "Лист1"  # или имя вашего листа
URL = f"https://docs.google.com/spreadsheets/d/e/2PACX-1vTxrNdMwRnWz4lu_YYK85LpRAPEgn0Sd_VsXHeg0la0MZl60CpMsJLf7k0XlwbwQdmic7m8e8egHouu/pub?gid=0&single=true&output=csv"
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df
try:
    df = load_data(URL)
    st.title("Книги по культуре Востока: Китай, Корея, Япония")
    st.dataframe(df)
    # Дополнительные элементы интерфейса (например, фильтры) можно добавить здесь
    st.subheader("Фильтрация по стране")
    country_filter = st.multiselect("Выберите страну", df['Страна'].unique())
    if country_filter:
        filtered_df = df[df['Страна'].isin(country_filter)]
        st.dataframe(filtered_df)
except Exception as e:
    st.error(f"Ошибка при загрузке данных: {e}")
    st.info("Убедитесь, что доступ к Google Sheets открыт для всех, у кого есть ссылка (File -> Share -> Publish to web).")
