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
        cursor.addRow(Array[Object]("1", "one"))
        cursor.addRow(Array[Object]("2", "two"))
        cursor.addRow(Array[Object]("3", "three"))
        cursor.addRow(Array[Object]("4", "four"))
        cursor.addRow(Array[Object]("5", "five"))
        cursor.addRow(Array[Object]("6", "six"))
        cursor.addRow(Array[Object]("7", "seven"))
        cursor.addRow(Array[Object]("8", "eight"))
        cursor.addRow(Array[Object]("9", "nine"))
        cursor.addRow(Array[Object]("10", "ten"))
        cursor
    }

    def getType(p1: Uri): String = EyesContract.MimeType

    def insert(p1: Uri, p2: ContentValues): Uri = p1

    def delete(p1: Uri, p2: String, p3: Array[String]): Int = 0

    def update(p1: Uri, p2: ContentValues, p3: String, p4: Array[String]): Int = 0
}
