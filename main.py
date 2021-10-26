import requests as re

url_host = "https://www.dnd5eapi.co/api/"
endpoint = "spells/"

def display_spell(spell):
  print(spell["name"] + ":")
  print("  Level: " + str(spell["level"]))
  print("\n  Description:")
  for i in spell["desc"]:
    print(i)
  try:
    print("\n  At Higher Levels: " + spell["higher_level"][0])
  except:
    pass
  print("\n  Range: " + spell["range"])
  print("  Components: " + "".join(spell["components"]))
  if "M" in spell["components"]:
    print("    Materials: " + spell["material"])
  print("\n  Duration: " + spell["duration"])
  print("\n  Casting Time: " + spell["casting_time"])
  try:
    print("\n  Damage: ")
    print("    Damage Type: " + spell["damage"]["damage_type"]["name"])
    if spell["damage"]["damage_at_slot_level"]["8"] == spell["damage"]["damage_at_slot_level"]["9"]:
      print("    Damage: " + spell["damage"]["damage_at_slot_level"]["1"])
    else:
      print("    Damage by Slot Level:")
      for k in spell["damage"]["damage_at_slot_level"]:
        print("      " + k + ": " + spell["damage"]["damage_at_slot_level"][k])
  except:
    pass

while True:
  query = input("Enter a spell index: ")
  url = url_host + endpoint + query
  spell = re.get(url)
  display_spell(spell.json())