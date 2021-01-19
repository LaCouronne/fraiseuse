import os
import json
import re

from objects.barrel import Barrel
from objects.template import Template
from objects.drill import Drill
from objects.work import Work
from objects.margin import Margin

save_dir = "saves"

saves = {}


def load_saves():
    for filename in os.listdir(save_dir):
        with open(os.path.join(save_dir, filename)) as f:
            save = json.load(f)
            saves[save.get("name")] = Work(
                barrel=Barrel(
                    height=save.get("barrel_height"),
                    diameter=save.get("barrel_diameter"),
                ),
                template=Template(
                    width=save.get("template_width"),
                    height=save.get("template_height"),
                    nb_copy=save.get("template_nb_copy"),
                ),
                drill=Drill(
                    diameter=save.get("drill_diameter"),
                ),
                margin=Margin(
                    margin_x=save.get("margin_x"),
                    margin_y=save.get("margin_y"),
                )
            )


def save_work(name, work):

    assert isinstance(work, Work)

    save = {
        "name": name,
        "barrel_height": work.barrel.height,
        "barrel_diameter": work.barrel.diameter,
        "template_width": work.template.width,
        "template_height": work.template.height,
        "template_nb_copy": work.template.nb_copy,
        "drill_diameter": work.drill.diameter,
        "margin_x" : work.motif_margin_x,
        "margin_y" : work.motif_margin_y
    }

    base_filename = slugify(name)
    filename = base_filename + ".json"
    suffix = 1

    while True:
        try:
            f = open(os.path.join(save_dir, filename))
            f.close()
            filename = f"{base_filename}_{suffix}.json"
            suffix += 1

        except FileNotFoundError:
            with open(os.path.join(save_dir, filename), 'w') as outfile:
                json.dump(save, outfile)
            saves[save.get('name')] = save
            return


non_url_safe = ['"', '#', '$', '%', '&', '+', ',', '/', ':', ';', '=', '?',  '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~', "'"]
non_url_safe_regex = re.compile(r'[{}]'.format(''.join(re.escape(x) for x in non_url_safe)))
translate_table = {ord(char): u'' for char in non_url_safe}


def slugify(text):
    text = text.translate(translate_table)
    text = u'_'.join(text.split())
    return text
