LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

OPENCVROOT:={}
OPENCV_CAMERA_MODULES:=on
OPENCV_INSTALL_MODULES:=on
OPENCV_LIB_TYPE:=SHARED
include ${OPENCVROOT}/native/jni/OpenCV.mk

LOCAL_MODULE    := opencvcamera
LOCAL_SRC_FILES := com_msrs_opencv_android_NativeCallMethods.cpp

LOCAL_LDLIBS += -llog -landroid -lEGL -lGLESv2
LOCAL_LDLIBS    += -lOpenMAXAL -lmediandk
LOCAL_LDLIBS    += -landroid
LOCAL_CFLAGS    += -UNDEBUG

include $(BUILD_SHARED_LIBRARY)
