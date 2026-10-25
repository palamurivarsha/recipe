
import os
import base64
import mimetypes
import tkinter as tk

from pathlib import Path
from tkinter import filedialog
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


# ==========================================
# STEP 1: LOAD GEMINI API KEY
# ==========================================

env_path = Path(__file__).resolve().parent / ".env"

load_dotenv(dotenv_path=env_path, override=True)

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY is missing. "
        "Please add your Gemini API key to the .env file."
    )

print("Gemini API key loaded successfully!")


# ==========================================
# STEP 2: INITIALIZE GEMINI MODEL
# ==========================================

model = init_chat_model(
    "gemini-3.8-flash",
    model_provider="google_genai",
    api_key=api_key
)

print("Gemini model initialized successfully!")


# ==========================================
# STEP 3: UPLOAD / SELECT IMAGE
# ==========================================

def select_image():

    root = tk.Tk()
    root.withdraw()

    image_path = filedialog.askopenfilename(
        title="Select Ingredients Image",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.webp")
        ]
    )

    root.destroy()

    return image_path


# ==========================================
# STEP 4: CONVERT IMAGE TO BASE64
# ==========================================

def convert_image_to_base64(image_path):

    mime_type, _ = mimetypes.guess_type(image_path)

    if mime_type is None:
        mime_type = "image/jpeg"

    with open(image_path, "rb") as file:
        raw_binary = file.read()

    image_base64 = base64.b64encode(
        raw_binary
    ).decode("utf-8")

    return image_base64, mime_type


# ==========================================
# STEP 5: DEFINE SYSTEM PROMPT
# ==========================================

system_prompt = """
You are an expert AI chef and recipe generator.

Analyze the uploaded image carefully.

Your tasks:

1. Identify all visible food ingredients.
2. Suggest exactly 3 different recipes using
   the identified ingredients.
3. For each recipe provide:

   - Recipe name
   - Ingredients with quantities
   - Additional ingredients required
   - Step-by-step cooking instructions
   - Approximate cooking time

4. Keep recipes beginner-friendly.
5. Do not assume uncertain ingredients are definitely present.
6. Format the response clearly using Markdown.
"""


# ==========================================
# STEP 6: GENERATE RECIPES
# ==========================================

def generate_recipes(image_path):

    image_base64, mime_type = convert_image_to_base64(
        image_path
    )

    message = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "Identify the ingredients in this "
                        "image and generate exactly 3 recipes."
                    )
                },
                {
                    "type": "image",
                    "base64": image_base64,
                    "mime_type": mime_type
                }
            ]
        }
    ]

    print("\nAnalyzing ingredients...")
    print("Generating recipes...\n")

    response = model.invoke(message)

    return response.text


# ==========================================
# STEP 7: MAIN PROGRAM
# ==========================================

def main():

    print("\n===== AI RECIPE GENERATOR =====\n")

    image_path = select_image()

    if not image_path:
        print("No image selected.")
        return

    print("Image selected successfully!")

    try:
        recipes = generate_recipes(image_path)

        print("\n===== GENERATED RECIPES =====\n")
        print(recipes)

    except Exception as e:
        print("\nError generating recipes:")
        print(str(e))


# ==========================================
# STEP 8: RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    main()