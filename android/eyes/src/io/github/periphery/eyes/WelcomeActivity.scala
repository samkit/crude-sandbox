package io.github.periphery.eyes

import android.support.v4.app.{LoaderManager, FragmentActivity}
import android.os.{CountDownTimer, Bundle}
import android.util.Log
import android.support.v4.content.{CursorLoader, Loader}
import android.database.Cursor
import android.support.v4.widget.CursorAdapter
import android.view.{ViewGroup, View}
import android.content.Context
import android.widget.{TextView, ListView}

/**
 * Created with IntelliJ IDEA.
 * User: samkit
 * Date: 21/7/13
 * Time: 10:39 AM
 */
class WelcomeActivity extends FragmentActivity with LoaderManager.LoaderCallbacks[Cursor] {
    private class EyesCursorAdapter(context: Context, cursor: Cursor, flags: Integer) extends CursorAdapter(context, cursor, flags) {
        def newView(p1: Context, p2: Cursor, p3: ViewGroup): View = {
            val layout = getLayoutInflater.inflate(R.layout.row, null)
            val view = layout.findViewById(R.id.one_row).asInstanceOf[TextView]
            val value = p2.getString(p2.getColumnIndex("Name"))
            view.setText(value)
            layout
        }

        def bindView(view: View, p2: Context, cursor: Cursor) {
//            view.asInstanceOf[TextView].setText(cursor.getString(cursor.getColumnIndex(EyesContract.Projection.Name)))
        }
    }

    private var adapter: EyesCursorAdapter = _

    override def onCreate(savedInstanceState: Bundle) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.welcome_screen)
        new CountDownTimer(1000 * 60, 1000) {
            def onFinish() {}
            def onTick(p1: Long) {
                Log.e("on-time", "doing something: " + p1)
            }
        }

        Log.e("welcome", "Content uri is " + EyesContract.ContentUri.toString)

        getSupportLoaderManager.initLoader(0, null, this)

        adapter = new EyesCursorAdapter(getApplicationContext, null, 0)
        val listView = findViewById(R.id.my_list_view).asInstanceOf[ListView]
        listView.setAdapter(adapter)
    }

    def onCreateLoader(p1: Int, p2: Bundle): Loader[Cursor] = {
        new CursorLoader(getApplicationContext, EyesContract.ContentUri,
            Array(EyesContract.Projection.Name), null, Array(""), null)
    }

    def onLoadFinished(p1: Loader[Cursor], p2: Cursor) {
        if (p2 != null) {
            Log.e("loader", "OnLoadFinished: Got " + p2.getCount + " rows")
            Log.e("loader", "OnLoadFinished: Column names " + p2.getColumnNames.mkString(","))
            while (p2.moveToNext) {
                Log.e("loader", "OnLoadFinished: COlumn values " + p2.getInt(p2.getColumnIndex("_Id")) +
                    ", " + p2.getString(p2.getColumnIndex("Name")))
            }
        }
        else
            Log.wtf("loader", "OnLoadFinished: no cursor returned")

        adapter.swapCursor(p2)
    }

    def onLoaderReset(p1: Loader[Cursor]) {
        Log.v("loader", "OnLoaderReset: ")
    }
}
