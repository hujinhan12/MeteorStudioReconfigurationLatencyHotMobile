# entry file. This file calls all the important functions needed to process images and estimate pose.
from MarkerDetectionAndPose import PoseEstimate
from genReferenceImage import ReferenceImage
from NameImages import NameImages
from readRaw import ReadRaw
from GenerateImages import GenerateImages
import os
import csv
import time

readRaw = ReadRaw()
referenceImage = ReferenceImage()
nameImages=NameImages()
poseEstimate=PoseEstimate()
generateImages=GenerateImages()

#the input image folder in our experiment contains 10 samples of each configuration in the 3024 x 4032 resolution
#A configuration is defined by distance between marker and camera, capture angle and resolution. The inputs can be either in dng format or jpg format

inputImageFolderPath = 'InputImageFolder'
outputImageFolderPath ='OutputImageFolder'

#if conversion is not needed directly paste the images into the output folder


#if the images are in RAW format uncomment the next portion of the code
'''
start_time_for_conversion = time.time()
all_files = [x for x in os.listdir(inputImageFolderPath)]
print all_files
num_files=len(all_files)
for i in range(0,num_files):
    readRaw.convertFileFromRaw(inputImageFolderPath+'/'+all_files[i],all_files[i])
print "Time for Image Conversion {}".format(time.time()-start_time_for_conversion)
'''

#renames all the images based on our configurations.Open NameImages.py for more information
nameImages.name_images(outputImageFolderPath)


#writing the header into a scv file which will be used to store the results
with open('output.csv', 'wb') as csvfile:
    fieldnames = ['numFeaturesReference','numFeaturesTest','width', 'height', 'distance', 'phi', 'theta', 'num', 'rvecs[0]', 'rvecs[1]', 'rvecs[2]',
                          'tvecs[0]', 'tvecs[1]', 'tvecs[2]']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator='\n')
    writer.writeheader()

#The following code creates many images of required sizes specified in the GenerateImages.py file
start_time_for_resize = time.time()
all_files = [x for x in os.listdir(outputImageFolderPath)]
num_files=len(all_files)
for i in range(0,num_files):
    generateImages.resize_save(outputImageFolderPath+'/'+all_files[i],all_files[i],outputImageFolderPath)
print "Time for Image Resize {}".format(time.time() - start_time_for_resize)

#the listFeatures specifies the number of features we want to use while generating data from the reference image
listFeatures = [5000]

for j in range(0,len(listFeatures)):

    numFeatures = listFeatures[j]
    all_files = [x for x in os.listdir(outputImageFolderPath)]
    num_files=len(all_files)
    start_time_for_pose = time.time()

    #we need to extract information from the reference Image only once for a given number of features.
    (keypointsReference, descriptorsReference, cameraParams, points3D) = referenceImage.generate_kp_desc(numFeatures)

    #we loop across all the files present
    for i in range(0,num_files):
        start_time_for_img = time.time()
        filename_no_extension = all_files[i].split('.')[0]
        file_details = filename_no_extension.split('_')
        dist = file_details[0]
        phi = file_details[1]
        theta = file_details[2]
        width = file_details[3]
        height = file_details[4]
        num = file_details[5]
        print all_files[i]

        #calculating pose
        numFeaturesTest = 5000;
        res = poseEstimate.calculate_Pose(outputImageFolderPath+'/'+all_files[i],keypointsReference,descriptorsReference,cameraParams,points3D,numFeaturesTest)

        #writing results to a csv file
        with open('output.csv', 'a') as csvfile:
            fieldnames = ['numFeaturesReference','numFeaturesTest','width', 'height', 'distance', 'phi', 'theta', 'num', 'rvecs[0]', 'rvecs[1]', 'rvecs[2]',
                          'tvecs[0]', 'tvecs[1]', 'tvecs[2]']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator='\n')

            if(res!=None):
                writer.writerow({'numFeaturesReference':numFeatures,'numFeaturesTest':numFeaturesTest,'width':width, 'height':height,'distance':dist,'phi':phi,'theta':theta,'num':num,'rvecs[0]':res[0],
                             'rvecs[1]':res[1],'rvecs[2]':res[2],'tvecs[0]':res[3],'tvecs[1]':res[4],'tvecs[2]':res[5]})

            else:
                writer.writerow({'numFeaturesReference':numFeatures,'numFeaturesTest':numFeaturesTest,'width': width, 'height': height, 'distance': dist, 'phi': phi, 'theta': theta, 'num': num,
                                 'rvecs[0]': str(None),
                                 'rvecs[1]': str(None), 'rvecs[2]': str(None), 'tvecs[0]': str(None), 'tvecs[1]': str(None),
                                 'tvecs[2]': str(None)})

        print "Time for {0} Image Pose Estimation {1}".format(all_files[j],time.time() - start_time_for_img)

print "Time for All file Pose Estimation {}".format(time.time()-start_time_for_pose)
