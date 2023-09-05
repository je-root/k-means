# clusters_page.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def main():
    # Load your dataset
    df = pd.read_csv('final.csv')
    df = df.drop(['KECAMATAN','KABUPATEN','NO'], axis=1)
    
    X = df.iloc[:, 0:7].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.subheader("Nilai Jumlah K")
    clust = st.slider("Pilih Jumlah Cluster: ", 2, 10, 3, 1)

    def k_means(n_clust):
        kmeans = KMeans(n_clusters=n_clust, init='k-means++', random_state=42)
        y_kmeans = kmeans.fit_predict(X)
        df['f_cluster'] = y_kmeans + 1
        
        # Your clustering visualization code here
        # ...
        
    k_means(clust)
