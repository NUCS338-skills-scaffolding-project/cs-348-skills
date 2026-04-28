# CS 348 TA Assistant

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Get a Gemini API key

Go to [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey), sign in with your Google account, and create a new API key. It's free.

### 3. Set the API key

**Mac / Linux:**
```bash
export GEMINI_API_KEY="your-key-here"
```

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY = "your-key-here"
```

### 4. Start the server

```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

> The API key must be set in the same terminal session before running `python app.py`. You'll need to set it again each time you open a new terminal.
