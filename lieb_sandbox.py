
import numpy as np
import itertools
import matplotlib.pyplot as plt
import matplotlib as mpl

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Nuts && bolts for lattice.
a = 0.5; # 'hopping' distance -- distance between nearest-neighbors
v = 1.0; # lattice constant (size)
v1 = v*np.array([1.0,0]); v2 = v*np.array([0,1.0])
R2 = np.array([[-1,0], [0,-1]]) # clockwise rotation pi 
R2v1 = np.dot(R2,v1); R2v2 = np.dot(R2,v2);
num_cells = 2; # default number to generate (symmetric about [0,0])
lieb_atoms= 3; # number of atomic sites in Lieb structure
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Nuts && bolts for vector display 
arrow_nodes =  np.array([(0,a), (a,0),(-a,0),(0,-a)])
anodex = [x[0] for x in arrow_nodes]
anodey = [x[1] for x in arrow_nodes]
epsi = 0.1; # cushion between arrow head and nodes
offset_text = 0.01; # offset text of annotated plot
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Nuts && bolts for plot.
num_cells = int(np.ceil(float(raw_input("How many lattice sites would you like? >> "))));
labels = ["B","A","C"]#,"D"] << for square
colors = ["r","g","b"]#,"y"] << for square
title_font = {'fontname':'Arial', 'size':'16','verticalalignment':'bottom'} 
axis_font = {'fontname':'Arial', 'size':'12'}
# Just want to display symmetric box.
x_max = num_cells/2
x_min = -x_max;
y_max = x_max;
y_min = -y_max;
cushion = 0.01; # offset axis limits for room between nodes and frame
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: build_lattice
# Parameters: n, a
# Purpose:
#     To generate the [x,y] coordinates of the atomic sites for
#     the Lieb lattice.
#     To do: Make the # of sites (Lieb <-> square) variable.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def build_lattice(n, a):
    lat_atoms = np.array([[0,0],[0,a], [a,0]])
    lat_B  = np.array([(0,0)])
    nodes = []
    cells = []
    for pair in itertools.combinations(range(-n/2,n/2+1),2):
        lat_atoms1 = [x+pair[0]*v1+pair[1]*v2 for x in lat_atoms];
        lat_atomsR1 = [x+pair[0]*R2v1+pair[1]*R2v2 for x in lat_atoms];
        nodes.extend(lat_atoms1)
        nodes.extend(lat_atomsR1)
    for i in range(-n/2,n/2+1):
        lat_atoms1 = [x+i*v1+i*v2 for x in lat_atoms];
        lat_atomsR1 = [x+i*R2v1+i*R2v2 for x in lat_atoms];
        nodes.extend(lat_atoms1)
        nodes.extend(lat_atomsR1)
    return nodes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def build_lattice2(n, a):
    # lat_atoms = np.array([(0,0),(0,a), (a,0)])
    # ^ Cannot do this. Only A and C can be reached this way.
    # In for loop:
    #   lat_atoms1 = [x+i*v1 for x in lat_atoms]
    #   lat_atoms2 = [x+i*v2 for x in lat_atoms]
    # does not generate the Lieb lattice.
    lat_atoms = np.array([[0,0],[0,a], [a,0]])
    lat_B  = np.array([(0,0)])
    nodes = []
    cells = []
    for i in range(-n/2,(n/2)+1,1): 
        # 'Diagonal' elements: 
        lat_atoms1 = [x+i*v1 for x in lat_atoms]
        lat_atoms2 = [x+i*v2 for x in lat_atoms]
        lat_atomsR1 = [x+i*Rv1 for x in lat_atoms]
        lat_atomsR2 = [x+i*Rv2 for x in lat_atoms]
        # Other combs:
        #lat_atoms3 = [x+i*v1+i*v2 for x in lat_atoms] << unecessary
        lat_atoms4 = [x+i*v1-i*v2 for x in lat_atoms]
        #lat_atoms5 = [x-i*v1+i*v2 for x in lat_atoms] << unecessary
        lat_atoms6 = [x-i*v1-i*v2 for x in lat_atoms]


        #at_atoms3 = [x+i*v1+i*v2 for x in lat_B]
        nodes.extend(lat_atoms1)
        nodes.extend(lat_atoms2)
        #nodes.extend(lat_atoms3)
        nodes.extend(lat_atoms4)
        #nodes.extend(lat_atoms5)
        nodes.extend(lat_atoms6)
        nodes.extend(lat_atomsR1)
        nodes.extend(lat_atomsR2)
        #nodes.extend(lat_atoms3)
    return nodes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Generate lattice.   
nodes = build_lattice(num_cells, a)
# Store x- and y-coordinates separately.
nodex = [x[0] for x in nodes]
nodey = [x[1] for x in nodes]
N = len(nodex)/lieb_atoms;
# Plot the triplet (B,A,C)
for i in range(0,N):
    nodex_lat = nodex[i*3:(i+1)*3+1];
    nodey_lat = nodey[i*3:(i+1)*3+1];  
    for xs,ys,l,c in zip(nodex_lat,nodey_lat,labels, colors):
        plt.scatter(xs, ys, color=c,s=25)
        plt.annotate( l, xy = (xs, ys),xytext = (-1.5, 1.5),textcoords = 'offset points', ha = 'right', va = 'bottom')


# Plot the vectors that generate the Lieb structure:
plt.arrow(0,0,v1[0]-epsi,v1[1],head_width=0.05,fc='0.75',ec='0.75')
plt.arrow(0,0,v2[0],v2[1]-epsi,head_width=0.05,fc='0.75',ec='0.75')

# Plot the hopping vectors (nearest neighbors)
for i in range(0,len(anodex)):
    if anodex[i] < 0:
        anodex[i]+=epsi;
    if anodex[i] > 0:
        anodex[i]+=-epsi;
    if anodey[i] < 0:
        anodey[i]+=epsi;
    if anodey[i] > 0:
        anodey[i]+=-epsi;
    plt.arrow(0,0,anodex[i],anodey[i],head_width=0.05,fc='k')


plt.xlabel("x axis", **axis_font)
plt.ylabel("y axis", **axis_font)
plt.title("Lieb Lattice", **title_font)

axes = plt.gca()
axes.set_xlim([x_min-cushion,x_max+cushion])
axes.set_ylim([y_min-cushion,y_max+cushion])
axes.set_aspect('equal')


plt.show()