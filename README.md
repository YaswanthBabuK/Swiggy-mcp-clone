# 🍔 Swiggy MCP Clone

A **Model Context Protocol (MCP)** based backend simulation inspired by **Swiggy**, built to demonstrate
**tool-driven AI integrations**, structured data modeling, and API-style workflows using Python.

This project is designed to be consumed by **LLMs / AI agents** via MCP, enabling intelligent interactions
such as order lookup, customer support, delivery status, and refund policies.

---

## 🚀 Features

- 🔧 MCP-compatible server for AI tool calling
- 👤 Customer management & lookup
- 🛒 Order handling and status tracking
- 🏪 Restaurant data simulation
- 📦 Late delivery & refund policy handling
- 🧠 Pydantic-based data validation
- 📓 Example notebooks for experimentation

---

## 📂 Project Structure

```text
swiggy-mcp/
├── main.py                  # MCP server entry point
├── customercare.py          # Customer care tools (AI callable)
├── customers.py             # Customer data & utilities
├── orders.py                # Order management logic
├── restaurants.py           # Restaurant data layer
├── models.py                # Pydantic models
├── notebooks/               # Experiments & demos
│   └── pydentic.ipynb
├── latetimedelivery.md      # Late delivery rules
├── refundpolicy.md          # Refund policy documentation
├── README.md                # Project documentation
├── pyproject.toml           # Project metadata & dependencies
├── uv.lock                  # Dependency lock file
├── .gitignore
├── .python-version
└── LICENSE
````

---

## 🛠 Tech Stack

* **Python ≥ 3.13**
* **Model Context Protocol (MCP)**
* **Pydantic v2**
* **HTTPX**
* **UV** (dependency management)

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YaswanthBabuK/Swiggy-mcp-clone.git
cd Swiggy-mcp-clone
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -e .
```

---

## ▶️ Running the MCP Server

```bash
python main.py
```

The server exposes **AI-callable tools** compatible with MCP-enabled clients (Claude, OpenAI agents, etc.).

---

## 🤖 Example Use Cases

* Retrieve customer details by email
* Fetch all orders for a customer
* Check order delivery status
* Handle late delivery scenarios
* Provide refund eligibility logic
* Simulate customer care workflows

---

## 🧪 Notebooks

The `notebooks/` folder contains:

* Pydantic model validation examples
* Data structure experimentation

Useful for understanding schema behavior and tool responses.

---

## 🎯 Learning Goals

This project demonstrates:

* Agent-tool communication using MCP
* Clean backend architecture for AI systems
* Schema-first development using Pydantic
* Designing AI-friendly APIs

---

## 📌 Future Enhancements

* Add authentication simulation
* Persist data using a database
* Add streaming tool responses
* Integrate with real LLM clients
* Add test coverage

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Yaswanth Babu Kamepalli**
Aspiring **GenAI & Agentic AI Developer**

🔗 GitHub: [https://github.com/YaswanthBabuK](https://github.com/YaswanthBabuK)

````

---

## ✅ What to do next

1. Save this as **README.md**
2. Run:
```bash
git add README.md
git commit -m "Add detailed project README"
git push
````

---

If you want, I can also:

* 🔥 Rewrite this for **internship applications**
* 🎯 Add **architecture diagram**
* 🧠 Make it **ATS / recruiter optimized**
* 🤖 Add **example MCP tool calls**

Just tell me 👍
