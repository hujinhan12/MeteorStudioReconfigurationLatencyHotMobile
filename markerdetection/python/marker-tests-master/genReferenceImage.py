import cv2
import numpy as np

class ReferenceImage:

    def generate_kp_desc(self,numFeatures):

        img1 = cv2.imread('referenceImage.jpg',0)    # queryImage
        
        
        # Camera params
        # cx is width/2, cy is height/2
        
        cx = 918
        cy = 637
        fx = cx * 1.73 #tan 30
        fy = cx * 1.73

        #creating the camera instrinsic parameters matrix
        cameraParams = np.zeros((3, 3), np.float32)

        cameraParams[0][0] = fx
        cameraParams[0][2] = cx
        cameraParams[1][1] = fy
        cameraParams[1][2] = cy
        cameraParams[2][2] = 1

        #the feature extractor being used. remember that ORB is binray which SIFT is not. Hence they return different datatypes for descriptors.
        #Changing the feature extactor means that you will have to change the feature extractor inside the MarkerDetectionAndPose.py as well.
        sift = cv2.SIFT(nfeatures = numFeatures)
        # sift = cv2.ORB(nfeatures=numFeatures)

        keypointsReference = sift.detect(img1, None)
        keypointsReference, descriptorsReference = sift.compute(img1, keypointsReference)

        heightforImage = 35
        num_kp = len(keypointsReference)
        points3D = np.empty((num_kp, 1, 3), np.float32)

        count = 0

        for kp in enumerate(keypointsReference):
            x = kp[1].pt[0]
            y = kp[1].pt[1]
            Z = 0
            X = (1.00 * heightforImage / fx) * (x-cx )
            Y = (1.00 * heightforImage / fy) * (y-cy )
            pt3d = np.zeros((1, 3), np.float32)
            pt3d[0][0] = X
            pt3d[0][1] = Y
            pt3d[0][2] = Z
            points3D[count] = pt3d
            count += 1


        return keypointsReference,descriptorsReference,cameraParams,points3D


