package com.example.timetracker

import android.os.{Message, Handler}
import android.util.Log

/**
 * Created with IntelliJ IDEA.
 * User: samkit
 * Date: 19/5/13
 * Time: 11:13 AM
 */
class AsyncTimer(callback: AsyncTimerCallback, interval: Long) extends Handler {
    override def handleMessage(message: Message) {
        callback.onTime(this)
        sendEmptyMessageDelayed(0, interval)
    }

    def start() = sendEmptyMessage(0)
    def stop() = removeMessages(0)
}
