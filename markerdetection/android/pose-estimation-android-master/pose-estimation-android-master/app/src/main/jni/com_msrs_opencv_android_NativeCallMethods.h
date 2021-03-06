/* DO NOT EDIT THIS FILE - it is machine generated */
#include <jni.h>
#include <opencv2/core/mat.hpp>
/* Header for class com_msrs_opencv_android_NativeCallMethods */

#ifndef _Included_com_msrs_opencv_android_NativeCallMethods
#define _Included_com_msrs_opencv_android_NativeCallMethods



#ifdef __cplusplus
extern "C" {
#endif


JNIEXPORT void JNICALL
        Java_com_msrs_pose_1estimation_NativeCallMethods_poseEstimateNative(JNIEnv *env, jclass type,
                                                                          jint width, jint height,
                                                                          jobject buffer, jobject dst,
                                                                          jboolean colorFlag);

JNIEXPORT jint JNICALL
Java_com_msrs_pose_1estimation_NativeCallMethods_generateReferenceImageNative(JNIEnv *env,
                                                                             jclass type,
                                                                             jbyteArray refImage);

#ifdef __cplusplus
}
#endif
#endif
