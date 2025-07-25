import os
from dotenv import load_dotenv

from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constant import MODEL

from autogen_ext.models.openai._model_info import ModelInfo

model_info = ModelInfo(
    name="your_custom_model_name",
    completion_type="chat",
    max_tokens=8192,
    vision=False,
    function_calling=None,
    json_output=False,
    family="gemini",
    # Add any other necessary fields here
)

load_dotenv()
# api_key = os.getenv('OPENAI_API_KEY')
api_key = os.getenv('GOOGLE_API_KEY')


def get_model_client():
    model_client = OpenAIChatCompletionClient( model=MODEL, model_info=model_info, api_key=api_key)
    return model_client


