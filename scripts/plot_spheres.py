####################################################################
###
### plot spheres
###
### call file:
### python3 plot_spheres.py ../system/sphere_data.txt
###
### Daniel Vogler
### daniel.vogler@erdw.ethz.ch
###
### July 2016
###
####################

import csv
import sys

import numpy as np

import matplotlib
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d as mp3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

print("System input variables")
print( str(sys.argv) )

# read in file_path from command line
file_path =  sys.argv[1]

figure_path = "./"

### plot settings
plot_grid = False
plot_axis = False
plot_transparent = True
plot_elevation = 40
plot_azimuth = 145

### function to draw spheres
def draw_sphere( x_center, y_center, z_center, r):

    ### draw sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x=np.cos(u)*np.sin(v)
    y=np.sin(u)*np.sin(v)
    z=np.cos(v)

    ### shift and scale sphere
    x = r*x + x_center
    y = r*y + y_center
    z = r*z + z_center

    ### return variables
    return (x,y,z)

### initiate variables
sphere_radius_scalar = 2.50

### system dimensions
x_min = 0
x_max = 50
y_min = 0
y_max = 100
z_min = 0
z_max = 20

### initialize variables to save file content
exp_file = []
exp_file_lines = []

### initialize sphere variables
sphere_number = []
sphere_conductivity = []
sphere_porosity = []
sphere_volumeSolid = []
sphere_volumeFluid = []
sphere_coordinate_x = []
sphere_coordinate_y = []
sphere_coordinate_z = []
sphere_radius = []

file_to_load = file_path
with open(file_to_load,'r') as f:
    ### skip headings
    next(f)
    next(f)

    ### read out lines of sphere file
    exp_file=csv.reader(f,delimiter='\t')

    ### sort file content by line
    for lines in exp_file:
    	exp_file_lines.append(lines)

### read out shape
exp_file_lines_shape = np.shape(exp_file_lines)

### seperate data sheets
for l in range( exp_file_lines_shape[0] ):
	sphere_number.append( float(exp_file_lines[l][0]) )
	sphere_conductivity.append( float(exp_file_lines[l][1]) )
	sphere_porosity.append( float(exp_file_lines[l][2]) )
	sphere_volumeSolid.append( float(exp_file_lines[l][3]) )
	sphere_volumeFluid.append( float(exp_file_lines[l][4]) )
	sphere_coordinate_x.append( float(exp_file_lines[l][5]) )
	sphere_coordinate_y.append( float(exp_file_lines[l][6]) )
	sphere_coordinate_z.append( float(exp_file_lines[l][7]) )
	sphere_radius.append( float(sphere_radius_scalar) )

### function for scaling
def short_proj():
  return np.dot(Axes3D.get_proj(ax), scale)

### plot figure
fig = pl.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
ax = fig.add_subplot(111, projection='3d')

### scaling
x_scale=2.5
y_scale=5
z_scale=1

### scale plot dimensions according to box dimensions
scale=np.diag([x_scale, y_scale, z_scale, 1.0])
scale=scale*(1.0/scale.max())
scale[3,3]=1.0

ax.get_proj=short_proj

### draw a sphere for each data point
for (xi,yi,zi,ri) in zip(sphere_coordinate_x, sphere_coordinate_y, sphere_coordinate_z, sphere_radius):
    (xs,ys,zs) = draw_sphere(xi,yi,zi,ri)

    ### plot wireframe of spheres
    ax.plot_wireframe(xs, ys, zs,linewidth=0.1,color='r', alpha=0.4)

    ### plot surface of spheres
    surf = ax.plot_surface(xs, ys, zs, rstride=4, cstride=4, cmap='jet',vmin=z_min,vmax=z_max,
        shade=True,linewidth=0.5, alpha=0.4)


###### draw box
### box corner points
points = np.array([[x_min, y_min, z_min],
                      [x_max, y_min, z_min ],
                      [x_max, y_max, z_min],
                      [x_min, y_max, z_min],
                      [x_min, y_min, z_max],
                      [x_max, y_min, z_max ],
                      [x_max, y_max, z_max],
                      [x_min, y_max, z_max]])

### dx, dy and dz for meshgrid
xr = [x_min,x_max]
yr = [y_min,y_max]
zr = [z_min,z_max]

### create surface meshgrids
xX, xY = np.meshgrid(xr, yr)
yX, yY = np.meshgrid(xr, zr)
zX, zY = np.meshgrid(yr, zr)

### transparency for box sides with darker in/outlet
transparency_alpha_one = 0.05
transparency_alpha_two = 0.3

### plot surfaces
# ax.plot_surface(xX,xY,z_max, alpha=transparency_alpha_one)
# ax.plot_surface(xX,xY,z_min, alpha=transparency_alpha_one)
# ax.plot_surface(yX,y_min,yY, alpha=transparency_alpha_two)
# ax.plot_surface(yX,y_max,yY, alpha=transparency_alpha_two)
# ax.plot_surface(x_max,zX,zY, alpha=transparency_alpha_one)
# ax.plot_surface(x_min,zX,zY, alpha=transparency_alpha_one)

### corner points
#ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])

### label plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

### plot settings
#ax = pl.gca(projection='3d')
ax._axis3don = plot_axis
ax.grid(b=plot_grid)
ax.view_init(elev=plot_elevation, azim=plot_azimuth)
fig.tight_layout()
fig.set_dpi(100)
#[__.set_clip_on(True) for __ in pl.gca().get_children()]

pl.subplots_adjust(left=-0.4, right=1.1, top=2.1, bottom=-0.1)
pl.savefig( str(figure_path+'experimental_system.png'),
    bbox_inches='tight', pad_inches=0)#, transparent=plot_transparent )

pl.show()
exit()
