import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def run():
    '''Membuat tampilan yang menampilkan grafik hasil Exploratory Data Analysis'''
    
    # Menambahkan tampilan title
    st.title('Telecom Customer Churn Dataset')

    # Load data
    st.header('Data Loading')
    df = pd.read_csv("C:/Users/Dionisius/Documents/GitHub/p1-ftds025-hck-m2-ray-dion/customer_churn_telecom_services.csv")
    st.write('Link dataset: https://www.kaggle.com/datasets/kapturovalexander/customers-churned-in-telecom-services')
    st.dataframe(df)
    st.write('---')
    # Tampilkan hasil EDA
    st.header('Analisis')

    # Menampilkan grafik stacked bar chart untuk layanan tertentu
    placeholder1 = st.empty()
    radio_button = st.selectbox('Pilih Kolom:', ['StreamingTV', 'StreamingMovies', 'OnlineSecurity', 'OnlineBackup', 'TechSupport'])
    placeholder1.subheader(f'Bagaimana Distribusi Churn Terhadap Layanan {radio_button}?')

    # Hitung jumlah churn per kategori layanan
    churn_counts = df.groupby([radio_button, 'Churn']).size().unstack()

    # Hitung persentase churn
    churn_counts = churn_counts.div(churn_counts.sum(axis=1), axis=0) * 100  
    churn_counts = churn_counts.reset_index()

    # Buat grafik Stacked Bar Chart
    fig = px.bar(churn_counts, 
                x=radio_button, 
                y=['No', 'Yes'], 
                text_auto=True, 
                labels={"value": "Persentase (%)", "x": radio_button}, 
                title=f'Persentase Churn Berdasarkan {radio_button}',
                color_discrete_map={"No": "blue", "Yes": "red"})

    fig.update_layout(barmode='stack', yaxis=dict(title="Persentase (%)"))

    # Tampilkan grafik di Streamlit
    st.plotly_chart(fig, use_container_width=True)

    if radio_button in ['OnlineSecurity', 'OnlineBackup', 'TechSupport']:
        st.markdown("""
    **🔍 Insight:**
    - Pelanggan yang memiliki layanan seperti **TechSupport, OnlineBackup, dan OnlineSecurity** lebih jarang melakukan **Churn**.
    - Pelanggan tanpa **Internet Service** juga cenderung tidak churn, kemungkinan karena mereka hanya menggunakan layanan telepon.
    """)
    else:
        st.markdown('''
    **🔍 Insight:**
    - Dari hasil grafik, tidak terlihat ada perbedaan signifikan atas pelanggan yang memiliki Streaming Service dengan yang tidak. 
    - Keputusan churn pelanggan tidak terlalu dipengaruhi oleh layanan Streaming.''')
        
    st.write('---')
    # Menampilkan grafik distribusi metode pembayaran yang Churn
    st.subheader(f'Bagaimana Distribusi Metode Pembayaran Pada Pelanggan yang Churn?')

    # Filter hanya pelanggan yang churn
    df_churn_yes = df[df["Churn"] == "Yes"]

    # Hitung jumlah churn berdasarkan metode pembayaran
    payment_counts = df_churn_yes["PaymentMethod"].value_counts()

    # Buat pie chart menggunakan Matplotlib
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', colors=plt.cm.Set3.colors)
    ax.set_title("Distribusi Metode Pembayaran untuk Pelanggan yang Churn")
    st.pyplot(fig)

    st.markdown("""
    **🔍 Insight:**
    - Berdasarkan hasil visualisasi, pelanggan yang memilih untuk **churn** didominasi oleh mereka yang menggunakan **Electronic Check** sebagai metode pembayaran.
    - Kemungkinan penyebab tingginya churn pada metode ini adalah karena **kurangnya kenyamanan** dalam penggunaan atau adanya **kendala teknis** yang membuat pelanggan tidak ingin bertransaksi lagi.
    """)
    st.write('---')

    # Menampilkan grafik distribusi
    placeholder2 = st.empty()
    radio_button1 = st.selectbox('Pilih Kolom:', ['tenure', 'MonthlyCharges', 'TotalCharges'])
    placeholder2.subheader(f'Bagaimana Distribusi kolom {radio_button1}?')

    # Membuat histogram
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df[radio_button1], kde=True, bins=30, color="skyblue", ax=ax)

    ax.set_title(f"Histogram {radio_button1}", fontsize=14)
    ax.set_xlabel(radio_button1, fontsize=12)
    ax.set_ylabel("Count", fontsize=12)

    # Tampilkan plot di Streamlit
    st.pyplot(fig)
    
    if radio_button1 == 'tenure':
        st.markdown("""
        **🔍 Insight:**
        Pelanggan mayoritas ada pada tenure mendekati 0 bulan atau mendekati 70 bulan. Hal ini menandakan mayoritas pelanggan antara berupa pelanggan baru atau pelanggan yang memang sudah lama menggunakan service Telecom Inc.
        """)
    
    elif radio_button1 == 'MonthlyCharges':
        st.markdown("""
        **🔍 Insight:**
        MonthlyCharges skewed ke arah kanan yang menandakan mayoritas pelangga memiliki biaya bulanan rendah (sekitar 40 kebawah).
        """)
    
    else:
        st.markdown("""
        **🔍 Insight:**
        TotalCharges skewed ke arah kanan juga, hal ini mungkin disebabkan oleh datangnya banyak pelanggan baru.
        """)

    st.write('---')
    st.subheader(f'Bagaimana Distribusi kolom {radio_button1} Terhadap Kolom Churn?')

    # Membuat histogram
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x=df['Churn'], y=df[radio_button1], palette='Spectral', hue=df['Churn'])

    ax.set_title(f"Boxplot {radio_button1} vs Churn", fontsize=14)
    ax.set_xlabel(radio_button1, fontsize=12)
    ax.set_ylabel("Count", fontsize=12)

    # Tampilkan plot di Streamlit
    st.pyplot(fig)

    if radio_button1 == 'tenure':
        st.markdown("""
        **🔍 Insight:**
        Semakin lama jangka tenure, pelanggan jarang churn.
        """)
    
    elif radio_button1 == 'MonthlyCharges':
        st.markdown("""
        **🔍 Insight:**
        Semakin tinggi harga MonthlyCharges, semakin tinggi juga kemungkinan pelanggan Churn.
        """)
    
    else:
        st.markdown("""
        **🔍 Insight:**
        Dari hasil TotalCharges, semakin tinggi semakin rendah kemungkinan mereka churn karena yang memiliki TotalCharges banyak ini adalah pelanggan yang sudah lama menggunaka service sehingga akumulasi TotalCharges juga semakin tinggi.
        """)

    st.write('---')

    # Membuat group bar chart
    placeholder3 = st.empty()
    radio_button2 = st.selectbox('Pilih Kolom:', ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod'])
    placeholder3.subheader(f'Bagaimana Rasio Churn terhadap kolom {radio_button2}?')
    
    # Membuat countplot
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x=df[radio_button2], hue=df["Churn"], ax=ax, palette="coolwarm")

    ax.set_title(f"{radio_button2} vs Churn", fontsize=14)
    ax.set_xlabel(radio_button2, fontsize=12)
    ax.set_ylabel("Count", fontsize=12)
    ax.tick_params(axis='x', rotation=45)

    # Tampilkan plot di Streamlit
    st.pyplot(fig)

    st.markdown("""
    **🔍 Insight:**
    Melihat hasil visualisai, berikut adalah beberapa key findings saya:
    1. Contract yang bertipe Month-to-month menghasilkan churn tertinggi.
    2. Pelanggan yang menggunakan internet service Fiber Optic memiliki churn yang tinggi. Hal ini menandakan mungkin ada masalah pada layanan Fiber Optic
    3. Pada kolom OnlineSecurity, OnlineBackup, DeviceProtection, dan TechSupport pelanggan yang tidak memilih untuk menggunakan layanan ini cenderung lebih memilih untuk churn.
    4. PaymentMethod Electronic Check menghasilkan churn yang jauh lebih tinggi dibanding PaymentMethod lain.
    """)

if __name__== '__main__':
    run()