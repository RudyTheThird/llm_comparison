
import requests
import json
import csv
import os
import time

# Constants
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY")

# Models to Compare
MODELS = {
    "gpt-4": "openai/gpt-4",
    "claude-2": "anthropic/claude-2",
    "gemini-pro": "google/gemini-pro"
}

# Load prompts
with open('prompts.json', 'r') as f:
    PROMPTS = json.load(f)

def query_model(model, prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error querying {model}: {e}")
        return "ERROR"

def evaluate_response(response, metric):
    # Placeholder: Simulate scoring logic
    return len(response) % 10 + 1  # Example scoring logic

def main():
    results = []
    for metric, prompt in PROMPTS.items():
        for model_name, model_id in MODELS.items():
            print(f"Testing {model_name} for {metric}...")
            response = query_model(model_id, prompt)
            score = evaluate_response(response, metric)
            results.append([model_name, metric, response, score])
            time.sleep(1)  # Avoid rate-limiting

    # Write results to CSV
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Model', 'Metric', 'Response', 'Score'])
        writer.writerows(results)

    print("Comparison complete. Results saved to results.csv")

if __name__ == "__main__":
    main()
