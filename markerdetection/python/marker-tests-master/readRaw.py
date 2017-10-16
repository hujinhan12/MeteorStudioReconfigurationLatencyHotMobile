import cv2
import numpy as np
from PIL import Image
from rawkit.raw import Raw
import imageio
import rawpy
import os


#incase the input format is .dng then we need to covert the images into a readable format for OpenCV.
class ReadRaw:

    def convertFileFromRaw(self,filepath,filename,outputFolder):

        filename_no_extension=filename.split('.')[0]
        raw = rawpy.imread(filepath)
        rgb = raw.postprocess(no_auto_bright=True,use_auto_wb =True,gamma=None)
        imageio.imwrite(outputFolder+'/'+filename_no_extension+'.jpg', rgb)


