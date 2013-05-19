package com.example.timetracker

/**
 * Created with IntelliJ IDEA.
 * User: samkit
 * Date: 19/5/13
 * Time: 11:22 AM
 */
trait AsyncTimerCallback {
    def onTime(timer: AsyncTimer)
}
