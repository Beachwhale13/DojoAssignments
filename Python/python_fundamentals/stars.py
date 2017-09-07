x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

# def draw_stars(x):
#     for number in x:
#         string = ''
#         for i in range(number):
#             string += '*'
#         print string
#
# draw_stars(x)


def draw_stars_2(x):
    for item in x:
        string = ''
        if isinstance(item, int):
            for i in range(item):
                string += "*"
            print string
        else:
            for char in item:
                string += item[0].lower()
            print string
draw_stars_2(x)
