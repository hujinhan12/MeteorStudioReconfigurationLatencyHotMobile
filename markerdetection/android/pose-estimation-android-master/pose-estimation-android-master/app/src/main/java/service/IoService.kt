package service

import android.app.PendingIntent.getActivity
import android.app.Service
import android.content.Context
import android.content.Intent
import android.os.IBinder
import android.os.Process
import android.util.Log
import com.msrs.pose_estimation.NativeCallMethods
import com.msrs.pose_estimation.R
import java.io.File
import java.io.FileOutputStream
import java.util.*


class IoService : Service() {

    lateinit var mReferenceImage: File

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        Log.d("IoService", "Starting service...")
        return super.onStartCommand(intent, flags, startId)
    }

    override fun onBind(intent: Intent): IBinder = binder

    fun getTime():String = "10:46"

    private val binder = object:IIoService.Stub(){
        override fun basicTypes(anInt: Int, aLong: Long, aBoolean: Boolean, aFloat: Float, aDouble: Double, aString: String?) {
            // Nothing
        }

        override fun getPid(): Int = Process.myPid()

//        fun getReferenceImage():ByteArray{
//
//
//            //load the reference image
//            try {
//                val `is` = resources.openRawResource(R.raw.stones)
//                val cascadeDir = getActivity().getDir("ref", Context.MODE_PRIVATE)
//
//                mReferenceImage = File(cascadeDir, "referenceImage.jpg")
//                val os = FileOutputStream(mReferenceImage)
//
//                val buffer = ByteArray(4096)
//                val bytesRead: Int
//                while ((bytesRead = `is`.read(buffer)) != -1) {
//                    os.write(buffer, 0, bytesRead)
//                }
//
//                `is`.close()
//                os.close()
//
//            } catch (e: Exception) {
//                e.printStackTrace()
//            }
//
//            val mat: MatOfPoint3f = NativeCallMethods.generateReferenceImage(mReferenceImage.absolutePath)
//        }
    }
}
