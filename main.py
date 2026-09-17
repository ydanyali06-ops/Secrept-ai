from google import genai

API_KEY = "YOUR_GEMINI_API_KEY"

client = genai.Client(api_key=API_KEY)

print("AI آماده است!")
print("برای خروج بنویس: خروج")

while True:
    user = input("تو: ")

    if user == "خروج":
        print("AI: خداحافظ 👋")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
تو یک دستیار فارسی‌زبان هستی.
حرف کاربر را تکرار نکن.
به سؤال او یک پاسخ طبیعی و مفید بده.

کاربر:
{user}
"""
    )

    print("AI:", response.text)
