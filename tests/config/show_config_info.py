"""
调试工具：打印所有 config/*.yaml 的加载情况，用于验证 config/__init__.py 的导入与值解析是否正常。
可以帮助开发者快速确认配置是否加载成功、字段是否缺失、格式是否有误。
"""

from config import (
    base_config,
    strategy_config,
    backtest_config,
    trading_config,
    model_config,
    tushare_token,
    get_config
)


def print_config(name: str, config: dict):
    print(f"===== 🔧 {name} =====")
    for k, v in config.items():
        print(f"{k}: {v}")
    print()


if __name__ == "__main__":
    print("🚀 正在加载并打印 config/ 下所有配置项...\n")

    print_config("base_config", base_config)
    print_config("strategy_config", strategy_config)
    print_config("backtest_config", backtest_config)
    print_config("trading_config", trading_config)
    print_config("model_config", model_config)

    print("===== 🔐 tushare_token =====")
    if tushare_token:
        print("TUSHARE_TOKEN: " + tushare_token[:6] + "..." + f" (长度: {len(tushare_token)})")
    else:
        print("TUSHARE_TOKEN 未设置（请检查 .env 或 base.yaml）")
