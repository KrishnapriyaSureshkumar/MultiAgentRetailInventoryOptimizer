# Multi-Agent Retail Inventory Optimizer

A lightweight, modular system designed to automate retail inventory monitoring and restocking using intelligent agents. Built with Python, Flask, and optional on-prem LLM (Phi via Ollama) for enhanced decision-making.

---

## Overview

This project simulates a smart retail environment using four collaborative agents:

- **Store Agent**  
  Monitors stock levels and triggers restock requests based on sales data and pricing input.

- **Warehouse Agent**  
  Maintains real-time inventory and processes restock requests.

- **Forecasting Agent**  
  Uses historical sales data to predict future demand.

- **Pricing Optimization Agent**  
  Analyzes competitor pricing and adjusts restock quantities accordingly.

- **LLM Query Agent (Optional)**  
  Powered by an on-prem Phi model via Ollama, this agent assists with intelligent query handling and supports the Forecasting and Pricing Agents when needed.

---

## Workflow

1. **Store Agent** detects low inventory.
2. It consults the **Forecasting Agent** and **Pricing Agent**.
3. The restock request is forwarded to the **Warehouse Agent**.
4. Optionally, user queries can be handled by the **LLM Agent** via the terminal.

---

## Tech Stack

- Python
- Flask (RESTful APIs)
- SQLite / CSV for data handling
- Ollama (optional LLM runtime)
- VS Code / Terminal-based interface

---

## Project Structure

```
.
├── create_db.py                 # Script to create the SQLite database
├── demand_forecasting.csv      # Historical sales data
├── forecast_agent.py           # Demand forecasting logic
├── inventory_monitoring.csv    # Store-side inventory records
├── ollama_tools.py             # LLM helper functions for Phi (via Ollama)
├── pricing_agent.py            # Price-based demand adjustment logic
├── pricing_optimization.csv    # Price competitor data
├── requirements.txt            # Python dependencies
├── retail_data.db              # SQLite database (generated)
├── run.py                      # Script to initialize and simulate system
├── store_agent.py              # Store agent logic
├── warehouse_agent.py          # Warehouse agent logic
├── README.md                   # Project documentation
└── env/                        # Python virtual environment
```

---

## Setup & Run

Follow these steps to run the project locally:

---

### 1️. Install dependencies
Use a virtual environment (recommended):

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

---

### 2️. Start each agent in its own terminal tab/window
Run these individually:

```bash
# Terminal 1 – Warehouse Agent
python warehouse_agent.py

# Terminal 2 – Forecasting Agent
python forecast_agent.py

# Terminal 3 – Pricing Agent
python pricing_agent.py

# Terminal 4 – Store Agent
python store_agent.py
```

---

### 3️. (Optional) Enable LLM support via `run.py`

To use intelligent LLM-based decision-making, open a **new terminal window** and run:

```bash
python run.py
```

This will launch an interactive CLI where you can:
- Ask the LLM questions via the Pricing or Forecasting Agent
- Skip LLM usage and trigger agents manually
- Simulate full inventory workflows from a single terminal

---

### 4️. (Optional) Start LLM backend (Ollama)

If you're using the on-prem LLM:

- Install [Ollama](https://ollama.com)
- Then run:

```bash
ollama run phi
```

This will launch the Phi model that supports natural language queries.

---

