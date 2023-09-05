import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('dspenjualan.csv')

def main():
    st.title('Aplikasi Sederhana menggunakan Streamlit')

    # Teks input dari pengguna
    object = 'MOTOR BEKAS','MOTOR BARU'
    object1 = st.selectbox('Pilih Object', object)


    # Pilihan dropdown
    list = 'YAMAHA','HONDA','KAWASAKI'
    merk = st.selectbox('Pilih Merk', list)
    listken = 'ABSOLUTE REVO','ADDRESS FI 110 R','ADV 150 ABS','ADV 150 CBS','AEROX 155 GP','AEROX 155 VVA','ALL NEW BYSON F1','ALL NEW NMAX 155','ALL NEW NMAX 155 ABS','ALL NEW R15 155 VVA', 'ALL NEW SOUL GT 125','ALL NEW VIXION','ALL NEW X-RIDE 125','ALL NEW XSR 155','ALL NEW NMAX 155C CON','ALN R15 CONNECTED','ALN VARIO 160 ABS','ALN VARIO 160 CBS','BAJAJ PULSAR 200NS','BEAT CBS FI','BEAT CW/FI','BEAT ESP CBS ISS DLX','BEAT FI CBS ESP PLUS','BEAT FI CBS ISS','BEAT FI CBS ISS PLUS','BEAT FI POP CBS ISS','BEAT FI POP CW/ESP','BEAT FI SPORTY CBS','BEAT FI SPORTY CW','BEAT FISPORTY CBSISS','BEAT FISPORTY CW ESP','BEAT FISPORTY CWPLUS','BYSON','CALLISTO 110','CB 150 R','CB 150 R STREETFIRE','CB 150 X','CB VERZA 150','CB150R MMC SE','CBR 150 R','CBR 150 REPSOL','CBR 250 RR','CRF 150 L','CROSS X 150','D TRACKER 150'
    kendaraan = st.selectbox('Pilih kendaraan', listken)
    #listdep = '','','','','','',''
    listten = 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37

    
    dp = st.selectbox('Pilih tenor',listten)
    #values = st.slider( 'Select a range of values', 0,100000,10000000,100000)

    #st.write('Values:', values)

    # Tombol untuk menampilkan output
    if st.button('Tampilkan Output'):
         # st.write(f"Halo Jenis Kendaraan anda , {object1}! Usia Anda adalah {merk} tahun.")
         # Define threshold value

# Note: == is equal, could be change with less (<), more (>), less than (<=), more than (>=)
        X = df[(df['OBJECT'] == object1) & (df['MERK'] == merk) & (df['JENIS'] == kendaraan) & (df['TENOR'] == dp)  ]
        st.write(X)
        

if __name__ == '__main__':
    main()
