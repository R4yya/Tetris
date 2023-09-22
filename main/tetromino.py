from settings import *

from block import Block


class Tetromino(object):
    def __init__(self, shape, group):
        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']

        self.blocks = [Block(group, position, self.color)
                       for position in self.block_positions]

    def next_move_horizontal_collide(self, blocks, amount):
        collision_list = [block.horizontal_collide(
            int(block.position.x + amount)) for block in self.blocks]
        return True if any(collision_list) else False

    def next_move_vertical_collide(self, blocks, amount):
        pass

    def move_down(self):
        for block in self.blocks:
            block.position.y += 1

    def move_horizontal(self, step):
        for block in self.blocks:
            block.position.x += step


if __name__ == '__main__':
    pass
