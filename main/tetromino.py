from settings import *

from block import Block


class Tetromino(object):
    def __init__(self, shape, group):
        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']

        self.blocks = [Block(group, position, self.color)
                       for position in self.block_positions]


if __name__ == '__main__':
    pass
