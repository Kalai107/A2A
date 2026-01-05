# Finance Assistant using ADK

This project is a simple **Finance Assistant Agent** built using **Google Agent Development Kit (ADK)**.  
The agent answers basic finance-related questions through a web interface.

---

## 📁 Project Structure


---

## 📦 Requirements

- Python 3.10 or above
- Virtual environment (venv)
- Google ADK
- Google API Key

---

## ⚙️ Setup Instructions (Windows)

### 1️⃣ Create a virtual environment
```powershell
uv venv

.venv\Scripts\activate

python -m pip install -r requirements.txt

GOOGLE_API_KEY=your_google_api_key_here

adk web

http://127.0.0.1:8000
