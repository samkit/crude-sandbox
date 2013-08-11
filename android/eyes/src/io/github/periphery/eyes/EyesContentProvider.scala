package io.github.periphery.eyes

import android.content.{ContentValues, ContentProvider}
import android.net.Uri
import android.database.{MatrixCursor, Cursor}
import android.util.Log

/**
 * Created by samkit on 10/8/13.
 */
class EyesContentProvider extends ContentProvider {
    def onCreate(): Boolean = {
        Log.e("provider", "onCreate")
        true
    }

    def query(p1: Uri, p2: Array[String], p3: String, p4: Array[String], p5: String): Cursor = {
        Log.e("provider", "queried!!!")
        val cursor = new MatrixCursor(Array("_Id", "Name"))
        cursor.addRow(Array[Object]("1", "first"))
        cursor.addRow(Array[Object]("2", "second"))
        cursor
    }

    def getType(p1: Uri): String = {
        val ret = getContext().getContentResolver().getType(android.provider.Settings.System.CONTENT_URI)
        Log.e("provider", "getType returning: " + ret)
        ret
    }

    def insert(p1: Uri, p2: ContentValues): Uri = p1

    def delete(p1: Uri, p2: String, p3: Array[String]): Int = 0

    def update(p1: Uri, p2: ContentValues, p3: String, p4: Array[String]): Int = 0
}
