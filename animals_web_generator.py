import json

def load_data(file_path):
    """Load a JSON file."""
    try:
        with open(file_path, "r") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return []

def serialize_animal(animal):
    """Serialize an animal object into HTML."""
    output = '<li class="cards__item">\n'
    if 'name' in animal:
        output += f'<div class="card__title">{animal["name"]}</div>\n'
    output += '<p class="card__text">\n'
    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
    if 'locations' in animal and len(animal['locations']) > 0:
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
    if 'type' in animal:
        output += f"<strong>Type:</strong> {animal['type']}<br/>\n"
    output += '</p>\n</li>\n'
    return output

# Load animal data
animals_data = load_data('animals_data.json')

# Print data for debugging purposes
for animal in animals_data:
    if 'name' in animal:
        print(f"Name: {animal['name']}")
    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        print(f"Diet: {animal['characteristics']['diet']}")
    if 'locations' in animal and len(animal['locations']) > 0:
        print(f"Location: {animal['locations'][0]}")
    if 'type' in animal:
        print(f"Type: {animal['type']}")
    print()

# Read HTML template
try:
    with open('animals_template.html', 'r') as template_file:
        template_content = template_file.read()
except FileNotFoundError:
    print("Error: The HTML template file 'animals_template.html' was not found.")
    template_content = ''

# Generate HTML output
output = ''.join(serialize_animal(animal) for animal in animals_data)

# Replace placeholder in template
if template_content:
    updated_html = template_content.replace('__REPLACE_ANIMALS_INFO__', output)

    # Write updated HTML to file
    with open('animals.html', 'w') as output_file:
        output_file.write(updated_html)
    print("HTML file 'animals.html' has been generated.")
else:
    print("HTML template content is empty. Cannot generate HTML output.")