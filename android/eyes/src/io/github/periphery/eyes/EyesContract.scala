package io.github.periphery.eyes

import android.net.Uri

/**
 * Created by samkit on 10/8/13.
 */
final object EyesContract {
    val Ssp = "//io.github.periphery.eyes.provider"
//    val ContentUri = Uri.fromParts(ContentResolver.SCHEME_CONTENT, Ssp, null)
    val ContentUri = Uri.parse("content://io.github.periphery.eyes.provider")
    val MimeType = "vnd.android.cursor.dir/io.github.periphery.eyes"
    final object Projection {
        val Name = "Name"
    }
}
