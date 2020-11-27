RESOURCE_PACK_NAME = "fix_dark_text"
RESOURCE_PACK_DESCRIPTION = "Dark mode fix inventory text all languages"

import json, os, shutil

def clearDir(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            os.remove(os.path.join(directory, filename))

LANG_PATH = os.path.join(RESOURCE_PACK_NAME, "assets", "minecraft", "lang")

if not os.path.exists(RESOURCE_PACK_NAME): os.mkdir(RESOURCE_PACK_NAME)
if not os.path.exists(os.path.join(RESOURCE_PACK_NAME, "assets")): os.mkdir(os.path.join(RESOURCE_PACK_NAME, "assets"))
if not os.path.exists(os.path.join(RESOURCE_PACK_NAME, "assets", "minecraft")): os.mkdir(os.path.join(RESOURCE_PACK_NAME, "assets", "minecraft"))
if not os.path.exists(LANG_PATH): os.mkdir(LANG_PATH)

clearDir(LANG_PATH)

for root, dirs, filenames in os.walk("original_lang"):
    for filename in filenames:
        name, extension = os.path.splitext(filename)
        if extension.lower() == ".json":
            with open(os.path.join("original_lang", filename)) as file:
                original_lang_dict = json.load(file)
            with open("base.json") as file:
                lang_dict = json.load(file)
            for key in lang_dict.copy():
                try:
                    lang_dict[key] += original_lang_dict[key]
                except KeyError:
                    del lang_dict[key]
            with open(os.path.join(LANG_PATH, filename), "w") as file:
                json.dump(lang_dict, file, indent=4, sort_keys=True)
                print("Generated", name)

with open(os.path.join(RESOURCE_PACK_NAME, "pack.mcmeta"), "w") as file:
    json.dump({"pack": {"pack_format": 6, "description": RESOURCE_PACK_DESCRIPTION}}, file, indent=4, sort_keys=True)

shutil.make_archive(RESOURCE_PACK_NAME, "zip", RESOURCE_PACK_NAME)
