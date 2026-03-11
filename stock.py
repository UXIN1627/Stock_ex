import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# 設定網頁標題
st.set_page_config(page_title="股價查詢器", layout="centered")

st.title("📈 股票價格查詢系統")

# --- 側邊欄：使用者輸入區 ---
st.sidebar.header("查詢條件")

# 股票代碼輸入 (預設台積電)
stock_code = st.sidebar.text_input("1. 輸入股票代碼", value="2330.TW")

# 日期選擇（預設過去半年）
default_start = datetime.now() - timedelta(days=180)
start_date = st.sidebar.date_input("2. 開始日期", value=default_start)
end_date = st.sidebar.date_input("3. 結束日期", value=datetime.now())

# 查詢按鈕
if st.sidebar.button("開始查詢"):
    try:
        # 抓取資料
        data = yf.download(stock_code, start=start_date, end=end_date, auto_adjust=True)

        if data.empty:
            st.error("找不到資料！請檢查代碼（如 2330.TW）或日期。")
        else:
            # 顯示資訊
            st.subheader(f"📊 {stock_code} 股價表現")
            
            # 繪製圖表
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(data.index, data['Close'], label='Close Price', color='#1f77b4')
            ax.set_title(f"{stock_code} Price Trend")
            ax.grid(True)
            plt.xticks(rotation=45)
            
            # 在網頁顯示圖表
            st.pyplot(fig)

            # 顯示數據表格
            st.write("近期數據：")
            st.dataframe(data.tail(10))

    except Exception as e:
        st.error(f"發生錯誤: {e}")
else:
    st.info("請在左側輸入代碼並點擊「開始查詢」。")
