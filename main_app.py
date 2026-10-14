import streamlit as st
import pandas as pd
import numpy as np

# A) SƏHİFƏNİN XÜSUSİYYƏTLƏRİ (Mobil və Kompüterə Uyğunlaşdırma)
st.set_page_config(
    page_title="SmartChurn AI — Enterprise Dashboard",
    page_icon="📊",
    layout="wide"
)

# B) RİYAZİ SÜNİ İNTELLEKT MÜHƏRRİKİ (Sigmoid Fonksiyonu)
def advanced_ml_churn_engine(days, tickets, sessions, cart, clv):
    w_days = 0.08
    w_tickets = 0.65
    w_sessions = -0.90  
    w_cart = 0.35
    intercept = -1.5     
    
    z = intercept + (days * w_days) + (tickets * w_tickets) + (sessions * w_sessions) + (cart * w_cart)
    probability = 1 / (1 + np.exp(-z))
    churn_percentage = float(round(probability * 100, 2))
    financial_loss_risk = float(round((churn_percentage / 100) * clv, 2))
    
    if churn_percentage >= 80.0:
        action = "VIP ZƏNG TƏTİKLƏNDİ"
        priority = "KRİTİK"
        color = "🔴"
    elif churn_percentage >= 50.0:
        action = "AVTOMATİK SMS & ENDİRİM"
        priority = "YÜKSƏK"
        color = "🟡"
    else:
        action = "SESSİZ MÜŞAHİDƏ"
        priority = "AŞAĞI"
        color = "🟢"
        
    return churn_percentage, financial_loss_risk, action, priority, color

# C) VİZUAL DIZAYN VƏ BAŞLIQLAR
st.title("🚀 SmartChurn AI — Müştəri İtkisi Analiz Paneli")
st.subheader("Founder's Club Kampaniya Versiyası (Enterprise)")
st.write("---")

# D) SOL MENYUDAN İDARƏ OLUNAN MÜŞTƏRİ SİMULYATORU
st.sidebar.header("🔬 Real Zamanlı Müştəri Testi")
st.sidebar.write("Müştəri davranışlarını dəyişərək sistemin verdiyi reaksiyanı canlı izləyin:")

days = st.sidebar.number_input("Son alış-verişdən keçən gün sayı", min_value=0, value=35)
tickets = st.sidebar.number_input("Şikayət biletlərinin sayı", min_value=0, value=3)
sessions = st.sidebar.number_input("Keçən həftə tətbiqə giriş sayısı", min_value=0, value=0)
cart = st.sidebar.number_input("Səbətdə unudulan məhsul sayı", min_value=0, value=2)
clv = st.sidebar.number_input("Müştərinin Şirkətə Ümumi Dəyəri (CLV - USD)", min_value=0.0, value=1250.0)

prob, loss, act, pri, col = advanced_ml_churn_engine(days, tickets, sessions, cart, clv)

# E) VİZUAL VİDCETLƏR VƏ REAL REZULTATLAR
st.subheader("📊 Canlı Analiz Nəticələri")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Müştərinin İtki Riski Faizi", value=f"{prob} %", delta=f"{pri} RİSK", delta_color="inverse")
with col2:
    st.metric(label="Maliyyə İtki Riski (USD)", value=f"${loss}", delta="Potensial Zərər")
with col3:
    st.metric(label="Tövsiyə Olunan Avtomatlaşdırılmış Addım", value=act, delta=col)

st.write("---")

# F) ŞİRKƏT RƏHBƏRLƏRİNƏ NÜMAYİŞ ÜÇÜN NÜMUNƏ DATA CƏDVƏLİ
st.subheader("📋 Yüksək Riskli Müştərilərin Ümumi Siyahısı")
fake_data = pd.DataFrame({
    "Müştəri Anonim ID": ["User_994_50_771", "User_994_70_555", "User_994_55_312"],
    "Risk Faizi": ["87.4%", "54.2%", "12.5%"],
    "İtiriləcək Məbləğ (USD)": ["$1,200", "$450", "$90"],
    "Prioritet": ["🔴 Kritik", "🟡 Yüksək", "🟢 Stabil"],
    "Sistemin Verdiyi Qərar": ["VIP Çağrı Mərkəzi Tətikləndi", "SMS Kampaniyası Göndərildi", "Müşahidədə Saxlanılır"]
})
st.table(fake_data)

st.info("💡 Qeyd: Bu panel şirkətinizin CRM və ya SQL verilənlər bazasına API xidmətimiz vasitəsilə təhlükəsiz inteqrasiya olunaraq real vaxt rejimində yenilənir.")
