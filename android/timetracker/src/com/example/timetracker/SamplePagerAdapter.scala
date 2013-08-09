package com.example.timetracker

import android.support.v4.app.{FragmentActivity, FragmentManager, Fragment, FragmentPagerAdapter}
import android.view.{View, ViewGroup, LayoutInflater}
import android.os.Bundle
import android.widget.{Button, TextView}
import android.support.v4.view.ViewPager
import android.util.Log

/**
 * Created with IntelliJ IDEA.
 * User: samkit
 * Date: 6/7/13
 * Time: 11:03 PM
 */
class SamplePagerAdapter(val manager: FragmentManager, val activity: FragmentActivity) extends FragmentPagerAdapter(manager) {
    def getCount: Int = 3

    def getItem(i: Int): Fragment = new Fragment {
        override def onCreateView(inflater: LayoutInflater, container: ViewGroup, savedInstanceState: Bundle): View = {
            val view = new TextView(activity)
            Log.e("TimeTracker", "Currently on tab " + i)
            view.setText("This is tab " + i)
//            container.addView(view, 0)
            return view
        }
    }
}
