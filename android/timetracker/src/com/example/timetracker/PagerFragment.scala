package com.example.timetracker

import android.app.Fragment
import android.view.{View, ViewGroup, LayoutInflater}
import android.os.Bundle

/**
 * Created with IntelliJ IDEA.
 * User: samkit
 * Date: 6/7/13
 * Time: 11:44 PM
 */
class PagerFragment extends Fragment {
    override def onCreateView(inflater: LayoutInflater, container: ViewGroup, savedInstanceState: Bundle): View = {
        inflater.inflate(R.id.pager, null)
    }
}
