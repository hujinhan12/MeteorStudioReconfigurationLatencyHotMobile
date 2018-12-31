package com.msrs.pose_estimation;


import android.graphics.ImageFormat;
import android.media.Image;
import android.view.Surface;

import org.opencv.core.Mat;
import org.opencv.core.MatOfPoint2f;
import org.opencv.core.MatOfPoint3f;

import java.nio.ByteBuffer;

public class NativeCallMethods {


    //loading library that is built with opencv modules and our cpp files
    static{
        System.loadLibrary("opencvcamera");
    }

    public static void poseEstimate(Image src, Surface dst, boolean colorFlag)
    {
        if (src.getFormat() != ImageFormat.YUV_420_888) {
            throw new IllegalArgumentException("src must have format YUV_420_888.");
        }

        Image.Plane[] planes = src.getPlanes();
        if (planes[1].getPixelStride() != 1 && planes[1].getPixelStride() != 2) {
            throw new IllegalArgumentException(
                    "src chroma plane must have a pixel stride of 1 or 2: got "
                            + planes[1].getPixelStride());
        }
        poseEstimateNative(src.getWidth(), src.getHeight(), planes[0].getBuffer(),dst,false);
    }
    public static int generateReferenceImage(byte[] refImage)
    {
        return generateReferenceImageNative(refImage);
    }

    //passing the image buffer to cpp code which estimates the pose based on feature matching, find homography and pnp transform.
    public static native void poseEstimateNative(int width, int height, ByteBuffer buffer, Surface dst, boolean colorFlag);
    //passing the reference image when the application starts up to extract and store keypoints. This is called only once.
    public static native int generateReferenceImageNative(byte[] refImage);
}
