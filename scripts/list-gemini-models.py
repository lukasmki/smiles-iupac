from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()

print("List of models that support batchGenerateContent:")
for m in client.models.list():
    for action in m.supported_actions:
        if action == "batchGenerateContent":
            print(m.name)
print()

print("List of models that support countTokens:")
for m in client.models.list():
    for action in m.supported_actions:
        if action == "countTokens":
            print(m.name)
print()