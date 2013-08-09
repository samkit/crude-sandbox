package io.github.periphery.eyes

import android.support.v4.app.FragmentActivity
import android.os.Bundle

/**
 * Created with IntelliJ IDEA.
 * User: samkit
 * Date: 21/7/13
 * Time: 10:39 AM
 */
class WelcomeActivity extends FragmentActivity {
    override def onCreate(savedInstanceState: Bundle) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.welcome_screen)
    }
}
