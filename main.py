import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    print("Hello from aiagent!")
    # Use the client to get a response

    if len(sys.argv) < 2:
        print("Error: No prompt provided.\nUsage: uv run main.py \"Your prompt here\" [--verbose]")
        sys.exit(1)
    
    # Detect and remove --verbose flag
    verbose = False

    if "--verbose" in sys.argv:
        verbose = True
        sys.argv.remove("--verbose")
   
    user_prompt = " ".join(sys.argv[1:])


    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
    	model = "gemini-2.0-flash-001",
    	contents = messages
	)

    print(response.text)
                   
    # Print token usage
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
