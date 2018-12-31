package service

import android.app.Service
import android.content.Intent
import android.os.IBinder
import android.os.Process
import android.util.Log
import com.msrs.pose_estimation.R
import java.io.ByteArrayOutputStream
import java.io.File


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

        override fun getReferenceImage():ByteArray{

            Log.d("IoService", "getReferenceImage()");
            //load the reference image
            try {
                val inputStream = resources.openRawResource(R.raw.stones)

                val bb = ByteArrayOutputStream()

                val buffer = ByteArray(4096)
                var bytesRead: Int = inputStream.read(buffer)
                while(bytesRead != -1) {
                    bb.write(buffer)
                    bytesRead = inputStream.read(buffer)
                }

                inputStream.close()
//                os.close()
                Log.d("IoService", "getReferenceImage() finished with " + bb.size() + " bytes")
                return bb.toByteArray()

            } catch (e: Exception) {
                e.printStackTrace()
            }
            return ByteArray(0)
        }
    }
}
