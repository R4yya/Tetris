from settings import *

from block import Block


class Tetromino(object):
    def __init__(self, shape, group):
        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']

        self.blocks = [Block(group, position, self.color)
                       for position in self.block_positions]

    def next_move_horizontal_collide(self, blocks, step):
        collision_list = [block.horizontal_collide(
            int(block.position.x + step)) for block in self.blocks]
        return True if any(collision_list) else False

    def next_move_vertical_collide(self, blocks, step):
        collision_list = [block.vertical_collide(
            int(block.position.y + step)) for block in self.blocks]
        return True if any(collision_list) else False

    def move_down(self, step):
        if not self.next_move_vertical_collide(self.blocks, step):
            for block in self.blocks:
                block.position.y += step
        else:
            self.create_new_teromino()

    def move_horizontal(self, step):
        if not self.next_move_horizontal_collide(self.blocks, step):
            for block in self.blocks:
                block.position.x += step


if __name__ == '__main__':
    pass
