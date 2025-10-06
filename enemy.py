import random
from typing import Dict, Optional

from entity import Entity
from position import Position


class Enemy(Entity):
    def __init__(self, position: Position, skin: str, sprites: dict, health: int, drops: Dict[Optional[str], float]):
        super().__init__(position, skin, sprites)
        self.health = health
        self.drops  = drops

    def drop(self):
        items = list(self.drops.keys())
        probabilities = list(self.drops.values())

        return random.choices(items, weights=probabilities, k=1)[0]
