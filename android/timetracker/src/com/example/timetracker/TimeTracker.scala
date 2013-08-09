package com.example.timetracker

import android.app.{FragmentTransaction, ActionBar, Activity}
import android.os.{Handler, Bundle}
import android.widget._
import android.text.format.DateUtils
import android.view.{MenuItem, Menu, View}
import android.content.DialogInterface.OnClickListener
import android.text.method.DateTimeKeyListener
import android.app.ActionBar.{Tab, TabListener}
import android.util.Log
import android.support.v4.view.ViewPager
import android.support.v4.app.FragmentActivity

/**
 * Created with IntelliJ IDEA.
 * User: samkit
 * Date: 18/5/13
 * Time: 8:45 PM
 */
class TimeTracker extends FragmentActivity with View.OnClickListener with AsyncTimerCallback {
    var listAdaptor: TimerListAdaptor = _
    var timer: AsyncTimer = new AsyncTimer(this, 250)
    var startTime: Long = 0

    override def onCreateOptionsMenu(menu: Menu): Boolean = {
        super.onCreateOptionsMenu(menu)
        getMenuInflater().inflate(R.menu.menu, menu)
        return true
    }

    override def onOptionsItemSelected(item: MenuItem): Boolean = item.getItemId match {
        case R.id.clear_all => {
            Toast.makeText(getApplicationContext(), "Clearing", Toast.LENGTH_SHORT).show()
            return true
        }
        case _ => super.onOptionsItemSelected(item)
    }

    override def onCreate(savedInstance: Bundle) {
        super.onCreate(savedInstance)
        setContentView(R.layout.main)

        val adaptor = new SamplePagerAdapter(getSupportFragmentManager(), this)
        val pager = findViewById(R.id.view_pager).asInstanceOf[ViewPager]
        pager.setAdapter(adaptor)
        pager.setCurrentItem(0)

        val bar = getActionBar()
        bar.setNavigationMode(ActionBar.NAVIGATION_MODE_TABS)

        val listener = new TabListener {
            def onTabReselected(tab: Tab, ft: FragmentTransaction) {
                Log.e("TimeTracker", "Tab is reselected " + tab.getText)
            }

            def onTabUnselected(tab: Tab, ft: FragmentTransaction) {
                Log.e("TimeTracker", "Tab is UNselected " + tab.getText)
            }

            def onTabSelected(tab: Tab, ft: FragmentTransaction) {
                Log.e("TimeTracker", "Tab is SElected " + tab.getText)
            }
        }

        bar.addTab(bar.newTab().setText("Tab 1").setTabListener(listener))
        bar.addTab(bar.newTab().setText("Tab 2").setTabListener(listener))

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
                currentTimeView.setText(savedInstance.getString("current_time"))
                lapTimesView.smoothScrollToPosition(firstVisibleIndex)
            }
        }
        else {
            currentTimeView.setText(DateUtils.formatElapsedTime(0))
        }

        lapTimesView.setAdapter(listAdaptor)

        findViewById(R.id.start_stop).asInstanceOf[Button].setOnClickListener(this)
        findViewById(R.id.reset).asInstanceOf[Button].setOnClickListener(this)
    }

    override def onSaveInstanceState(bundle: Bundle) {
        val currentTimeView = findViewById(R.id.current_time).asInstanceOf[TextView]
        val listView = findViewById(R.id.list_view).asInstanceOf[ListView]
        bundle.putInt("first_visible", listView.getFirstVisiblePosition)
        val lapTimes = new Array[Long](listAdaptor.getCount)
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

    private def elapsedTime = (System.currentTimeMillis - startTime) / 1000

    private def startTimer() {
        startTime = System.currentTimeMillis
        timer.start
    }

    private def stopTimer() {
        listAdaptor.add(elapsedTime)
        timer.stop
    }
}
