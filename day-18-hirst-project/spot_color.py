import colorgram

color_palette = []
color_extract = colorgram.extract("hirst1.jpeg", 100)
for no in range(len(color_extract)):
    color = color_extract[no].rgb
    #print(color)
    #print(color[:])      # Extract tuple from the object
    r = color_extract[no].rgb.r
    g = color_extract[no].rgb.g
    b = color_extract[no].rgb.b
    color_palette.append((r, g, b))

print(color_palette)


color_list = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182), (180, 187, 211)]
