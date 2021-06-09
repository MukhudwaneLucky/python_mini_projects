# import program modules

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import argparse

""" constant values """
ON = 255
OFF = 0
vals = [ON, OFF]


def random_grid(N):
    """ initial conditions """
    # set the initial state randomly
    # parameters: np.random.choice(list,size,prob).reshape(row,col)
    # list=values used to populate the array given in a list
    # prob=the probability of a value from the list being chosen, 0->0.2(20%) and 255->0.8(80%), values must add up to 1
    # size=size of the grid, row*col
    # choice create a 16 value 1d array, use reshape to make it 2d with rows and cols sizes
    return np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)


# set the initial condition to a pattern
def add_glider(i, j, grid):
    # adds a glider with top left cell at (i, j)
    # glider is an observed pattern that moves steadily across the grid
    glider = np.array([[0, 0, 255],
                       [255, 0, 255],
                       [0, 255, 255]])
    # using the numpy slice to copy pattern to 2d grid
    grid[i:i + 3, j:j + 3] = glider


def update(frame_num, img, grid, N):
    # copy grid since we require 8 neighbors for calculation and go line by line
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8-neighbor sum using toroidal boundary conditions
            # x and y wrap around , simulation take place on toroidal surface
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]) / 255)
            # apply conway's rules
            if grid[i, j] == ON:
                # any cell with less than 2 or greater than 3 ON neighbor cells is turned OFF
                if (total < 2) or (total > 3):
                    new_grid[i, j] = OFF
                else:
                    # any cell OFF with exactly 3 ON neighbor cells is turned ON
                    if total == 3:
                        new_grid[i, j] = ON
    # update data
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,


# representing the grid
def main():
    # get command line arguments / add command line options
    parser = argparse.ArgumentParser(description="Run's Conway's Game of Life Simulation.")
    # add arguments
    parser.add_argument('--grid_size', dest='N', required=False)             # simulation grid size
    parser.add_argument('--mov-file', dest='movfile', required=False)        # filename
    parser.add_argument('--interval', dest='interval', required=False)       # animation update interval in milliseconds
    parser.add_argument('--glider', action='store_true', required=False)     # start simulation with glider pattern
    args = parser.parse_args()

    # set grid size
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)

    # set animation update interval
    update_interval = 50
    if args.interval:
        update_interval = int(args.interval)

    # declare grid
    grid = np.array([])
    # check id glider demo flag is specified
    if args.glider:
        # create an NxN array of zeros
        grid = np.zeros(N * N).reshape(N, N)
        add_glider(1, 1, grid)
    else:
        # populate grid with random on/off - more off than on
        grid = random_grid(N)

    # set up animation
    fig, ax = plt.subplots()
    # use nearest to get sharp edges of the cells
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames=10,
                                  interval=update_interval,
                                  save_count=50)
    # number of frames?
    # set the output file
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    # display the matrix
    plt.show()


# run
if __name__ == '__main__':
    main()
