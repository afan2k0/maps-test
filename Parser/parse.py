import json
import re

def prune_duplicates(input_file, output_file):
    # Load the data from the JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Use a dictionary to prune duplicates based on 'place_id'
    pruned_data = {}
    for item in data:
        place_id = item.get('place_id')
        compound_code = item.get('plus_code', {}).get('compound_code', '')

        # Check if the compound_code contains "New Brunswick"
        if not re.search(r'new brunswick', compound_code, re.IGNORECASE):
            print(f"Skipped business: {item['name']} with compound_code: {compound_code}")
            continue

        if place_id:
            # If the place_id already exists in pruned_data, it's a duplicate
            if place_id in pruned_data:
                print(f"Duplicate business: {item['name']}")
            pruned_data[place_id] = item

    # Convert the dictionary values back to a list
    pruned_list = list(pruned_data.values())

    # Print the number of unique businesses
    print(f"Number of unique businesses after pruning: {len(pruned_list)}")

    # Write the pruned list to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(pruned_list, f, indent=2)

    print(f"Pruned data written to {output_file}")

# Usage
input_filename = 'maps-test\Parser\outputs.json'
output_filename = 'maps-test\Parser\pruned_outputs.json'
prune_duplicates(input_filename, output_filename)
