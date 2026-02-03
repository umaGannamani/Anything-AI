# Binance Futures Trading Bot (Testnet)

## Objective
A professional-grade CLI tool to place Futures orders on Binance Testnet.

## Features
- Market & Limit orders
- BUY / SELL support
- Input validation
- Structured logging
- Decoupled architecture

## Setup
1. Create Binance Futures Testnet API keys
2. Add them to `.env`
3. Install dependencies

Project Structure

trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── .env
├── requirements.txt
├── README.md
└── logs/
    └── trading.log



```bash
pip install -r requirements.txt


Usage
Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003

Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000

Logs

Stored in logs/trading.log

Assumptions

USDT-M futures only

Cross margin default