# datasets/features.py
# 为股票行情数据添加技术指标，如 MA 和 RSI，供策略和模型使用

def add_technical_indicators(df):
    df = df.copy()
    df['ma_10'] = df['close'].rolling(10).mean()
    df['ma_30'] = df['close'].rolling(30).mean()
    df['rsi_14'] = compute_rsi(df['close'], 14)
    return df

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / (avg_loss + 1e-9)
    return 100 - (100 / (1 + rs))
