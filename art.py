from colors import Colors
print('hello')
print(f"{Colors.BRIGHT_RED}This is red text{Colors.RESET}")
print(chr(0x2588)*2)
print(f"{Colors.CYAN}{chr(0x2588)*2}{Colors.RESET}")

#Using a 2d array do this or smn:
#https://www.clipartmax.com/png/middle/133-1334472_mario-clipart-8bit-super-mario-8-bit.png
#you get one print



b = Colors.BLACK
r = Colors.RED
g = Colors.GREEN
y = Colors.YELLOW
px = chr(0x2588)*2

board = [
    [b, px, b, px, b, px, b, px, b, px, b, px, b, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, b, px, b, px, b, px,'\n'],
    [b, px, b, px, b, px, b, px, b, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, r, px, b, px,'\n'],
    [b, px, b, px, b, px, b, px, b, px, g, px, g, px, g, px, g, px, g, px, g, px, g, px, y, px, y, px, y, px, y, px, y, px, g, px, g, px, y, px, y, px,'\n'],
    [b, px, b, px, b, px, g, px, g, px, y, px, y, px, g, px, g, px, g, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, g, px, g, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px,'\n'],
    [b, px, b, px, b, px, g, px, g, px, y, px, y, px, g, px, g, px, g, px, g, px, g, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, g, px, g, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px,'\n'],
    [b, px, b, px, b, px, g, px, g, px, g, px, g, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, g, px, g, px, g, px, g, px, g, px, g, px, g, px, g, px, g, px,'\n'],
    [b, px, b, px, b, px, b, px, b, px, b, px, b, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px, y, px,'\n'],
    [b, px, b, px, b, px, b, px, b, px, g, px, g, px]
]

for row in board:
    for color in row:
        print(color, end='')