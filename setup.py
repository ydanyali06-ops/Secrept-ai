from pathlib import Path

# پوشه اصلی
root = Path("gemini_ai")

# پوشه‌ها
backend = root / "backend"
frontend = root / "frontend"

backend.mkdir(parents=True, exist_ok=True)
frontend.mkdir(parents=True, exist_ok=True)

# فایل‌های لازم
files = {
    backend / "main.py": "# کد Gemini API اینجا قرار می‌گیرد\n",
    backend / "data.json": "[]\n",
    backend / "requirements.txt": "google-genai\n",
    frontend / "index.html": "<!DOCTYPE html>\n<html><body><h1>Gemini AI</h1></body></html>\n",
}

for file, content in files.items():
    if not file.exists():
        file.write_text(content, encoding="utf-8")

print("✅ پروژه مرتب شد!")
print("""
gemini_ai/
├── backend/
│   ├── main.py
│   ├── data.json
│   └── requirements.txt
│
└── frontend/
    └── index.html
""")
