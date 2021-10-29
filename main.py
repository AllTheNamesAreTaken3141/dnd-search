import requests as re

url_host = "https://www.dnd5eapi.co/api/"
endpoint = "spells/"

def split_at_comma(txt):
    split_txt = []
    current_word = ""
    for i, item in enumerate(txt):
        if len(current_word) == 0 and item == " ":
            continue
        if item == ",":
            split_txt.append(current_word)
            current_word = ""
        else:
            current_word += item
    
    split_txt.append(current_word)
    return split_txt

def replace_spaces(txt, char):
    new_txt = ""
    for i in txt:
        if i == " ":
            new_txt += char
        else:
            new_txt += i
    return new_txt

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
  print("\n  School: " + spell["school"]["name"])
  print("\n  Classes:")
  for i in spell["classes"]:
   print("    " + i["name"])

def display_search(search, query):
  if (search["count"] == 0):
    print("No results found for \"" + query + "\"")
  else:
    print(str(search["count"]) + " results found for \"" + query + "\":")
    for i in search["results"]:
      print("  " + i["name"])

def display_monster(monster):
  print(monster["name"] + ":")
  print("  Size: " + monster["size"])
  print("\n  Type: " + monster["type"])
  print("\n  Alignment: " + monster["alignment"])
  print("\n  AC: " + str(monster["armor_class"]))
  print("\n  HP: " + str(monster["hit_points"]))
  print("\n  Hit Dice: " + monster["hit_dice"])
  print("\n  Speed:")
  for i in monster["speed"]:
    print("    " + i + ": " + monster["speed"][i])
  print("\n  Stats:")
  print("    STR: " + str(monster["strength"]))
  print("    DEX: " + str(monster["dexterity"]))
  print("    CON: " + str(monster["constitution"]))
  print("    WIS: " + str(monster["wisdom"]))
  print("    INT: " + str(monster["intelligence"]))
  print("    CHR: " + str(monster["charisma"]))


class CmndLine:
    
  def __init__(self, host):
    self.input = ""
    self.host_url = host
    self.endpoint = ""
    self.query = ""
    self.url = ""
    self.response = None
  
  def get_input(self, txt):
    self.input = input(txt)

  def display_response(self):
    if self.response.status_code == 200:
      if self.input[0] == "spells":
        display_spell(self.response.json())
      elif self.input[0] == "search":
        display_search(self.response.json(), self.input[2])
      elif self.input[0] == "monsters":
        display_monster(self.response.json())
    else:
      print("Something went wrong.")
      
  def search_api(self):
    self.endpoint = replace_spaces(self.input[1], "-") + "/"
    self.query = "?name=" + replace_spaces(self.input[2], "+")
    self.url = self.host_url + self.endpoint + self.query
    self.response = re.get(self.url)
  
  def get_api_item(self):
    self.endpoint = replace_spaces(self.input[0], "-") + "/"
    self.query = replace_spaces(self.input[1], "-")
    self.url = self.host_url + self.endpoint + self.query
    self.response = re.get(self.url)

  def parse_input(self):
    self.input = split_at_comma(self.input)
    if self.input[0] == "search":
      try:
        self.search_api()
      except:
        print("Something went wrong.")
        return 0
    else:
      try:
        self.get_api_item()
      except:
        print("Something went wrong.")
        return 0
    self.display_response()

cmnd_line = CmndLine(url_host)

while True:
  cmnd_line.get_input(">>")
  cmnd_line.parse_input()