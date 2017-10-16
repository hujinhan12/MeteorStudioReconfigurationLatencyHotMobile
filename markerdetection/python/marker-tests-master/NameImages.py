import os
class NameImages:


    #the images that we capture have a different file names but we need to encode important information about the image into the name for easy access.
    #So, since we know the order in which images were captured we can then loop through the folder and rename them picking image names from the following list
    #Image names are as distance_phi_theta_width_height_sampleNumber.jpg

    file_arr = []
    file_arr.append('55_0_0_3024_4032_1.jpg')
    file_arr.append('55_0_0_3024_4032_2.jpg')
    file_arr.append('55_0_0_3024_4032_3.jpg')
    file_arr.append('55_0_0_3024_4032_4.jpg')
    file_arr.append('55_0_0_3024_4032_5.jpg')
    file_arr.append('55_0_0_3024_4032_6.jpg')
    file_arr.append('55_0_0_3024_4032_7.jpg')
    file_arr.append('55_0_0_3024_4032_8.jpg')
    file_arr.append('55_0_0_3024_4032_9.jpg')
    file_arr.append('55_0_0_3024_4032_10.jpg')


    file_arr.append('100_0_0_3024_4032_1.jpg')
    file_arr.append('100_0_0_3024_4032_2.jpg')
    file_arr.append('100_0_0_3024_4032_3.jpg')
    file_arr.append('100_0_0_3024_4032_4.jpg')
    file_arr.append('100_0_0_3024_4032_5.jpg')
    file_arr.append('100_0_0_3024_4032_6.jpg')
    file_arr.append('100_0_0_3024_4032_7.jpg')
    file_arr.append('100_0_0_3024_4032_8.jpg')
    file_arr.append('100_0_0_3024_4032_9.jpg')
    file_arr.append('100_0_0_3024_4032_10.jpg')


    file_arr.append('200_0_0_3024_4032_1.jpg')
    file_arr.append('200_0_0_3024_4032_2.jpg')
    file_arr.append('200_0_0_3024_4032_3.jpg')
    file_arr.append('200_0_0_3024_4032_4.jpg')
    file_arr.append('200_0_0_3024_4032_5.jpg')
    file_arr.append('200_0_0_3024_4032_6.jpg')
    file_arr.append('200_0_0_3024_4032_7.jpg')
    file_arr.append('200_0_0_3024_4032_8.jpg')
    file_arr.append('200_0_0_3024_4032_9.jpg')
    file_arr.append('200_0_0_3024_4032_10.jpg')

    file_arr.append('100_0_45_3024_4032_1.jpg')
    file_arr.append('100_0_45_3024_4032_2.jpg')
    file_arr.append('100_0_45_3024_4032_3.jpg')
    file_arr.append('100_0_45_3024_4032_4.jpg')
    file_arr.append('100_0_45_3024_4032_5.jpg')
    file_arr.append('100_0_45_3024_4032_6.jpg')
    file_arr.append('100_0_45_3024_4032_7.jpg')
    file_arr.append('100_0_45_3024_4032_8.jpg')
    file_arr.append('100_0_45_3024_4032_9.jpg')
    file_arr.append('100_0_45_3024_4032_10.jpg')


    file_arr.append('200_0_45_3024_4032_1.jpg')
    file_arr.append('200_0_45_3024_4032_2.jpg')
    file_arr.append('200_0_45_3024_4032_3.jpg')
    file_arr.append('200_0_45_3024_4032_4.jpg')
    file_arr.append('200_0_45_3024_4032_5.jpg')
    file_arr.append('200_0_45_3024_4032_6.jpg')
    file_arr.append('200_0_45_3024_4032_7.jpg')
    file_arr.append('200_0_45_3024_4032_8.jpg')
    file_arr.append('200_0_45_3024_4032_9.jpg')
    file_arr.append('200_0_45_3024_4032_10.jpg')


    file_arr.append('55_0_45_3024_4032_1.jpg')
    file_arr.append('55_0_45_3024_4032_2.jpg')
    file_arr.append('55_0_45_3024_4032_3.jpg')
    file_arr.append('55_0_45_3024_4032_4.jpg')
    file_arr.append('55_0_45_3024_4032_5.jpg')
    file_arr.append('55_0_45_3024_4032_6.jpg')
    file_arr.append('55_0_45_3024_4032_7.jpg')
    file_arr.append('55_0_45_3024_4032_8.jpg')
    file_arr.append('55_0_45_3024_4032_9.jpg')
    file_arr.append('55_0_45_3024_4032_10.jpg')

    def name_images(self,folderpath):

        arr_txt = [x for x in os.listdir(folderpath)]
        print arr_txt
        num_files=len(arr_txt)
        for i in range(0,num_files):
            os.rename(folderpath+"/"+arr_txt[i],folderpath+"/"+self.file_arr[i])
