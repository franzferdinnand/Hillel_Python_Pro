class colorizer:
    def __init__(self, color):
        self.colors = {
            'grey': '90',
            'red': '91',
            'green': '92',
            'yellow': '93',
            'blue': '94',
            'pink': '95',
            'turquoise': '96'
        }
        self.color_name = color
        self.color_end = '\033[0m'

    def __enter__(self):
        if self.color_name not in self.colors:
            raise ValueError('COLOR NOT FOUND')
        else:
            self.colour = f'\033[{self.colors[self.color_name]}m'
            print(self.colour, end='')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.color_end, end='')


with colorizer('red'):
    print('printed in red')
print('printed in default color')