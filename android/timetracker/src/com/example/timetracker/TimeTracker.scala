package com.example.timetracker

import android.app.Activity
import android.os.{Handler, Bundle}
import android.widget._
import android.text.format.DateUtils
import android.view.View
import android.content.DialogInterface.OnClickListener
import android.text.method.DateTimeKeyListener

/**
 * Created with IntelliJ IDEA.
 * User: samkit
 * Date: 18/5/13
 * Time: 8:45 PM
 */
class TimeTracker extends Activity with View.OnClickListener with AsyncTimerCallback {
    var listAdaptor: TimerListAdaptor = _
    var timer: AsyncTimer = new AsyncTimer(this, 250)
    var startTime: Long = 0

    override def onCreate(savedInstance: Bundle) {
        super.onCreate(savedInstance)
        setContentView(R.layout.main)

        listAdaptor = new TimerListAdaptor(this, 0)

        val lapTimesView = findViewById(R.id.list_view).asInstanceOf[ListView]
        val currentTimeView = findViewById(R.id.current_time).asInstanceOf[TextView]

        currentTimeView.setText(DateUtils.formatElapsedTime(0))

        if (savedInstance != null) {
            val firstVisibleIndex = savedInstance.getInt("first_visible", -1)
            if (firstVisibleIndex != -1) {
                val lapTimes = savedInstance.getLongArray("lap_times")
                if (lapTimes != null) {
                    lapTimes.map { listAdaptor.add(_) }
                }
                lapTimesView.smoothScrollToPosition(firstVisibleIndex)
                currentTimeView.setText(savedInstance.getString("current_time"))
            }
        }

        findViewById(R.id.current_time).asInstanceOf[TextView].setText(DateUtils.formatElapsedTime(0))
        lapTimesView.setAdapter(listAdaptor)

        findViewById(R.id.start_stop).asInstanceOf[Button].setOnClickListener(this)
        findViewById(R.id.reset).asInstanceOf[Button].setOnClickListener(this)
    }

    override def onSaveInstanceState(bundle: Bundle) {
        val currentTimeView = findViewById(R.id.current_time).asInstanceOf[TextView]
        val listView = findViewById(R.id.list_view).asInstanceOf[ListView]
        bundle.putInt("first_visible", listView.getFirstVisiblePosition)
        var lapTimes = new Array[Long](listAdaptor.getCount)
        for (lap <- 0 to listAdaptor.getCount - 1)
            lapTimes.update(lap, listAdaptor.getItem(lap))
        bundle.putLongArray("lap_times", lapTimes)
        bundle.putString("current_time", currentTimeView.getText.toString)
        super.onSaveInstanceState(bundle)
    }

    override def onClick(view: View) = view.getId match {
        case R.id.start_stop => {
            val textView = view.asInstanceOf[TextView]
            if (textView.getText == "Start") {
                startTimer()
                textView.setText("Stop")
            }
            else {
                stopTimer()
                textView.setText("Start")
            }
        }
        case _ => {
            stopTimer()
            val currentTimeView = findViewById(R.id.current_time).asInstanceOf[TextView]
            currentTimeView.setText(DateUtils.formatElapsedTime(0))
            listAdaptor.clear
        }
    }

    override def onTime(timer: AsyncTimer) {
        val view = findViewById(R.id.current_time).asInstanceOf[TextView]
        view.setText(DateUtils.formatElapsedTime(elapsedTime))
    }

    private def elapsedTime = System.currentTimeMillis - startTime

    private def startTimer() {
        startTime = System.currentTimeMillis
        timer.start
    }

    private def stopTimer() {
        listAdaptor.add(elapsedTime)
        timer.stop
    }
}
