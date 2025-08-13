import json

# read the HTML template
with open("animals_template.html", "r") as file:
    template = file.read()

# Load the animal Data
with open("animals_data.json", "r") as file:
    animals_data = json.load(file)


output = "" # define an empty string
for animal in animals_data:
    name_animal = animal.get("name")
    characteristics_animal = animal.get("characteristics")
    diet_animal = characteristics_animal.get("diet")
    type_animal = characteristics_animal.get("type")
    location_animal = animal.get("locations", [])
    first_location = location_animal[0]


    # append information to each string
    output += '<li class="cards__item">'
    output += f"Name: {name_animal}<br/>\n"
    output += f"Diet: {diet_animal}<br/>\n"
    output += f"Location: {first_location}<br/>\n"
    if type_animal:
        output += f"Type: {type_animal}<br/>\n\n"
    else:
        pass

    output += '</li>\n\n'

final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as file:
    file.write(final_html)