package com.example.timetracker

import android.widget.{TextView, ArrayAdapter}
import android.content.Context
import android.view.{LayoutInflater, ViewGroup, View}
import android.text.format.DateUtils

/**
 * Created with IntelliJ IDEA.
 * User: samkit
 * Date: 18/5/13
 * Time: 9:13 PM
 */
class TimerListAdaptor(context: Context, id: Int) extends ArrayAdapter[Long](context, id) {
    override def getView(position: Int, currentView: View, parent: ViewGroup): View = {
        var view = currentView
        if (view == null) {
            view = LayoutInflater.from(context).inflate(R.layout.row, null)
        }

        val time = getItem(position)
        val lapNumber = view.findViewById(R.id.lap_number).asInstanceOf[TextView]
        val lapTime = view.findViewById(R.id.lap_time).asInstanceOf[TextView]
        lapNumber.setText("Lap " + (position + 1))
        lapTime.setText(DateUtils.formatElapsedTime(time))
        view
    }
}
