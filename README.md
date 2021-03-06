# Fix dark mode for Vanillatweaks

Vanillatweaks' dark mode inventory text is not white for other languages than english. To fix your dark mode, simply download [`fix_dark_text.zip`](https://github.com/sigurdo/fix_vanillatweaks_dark_mode/raw/master/fix_dark_text.zip) to your resource pack folder and add it to your applied resource packs. The zip file is generated by the python script `main.py`.

## What the script does

The script generates a resource pack directory and zip file that you can add on top of the vanillatweaks resource pack to get white text in inventory on other languages than english.

## How the script works

The script takes a directory called `original_langs` that contains the original language json from the default minecraft resource pack.

It also takes a file called `base.json` that contains the language entries we need to modify with white color prefixes.

Then it loops all entries in `base.json` for each file in `original_langs` and appends the name of the item from `original_langs` to the dictionary generated from `base.json`.

The results are saved in a folder called `<RESOURCE_PACK_NAME>/assets/minecraft/lang`.

At last the script also generates a `pack.mcmeta` file and saves the resource pack as a zip file.
