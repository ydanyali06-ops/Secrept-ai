import os

# ==============================
# ساخت پروژه کامل AI
# ==============================

PROJECT = "MyAI"

files = {

"ai.py": r'''
import json
import os
import difflib
import ast
import operator

MEMORY_FILE = "memory.json"

memory = {
    "سلام": "سلام! 👋",
    "خوبی": "مرسی، خوبم 😄",
    "اسمت چیه": "من MyAI هستم 🤖",
    "تو چی هستی": "من یک هوش مصنوعی قابل یادگیری هستم.",
    "ممنون": "خواهش می‌کنم ❤️",
    "خداحافظ": "خداحافظ 👋"
}

def load_memory():
    global memory

    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, dict):
                memory.update(data)

        except:
            pass


def save_memory():
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)


def clean(text):
    return text.strip().lower().replace("ي", "ی").replace("ك", "ک")


def teach(text):

    if "|" not in text:
        return "فرمت درست:\nیاد بگیر: سؤال | جواب"

    q, a = text.split("|", 1)

    q = q.replace("یاد بگیر:", "").strip()
    a = a.strip()

    if not q or not a:
        return "سؤال یا جواب خالی است."

    memory[clean(q)] = a
    save_memory()

    return "✅ یاد گرفتم."


def calculate(expression):

    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow
    }

    try:
        tree = ast.parse(expression, mode="eval")

        def solve(node):

            if isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value
                raise ValueError()

            if isinstance(node, ast.BinOp):
                return operators[type(node.op)](
                    solve(node.left),
                    solve(node.right)
                )

            if isinstance(node, ast.UnaryOp):
                value = solve(node.operand)

                if isinstance(node.op, ast.USub):
                    return -value

                return value

            raise ValueError()

        return solve(tree.body)

    except:
        return None


def image_info(path):

    if not os.path.exists(path):
        return "❌ عکس پیدا نشد."

    try:
        from PIL import Image

        img = Image.open(path)

        return (
            "🖼️ عکس دریافت شد\n"
            f"فرمت: {img.format}\n"
            f"اندازه: {img.width} × {img.height}\n"
            f"رنگ: {img.mode}"
        )

    except ImportError:
        return "برای عکس این دستور را نصب کن:\npip install pillow"

    except Exception as e:
        return "خطا: " + str(e)


def answer(message):

    text = clean(message)

    # آموزش
    if text.startswith("یاد بگیر:"):
        return teach(message)

    # عکس
    if text.startswith("عکس:"):
        path = message.split(":", 1)[1].strip()
        return image_info(path)

    # ماشین حساب
    if text.startswith("حساب کن:"):
        expression = message.split(":", 1)[1].strip()

        result = calculate(expression)

        if result is None:
            return "❌ محاسبه نامعتبر است."

        return "🧮 جواب: " + str(result)

    # راهنما
    if text == "/help":
        return """
🤖 MyAI

دستورات:

/help
راهنما

/memory
تعداد حافظه

/clear
پاک کردن حافظه

یاد بگیر: سؤال | جواب

عکس: مسیر عکس

حساب کن: 20 + 30 * 2
"""

    # حافظه
    if text == "/memory":
        return f"🧠 {len(memory)} مورد در حافظه دارم."

    # پاک کردن
    if text == "/clear":
        memory.clear()
        save_memory()
        return "🧹 حافظه پاک شد."

    # پاسخ مستقیم
    if text in memory:
        return memory[text]

    # پاسخ مشابه
    keys = list(memory.keys())

    if keys:

        matches = difflib.get_close_matches(
            text,
            keys,
            n=1,
            cutoff=0.55
        )

        if matches:
            return memory[matches[0]]

    # جستجوی بخشی
    for q, a in memory.items():

        if q in text or text in q:
            return a

    return (
        "🤔 این را هنوز بلد نیستم.\n\n"
        "برای یاد دادن بنویس:\n"
        "یاد بگیر: سؤال | جواب"
    )


def main():

    load_memory()

    print("=" * 45)
    print("🤖 MyAI روشن شد")
    print("🧠 حافظه: روشن")
    print("📚 یادگیری: روشن")
    print("🧮 ماشین حساب: روشن")
    print("🖼️ عکس: روشن")
    print("=" * 45)

    while True:

        try:
            msg = input("\nشما: ")

        except KeyboardInterrupt:
            break

        if clean(msg) in ["خروج", "exit", "quit"]:
            print("AI: خداحافظ 👋")
            break

        if msg.strip():
            print("AI:", answer(msg))


if __name__ == "__main__":
    main()
''',

"requirements.txt": r'''
Pillow
''',

"README.txt": r'''
MyAI

اجرای برنامه:

python ai.py

برای قابلیت عکس:

pip install -r requirements.txt

نمونه:

سلام

یاد بگیر: اسم من چیست؟ | اسم تو علی است

اسم من چیست؟

حساب کن: 100 + 50 * 2

عکس: photo.jpg
'''
}


# ==============================
# ساخت پوشه
# ==============================

os.makedirs(PROJECT, exist_ok=True)

for filename, content in files.items():

    path = os.path.join(PROJECT, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ساخت پوشه عکس
os.makedirs(os.path.join(PROJECT, "images"), exist_ok=True)

print()
print("================================")
print("✅ پروژه کامل ساخته شد!")
print("================================")
print()
print("📁 پوشه:", PROJECT)
print()
print("فایل‌ها:")

for filename in files:
    print("  ├──", filename)

print("  └── images/")
print()
print("برای اجرا:")
print()
print("cd MyAI")
print("python ai.py")
print()
print("🤖 AI آماده است.")
