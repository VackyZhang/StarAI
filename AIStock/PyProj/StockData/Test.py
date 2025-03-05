import yfinance as yf

# 选择股票代码（以苹果公司AAPL为例）
ticker = "AAPL"
stock = yf.Ticker(ticker)

# 获取基本信息
print(stock.info)  # 公司概况、行业等信息

# 获取历史市场数据
history = stock.history(period="1mo")  # 过去一个月的数据
print(history)

# 获取股息信息
dividends = stock.dividends
print(dividends)

# 获取财务报表
balance_sheet = stock.balance_sheet
print(balance_sheet)

# 获取股票价格
price = stock.history(period="1d")
print(price)

def get_weekly_price(symbol):
    """获取指定股票最近7天的价格数据"""
    stock = yf.Ticker(symbol)
    weekly_data = stock.history(period="7d")
    return weekly_data

# 获取AAPL过去7天数据
weekly_prices = get_weekly_price("AAPL")
print("\n最近7天的价格数据：")
print(weekly_prices)