package service

import android.app.Service
import android.content.Intent
import android.os.IBinder
import android.os.Process
import android.util.Log
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

    }
}
