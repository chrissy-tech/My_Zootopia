import json

# read the HTML template
with open("animals_template.html", "r", encoding="utf-8") as file:
    template = file.read()

# Load the animal Data
with open("animals_data.json", "r") as file:
    animals_data = json.load(file)

def serialize_animals(animals_data):
    output = "" # define an empty string
    for animal in animals_data:
        name_animal = animal.get("name")
        characteristics_animal = animal.get("characteristics", {})
        diet_animal = characteristics_animal.get("diet")
        type_animal = characteristics_animal.get("type")
        location_animal = animal.get("locations", [])
        first_location = location_animal[0] if location_animal else ""
        output += '<li class="cards__item">\n'
        output += f'    <div class="card__title">{name_animal}</div>\n'
        output += '    <p class="card__text">'
        output += f'<strong>Diet:</strong> {diet_animal}<br/>\n'
        output += f'<strong>Location:</strong> {first_location}<br/>\n'
        if type_animal:  # nur ausgeben, wenn vorhanden
            output += f'<strong>Type:</strong> {type_animal}<br/>\n'
        output += '    </p></li>\n'
    return output


output = serialize_animals(animals_data)
final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(final_html)