import openai
import json

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

def classify_business(business_name, business_types):
    """Classify business based on its name and types using OpenAI GPT API."""
    types_str = ', '.join(business_types)
    prompt = f"Based on the business name '{business_name}' and its types '{types_str}', classify it into one of the following categories: Food (Convenience), Food (restaurant), Food (grocery), Sporting Goods, Sporting Services, HABA Goods, HABA Services, Home Goods, Automotive, Entertainment, Electronics, Electronics Services, Liquor Store, Bar, Smoke Shop."
    response = openai.Completion.create(
      engine="gpt-3.5-turbo-instruct",
      prompt=prompt,
      max_tokens=50
    )
    return response.choices[0].text.strip()

def classify_businesses(input_file, output_file):
    # Load the pruned data from the JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Only process the first 10 items for testing
    test_data = data[:10]

    # Classify each business based on its name and types using the GPT API
    for item in test_data:
        name = item.get('name', '')
        types = item.get('types', [])
        classification = classify_business(name, types)
        item['classification'] = classification

    # Write the classified test data to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(test_data, f, indent=2)

    print(f"Classified data written to {output_file}")

# Usage
input_filename = 'maps-test\Parser\pruned_outputs.json'
output_filename = 'maps-test\Parser\classified_test_outputs.json'
classify_businesses(input_filename, output_filename)
