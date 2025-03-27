# API 参考手册

## `quant_ai.data_loader.load_stock_data`
**功能**：获取股票数据并计算收益率

**参数**：
- `symbol (str)`: 股票代码，例如 `"AAPL"`
- `start (str)`: 开始日期，例如 `"2023-01-01"`
- `end (str)`: 结束日期，例如 `"2024-01-01"`

**示例**
```python
from quant_ai.data_loader import load_stock_data
df = load_stock_data("AAPL", "2023-01-01", "2024-01-01")
print(df.head())

📌 **适合工具**：
- **Markdown**（`.md`）  
- **Sphinx**（自动生成 API 文档）  

📌 **如何使用**：
```bash
cd docs
sphinx-build . _build/html
