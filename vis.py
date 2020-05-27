
"""
REFERENCES
(1) GenerateMesh() --> KinematicModel.cpp - no normalization
(2) vis_data object, connections --> VisualizeData.h - no normalization
(3) plotskeleton (), vis_type = 2 -->renderer.cpp - no normalization


"""

""" double gResultJoint[21 * 3 + 2 * 21 * 3];
 Format is [x,y,z,x,y,z,...]
x --> 3*i
y --> 3*i+1
z --> 3*i+2

for (int i = 0; i < 21; i++)
{
	resultJoint[3 * i] = J_coco(map_cocoreg_to_measure[i], 0);
	resultJoint[3 * i + 1] = J_coco(map_cocoreg_to_measure[i], 1);
	resultJoint[3 * i + 2] = J_coco(map_cocoreg_to_measure[i], 2);
}


CONNECTIONS
int hand[] = {0, 1, 1, 2, 2, 3, 3, 4,
	0, 5, 5, 6, 6, 7, 7, 8,
	0, 9, 9, 10, 10, 11, 11, 12,
	0, 13, 13, 14, 14, 15, 15, 16,
	0, 17, 17, 18, 18, 19, 19, 20
};

int body[] = {
	0, 1,
	0, 3, 3, 4, 4, 5,
	0, 9, 9, 10, 10, 11,
	0, 2,
	2, 6, 6, 7, 7, 8,
	2, 12, 12, 13, 13, 14,
	1, 15, 15, 16,
	1, 17, 17, 18
};


"""

"""
Normalize all coords to -1 to 1 based on max x,y,z coords and plot

- Remove tracking and optical flow

plot for example_dance (crop to a smaller video
)

"""


from matplotlib import pyplot as plt 
import numpy as np


def plot_skeleton(joints):
	fig = plt.figure(figsize=(15,15))
	ax = fig.add_subplot(121, projection='3d')

	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	# ax.set_xlim(-1, 1)
	# ax.set_ylim(-1, 1)
	# ax.set_zlim(-1.5, 1)

	ax.scatter(joints[:, 0], joints[:, 1], joints[:, 2], color='r')
	for i in range(21):
		ax.text(joints[i, 0], joints[i, 1], joints[i, 2], str(i))
	# ax.view_init(-140, 30)

	plt.draw()
	plt.show()


lines= [] 
with open('output.txt') as f: 
	for i in f: 
		lines.append(i.rstrip()) 

data = [] 
for i in lines: 
	x = i.split(' ') 
	x = [float(j) for j in x] 
	data.append(x) 

data =  np.asarray(data, dtype=np.float32) # (nx189)
data_reshaped = np.zeros(shape = (data.shape[0], 21,3))

body_pose = data[:,:63]
data_reshaped = body_pose.reshape(data.shape[0], 21,3)

# import pdb; pdb.set_trace()

plot_skeleton(data_reshaped[0])

