# Simple A2A Agent Demo

This repository demonstrates a **basic Agent-to-Agent (A2A) SDK** setup with:
- A simple agent (server)
- A test client that interacts with the agent

This project provides a minimal and easy-to-understand example of A2A communication.

---

## 📌 Prerequisites (Windows)

Before running the project, ensure the following are installed:

- **Python 3.13** (Required for `a2a-sdk`)
- **uv** – Python package management tool  

Install uv from:
https://docs.astral.sh/uv/getting-started/installation/

Verify installations:
```powershell
python --version
uv --version

---

# Create Virtual Environment and Install Dependencies
## Open PowerShell in the project directory and run:

uv venv
.venv\Scripts\activate

#Run the Agent (Server)
uv run .
The agent will start running at:
http://localhost:9999

# Run the test_client
Open a new PowerShell window and run:

uv run test_client.py

You will see the client communicating with the agent in the terminal.
