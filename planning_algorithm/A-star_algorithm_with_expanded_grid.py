# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
# 
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def check_boundary(grid, neighbor):
    #print "before check_boundary neighbor:"
    #print neighbor
    if (neighbor[0]<0):
            neighbor[0] = 0
    if (neighbor[1]<0):
            neighbor[1] = 0
    if neighbor[0] > (len(grid) - 1):
            neighbor[0] = len(grid) - 1
    if neighbor [1] > (len(grid[0]) - 1):
            neighbor[1] = len(grid[0]) - 1
    #print "after check_boundary_neighbor:"
    #print neighbor
    return neighbor
    
def valid_move(grid, neighbor):
    if grid[neighbor[0]][neighbor[1]] == 0:
        return 1
    else:
        return 0
    
def move(grid, delta, check, open_list, cost):
    list1 = []
    final_cost = open_list[0] + cost

    for i in range(len(delta)):
        
        neighbor = [open_list[1] + delta[i][0], open_list[2] + delta[i][1]]
        
        neighbor = check_boundary(grid, neighbor)
        #print "neighbor in move:", neighbor
        valid = valid_move(grid, neighbor)
        
        if (neighbor not in check) and (valid == 1):
            g_value = final_cost
            x_coord = neighbor[0]
            y_coord = neighbor[1]
            
            list1.append([g_value, x_coord, y_coord])
    
    return list1
def search(grid,init,goal,cost, heuristic):
    
    # to keep track of visited points in grid
    check = []
    check.append(init) #appending first point to the check
    # open a triplet list to track the g value according to the current position
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    open_list = [0]*3
    g_value = open_list[0]
    
    x_value = open_list[1]
    y_value = open_list[2]
    count = 0
    expand[x_value][y_value] = 0
    
    old_g_value = g_value
    coord = [x_value, y_value]
    new_h_value = heuristic[0][0]
    new_f_value = old_g_value + new_h_value
    #print g_value, x_value, y_value
    feed_list = open_list
    while ((coord[0] != goal[0]) or (coord[1] != goal[1])): # end condition
        
        open_list1 = move(grid, delta, check, feed_list, cost)
        if not open_list1:
            return "fail"
        new_g_value = open_list1[0][0]
        #print "g_value", new_g_value
        #new_h_value = heuristic[0][0]
        #new_f_value = new_g_value + new_h_value
        nei_id = 0
        for i in range(len(open_list1)):
            
            coord = [open_list1[i][1], open_list1[i][2]]
            #print "coord", coord
            check.append(coord)
            
            if (open_list1[i][0] <= new_f_value):
                #print "old f value", new_f_value
                new_g_value = open_list1[i][0]
                nei_id = i
                nei_x = open_list1[i][1]
                nei_y = open_list1[i][2]
                new_h_value = heuristic[nei_x][nei_y]
                new_f_value = new_g_value + new_h_value
                #print "open_list[i][0]", open_list1[i][0]
                #print "new_f_value", new_f_value
                
        #print "open_list: ", open_list1
        #print "check: ", check
        #print nei_id
        count += 1;
        expand[nei_x][nei_y] = count
        feed_list[0] = new_g_value
        feed_list[1] = nei_x
        feed_list[2] = nei_y
        #print "coord 0:", nei_x, ": goal 0: ", goal[0]
        #print "coord 1:", nei_y, ": goal 1: ", goal[1]
        #print "feed_list: ", feed_list
        #print " "
       
    #path = feed_list       
    print expand
    return expand
    #print path
    #return path

search(grid,init,goal,cost, heuristic)