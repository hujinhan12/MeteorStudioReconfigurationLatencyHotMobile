import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,AnnotationBbox)
import numpy as np

y0=[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,1.79,1.15,1.45,1.28,1.13,1.01,0.9,0.82,0.67,0.65,0.57,0.45,0.32,0.25,0.2,0.16,0.14,0.13,0.11,0.08,0.08,0.07,0.07,0.06,0.05,0.04,0.04,0.03,0.03]

y40=[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,2.34,2.08,1.85,1.66,1.5,1.24,1.19,1.04,0.82,0.59,0.46,0.38,0.3,0.26,0.24,0.2,0.16,0.14,0.13,0.12,0.11,0.09,0.08,0.07,0.06,0.06]

x=[0.000768,0.001728,0.003072,0.0048,0.0075,0.0108,0.0147,0.017328,0.0192,0.0243,0.03,0.0363,0.047628,0.0588,0.0675,0.0768,0.0972,0.12,0.1452,0.1728,0.1875,0.2187,0.2523,0.27,0.3072,0.3468,0.3888,0.4332,0.48,0.5808,0.6075,0.6912,0.8748,1.2288,1.5552,1.92,2.43,2.7648,3,3.63,4.6128,5.07,5.5488,5.88,6.75,7.8732,8.8752,9.9372,11.244288,12]

xy1=[0,2]
xy2=[0,0.5]
fig, ax = plt.subplots()
img1 = mpimg.imread('/Users/Americadog/Documents/phd/Hotmobilereconfig/result/2percent.JPG')
imagebox = OffsetImage(img1, zoom=0.07)
imagebox.image.axes = ax
ab = AnnotationBbox(imagebox, xy1,
xybox=(250., -60.), xycoords='data',
boxcoords="offset points",
pad=0.5,
arrowprops=dict(
arrowstyle="->",
connectionstyle="angle,angleA=90,angleB=180,rad=3"))
ax.add_artist(ab)
img2 = mpimg.imread('/Users/Americadog/Documents/phd/Hotmobilereconfig/result/05percent.JPG')
imagebox = OffsetImage(img2, zoom=0.07)
imagebox.image.axes = ax
ab = AnnotationBbox(imagebox, xy2,
xybox=(800., 70.), xycoords='data',
boxcoords="offset points",
pad=0.5,
arrowprops=dict(
arrowstyle="->",
connectionstyle="angle,angleA=90,angleB=180,rad=3"))
ax.add_artist(ab)
ax.plot(x, y0, 'k*',label="0˚   View angle", markersize = 20)
ax.plot(x, y40, 'c^',label="48˚ View angle", markersize = 20)
plt.xlabel('Number of megapixels captured per frame', fontsize = 48)
plt.ylabel('Min. marker pixels as\npercentage of frame', fontsize = 48)
plt.xticks(fontsize=34)
plt.yticks(fontsize=34)
plt.legend(loc = 'upper right', fontsize=48)
plt.show()
