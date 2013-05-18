package com.example.timetracker

import android.app.Activity
import android.os.Bundle
import android.widget.{Button, TextView, ListAdapter, ListView}
import android.text.format.DateUtils
import android.view.View
import android.content.DialogInterface.OnClickListener

/**
 * Created with IntelliJ IDEA.
 * User: samkit
 * Date: 18/5/13
 * Time: 8:45 PM
 */
class TimeTracker extends Activity with View.OnClickListener {
    var listAdaptor: TimerListAdaptor = _
    var count: Int = 0

    override def onCreate(savedInstance: Bundle) {
        super.onCreate(savedInstance)
        setContentView(R.layout.main)

        if (listAdaptor == null) {
            listAdaptor = new TimerListAdaptor(this, 0)
        }
        findViewById(R.id.current_time).asInstanceOf[TextView].setText(DateUtils.formatElapsedTime(0))
        val lapTimes = findViewById(R.id.list_view).asInstanceOf[ListView]
        lapTimes.setAdapter(listAdaptor)

        findViewById(R.id.start).asInstanceOf[Button].setOnClickListener(this)
        findViewById(R.id.stop).asInstanceOf[Button].setOnClickListener(this)
    }

    override def onClick(view: View) {
        if (view.getId == R.id.start) {
            count += 1
            listAdaptor.add(count)
        }
    }
}
