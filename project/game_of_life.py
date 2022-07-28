"""The Game of Life
.. module:: game_of_life
    :platform: Unix, OS
    :synopsis:  This is a project to create the program Conway's Game of Life using python3.
                This game is set to a 30x80 grid, but the user can select how many generations
                and which boxes (or individuals) are alive (turned on) on the command line.
                The rules are as followed:
                    Any “on” cell with fewer than two live neighbors is turned “off”.
                    Any “on” cell with two or three “on” neighbors remains “on”.
                    Any “on” cell with more than three “on” neighbors is turned “off”.
                    Any “off” cell with exactly three live neighbors is turned “on”.
                    A neighbor is any adjacent cell, including those to the East, West, North, South,
                    Northeast, Northwest, Southeast and Southwest of the cell.
                 X represents "on" or alive
                 - represents "off" or dead

.. moduleauthor:: Kara Ryan kara.ryan@wsu.edu

"""

from sys import argv

# create a function to create a blank starting grid
def blank_grid(row, col):
    """ Create a blank starting grid.
    Blank grid creates a starting 30x80 grid that is populated with all "off" cells.

    :param row: The number of rows in the grid.
    :type row: A string.

    :param col: The number of columns in the grid.
    :type col: A string.

    """
    grid = ['-'] * row # Create list of dashes for length row named grid
    for i in range(row): # loop through list for each value of row
        grid[i] = ['-'] * col # add list of '-' length col to grid
    return grid  # return a grid that is a list of lists of dashes

# Create a function to split and unpack to assign
def starting_alive(alive, grid):
    """ Starting alive function takes the coordinates the user has chosen on
    the commandline and sets them as starting alive

    :param alive: Contains the coordinates in row:col the user has chosen to
    set as alive for the start.
    :type alive: A list.

    :param grid: A 30x80 rectangle containing '-' for off/dead cells and 'X' for
    on/alive cells.
    :type grid: A list.

    """
    for i in alive: # for each element of alive
        row, col = i.split(":") # split at the : and set row, col to 1st, 2nd element
        row, col = int(row), int(col) # convert to integer
        grid[row][col] = 'X' # turn on cells in grid that user has inputted
    return grid # return the new populated grid

# create a function to print the grid
def print_grid(grid):
    """ Print the grid function prints the 30x80 grid to the console.

    :param grid: a 30x80 rectangle containing '-' for off/dead cells and 'X' for
    on/alive cells.
    :type grid: A list.

    """
    for i in grid: # loop through grid
        for j in i:
            print(j, end='') # print each list on new line
        print()
    print() # print space between each grid

# Create a function to apply the rules of the game
def apply_rules(grid, row, col):
    """ Apply the rules function considers Conway's Game of Life rules
    and creates a grid for the next generation.

    This function first creates a blank new_grid to store the restults of
    survival for the next generation using the blank_grid function.  For each
    cell of the grid, this function will look for neighbors in all directions.
    If there is an alive individual (X), then it will add 1 to the total_neighbors
    count. If there is no cell present, it will skip the count. Then, it applies
    the rules of the game based on if the cell is starting on or off and the total
    neigbors of the cell. The corresponding cell in new_grid will get an 'X' if
    it is turned on in the next generation or '-' if turned off.

    :param grid: A rectangle of 'X' for alive individuals (on) and '-' for no
    individual.
    type grid: list.

    param row: The number of rows in the grid.
    :type row: An integer.
​
    :param col: The number of columns in the grid.
    :type col: An integer.
    """
    new_grid = blank_grid(row, col) # create a new blank grid
    for i in range(row): # loop through rows
        for j in range(col): # loop through each col of that row
            total_neighbors = 0 # set starting neighbors to 0
            if grid[i][j - 1] == 'X': # check W, if alive add 1 to total_neighbors
                total_neighbors += 1
            if grid[i - 1][j] == 'X': # check N, if alive add 1 to total_neighbors
                total_neighbors += 1
            if grid[i - 1][j - 1] == 'X': # check NW, if alive add 1 to total_neighbors
                total_neighbors += 1
            if j + 1 >= col: # if there is no cell E, skip this cell
                pass
            else: # if there is a cell E
                if grid[i][j + 1] == 'X': # and if the cell is alive, add 1 to total_neighbors
                    total_neighbors += 1
            if i + 1 >= row: # if there is no cell S, skip this cell
                pass
            else: # if there is a cell S
                if grid[i + 1][j] == 'X': # and that cell is alive, add 1 to neighbors
                    total_neighbors += 1
            if i + 1 >= row: # if there is no cell SW, skip this cell
                pass
            else:
                if grid[i + 1][j - 1] == 'X': # and that cell is alive, add 1 to neighbors
                    total_neighbors += 1
            if i + 1 >= row or j + 1 >= col: # if there is no cell SE, skip this cell
                pass
            else:
                if grid[i + 1][j + 1] == 'X': # and that cell is alive, add 1 to neighbors
                    total_neighbors += 1
            if j + 1 >= col: # if there is no cell NE, skip this cell
                pass
            else:
                if grid[i - 1][j + 1 ] == 'X': # and that cell is alive, add 1 to neighbors
                    total_neighbors += 1

            # if cell on and fewer than 2 neighbors, turn off
            if grid[i][j] == 'X' and total_neighbors < 2:
                new_grid[i][j] = '-' 
            # The indivdiual is alive and has 2 or 3 neighbors, turn on
            if grid[i][j] == 'X' and (
            total_neighbors == 2 or total_neighbors == 3):
                  new_grid[i][j] = 'X'
            # The individual is alive but has > 3 total neighbors, turn off
            if grid[i][j] == 'X' and total_neighbors > 3:
                new_grid[i][j] = '-'
            # If there is no living individual but has 3 total neighbors, turn on
            if grid[i][j] == '-' and total_neighbors == 3:
                new_grid[i][j] = 'X'

    return new_grid

def main(argv):

    """The main executable function of this script.

    This will create a blank grid, assign the user-defined "alive" cells to begin
    and run for user-defined amountof generations. This script is written using
    python3.7 and can be executed on the command line as game_of_life.py
    generations alive where generation is an integer from 1 to infinity and alive
    is row:col coordinates for cells.

    :param argv: This function recieves as input the argv object provided
    by the sys moddule which contains the list of command-line arguments
    including generation time and alive cells.

    :type argv: A list """

    # Unpack arguments
    script = argv[0]
    max_generation = int(argv[1])
    alive = []
    alive = argv[2:]

    # Create grid that is 30 cells high (rows) and 80 cells long (columns)
    row = 30
    col = 80
    current_generation = 1
    grid = blank_grid(row, col)
    grid = starting_alive(alive, grid)
    print_grid(grid)

    while current_generation <= max_generation:
        new_grid = apply_rules(grid, row, col)
        print_grid(new_grid)
        grid = new_grid
        current_generation += 1

if __name__ == "__main__":
    main(argv)
