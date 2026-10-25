# recipe
# 🍳 AI Recipe Generator Using Gemini

An AI-powered recipe recommendation application that identifies food ingredients from uploaded images and generates three personalized recipe suggestions using Google's Gemini multimodal AI model.

## 📌 Project Overview

The AI Recipe Generator helps users discover recipes based on ingredients they already have.

Instead of manually entering ingredients, users can upload an image of available food items. The application uses Gemini's image-understanding capabilities to identify visible ingredients and recommend three recipes with cooking instructions.

## ✨ Features

* **Image-Based Ingredient Recognition:** Upload an image containing food ingredients.
* **AI-Powered Recipe Generation:** Generate three recipe suggestions using Gemini.
* **Step-by-Step Instructions:** Receive cooking instructions for each recipe.
* **Ingredient Lists:** View required ingredients and additional items needed.
* **Cooking Time Estimates:** Get approximate preparation and cooking times.
* **Interactive Web Interface:** Upload images and view recipes using Gradio.
* **Standalone Python Script:** Test recipe generation using a local image-selection window.

## 🛠️ Technologies Used

| Technology        | Purpose                                   |
| ----------------- | ----------------------------------------- |
| Python            | Application development                   |
| Google Gemini API | Image understanding and recipe generation |
| LangChain         | Integration with Gemini models            |
| Gradio            | Interactive web interface                 |
| Python-dotenv     | Environment variable management           |
| Base64            | Image encoding for model requests         |

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/palamurivarsha/recipe.git
cd recipe
```

### 2. Create a virtual environment

Use Python 3.12.

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

Generate your API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Security:** Never commit your `.env` file or expose your API key publicly.

### 5. Run the Gradio application

```bash
python gradio_app.py
```

Open the local URL displayed in your terminal, usually:

`http://127.0.0.1:7860`

### 6. Run the standalone Python application (optional)

```bash
python text_query_gemini.py
```

A file-selection window will appear. Select an image containing ingredients to generate recipes in your terminal.

## 🔄 How It Works

1. The user uploads or selects an image containing food ingredients.
2. Python reads the image and converts it into Base64 format.
3. The application sends the image and recipe-generation instructions to Gemini through LangChain.
4. Gemini identifies visible ingredients and generates three recipes.
5. The application displays recipe names, ingredient lists, cooking instructions, and estimated cooking times.

## 📷 Application Screenshots

Add screenshots of your running Gradio application here.

Recommended screenshots:

* Ingredient image upload screen
* Generated recipe results

## 📂 Project Structure

```text
recipe/
├── gradio_app.py
├── text_query_gemini.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

The `.env` and `.venv` files are kept locally and excluded from Git.

## 🚀 Future Enhancements

* Generate ingredient illustrations for each recipe.
* Support dietary preferences such as vegetarian, vegan, and gluten-free.
* Provide estimated nutritional information.
* Suggest recipes based on preparation time.
* Allow users to save favorite recipes.
* Add multilingual recipe recommendations.
* Deploy the application for online access.

## ⚠️ Limitations

* Ingredient identification depends on image quality and visibility.
* Gemini may occasionally misidentify ingredients.
* Suggested recipes may require additional ingredients.
* AI-generated cooking instructions should be checked for food safety.
* Gemini API access and model availability may change.

## 👩‍💻 Author

**Varsha Palamuri**

GitHub: [palamurivarsha](https://github.com/palamurivarsha)

## 📄 License

No license has been specified yet. Add a license if you want to define how others may reuse or modify this project.
