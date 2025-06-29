import google.generativeai as genai

genai.configure(api_key="SUA_CHAVE_AQUI")

def query_gemini(prompt, context):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
    response = model.generate_content(f"{context}\nUsuário: {prompt}")
    return response.text
