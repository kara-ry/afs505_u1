
dead_cell = "-"
living_cell = "X"

# create a function to create a blank starting grid
def blank_grid():


    # Create empty list to fill with "off" dead cells
    row = []
    # add dashes for 80 columns
    for i in range(80):
        row.append(dead_cell)

    # create empty grid list
    grid = []

    # append dashed row list for 30 rows
    for j in range (30):
        grid.append(row[:])

    return grid

print(blank_grid()) # test if a blank grid will print


def print_grid(grid):
    for i in grid:
        for j in i:
            print(j, end = "")
        print()
    return blank_grid
print_grid(blank_grid) # test if grid will print
