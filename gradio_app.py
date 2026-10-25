
import os
import gradio as gr
import base64
import mimetypes

from pathlib import Path
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
# STEP 3: DEFINE SYSTEM PROMPT
# ==========================================

system_prompt = """
You are an expert AI chef and recipe generator.

Analyze the uploaded image carefully.

First, identify the main food ingredients
visible in the image.

Then suggest exactly 3 different recipes
using those ingredients.

For each recipe provide:

1. Recipe name
2. Ingredients with quantities
3. Additional ingredients required
4. Step-by-step cooking instructions
5. Approximate cooking time

Make the recipes beginner-friendly.

Do not claim uncertain ingredients are
definitely present.

Format the response clearly using Markdown.
"""


# ==========================================
# STEP 4: IDENTIFY INGREDIENTS AND RECIPES
# ==========================================

def identify_ingredients(image_path):

    print("Submit button clicked!")

    if not image_path:
        return "Please upload an image first."

    try:
        # Identify uploaded image MIME type
        mime_type, _ = mimetypes.guess_type(
            image_path
        )

        mime_type = mime_type or "image/jpeg"

        # Convert uploaded image to Base64
        with open(image_path, "rb") as file:
            raw_binary = file.read()

        image_base64 = base64.b64encode(
            raw_binary
        ).decode("utf-8")

        print("Image uploaded successfully!")

        # Prepare message for Gemini
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
                            "Identify the ingredients "
                            "visible in this image and "
                            "generate exactly 3 recipes."
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

        print("Sending request to Gemini...")

        # Generate recipes
        response = model.invoke(message)

        print("Recipes generated successfully!")

        return response.text

    except Exception as e:
        print("Error:", repr(e))
        return f"**Error generating recipes:** {str(e)}"


# ==========================================
# STEP 5: CREATE GRADIO INTERFACE
# ==========================================

demo = gr.Interface(
    fn=identify_ingredients,

    inputs=gr.Image(
        type="filepath",
        label="Upload Ingredients Image",
        sources=["upload", "webcam", "clipboard"]
    ),

    outputs=gr.Markdown(
        label="AI Generated Recipes"
    ),

    title="AI Recipe Generator",

    description=(
        "Upload any image of ingredients "
        "and get 3 AI-generated recipes "
        "with step-by-step instructions."
    ),

    flagging_mode="never"
)


# ==========================================
# STEP 6: LAUNCH APPLICATION
# ==========================================

if __name__ == "__main__":
    demo.launch(debug=True)