# AI Trading Bot 🚀

An automated AI-powered trading bot system equipped with exchange client integrations and a real-time web dashboard.

---

## 📌 Project Overview
This project provides an automated trading, monitoring, and state management system. It includes API client wrappers for crypto/equity trading, structured logging, memory management, and an interactive local dashboard.

---

## ✨ Key Features
* **Interactive Web Dashboard:** Real-time local interface to monitor bot operations, logs, and activity.
* **Exchange Integration:** Integrated support for Blofin and Zerodha trading clients.
* **State & Memory Management:** Built-in cloud memory support, structured transaction ledgers, and local caching.
* **Modular Architecture:** Clean separation between trading logic, UI, and external data connectors.

---

## 📁 Repository Structure
```text
├── app.py                  # Main entry point & local web server
├── cloud/                  # Cloud integrations and memory modules
├── data/                   # Data storage and local caches
├── mcp/                    # Model Context Protocol integrations
├── trading_bot/            # Core trading algorithms & exchange clients
│   ├── blofin_client.py    # Blofin API client wrapper
│   ├── zerodha_client.py   # Zerodha API client wrapper
│   ├── config.py           # Configuration parameters
│   ├── learning.py         # Bot learning and optimization models
│   └── ledger.py           # Trade history & transaction ledger
└── web/                    # Dashboard UI templates and static assets