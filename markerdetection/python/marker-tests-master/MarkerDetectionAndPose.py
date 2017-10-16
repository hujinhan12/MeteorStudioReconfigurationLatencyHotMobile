import numpy as np
import cv2
import sys, getopt


class PoseEstimate:
    def calculate_Pose(self, inputimage, keypointsReference, descriptorsReference, cameraParams, points3D,numFeatures):

        imgColor = cv2.imread(inputimage)

        img2 = cv2.imread(inputimage, 0)  # trainIma

        #cx is width/2, cy is height/2
        cx = img2.shape[1] / 2
        cy = img2.shape[0] / 2
        fx = cx * 1.73
        fy = cx * 1.73

        #creating the camera instrinsic parameters matrix
        cameraParams = np.zeros((3, 3), np.float32)

        cameraParams[0][0] = fx
        cameraParams[0][2] = cx
        cameraParams[1][1] = fy
        cameraParams[1][2] = cy
        cameraParams[2][2] = 1

        # SIFT Implementation, Comment the Orb portion if using SIFT. also Change the feature extractor in the genReferenceImageFile accordingly
        sift = cv2.SIFT(nfeatures=numFeatures)

        keypointsDest = sift.detect(img2, None)
        keypointsDest, descriptorsDest = sift.compute(img2, keypointsDest)

        # taking a flann based matcher
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)

        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(descriptorsDest, descriptorsReference, k=2)
        good = []

        for (m, n) in (matches):
            if m.distance < 0.7 * n.distance:
                good.append(m)

        kp2 = []
        print "Matches", len(good)
        for i in range(0, len(good)):
            idx = good[i].queryIdx
            kp2.append(keypointsDest[idx])

        # SIFT implementation ends

        # ORB Implementation

        '''
        orb =cv2.ORB(nfeatures=5000)
        keypointsDest, descriptorsDest = orb.detectAndCompute(img2, None)

        FLANN_INDEX_LSH = 6
        index_params = dict(algorithm=FLANN_INDEX_LSH,table_number=6,key_size=10, multi_probe_level=2)
        search_params = dict(checks=50)

        if(descriptorsReference==None or descriptorsDest==None):
            return None
        descriptorsReference.astype(np.float32)
        descriptorsDest.astype(np.float32)

        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(descriptorsDest, descriptorsReference, k=2)
        good = []

        for match in matches:
            try:

                if(match[0] and match[1]):
                    if match[0].distance < 0.8*match[1].distance:
                        good.append(match[0])
            except:
                print "Error"

        # drawing matches on
        # good = [[0, 0] for i in xrange(len(matches))]
        #
        # for i, (m, n) in enumerate(matches):
        #     if m.distance < 0.7 * n.distance:
        #         good[i] = [1, 0]

        kp2 = []
        print "Matches", len(good)
        for i in range(0, len(good)):
            idx = good[i].queryIdx
            kp2.append(keypointsDest[idx])

        
        '''
        # ORB Implementation ends

        # prepare data for findHomography
        src_pts = np.float32([keypointsReference[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypointsDest[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)

        try:
            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        except:
            print "Error"
            return None

        matchesMask = mask.ravel().tolist()

        inliers = []

        for i in range(0, len(matchesMask)):
            if (matchesMask[i]):
                inliers.append(good[i])

        num_inliers = len(inliers)

        # making a list of corresponding 3D and 2D points

        pnp3d = np.empty((num_inliers, 1, 3), np.float32)
        pnp2d = np.empty((num_inliers, 1, 2), np.float32)
        for i in range(0, num_inliers):
            i1 = inliers[i].trainIdx
            pnp3d[i] = (points3D[i1])
            i2 = inliers[i].queryIdx
            pnp2d[i] = keypointsDest[i2].pt

        dist = np.zeros((5, 1), np.float32)

        rvecs, tvecs, inliers = cv2.solvePnPRansac(pnp3d, pnp2d, cameraParams, dist)

        axisLength = 10
        axisCube = np.float32([[0, 0, 0], [0, axisLength, 0], [axisLength, axisLength, 0], [axisLength, 0, 0],
                               [0, 0, -axisLength], [0, axisLength, -axisLength], [axisLength, axisLength, -axisLength],
                               [axisLength, 0, -axisLength]])

        imgpts, jac = cv2.projectPoints(axisCube, rvecs, tvecs, cameraParams, dist)

        # drawing the cube
        imgpts = np.int32(imgpts).reshape(-1, 2)

        # draw ground floor in black filled
        cv2.drawContours(imgColor, [imgpts[:4]], -1, (0,0 ,0),-1);
        cv2.drawContours(imgColor, [imgpts[:4]], -1, (223, 223, 255), 9);

        # draw pillars in light red color
        for i, j in zip(range(4), range(4, 8)):
            cv2.line(imgColor, tuple(imgpts[i]), tuple(imgpts[j]), (223, 223, 255), 9)

        # draw top layer in red color
        cv2.drawContours(imgColor, [imgpts[4:]], -1, (223, 223, 255), 9)

        #uncomment the following code to show the image on the screen.
        '''
        cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('img', 1000, 1333)
        cv2.imshow('img', imgColor)
        cv2.waitKey(0)
        '''

        a = [0] * 6

        a[0] = rvecs[0][0] * 180 / 3.14
        a[1] = rvecs[1][0] * 180 / 3.14
        a[2] = rvecs[2][0] * 180 / 3.14
        a[3] = tvecs[0][0]
        a[4] = tvecs[1][0]
        a[5] = tvecs[2][0]

        return a
