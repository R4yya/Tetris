from settings import *

from block import Block


class Tetromino(object):
    def __init__(self, shape, group, create_new_teromino, field_data):
        self.shape = shape
        self.block_positions = Settings.TETROMINOS[self.shape]['shape']
        self.color = Settings.TETROMINOS[self.shape]['color']

        self.create_new_teromino = create_new_teromino
        self.field_data = field_data

        self.blocks = [Block(group, position, self.color) for position in self.block_positions]

    def next_move_horizontal_collide(self, blocks, step):
        collision_list = [block.horizontal_collide(int(block.position.x + step), self.field_data) for block in self.blocks]

        return True if any(collision_list) else False

    def next_move_vertical_collide(self, blocks, step):
        collision_list = [block.vertical_collide(int(block.position.y + step), self.field_data) for block in self.blocks]

        return True if any(collision_list) else False

    def move_down(self, step):
        if not self.next_move_vertical_collide(self.blocks, step):
            for block in self.blocks:
                block.position.y += step
        else:
            for block in self.blocks:
                self.field_data[int(block.position.y)][int(block.position.x)] = block
            self.create_new_teromino()

    def move_horizontal(self, step):
        if not self.next_move_horizontal_collide(self.blocks, step):
            for block in self.blocks:
                block.position.x += step

    def rotate(self):
        if self.shape != 'O':
            pivot_position = self.blocks[0].position

            new_block_positions = [block.rotate(pivot_position) for block in self.blocks]

            for position in new_block_positions:
                if position.x < 0 or position.x >= Settings.COLUMNS:
                    return

                if self.field_data[int(position.y)][int(position.x)]:
                    return

                if position.y > Settings.ROWS:
                    return

            for i, block in enumerate(self.blocks):
                block.position = new_block_positions[i]


if __name__ == '__main__':
    pass
