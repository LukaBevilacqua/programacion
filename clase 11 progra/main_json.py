import json

persona_string = '{"id":1,"nombre":"Juan","edad":40}'
print(type(persona_string))
print(persona_string)

persona_dict = json.loads(persona_string) # convierte un str en un dict
print(type(persona_dict))
print(persona_dict)
print(persona_dict['nombre'])

persona_json = json.dumps(persona_dict, indent=2) # convierte un dict en un str
print(persona_json)
print(type(persona_json))