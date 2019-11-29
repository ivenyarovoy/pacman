"""
Write a module docstring here
"""

__author__ = "Iven Yarovoy"


def pacman(input_file):
    """ Use this function to format your input/output arguments. Be sure not to change the order of the output arguments. 
    Remember that code organization is very important to us, so we encourage the use of helper fuctions and classes as you see fit.
    
    Input:
        1. input_file (String) = contains the name of a text file you need to read that is in the same directory, includes the ".txt" extension
           (ie. "input.txt")
    Outputs:
        1. final_pos_x (int) = final x location of Pacman
        2. final_pos_y (int) = final y location of Pacman
        3. coins_collected (int) = the number of coins that have been collected by Pacman across all movements
    """
    #input_file = "input_file.txt" 
    #f=open(input_file,'r')

    with open(input_file, 'r') as f:
        all_lines = [[(num) for num in line.split()] for line in f]
        
    grid_size_x=int(all_lines[0][0])
    grid_size_y=int(all_lines[0][1])
    init_pos_x=int(all_lines[1][0])
    init_pos_y=int(all_lines[1][1])
    direction_list=all_lines[2]
    direction_array = direction_list[0]
    wall_list=all_lines[3:]
    fail = 0
    
    #some edge case correction
    if (init_pos_x >= grid_size_x or init_pos_x < 0 or init_pos_y < 0 or init_pos_y >= grid_size_y):
        fail = 1
    
    #initialize current positions
    curr_x=init_pos_x
    curr_y=init_pos_y
    
    coins_collected = 0
    
    visited_points = [[curr_x,curr_y]]
    
    #get directions from list and set potential position
    if fail == 0:
        for i in range(len(direction_array)):
            pot_x=curr_x
            pot_y=curr_y
            hit_edge=0
            hit_wall=0
            
            if direction_array[i] == 'N':
                #check if within the grid
                if curr_y+1<grid_size_y:
                    pot_y=curr_y+1
                    pot_x=curr_x
                else:
                    hit_edge=1
            elif direction_array[i] == 'S':
                if curr_y-1>=0:
                    pot_y=curr_y-1
                    pot_x=curr_x
                else:
                    hit_edge=1
            elif direction_array[i] == 'E':
                if curr_x+1<grid_size_x:
                    pot_x=curr_x+1
                    pot_y=curr_y
                else:
                    hit_edge=1
            elif direction_array[i] == 'W':
                if curr_x-1>=0:
                    pot_x=curr_x-1
                    pot_y=curr_y
                else:
                    hit_edge=1
    
            #convert potential x and y into a list of strings
            if hit_edge == 0:
                potlist = [str(pot_x),str(pot_y)]
                for j in range (len(wall_list)):
                    if wall_list[j] == potlist:
                        hit_wall = 1
                if hit_wall == 0:
                    curr_x=pot_x
                    curr_y=pot_y
                    for k in range (len(visited_points)):
                        if visited_points[k] != [curr_x,curr_y]:
                            coins_collected = coins_collected+1
                            visited_points.insert(0,[curr_x,curr_y])
    
    #finished all cardinal direction inputs
    final_pos_x = curr_x
    final_pos_y = curr_y
    
    #failure return
    if fail == 1:
        final_pos_x, final_pos_y = -1,-1
        coins_collected = 0
    
    print (len(direction_array))
    
    # return final_pos_x, final_pos_y, coins_collected
    return (final_pos_x,final_pos_y,coins_collected)

