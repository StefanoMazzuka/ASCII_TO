Create exe:

```pyinstaller --onefile --windowed --add-data "app_2.py;." --add-data "constants.py;." --add-data "element.py;." --add-data "enemy.py;." --add-data "entity.py;." --add-data "item.py;." --add-data "level.py;." --add-data "map.py;." --add-data "player.py;." --add-data "position.py;." json_to_lvl.py```