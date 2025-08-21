import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def get_car_ai_bio(model_name, brand, factory_year):
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("Chave de API não encontrada.")

        genai.configure(api_key=api_key)

        ai_model = genai.GenerativeModel('gemini-2.5-flash')

        prompt = f"""
Crie um parágrafo de marketing curto e atraente, com no máximo 250 caracteres, para a venda de um carro {brand} {model_name} do ano {factory_year}.

O texto deve ser convincente e focado nos pontos fortes do veículo, como seu design, conforto ou performance.

**Regras estritas:**
- O texto NÃO PODE conter o preço ou qualquer símbolo monetário (como R$).
- O texto NÃO PODE conter a palavra "Genai" ou qualquer menção à inteligência artificial.
- O tom deve ser profissional e vendedor.
"""
        response = ai_model.generate_content(prompt)
        
        return response.text.strip()

    except Exception as e:
        print(f"Ocorreu um erro ao chamar a API: {e}")
        return "Descrição gerada por IA indisponível no momento."