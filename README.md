# 多交易所策略交易工具

**Multi-Exchange Strategy Automation System**

## 🎯 项目简介

这是一个企业级的多交易所加密货币自动化交易系统，提供高性能、高可靠性的网格交易、刷量交易、套利监控和市场监控功能。系统采用严格的分层架构设计，支持 Hyperliquid、Backpack、Lighter、Binance、OKX、EdgeX 等多个交易所的完整适配。

## 🏗️ 核心系统架构

### 系统组件

```
多交易所策略自动化系统
├── 📊 网格交易系统 (Grid Trading)
│   ├── 普通网格              # 固定价格区间网格
│   ├── 马丁网格              # 马丁格尔递增策略
│   ├── 价格移动网格          # 动态跟随价格
│   ├── 剥头皮模式            # 快速止损策略
│   ├── 智能剥头皮            # 多次深跌检测
│   ├── 本金保护模式          # 自动止损保护
│   ├── 止盈模式              # 到达目标自动平仓
│   └── 现货预留管理          # 现货币种预留
├── 🔍 网格波动率扫描器 (Grid Volatility Scanner)
│   ├── 虚拟网格模拟          # 无需实际下单的模拟网格
│   ├── 实时APR计算           # 准确预测年化收益率
│   ├── 代币排行榜            # 按波动率和APR排序
│   ├── 智能评级系统          # S/A/B/C/D等级评估
│   └── 终端 UI              # Rich 实时监控界面
├── 💹 刷量交易系统 (Volume Maker)
│   ├── 挂单模式              # 限价单刷量（Backpack）
│   └── 市价模式              # 市价单快速刷量（Lighter）
├── 🔄 套利监控系统 (Arbitrage Monitor)
│   ├── 价格监控              # 实时价格差监控
│   ├── 资金费率监控          # 跨交易所费率差异
│   ├── 套利机会识别          # 价差和费率套利
│   ├── 终端 UI              # Rich 实时监控界面
│   └── 交易对自动发现        # 多交易所交易对匹配
├── 🔔 价格提醒系统 (Price Alert)
│   ├── 价格突破监控          # 价格触及目标提醒
│   ├── 多交易所支持          # 支持所有接入的交易所
│   ├── 终端 UI              # 实时价格显示
│   └── 声音提醒              # 突破时声音通知
├── 🔗 交易所适配层 (Exchange Adapters)
│   ├── Hyperliquid 适配器    # 永续合约 + 现货
│   ├── Backpack 适配器       # 永续合约
│   ├── Lighter 适配器        # 永续合约（低手续费）
│   ├── Binance 适配器        # 现货 + 永续合约
│   ├── OKX 适配器            # 现货 + 永续合约
│   ├── EdgeX 适配器          # 永续合约
│   └── 统一接口标准          # 标准化 API 接口
└── 🏛️ 基础设施层 (Infrastructure)
    ├── 依赖注入容器          # DI 容器管理
    ├── 事件系统              # 事件驱动架构
    ├── 日志系统              # 结构化日志
    ├── 配置管理              # YAML 配置系统
    └── 数据聚合器            # 多交易所数据聚合
```

## 🚀 快速开始

### 系统要求

- Python 3.8+
- 支持的操作系统：Linux、macOS、Windows
- 可选：tmux（用于多进程管理）

### 安装依赖

```bash
# 安装 Python 依赖
pip install -r requirements.txt
```

### 配置 API 密钥

在 `config/exchanges/` 目录下配置对应交易所的 API 密钥：

```bash
config/exchanges/
├── hyperliquid_config.yaml   # Hyperliquid 配置
├── backpack_config.yaml       # Backpack 配置
├── lighter_config.yaml        # Lighter 配置
├── binance_config.yaml        # Binance 配置
├── okx_config.yaml            # OKX 配置
└── edgex_config.yaml          # EdgeX 配置
```

### 快速启动各系统

#### 网格交易系统
```bash
python3 run_grid_trading.py config/grid/lighter-long-perp-btc.yaml
```

#### 刷量交易系统（Backpack挂单模式）
```bash
python3 run_volume_maker.py config/volume_maker/backpack_btc_volume_maker.yaml
```

#### 刷量交易系统（Lighter市价模式）
```bash
python3 run_lighter_volume_maker.py config/volume_maker/lighter_volume_maker.yaml
```

#### 套利监控系统
```bash
python3 run_arbitrage_monitor.py
```

#### 价格提醒系统
```bash
python3 run_price_alert.py config/price_alert/binance_alert.yaml
```

#### 网格波动率扫描器
```bash
python3 grid_volatility_scanner/run_scanner.py
```

## 📋 核心功能详解

### 1️⃣ 网格交易系统

#### 功能特性

- **多种网格模式**：普通网格、马丁网格、价格移动网格
- **智能策略**：剥头皮、智能剥头皮、本金保护、止盈模式
- **健康检查**：自动订单校验和修复机制
- **终端 UI**：实时监控界面，显示持仓、盈亏、网格状态
- **现货支持**：现货预留管理（自动维持币种余额）
- **多交易所**：支持 Hyperliquid、Backpack、Lighter

#### 配置文件位置

```
config/grid/
├── lighter_btc_perp_long.yaml              # Lighter BTC 做多
├── lighter_btc_perp_short.yaml             # Lighter BTC 做空
├── hyperliquid_btc_perp_long.yaml          # Hyperliquid BTC 做多
├── hyperliquid_btc_perp_short.yaml         # Hyperliquid BTC 做空
├── hyperliquid_btc_spot_long.yaml          # Hyperliquid 现货做多
├── backpack_capital_protection_long_btc.yaml   # Backpack BTC 本金保护
├── backpack_capital_protection_long_eth.yaml   # Backpack ETH 本金保护
├── backpack_capital_protection_long_sol.yaml   # Backpack SOL 本金保护
├── backpack_capital_protection_long_bnb.yaml   # Backpack BNB 本金保护
└── backpack_capital_protection_long_hype.yaml  # Backpack HYPE 本金保护
```

#### 启动方式

```bash
# 方式1：直接启动（推荐）
python3 run_grid_trading.py config/grid/lighter_btc_perp_long.yaml
python3 run_grid_trading.py config/grid/lighter_eth_perp_long.yaml

# 方式2：DEBUG 模式启动（查看详细日志）
python3 run_grid_trading.py config/grid/lighter_btc_perp_long.yaml --debug

# 方式3：使用 Shell 脚本批量启动（tmux）
./scripts/start_all_grids.sh
```

#### 核心文件

| 文件路径 | 说明 |
|---------|------|
| `run_grid_trading.py` | 网格交易系统主启动脚本 |
| `core/services/grid/coordinator/grid_coordinator.py` | 网格系统协调器（核心逻辑） |
| `core/services/grid/implementations/grid_engine_impl.py` | 网格执行引擎 |
| `core/services/grid/implementations/grid_strategy_impl.py` | 网格策略实现 |
| `core/services/grid/implementations/position_tracker_impl.py` | 持仓跟踪器 |
| `core/services/grid/implementations/order_health_checker.py` | 订单健康检查器 |
| `core/services/grid/scalping/scalping_manager.py` | 剥头皮管理器 |
| `core/services/grid/scalping/smart_scalping_tracker.py` | 智能剥头皮追踪器 |
| `core/services/grid/capital_protection/capital_protection_manager.py` | 本金保护管理器 |
| `core/services/grid/terminal_ui.py` | 终端 UI 界面 |

### 2️⃣ 刷量交易系统

#### 功能特性

- **双交易模式**：挂单模式（Backpack）、市价模式（Lighter）
- **信号源支持**：Backpack REST API、Hyperliquid WebSocket
- **智能判断**：买卖单数量对比、价格变动监控
- **实时统计**：成交量、成交金额、手续费统计
- **终端 UI**：实时显示交易状态和统计信息

#### 配置文件位置

```
config/volume_maker/
├── backpack_btc_volume_maker.yaml   # Backpack 挂单模式
└── lighter_volume_maker.yaml        # Lighter 市价模式（支持多信号源）
```

#### 启动方式

```bash
# Backpack 挂单模式刷量
python3 run_volume_maker.py config/volume_maker/backpack_btc_volume_maker.yaml
# 或使用快速启动脚本
./scripts/start_volume_maker.sh

# Lighter 市价模式刷量（支持 Backpack/Hyperliquid 信号源）
python3 run_lighter_volume_maker.py config/volume_maker/lighter_volume_maker.yaml
# 或使用快速启动脚本
./scripts/start_lighter_volume_maker.sh
```

#### 核心文件

| 文件路径 | 说明 |
|---------|------|
| `run_volume_maker.py` | 挂单模式刷量启动脚本（Backpack） |
| `run_lighter_volume_maker.py` | 市价模式刷量启动脚本（Lighter） |
| `core/services/volume_maker/implementations/volume_maker_service_impl.py` | 挂单模式服务实现 |
| `core/services/volume_maker/implementations/lighter_market_volume_maker_service.py` | 市价模式服务实现 |
| `core/services/volume_maker/terminal_ui.py` | 刷量系统终端 UI |
| `core/services/volume_maker/hourly_statistics.py` | 小时统计模块 |

### 3️⃣ 套利监控系统

#### 功能特性

- **价格监控**：实时监控多交易所价格差（EdgeX、Lighter）
- **资金费率监控**：跨交易所资金费率差异追踪
- **套利机会识别**：价差套利和费率套利机会
- **终端 UI**：Rich 库实现的现代化实时监控界面
- **交易对自动发现**：自动匹配多交易所支持的交易对
- **费率差持续时间追踪**：记录高费率差持续时长
- **动态价格精度**：根据价格大小自动调整显示精度
- **智能排序**：按价差排序，定时刷新避免界面抖动

#### 配置文件位置

```
config/arbitrage/
└── monitor.yaml               # 套利监控配置
```

#### 启动方式

```bash
# 直接启动
python3 run_arbitrage_monitor.py

# 使用快速启动脚本
./scripts/start_arbitrage_monitor.sh
```

#### 核心文件

| 文件路径 | 说明 |
|---------|------|
| `run_arbitrage_monitor.py` | 套利监控系统启动脚本 |
| `core/services/arbitrage_monitor/implementations/arbitrage_monitor_impl.py` | 监控服务实现 |
| `core/services/arbitrage_monitor/interfaces/arbitrage_monitor_service.py` | 监控服务接口 |
| `core/services/arbitrage_monitor/models/arbitrage_models.py` | 套利数据模型 |
| `core/services/arbitrage_monitor/utils/symbol_converter.py` | 交易对转换器 |

### 4️⃣ 价格提醒系统

#### 功能特性

- **价格突破监控**：监控价格触及设定的上下限
- **多交易所支持**：支持所有接入的交易所
- **终端 UI**：实时显示当前价格和目标价格
- **声音提醒**：价格突破时发出声音通知
- **自动退出**：触发提醒后自动退出程序

#### 配置文件位置

```
config/price_alert/
└── binance_alert.yaml         # 价格提醒配置
```

#### 启动方式

```bash
# 直接启动
python3 run_price_alert.py config/price_alert/binance_alert.yaml

# 使用快速启动脚本
./scripts/start_price_alert.sh
```

#### 核心文件

| 文件路径 | 说明 |
|---------|------|
| `run_price_alert.py` | 价格提醒系统启动脚本 |
| `core/services/price_alert/implementations/price_alert_service_impl.py` | 提醒服务实现 |
| `core/services/price_alert/interfaces/price_alert_service.py` | 提醒服务接口 |
| `core/services/price_alert/models/alert_config.py` | 提醒配置模型 |
| `core/services/price_alert/models/alert_statistics.py` | 提醒统计模型 |

### 5️⃣ 网格波动率扫描器

#### 功能特性

- **虚拟网格模拟**：模拟网格交易，无需实际下单
- **实时APR计算**：准确预测年化收益率
- **代币排行榜**：按波动率和APR排序，展示Top代币
- **智能评级系统**：S/A/B/C/D等级评估（S级≥500% APR）
- **终端 UI**：Rich库实现的现代化实时监控界面
- **灵活配置**：支持自定义网格宽度、间距、扫描时长
- **多交易所支持**：支持Lighter、Hyperliquid等交易所

#### 配置文件位置

```
grid_volatility_scanner/config/
└── market_config.yaml         # 市场配置（网格参数）
```

#### 启动方式

```bash
# 基础启动（扫描1小时）
python3 grid_volatility_scanner/run_scanner.py

# 自定义扫描时长（30分钟）
python3 grid_volatility_scanner/run_scanner.py --duration 1800

# 指定交易所（Hyperliquid）
python3 grid_volatility_scanner/run_scanner.py --exchange hyperliquid

# 使用自定义配置文件
python3 grid_volatility_scanner/run_scanner.py --config my_config.yaml
```

#### 核心文件

| 文件路径 | 说明 |
|---------|------|
| `grid_volatility_scanner/run_scanner.py` | 扫描器启动脚本 |
| `grid_volatility_scanner/scanner.py` | 主扫描器逻辑 |
| `grid_volatility_scanner/models/virtual_grid.py` | 虚拟网格模型 |
| `grid_volatility_scanner/models/simulation_result.py` | 模拟结果模型 |
| `grid_volatility_scanner/core/price_monitor.py` | 价格监控器 |
| `grid_volatility_scanner/core/cycle_detector.py` | 循环检测器 |
| `grid_volatility_scanner/core/apr_calculator.py` | APR计算器 |
| `grid_volatility_scanner/ui/scanner_ui.py` | Rich终端UI |

#### APR计算公式

```
APR = (格子间距% - 手续费%) × 格子间距% / 网格宽度% × 每小时循环 × 8760
```

#### 评级系统

| 评级 | APR范围 | 说明 |
|------|---------|------|
| 🔥 S | ≥ 500% | 极度推荐 |
| ⭐ A | ≥ 300% | 强烈推荐 |
| ✅ B | ≥ 150% | 推荐 |
| 🟡 C | ≥ 50%  | 可考虑 |
| ❌ D | < 50%  | 不推荐 |

## 🔗 支持的交易所

### 完整适配交易所

| 交易所 | 现货 | 永续合约 | REST API | WebSocket | 状态 |
|--------|------|---------|----------|-----------|------|
| **Hyperliquid** | ✅ | ✅ | ✅ | ✅ | ✅ 完整适配 |
| **Backpack** | ❌ | ✅ | ✅ | ✅ | ✅ 完整适配 |
| **Lighter** | ❌ | ✅ | ✅ | ✅ | ✅ 完整适配 |
| **Binance** | ✅ | ✅ | ✅ | ✅ | ✅ 完整适配 |
| **OKX** | ✅ | ✅ | ✅ | ✅ | ✅ 完整适配 |
| **EdgeX** | ❌ | ✅ | ✅ | ✅ | ✅ 完整适配 |

### 交易所适配器文件

```
core/adapters/exchanges/adapters/
├── hyperliquid.py           # Hyperliquid 统一接口
├── hyperliquid_base.py      # 基础类
├── hyperliquid_rest.py      # REST API
├── hyperliquid_websocket.py # WebSocket
├── backpack.py              # Backpack 统一接口
├── backpack_base.py         # 基础类
├── backpack_rest.py         # REST API
├── backpack_websocket.py    # WebSocket
├── lighter.py               # Lighter 统一接口
├── lighter_base.py          # 基础类
├── lighter_rest.py          # REST API
├── lighter_websocket.py     # WebSocket
├── binance.py               # Binance 统一接口
├── okx.py                   # OKX 统一接口
└── edgex.py                 # EdgeX 统一接口
```

## 📁 完整项目结构

```
crypto-trading/
├── 🚀 启动脚本 (Root Scripts)
│   ├── run_grid_trading.py                # 网格交易系统启动
│   ├── run_volume_maker.py                # 挂单刷量系统启动（Backpack）
│   ├── run_lighter_volume_maker.py        # 市价刷量系统启动（Lighter）
│   ├── run_arbitrage_monitor.py           # 套利监控系统启动
│   ├── run_price_alert.py                 # 价格提醒系统启动
│   └── grid_volatility_scanner/
│       └── run_scanner.py                 # 网格波动率扫描器启动
├── 🏛️ core/ - 核心业务层
│   ├── data_aggregator.py                 # 数据聚合器
│   ├── __init__.py
│   ├── adapters/ - 交易所适配层
│   │   └── exchanges/
│   │       ├── adapter.py                 # 适配器基类
│   │       ├── factory.py                 # 适配器工厂
│   │       ├── interface.py               # 统一接口定义
│   │       ├── manager.py                 # 适配器管理器
│   │       ├── models.py                  # 数据模型
│   │       ├── subscription_manager.py    # 订阅管理器
│   │       ├── websocket_manager.py       # WebSocket 管理器
│   │       ├── adapters/                  # 各交易所适配器实现
│   │       │   ├── hyperliquid*.py        # Hyperliquid 适配器
│   │       │   ├── backpack*.py           # Backpack 适配器
│   │       │   ├── lighter*.py            # Lighter 适配器
│   │       │   ├── binance*.py            # Binance 适配器
│   │       │   ├── okx*.py                # OKX 适配器
│   │       │   └── edgex*.py              # EdgeX 适配器
│   │       └── utils/                     # 工具类
│   │           ├── log_formatter.py       # 日志格式化
│   │           └── setup_logging.py       # 日志设置
│   ├── services/ - 业务服务层
│   │   ├── grid/ - 网格交易服务
│   │   │   ├── coordinator/               # 协调器模块
│   │   │   │   ├── grid_coordinator.py    # 网格协调器（核心）
│   │   │   │   ├── balance_monitor.py     # 余额监控
│   │   │   │   ├── position_monitor.py    # 持仓监控
│   │   │   │   ├── order_operations.py    # 订单操作
│   │   │   │   ├── scalping_operations.py # 剥头皮操作
│   │   │   │   ├── grid_reset_manager.py  # 网格重置管理
│   │   │   │   └── verification_utils.py  # 验证工具
│   │   │   ├── implementations/           # 实现模块
│   │   │   │   ├── grid_engine_impl.py    # 执行引擎
│   │   │   │   ├── grid_strategy_impl.py  # 策略实现
│   │   │   │   ├── position_tracker_impl.py   # 持仓跟踪
│   │   │   │   ├── order_health_checker.py    # 健康检查
│   │   │   │   └── order_monitor.py       # 订单监控
│   │   │   ├── interfaces/                # 接口定义
│   │   │   │   ├── grid_engine.py
│   │   │   │   ├── grid_strategy.py
│   │   │   │   └── position_tracker.py
│   │   │   ├── models/                    # 数据模型
│   │   │   │   ├── grid_config.py         # 网格配置
│   │   │   │   ├── grid_state.py          # 网格状态
│   │   │   │   ├── grid_order.py          # 网格订单
│   │   │   │   └── grid_metrics.py        # 网格指标
│   │   │   ├── scalping/                  # 剥头皮模块
│   │   │   │   ├── scalping_manager.py    # 剥头皮管理器
│   │   │   │   └── smart_scalping_tracker.py  # 智能剥头皮追踪
│   │   │   ├── capital_protection/        # 本金保护模块
│   │   │   │   └── capital_protection_manager.py
│   │   │   ├── take_profit/               # 止盈模块
│   │   │   │   └── take_profit_manager.py
│   │   │   ├── price_lock/                # 价格锁定模块
│   │   │   │   └── price_lock_manager.py
│   │   │   ├── reserve/                   # 现货预留模块
│   │   │   │   ├── spot_reserve_manager.py
│   │   │   │   ├── reserve_monitor.py
│   │   │   │   └── reserve_checker.py
│   │   │   └── terminal_ui.py             # 网格系统终端 UI
│   │   ├── volume_maker/ - 刷量交易服务
│   │   │   ├── implementations/
│   │   │   │   ├── volume_maker_service_impl.py   # 挂单模式实现
│   │   │   │   └── lighter_market_volume_maker_service.py  # 市价模式实现
│   │   │   ├── interfaces/
│   │   │   │   └── volume_maker_service.py
│   │   │   ├── models/
│   │   │   │   ├── volume_maker_config.py
│   │   │   │   └── volume_maker_statistics.py
│   │   │   ├── hourly_statistics.py       # 小时统计
│   │   │   └── terminal_ui.py             # 刷量系统终端 UI
│   │   ├── arbitrage_monitor/ - 套利监控服务
│   │   │   ├── implementations/
│   │   │   │   └── arbitrage_monitor_impl.py   # 监控服务实现
│   │   │   ├── interfaces/
│   │   │   │   └── arbitrage_monitor_service.py  # 监控服务接口
│   │   │   ├── models/
│   │   │   │   └── arbitrage_models.py    # 套利数据模型
│   │   │   └── utils/
│   │   │       └── symbol_converter.py    # 交易对转换器
│   │   ├── price_alert/ - 价格提醒服务
│   │   │   ├── implementations/
│   │   │   │   └── price_alert_service_impl.py  # 提醒服务实现
│   │   │   ├── interfaces/
│   │   │   │   └── price_alert_service.py # 提醒服务接口
│   │   │   └── models/
│   │   │       ├── alert_config.py        # 提醒配置模型
│   │   │       └── alert_statistics.py    # 提醒统计模型
│   │   ├── symbol_manager/ - 交易对管理服务
│   │   │   ├── implementations/
│   │   │   │   ├── symbol_conversion_service.py
│   │   │   │   └── symbol_cache_service.py
│   │   │   ├── interfaces/
│   │   │   │   ├── symbol_conversion_service.py
│   │   │   │   └── symbol_cache.py
│   │   │   └── models/
│   │   │       ├── symbol_normalization.py
│   │   │       └── symbol_cache_models.py
│   │   ├── events/ - 事件系统
│   │   │   ├── event.py
│   │   │   ├── event_handler.py
│   │   │   └── __init__.py
│   │   ├── implementations/ - 通用服务实现
│   │   │   └── config_service.py
│   │   └── interfaces/ - 通用服务接口
│   │       ├── base.py
│   │       └── config_service.py
│   ├── domain/ - 领域模型层
│   │   ├── __init__.py
│   │   └── （领域实体和值对象）
│   ├── infrastructure/ - 基础设施层
│   │   ├── __init__.py
│   │   └── （缓存、数据库、消息队列等）
│   ├── di/ - 依赖注入容器
│   │   ├── container.py                   # DI 容器
│   │   ├── modules.py                     # 模块注册
│   │   └── （其他 DI 相关文件）
│   └── logging/ - 日志系统
│       ├── __init__.py
│       └── （日志配置和工具）
├── 🌐 api/ - API 层
│   ├── gateway.py                         # FastAPI 网关
│   ├── middleware/                        # 中间件
│   │   ├── logging.py
│   │   └── __init__.py
│   ├── websocket/                         # WebSocket 服务
│   │   └── __init__.py
│   └── graphql/                           # GraphQL 服务
│       └── __init__.py
├── 🔧 config/ - 配置文件
│   ├── exchanges/                         # 交易所配置
│   │   ├── hyperliquid_config.yaml
│   │   ├── backpack_config.yaml
│   │   ├── lighter_config.yaml
│   │   ├── binance_config.yaml
│   │   ├── okx_config.yaml
│   │   └── edgex_config.yaml
│   ├── grid/                              # 网格配置
│   │   ├── lighter_btc_perp_long.yaml
│   │   ├── lighter_btc_perp_short.yaml
│   │   ├── hyperliquid_btc_perp_long.yaml
│   │   ├── hyperliquid_btc_perp_short.yaml
│   │   ├── hyperliquid_btc_spot_long.yaml
│   │   └── backpack_capital_protection_*.yaml  （多个）
│   ├── volume_maker/                      # 刷量配置
│   │   ├── backpack_btc_volume_maker.yaml
│   │   └── lighter_volume_maker.yaml
│   ├── arbitrage/                         # 套利配置
│   │   └── monitor.yaml
│   ├── price_alert/                       # 价格提醒配置
│   │   └── binance_alert.yaml
│   ├── symbol_conversion.yaml             # 交易对转换配置
│   └── logging.yaml                       # 日志配置
├── 🛠️ tools/ - 工具脚本
│   ├── martin_grid_calculator.py          # 马丁网格计算器
│   ├── convert_account_index.py           # 账户索引转换
│   ├── query_account_simple.py            # 简单账户查询
│   ├── query_account_with_apikey.py       # API Key 账户查询
│   ├── test_apikey_direct.py              # API Key 直接测试
│   └── README.md                          # 工具说明文档
├── 📜 scripts/ - 运维脚本
│   ├── start_all_grids.sh                 # 批量启动网格（tmux）
│   ├── stop_all_grids.sh                  # 批量停止网格
│   ├── start_volume_maker.sh              # 启动挂单刷量
│   ├── start_lighter_volume_maker.sh      # 启动市价刷量
│   ├── start_arbitrage_monitor.sh         # 启动套利监控
│   ├── start_price_alert.sh               # 启动价格提醒
│   ├── check_ports.sh                     # 端口检查
│   ├── apply_log_optimization.sh          # 日志优化
│   ├── release.sh                         # 发布脚本
│   ├── deployment/                        # 部署脚本
│   │   ├── start_system.sh
│   │   └── stop_system.sh
│   ├── migration/                         # 迁移脚本
│   │   └── （数据迁移脚本）
│   └── README.md                          # 脚本说明文档
├── 🧪 tests/ - 测试代码
│   ├── adapters/                          # 适配器测试
│   │   ├── hyperliquid/                   # Hyperliquid 测试
│   │   ├── backpack/                      # Backpack 测试
│   │   ├── lighter/                       # Lighter 测试
│   │   ├── binance/                       # Binance 测试
│   │   └── okx/                           # OKX 测试
│   ├── strategies/                        # 策略测试
│   │   ├── grid/                          # 网格策略测试
│   │   └── volume_maker/                  # 刷量策略测试
│   ├── arbitrage/                         # 套利系统测试
│   │   └── reports/                       # 测试报告
│   ├── integration/                       # 集成测试
│   ├── unit/                              # 单元测试
│   ├── performance/                       # 性能测试
│   ├── debug/                             # 调试测试
│   └── README.md                          # 测试说明文档
├── 🧪 test/ - 快速测试脚本
│   ├── test_lighter_*.py                  # Lighter 快速测试
│   ├── test_hyperliquid_*.py              # Hyperliquid 快速测试
│   ├── verify_liquidation_price.py        # 清算价格验证
│   ├── compare_liquidation_methods.py     # 清算方法对比
│   ├── test_log_optimization.py           # 日志优化测试
│   └── （其他快速测试脚本）
├── 📝 examples/ - 示例代码
│   ├── basic_demo.py                      # 基础演示
│   ├── exchange_adapter_demo.py           # 适配器演示
│   ├── edgex_adapter_demo.py              # EdgeX 演示
│   ├── subscription_mode_demo.py          # 订阅模式演示
│   └── （其他示例脚本）
├── 🔍 grid_volatility_scanner/ - 网格波动率扫描器
│   ├── __init__.py                        # 模块初始化
│   ├── scanner.py                         # 主扫描器逻辑
│   ├── run_scanner.py                     # 启动脚本
│   ├── README.md                          # 扫描器文档
│   ├── config/
│   │   └── market_config.yaml             # 市场配置文件
│   ├── models/
│   │   ├── virtual_grid.py                # 虚拟网格模型
│   │   └── simulation_result.py           # 模拟结果模型
│   ├── core/
│   │   ├── price_monitor.py               # 价格监控器
│   │   ├── cycle_detector.py              # 循环检测器
│   │   └── apr_calculator.py              # APR计算器
│   └── ui/
│       └── scanner_ui.py                  # Rich终端UI
├── 📚 docs/ - 文档
│   ├── README.md                          # 文档总入口
│   ├── INDEX.md                           # 文档索引
│   ├── grid-trading/                      # 网格交易文档
│   │   └── （70+ 篇详细文档）
│   ├── grid_volatility_scanner/           # 网格波动率扫描器文档
│   │   └── （7 篇详细文档）
│   ├── volume-maker/                      # 刷量系统文档
│   │   └── （42 篇详细文档）
│   ├── arbitrage_monitor/                 # 套利监控系统文档
│   │   └── （10 篇详细文档）
│   ├── price-alert/                       # 价格提醒系统文档
│   │   └── （1 篇文档）
│   ├── lighter/                           # Lighter 交易所文档
│   │   └── （47 篇详细文档）
│   ├── hyperliquid/                       # Hyperliquid 交易所文档
│   │   └── （23 篇详细文档）
│   ├── architecture/                      # 架构设计文档
│   │   └── （36 篇架构文档）
│   ├── adapters/                          # 适配器文档
│   │   └── （10 篇适配器文档）
│   ├── features/                          # 功能特性文档
│   │   └── （7 篇功能文档）
│   ├── fixes/                             # 问题修复文档
│   │   └── （107 篇修复记录）
│   ├── troubleshooting/                   # 故障排查文档
│   │   └── （22 篇排查指南）
│   ├── tools/                             # 工具文档
│   │   └── （1 篇工具文档）
│   ├── websocket/                         # WebSocket 文档
│   │   └── （2 篇 WebSocket 文档）
│   ├── legacy/                            # 遗留文档
│   │   └── （3 篇文档）
│   ├── 终端UI稳定显示设计指南.md         # 终端UI设计指南
│   ├── Python终端UI库对比指南.md         # Python UI库对比
│   └── （其他专题文档）
├── 🗂️ deprecated/ - 废弃代码
│   └── old_monitoring_system/            # 旧版监控系统
├── 📦 web-console/ - Web 前端（可选）
│   ├── src/                               # 源代码
│   │   ├── components/                    # 通用组件
│   │   ├── pages/                         # 页面组件
│   │   ├── services/                      # 前端服务
│   │   └── types/                         # 类型定义
│   ├── package.json                       # 前端依赖
│   └── vite.config.ts                     # 构建配置
├── 📋 logs/ - 日志目录
│   ├── system.log                         # 系统日志
│   ├── ExchangeAdapter.log                # 适配器日志
│   ├── core.services.grid.*.log           # 网格系统日志
│   └── （其他日志文件）
├── 🐳 docker/ - Docker 配置
│   └── README.md
├── 📄 requirements.txt                    # Python 依赖
├── 📖 README.md                           # 项目说明文档（本文件）
├── 📋 PROJECT_STRUCTURE.md                # 项目结构说明
├── 📋 REST_API使用总结.md                  # REST API 使用总结
├── 📋 CHANGELOG.md                        # 变更日志
└── 📋 VERSION                             # 版本号
```

## 📊 启动脚本总结

### 网格交易系统

| 脚本 | 命令 | 说明 |
|------|------|------|
| 单个网格启动 | `python3 run_grid_trading.py <配置文件>` | 启动单个网格交易 |
| DEBUG 模式 | `python3 run_grid_trading.py <配置文件> --debug` | 详细日志模式 |
| 批量启动 | `./scripts/start_all_grids.sh` | tmux 批量启动多个网格 |
| 批量停止 | `./scripts/stop_all_grids.sh` | 停止所有网格 |

### 刷量交易系统

| 脚本 | 命令 | 说明 |
|------|------|------|
| 挂单模式 | `python3 run_volume_maker.py <配置文件>` | Backpack 挂单刷量 |
| 挂单快速启动 | `./scripts/start_volume_maker.sh` | 快速启动 Backpack 刷量 |
| 市价模式 | `python3 run_lighter_volume_maker.py <配置文件>` | Lighter 市价刷量 |
| 市价快速启动 | `./scripts/start_lighter_volume_maker.sh` | 快速启动 Lighter 刷量 |

### 监控系统

| 脚本 | 命令 | 说明 |
|------|------|------|
| 套利监控 | `python3 run_arbitrage_monitor.py` | 启动套利监控系统 |
| 套利监控快速启动 | `./scripts/start_arbitrage_monitor.sh` | 快速启动套利监控 |
| 价格提醒 | `python3 run_price_alert.py <配置文件>` | 启动价格提醒系统 |
| 价格提醒快速启动 | `./scripts/start_price_alert.sh` | 快速启动价格提醒 |

### 分析工具

| 脚本 | 命令 | 说明 |
|------|------|------|
| 网格波动率扫描器 | `python3 grid_volatility_scanner/run_scanner.py` | 扫描并推荐最佳网格标的 |
| 自定义扫描时长 | `python3 grid_volatility_scanner/run_scanner.py --duration <秒>` | 指定扫描时长（秒） |
| 指定交易所 | `python3 grid_volatility_scanner/run_scanner.py --exchange <交易所>` | 指定交易所扫描 |

## 🛠️ 工具脚本

### 马丁网格计算器

```bash
# 计算马丁网格所需资金和风险分布
python3 tools/martin_grid_calculator.py
```

### 账户查询工具

```bash
# 简单账户查询
python3 tools/query_account_simple.py

# 使用 API Key 查询账户
python3 tools/query_account_with_apikey.py
```

### 账户索引转换工具

```bash
# 转换 Lighter 账户索引
python3 tools/convert_account_index.py
```

## 🧪 测试脚本

### 交易所适配器测试

```bash
# Lighter 测试
python3 test/test_lighter_price_subscription.py
python3 test/test_lighter_get_open_orders.py
python3 test/test_lighter_position_query.py

# Hyperliquid 测试
python3 test/test_hyperliquid_orderbook_simple.py
python3 test/test_hyperliquid_orderbook_ws.py
```

### 清算价格验证

```bash
# 验证清算价格计算
python3 test/verify_liquidation_price.py

# 对比不同清算方法
python3 test/compare_liquidation_methods.py
```

## 🎯 核心架构原则

### 分层架构

```
API 层 (api/)
  ↓
服务层 (core/services/)
  ↓
领域层 (core/domain/)
  ↓
适配器层 (core/adapters/)
  ↓
基础设施层 (core/infrastructure/)
```

### 架构特点

1. **依赖倒置原则**：高层模块不依赖低层模块，都依赖抽象
2. **接口分离原则**：服务接口定义与实现分离
3. **单一职责原则**：每个模块只负责一个明确的业务功能
4. **开闭原则**：通过接口扩展功能，不修改现有实现

### 禁止的架构违规

- ❌ API 层直接调用适配器层
- ❌ 服务层硬编码具体依赖
- ❌ 跨层级的直接调用
- ❌ 循环依赖关系

## 📖 技术栈

### 后端技术

- **核心语言**：Python 3.8+
- **异步框架**：asyncio, aiohttp
- **API 框架**：FastAPI
- **数据验证**：Pydantic
- **WebSocket**：websockets, aiohttp
- **配置管理**：PyYAML
- **日志系统**：structlog, logging
- **终端 UI**：Rich（现代化终端界面库）
- **测试框架**：pytest, pytest-asyncio

### 开发工具

- **进程管理**：tmux（多进程管理）
- **容器化**：Docker（可选）
- **版本控制**：Git

## 📝 开发规范

详细开发规范请参考 `.cursor/rules/` 目录下的规则文件：

- **architecture.mdc** - 分层架构设计原则
- **dependency_injection.mdc** - 依赖注入模式规范
- **code_style.mdc** - Python 代码风格规范
- **imports.mdc** - 导入路径规范
- **api_layer.mdc** - API 层设计规范
- **services.mdc** - 服务层开发规范
- **testing.mdc** - 测试规范

## 📚 文档资源

### 核心文档

- **[文档总入口](docs/README.md)** - 完整文档导航
- **[文档索引](docs/INDEX.md)** - 所有文档索引
- **[网格交易系统完整指南](docs/grid-trading/)** - 70+ 篇网格交易详细文档
- **[网格波动率扫描器文档](grid_volatility_scanner/README.md)** - 扫描器使用指南
- **[刷量系统文档](docs/volume-maker/)** - 42 篇刷量系统文档
- **[套利监控系统文档](docs/arbitrage_monitor/)** - 10 篇套利监控文档
- **[架构设计文档](docs/architecture/)** - 36 篇架构设计文档

### 交易所专题文档

- **[Lighter 交易所文档](docs/lighter/)** - 47 篇 Lighter 专题文档
- **[Hyperliquid 交易所文档](docs/hyperliquid/)** - 23 篇 Hyperliquid 专题文档
- **[多交易所接入快速参考](docs/多交易所接入快速参考.md)** - 快速接入指南

### 工具文档

- **[工具说明](tools/README.md)** - 所有工具的详细说明
- **[脚本说明](scripts/README.md)** - 运维脚本使用说明
- **[测试说明](tests/README.md)** - 测试代码组织和使用

## 🔧 常见问题

### 1. 如何配置 API 密钥？

在 `config/exchanges/` 目录下找到对应交易所的配置文件，填入 API 密钥：

```yaml
# config/exchanges/lighter_config.yaml 示例
api_config:
  auth:
    api_key_private_key: "你的API密钥私钥"
    account_index: 0
    api_key_index: 0
```

### 2. 如何添加新的交易对？

复制现有的配置文件（如 `config/grid/lighter_btc_perp_long.yaml`），修改 `symbol` 字段和相关参数即可。

### 3. 网格系统支持哪些模式？

- 普通网格（固定价格区间）
- 马丁网格（递增订单量）
- 价格移动网格（动态跟随价格）
- 剥头皮模式（快速止损）
- 智能剥头皮（多次深跌检测）
- 本金保护模式（自动止损）
- 止盈模式（达到目标自动平仓）

### 4. 刷量系统有什么区别？

- **挂单模式**（Backpack）：使用限价单，成交率较低但手续费有返佣
- **市价模式**（Lighter）：使用市价单，立即成交但手续费较高

### 5. 如何停止正在运行的系统？

- **单个脚本**：按 `Ctrl+C` 或在终端 UI 中按 `Q` 键
- **tmux 批量启动的网格**：运行 `./scripts/stop_all_grids.sh`

### 6. 日志文件在哪里？

所有日志文件位于 `logs/` 目录下，按模块分类：
- `system.log` - 系统总日志
- `ExchangeAdapter.log` - 交易所适配器日志
- `core.services.grid.*.log` - 网格系统各模块日志

### 7. 如何查看详细的调试日志？

使用 `--debug` 参数启动脚本：

```bash
python3 run_grid_trading.py config/grid/lighter_btc_perp_long.yaml --debug
```

### 8. 如何使用网格波动率扫描器？

网格波动率扫描器可以帮助您快速识别最适合做网格的代币：

```bash
# 扫描1小时（默认）
python3 grid_volatility_scanner/run_scanner.py

# 扫描30分钟
python3 grid_volatility_scanner/run_scanner.py --duration 1800

# 使用Hyperliquid交易所
python3 grid_volatility_scanner/run_scanner.py --exchange hyperliquid
```

扫描器会实时显示代币的APR排名，S级（≥500% APR）代币强烈推荐用于网格交易。

## 🚨 注意事项

1. **API 密钥安全**：请妥善保管 API 密钥，不要上传到公共仓库
2. **资金安全**：建议先用小额资金测试系统
3. **网络稳定**：确保网络连接稳定，WebSocket 断线会自动重连
4. **交易限制**：注意交易所的订单数量限制（如 Lighter 每个市场的最大活跃订单数）
5. **现货做空**：现货市场不支持做空，仅支持做多网格
6. **手续费**：不同交易所手续费不同，请在配置文件中正确设置 `fee_rate`
7. **精度问题**：不同交易对的数量精度不同，请在配置中正确设置 `quantity_precision`

## 📞 支持与反馈

如有问题或建议，请参考 `docs/` 目录下的详细文档，或查看 `docs/troubleshooting/` 中的故障排查指南。

---

**多交易所策略自动化系统 v2.0.0** - 企业级加密货币自动化交易平台
