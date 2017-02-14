
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

a = 0.5; 
v = 1.0; # lattice constant
v1 = v*np.array([1.0,0]); v2 = v*np.array([0,1.0])
R = np.array([[0,-1], [1,0]]) # clockwise rotation pi/2
Rv1 = np.dot(R,v1); Rv2 = np.dot(R,v2);   

num_cells = 2;
lieb_atoms= 3;
nodes = []
cells = []
n = int(raw_input("How many lattice sites would you like? >> "));

def build_lattice(num_cells, a):
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
    for i in range(-num_cells/2,(num_cells/2)+1,1):
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
    
nodes = build_lattice(n, a)

nodex = [x[0] for x in nodes]
nodey = [x[1] for x in nodes]
x_max = num_cells/2;
x_min = -num_cells/2;
y_max = num_cells/2;
y_min = -num_cells/2;

N = len(nodex)/lieb_atoms
labels = ["B","A","C"]#,"D"]
colors = ["r","g","b"]#,"y"]
for i in range(0,N):
    nodex_lat = nodex[i*3:(i+1)*3+1];
    nodey_lat = nodey[i*3:(i+1)*3+1];
   
    for xs,ys,l,c in zip(nodex_lat,nodey_lat,labels, colors):
        plt.scatter(xs, ys, color=c,s=25)
        plt.annotate( l, xy = (xs, ys),xytext = (-1.5, 1.5),textcoords = 'offset points', ha = 'right', va = 'bottom')


epsi = 0.1;
offset_text = 0.01;
plt.arrow(0,0,0,1-epsi,head_width=0.05,fc='0.75',ec='0.75')
plt.arrow(0,0,1-epsi,0,head_width=0.05,fc='0.75',ec='0.75')


arrow_nodes =  np.array([(0,a), (a,0),(-a,0),(0,-a)])
anodex = [x[0] for x in arrow_nodes]
anodey = [x[1] for x in arrow_nodes]
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


title_font = {'fontname':'Arial', 'size':'16','verticalalignment':'bottom'} 
axis_font = {'fontname':'Arial', 'size':'12'}
plt.xlabel("x axis", **axis_font)
plt.ylabel("y axis", **axis_font)
plt.title("Lieb Lattice", **title_font)
cushion = 0.1;
axes = plt.gca()
axes.set_xlim([x_min-cushion,x_max+cushion])
axes.set_ylim([y_min-cushion,y_max+cushion])
axes.set_aspect('equal')


plt.show()