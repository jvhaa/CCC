# Canadian Computing Competition: 2004 Stage 1, Junior #5
# https://dmoj.ca/problem/ccc04j5

import sys # import sys

level, width, x = list(map(int, sys.stdin.readlines(1)[0].split(" "))) # splits into level width and x

fractals = [(0, width, 1, 1, 1)] # starting fractal outline of just a line

for _ in range(level): # loops for levels
    nfs = [] # list for fractals
    for fractal in fractals: # loops for each fractal
        sx, ex, sy, ey, dir = fractal # grab the start, end x and y and direction from fractal
        if sy == ey: # if horozontal
            nw = abs(sx-ex)//3 # new width
            nfs.append((sx, sx + nw, sy, ey, dir)) # left outer
            nfs.append((ex - nw, ex, sy, ey, dir)) # right outer
            nfs.append((sx + nw, ex - nw, sy+nw*dir, sy+nw*dir, dir)) # top
            nsy, ney = sorted((ey, sy+nw*dir)) # new start, end y
            nfs.append((sx+nw, sx+nw, nsy, ney, -1)) # left side
            nfs.append((ex-nw, ex-nw, nsy, ney, 1)) # right side
        else: # if vertical
            nw = abs(sy-ey)//3 # new width
            nfs.append((sx, ex, sy, sy + nw, dir)) # down outer
            nfs.append((sx, ex, ey - nw, ey, dir)) # top outer
            nfs.append((sx + nw * dir, ex + nw*dir, sy+nw, ey-nw, dir)) # side
            nsx, nex = sorted((sx, sx+ nw*dir)) # new start, end x
            nfs.append((nsx, nex, sy + nw, sy+nw, -1)) # down side
            nfs.append((nsx, nex, ey-nw, ey-nw, 1)) # top side
    fractals = nfs[::] # fractal is now the new fractal outline

answers = set() # makes the answers a set so no duplicates
for fractal in fractals: # looks for out line
    sx, ex, sy, ey, _ = fractal # grabs coords of line
    if sx <= x <= ex: # check if x is in between a line because it is bound to cross if it is
        for y in range(sy, ey + 1): # loops for y it crosses. for example if it crosses a horontal line at y = 3 since sy == ey then range(3, 4) is just 3 the same thing for vertical lines, it touches it from 3 to 5 and adding one more woulld loop throught 3 to 5
            answers.add(y) # adds y to loop
print(*sorted(answers)) # sorts the answers from low to high
