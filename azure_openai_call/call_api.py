from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = "https://**.services.ai.azure.com/openai/v1"
deployment_name = "model_name"
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider, 
  
)

response = client.responses.create(
    model=deployment_name,
    input="What is the capital of France?",
    temperature=1,
    #Max token must be 16
    max_output_tokens=20,  # renamed; 1 is too low, you'll get truncated/empty output
)


print(f"answer: {response.output[0]}")
