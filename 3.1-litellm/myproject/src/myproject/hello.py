from litellm import completion
import os

# Set your API keys
os.environ["OPENAI_API_KEY"] = "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"
os.environ["GEMINI_API_KEY"] = "AIzaSyBZ-z07-FMMpuXI2xcUOzpoTuUgy8iTBMg"

def query_model(model_name, label, message):
    try:
        response = completion(
            model=model_name,
            messages=[{"content": message, "role": "user"}]
        )
        print(f"\n{label} Response:\n{response['choices'][0]['message']['content']}")
    except Exception as e:
        print(f"Error with {label}: {e}")

def main():
    msg = input("Enter your message: ")
    query_model("openai/gpt-4o", "🧠 GPT-4o", msg)
    query_model("gemini/gemini-1.5-flash", "🔮 Gemini 1.5", msg)
    query_model("gemini/gemini-2.0-flash-exp", "✨ Gemini 2.0", msg)

if __name__ == "__main__":
    main()
