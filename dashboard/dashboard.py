# Proyek Analisis Data: Bike Data Sharing Dataset
# - **Nama:** Muhamad Aditya Yusuf Jatikusumo
# - **Email:** yusufjana18@gmail.com
# - **ID Dicoding:** muhamad_adityayusuf

# Import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mengambil data dari file csv
df = pd.read_csv('main.csv')

# Init streamlit app
st.title('Dashboard Analisis Data Bike Sharing')

# Menampilkan data
with st.sidebar:
    st.title("Bike Sharing Data")   


menu = st.sidebar.radio(
    'Menu',
    ['Data Overview', 'Apakah musim mempengaruhi jumlah peminjaman sepeda?', 'Bagaimana kinerja peminjaman sepeda per bulan?']
)

# Data overview
if menu == 'Data Overview':
    st.write('Data Overview')
    st.write('Data yang digunakan adalah data penyewaan sepeda dari tahun 2011 hingga 2012.')
    st.write('Data yang ditampilkan:')
    row = st.slider('Jumlah Baris', 1, 100, 10)
    st.write('Ukuran Tabel:')
    width = st.slider('Lebar', 100, 1000, 300)
    height = st.slider('Tinggi', 100, 1000, 300)
    st.dataframe(df.head(row), width, height)

# Apakah musim mempengaruhi jumlah peminjaman sepeda?
if menu == 'Apakah musim mempengaruhi jumlah peminjaman sepeda?':
    st.write('Apakah musim mempengaruhi jumlah peminjaman sepeda?')
    st.write('Jawab: Ya, musim mempengaruhi jumlah peminjaman sepeda. Pada musim semi dan musim panas, jumlah peminjaman sepeda lebih tinggi dibandingkan musim gugur dan musim dingin.')

    # Visualisasi data
    season = df.groupby('season')[['total_count']].sum().reset_index()
    fig, ax = plt.subplots()
    ax.set_title('Perbandingan Jumlah Penyewa Sepeda Setiap Tahun Berdasarkan Musim')
    sns.set_palette('pastel')
    sns.set_style('whitegrid')
    sns.barplot(data=season, x='season', y='total_count', ax=ax)
    st.pyplot(fig)

    # Conclusion
    st.write("<h2> Conlusion: </h2>", unsafe_allow_html=True)
    st.write("""
                Berdasarkan bar chart Perbandingan Jumlah Penyewa Sepeda Setiap Tahun Berdasarkan Musim, pada tahun 2011 jumlah penyewa terbesar terjadi pada musim fall dengan jumlah penyewanya sebanyak 419,650, sedangkan jumlah penyewa terkecil terjadi pada musim Springer dengan jumlah penyewanya sebanyak 150,000. 
                Lalu, pada tahun 2012 jumlah penyewa terbesar juga terjadi pada musim fall dan jumlah penyewa terkecil terjadi pada musim Spring. 
                Dari bar chart tersebut, kita juga bisa melihat bahwa jumlah penyewa sepeda dari tahun 2011 ke tahun 2012 mengalami kenaikan yang cukup signifikan di semua musim.
            """)
    st.write("<h2> Recommendation: </h2>", unsafe_allow_html=True)
    st.write("""
                Dari data tersebut, kita bisa melihat bahwa musim fall merupakan musim yang paling banyak diminati oleh penyewa sepeda. 
                Maka dari itu, kita bisa menambahkan sepeda lebih banyak lagi pada musim fall agar bisa memenuhi kebutuhan penyewa sepeda. 
                Selain itu, kita juga bisa melakukan promosi lebih banyak lagi pada musim fall agar bisa menarik lebih banyak penyewa sepeda.
            """)

# Bagaimana kinerja peminjaman sepeda per bulan?
if menu == 'Bagaimana kinerja peminjaman sepeda per bulan?':
    st.write('Bagaimana kinerja peminjaman sepeda per bulan?')
    st.write('Jawab: Pada bulan Juni, Juli, dan Agustus, jumlah peminjaman sepeda lebih tinggi dibandingkan bulan-bulan lainnya.')

    # Visualisasi data
    bike_sharing = df.groupby('month')[['total_count']].sum().reset_index()
    fig, ax = plt.subplots()
    ax.set_title('Perbandingan Jumlah Penyewa Sepeda Setiap Tahun Berdasarkan Bulan')
    sns.color_palette("rocket", as_cmap=True)
    sns.set_style('whitegrid')
    sns.barplot(data=bike_sharing, x='month', y='total_count', ax=ax)
    st.pyplot(fig)

    # Conclusion
    st.write("<h2> Conlusion: </h2>", unsafe_allow_html=True)
    st.write("""
                Berdasarkan bar chart Perbandingan Jumlah Penyewa Sepeda Setiap Tahun Berdasarkan Bulan, pada tahun 2011 jumlah penyewa terbesar terjadi pada bulan September dengan jumlah penyewanya sebanyak 489,516, sedangkan jumlah penyewa terkecil terjadi pada bulan January dengan jumlah penyewanya sebanyak 134,933. 
                Lalu, pada tahun 2012 jumlah penyewa terbesar juga terjadi pada bulan September dan jumlah penyewa terkecil terjadi pada bulan January. 
                Dari bar chart tersebut, kita juga bisa melihat bahwa jumlah penyewa sepeda dari tahun 2011 ke tahun 2012 mengalami kenaikan yang cukup signifikan di semua bulan.
            """)
    st.write("<h2> Recommendation: </h2>", unsafe_allow_html=True)
    st.write("""
                Dari data tersebut, kita bisa melihat bahwa bulan September merupakan bulan yang paling banyak diminati oleh penyewa sepeda. 
                Maka dari itu, kita bisa menambahkan sepeda lebih banyak lagi pada bulan September agar bisa memenuhi kebutuhan penyewa sepeda. 
                Selain itu, kita juga bisa melakukan promosi lebih banyak lagi pada bulan September agar bisa menarik lebih banyak penyewa sepeda.
            """)
