import streamlit as st
import folium as folium 
import pandas as pd
from streamlit_folium import st_folium

from folium import IFrame
import numpy as np


st.set_page_config(layout="wide")

st.write('''<br><br><br><center><font color = "#0000ff" size = 7>Penelusuran Literatur tentang "Aplikasi Partial Least Squares Structural Equation Modeling (PLS-SEM) untuk Kinerja Keuangan atau Kinerja Perusahaan" </font></center>



             ''', unsafe_allow_html = True)


col1, col2, col3 = st.columns([4, 4, 4])
with col1:
    tinggi_peta = st.slider(label = 'Atur Ketinggian ada Peta:', min_value = 100, max_value = 1500, value = 500)


col4, col5, col6, col7, col8, col9 = st.columns([1, 3, 2, 2, 2, 2])
with col4:
    form = st.form(key='my-form')
    submit = form.form_submit_button('Update Peta')

if submit:
    st.write(tinggi_peta)
    m = folium.Map(location = [-0.789275, 113.921327],
               zoom_start = 5,
              )
    st_folium(m, width = "100%", height = tinggi_peta, returned_objects=[])

    












st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")






st.markdown(
    """<center><img src="https://statkomat.com/gambar/ugi.png" width="500"></center>
    <h2 style='text-align: justify; color: blue;'><center>Prana Ugiana Gio, Founder of <a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'>STATCAL</a></center></h2>""",
    unsafe_allow_html=True)




col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 2, 2, 2, 2])
with col1:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/logo_figshare2.png" width="50"><br><a href = 'https://figshare.com/authors/prana_ugiana_gio/17826386' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>FIGSHARE</b></font></center></a>""",unsafe_allow_html=True)
with col2:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/statkomat.gif" width="50"><br><a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STATKOMAT</b></font></center></a>""",unsafe_allow_html=True)
with col3:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/youtube.png" width="50"><br><a href = 'https://www.youtube.com/@STATKOMAT/videos' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>YOUTUBE</b></font></center></a>""",unsafe_allow_html=True)
with col4:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/literature-review.gif" width="50"><br><a href = 'https://literaturereview.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>LITERATURE REVIEW</b></font></center></a>""",unsafe_allow_html=True)
with col5:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/list-papers.gif" width="50"><br><a href = 'https://daftar-paper.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>LIST OF JOURNALS</b></font></center></a>""",unsafe_allow_html=True)
with col6:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/my-papers.gif" width="50"><br><a href = 'https://ugi-publikasi.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>MY PAPERS</b></font></center></a>""",unsafe_allow_html=True)

st.markdown("")
st.markdown("")

col7, col8, col9, col10, col11, col12 = st.columns([2, 2, 2, 2, 2, 2])
with col7:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/pls-sem.gif" width="50"><br><a href = 'https://aplikasi-plssem.streamlit.app//' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STRUCTURAL EQUATION MODELING (PLS-SEM)</b></font></center></a>""",unsafe_allow_html=True)
with col8:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/statcal.gif" width="50"><br><a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STATCAL</b></font></center></a>""",unsafe_allow_html=True)
with col9:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/shiny.gif" width="50"><br><a href = 'https://share-your-shiny-app.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>SHINY</b></font></center></a>""",unsafe_allow_html=True)
with col10:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/ugi-gio.gif" width="50"><br><a href = 'https://ugi-gio.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>UGI</b></font></center></a>""",unsafe_allow_html=True)
with col11:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/indcomp.gif" width="50"><br><a href = 'https://indcomp-stats.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>INDCOMP</b></font></center></a>""",unsafe_allow_html=True)
with col12:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/github.png" width="50"><br><a href = 'https://github.com/gioprana89' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>GITHUB</b></font></center></a>""",unsafe_allow_html=True)






















st.markdown("")
st.markdown("")

col13, col14, col15, col16, col17, col18 = st.columns([2, 2, 2, 2, 2, 2])
with col13:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/cfa.gif" width="50"><br><a href = 'https://cfa-aplikasi.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>CONFIRMATORY FACTOR ANALYSIS (CFA)</b></font></center></a>""",unsafe_allow_html=True)
with col14:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/pls-sem-kinerja-keuangan.gif" width="50"><br><a href = 'https://pls-sem-kinerja-keuangan.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>APLIKASI PLS-SEM PADA KINERJA KEUANGAN</b></font></center></a>""",unsafe_allow_html=True)































st.markdown("")
st.markdown("")

st.markdown("""<a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><center><img src="https://statkomat.com/streamlit-ugi/kopi.gif" width="150"></center></a><br><center><b><a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><font color = 'orange' size = 7>Buy Me a Cup of Coffee</font></a></b></font></center>""",unsafe_allow_html=True)












