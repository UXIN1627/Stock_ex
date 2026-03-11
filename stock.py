import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def plot_stock_price():
    print("--- 股票價格查詢系統 ---")
    
    # 1. 使用者輸入
    stock_code = input("請輸入股票代碼 (例如 AAPL 或 2330.TW): ").strip()
    start_date = input("請輸入開始日期 (格式 YYYY-MM-DD, 例如 2023-01-01): ").strip()
    end_date = input("請輸入結束日期 (格式 YYYY-MM-DD, 例如 2023-12-31): ").strip()

    try:
        # 2. 抓取資料
        print(f"正在從 Yahoo Finance 抓取 {stock_code} 的資料...")
        # auto_adjust=True 會自動處理除權息後的調整股價
        data = yf.download(stock_code, start=start_date, end=end_date, auto_adjust=True)

        if data.empty:
            print("錯誤：找不到該時段的資料，請檢查股票代碼或日期格式是否正確。")
            return

        # 3. 繪製圖表
        plt.figure(figsize=(12, 6))
        plt.plot(data['Close'], label='Adjusted Close Price', color='blue', linewidth=2)
        
        # 設定標題與標籤
        plt.title(f"Stock Price Change: {stock_code}", fontsize=16)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Price (USD/TWD)", fontsize=12)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # 自動調整日期顯示方式
        plt.gcf().autofmt_xdate()
        
        print("圖表已生成，請查看彈出視窗。")
        plt.show()

    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    plot_stock_price()