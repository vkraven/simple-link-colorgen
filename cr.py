#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Generate all colours of at least 3:1 to Body colour, and 4.5:1 to Background colour.')
parser.add_argument('--body', dest = 'c1', type=str, help='the body colour in hexadecimal format. Casing does not matter', required=True)
parser.add_argument('--background', dest = 'c2', type=str, help='the background colour in hexadecimal format. Casing does not matter', required=True)

args = parser.parse_args()

def colourconv(c):
    if c <= 0.03928:
        return c / 12.92
    else:
        return ((c + 0.055) / 1.055) ** 2.4

def luminance(r, g, b):
    r_r = 0.2126
    g_r = 0.7152
    b_r = 0.0722
    r1 = r / 255.0
    g1 = g / 255.0
    b1 = b / 255.0
    r2 = colourconv(r1)
    g2 = colourconv(g1)
    b2 = colourconv(b1)
    return (r_r * r2) + (g_r * g2) + (b_r * b2)

def contrastratio(light, dark):
    return 1 / ((luminance(light[0], light[1], light[2]) + 0.05) / (luminance(dark[0], dark[1], dark[2]) + 0.05))

def contrast_ratio(c1, c2):
    if contrastratio(c1, c2) < 1.0:
        return contrastratio(c2, c1)
    else:
        return contrastratio(c1, c2)

def generate_okay_colours(colour1, colour2):
    all_colours = ((x, y, z) for x in range(0, 256) for y in range(0, 256) for z in range(0, 256))
    result = []
    for c in all_colours:
        if (contrast_ratio(c, colour1) >= 3.0) and (contrast_ratio(c, colour2) >= 4.5):
            print("Accepting ", colour_to_hex(c), "\t|\tRatio to ", colour_to_hex(colour1), " = ", '%0.4f' % contrast_ratio(c, colour1), "\t|\tRatio to ", colour_to_hex(colour2), " = ", '%0.4f' % contrast_ratio(c, colour2))
            result.append(c)
    return result

def generate_okay_colours_hex(chex1, chex2):
    c_hex1 = chex1.replace('#', '')
    c_hex2 = chex2.replace('#', '')
    left = (int(c_hex1[0:2], 16), int(c_hex1[2:4], 16), int(c_hex1[4:6], 16))
    right = (int(c_hex2[0:2], 16), int(c_hex2[2:4], 16), int(c_hex2[4:6], 16))
    return generate_okay_colours(left, right)

def colour_to_hex(c):
    return '#' + ''.join('%02x' % i for i in c).upper()

fname = args.c1 + '_' + args.c2 + '.txt'

x = generate_okay_colours_hex(args.c1, args.c2)
print("Total colours found: ", len(x))
print("Generating output file ", fname)

with open(fname, 'w') as f:
    for c in x:
        f.write(colour_to_hex(c) + '\n')
