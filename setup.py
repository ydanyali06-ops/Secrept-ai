from pathlib import Path

# پوشه اصلی پروژه
root = Path("gemini_ai")

# ساخت پوشه‌ها
backend = root / "backend"
frontend = root / "frontend"

backend.mkdir(parents=True, exist_ok=True)
frontend.mkdir(parents=True, exist_ok=True)

# فایل‌های Backend
(backend / "main.py").touch()
(backend / "data.json").write_text("[]", encoding="utf-8")
(backend / "requirements.txt").write_text(
    "google-genai\n",
    encoding="utf-8"
)

# فایل صفحه چت
(frontend / "index.html").touch()

print("✅ پروژه ساخته و مرتب شد!")

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
