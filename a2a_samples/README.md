# 🕒 TellTimeAgent – Google A2A Protocol Demo

- A simple A2A server agent (`TellTimeAgent`) built with Flask
- A client agent that discovers and communicates with it
- Full compliance with the A2A message structure and discovery flow

---

## 🚀 Features

- Implements A2A discovery via `/.well-known/agent.json`
- Exposes a `tasks/send` endpoint for receiving tasks
- Replies to queries with the current system time
- Client generates a task and parses the response using A2A conventions

---

## 📂 Project Structure

```
a2a_samples/
├── server/
│   └── tell_time_server.py       # Flask-based A2A server agent
├── client/
│   └── time_client.py            # A2A client agent that queries the server
```

---

## 🧪 How to Run

### 1. Install dependencies

```bash
pip install flask requests
```

### 2. Start the server

```bash
cd a2a_samples/server
python3 tell_time_server.py
```

### 3. Run the client

In a separate terminal:

```bash
cd a2a_samples/client
python3 time_client.py
```

### ✅ Output

```
Connected to: TellTimeAgent – Tells the current time when asked.
Agent says: The current time is: 2025-04-16 22:10:45
```

---

