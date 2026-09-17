from google import genai

client = genai.Client(api_key="API_KEY_خودت")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words"
)

print(interaction.output_text)
