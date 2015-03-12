#!/usr/bin/env python

from pprint import pprint
import urllib2
import os
import sys

vars = {

##############rls/DEPS
  "chrev": "@119173",

############ native_client/DEPS

  # These revisions are slices of the chromium repository.
  # Because they come from separate sub-slices, their hashes do not match at
  # equivalent revisions. When updating them, use the roll-dep script
  # to move them to equivalent revisions. Additionally, because not all
  # directories contain commits at each revision, you will need to select
  # revisions at latest revision up to a high watermark from each slice.
  # Document the high watermark here:
  # chrome_rev: 314402
  "valgrind_rev": "59886873b4b8258a8e0f098c23e1958e0d0c0a26", # from svn revision 231553
  "tools_valgrind_rev": "b81cde70b77b0461b18ad24616bdadb98a466647", # from svn revision 275834
  "clang_rev": "0825693c3460f23b1d78ad272999f850447ad333", # from cr commit position 313267

  # NOTE!  These five should be kept up to date with their counterparts in
  # chromium/src/DEPS.
  # Be sure to update them when updating the chromium slice revisions above.
  # (This is not essential for Breakpad, because we do not use its code
  # in the build that goes into Chromium.  But we might as well update it too.)
  # You should now use the roll-dep script in depot_tools to do this update.
  "gtest_rev": "be1868139ffe0ccd0e8e3b37292b84c821d9c8ad", # from svn revision 704
  "gyp_rev": "4d7c139b1820c5fcb993868c61f170a02cda8a40", # from svn revision 2030
  "lss_rev": "952107fa7cea0daaabead28c0e92d579bee517eb",
  "breakpad_rev": "a4eb2e302cefff9908ec955e761fef5d813d1b00", # from svn revision 1416
  "android_tools_rev": "f6e2370dff438125897bb3b3800de1ad7aa62c27",

  # Separately pinned repositories, update with roll-dep individually.
  "third_party_rev": "7e4c04567bd393069233676fc648333885e18da9", # from svn revision 13800
  "lcov_rev": "b37daf5968200da8ff520ce65c4e5bce4047dd15", # from svn revision 149720
  "gnu_binutils_rev": "f4003433b61b25666565690caf3d7a7a1a4ec436", # from svn revision 8151
  "mingw_rev": "3cc8b140b883a9fe4986d12cfd46c16a093d3527", # from svn revision 7064
  "nsis_rev": "21b6ad22daa7bfc04b9f1c1805a34622e2607a93", # from svn revision 7071
  "ragel_rev": "da42bb33f1b67c2d70b38ec1d2edf5263271b635", # from svn revision 9010
  "validator_snapshots_rev": "2d6ceadd4db38961fb3e1d45a1441319f47b2f6b",

  "chromium_git": "https://chromium.googlesource.com",

  # Three lines of non-changing comments so that
  # the commit queue can handle CLs rolling build tools
  # and whatever else without interference from each other.
  "buildtools_revision": "93b3d0af1b30db55ee42bd2e983f7753153217db",

##########################

    'eyes-free':
         'http://eyes-free.googlecode.com/svn',
    'webkit_rev':
         '@c52126b48d6307e0dd7b63cf71458ed4d18c53d8',
    'blink':
         'http://src.chromium.org/blink',
    'skia':
         'http://skia.googlecode.com/svn',
    'google-breakpad':
         'http://google-breakpad.googlecode.com/svn',
    'sawbuck':
         'http://sawbuck.googlecode.com/svn',
    'mozc':
         'http://mozc.googlecode.com/svn',
    'git.chromium.org':
         'https://chromium.googlesource.com',
    'v8-i18n':
         'http://v8-i18n.googlecode.com/svn',
    'selenium':
         'http://selenium.googlecode.com/svn',
    'buildspec_platforms':
         'all',
    'webkit_url':
         'https://chromium.googlesource.com/chromium/blink.git',
    'snappy':
         'http://snappy.googlecode.com/svn',
    'ppapi':
         'http://ppapi.googlecode.com/svn',
    'webrtc':
         'http://webrtc.googlecode.com/svn',
    'libaddressinput':
         'http://libaddressinput.googlecode.com/svn',
    'google-cache-invalidation-api':
         'http://google-cache-invalidation-api.googlecode.com/svn',
    'google-url':
         'http://google-url.googlecode.com/svn',
    'googletest':
         'http://googletest.googlecode.com/svn',
    'gyp':
         'http://gyp.googlecode.com/svn',
    'seccompsandbox':
         'http://seccompsandbox.googlecode.com/svn',
    'ots':
         'http://ots.googlecode.com/svn',
    'angleproject':
         'http://angleproject.googlecode.com/svn',
    'pefile':
         'http://pefile.googlecode.com/svn',
    'open-vcdiff':
         'http://open-vcdiff.googlecode.com/svn',
    'linux-syscall-support':
         'http://linux-syscall-support.googlecode.com/svn',
    'jsoncpp':
         'http://svn.code.sf.net/p/jsoncpp/code',
    'pywebsocket':
         'http://pywebsocket.googlecode.com/svn',
    'web-page-replay':
         'http://web-page-replay.googlecode.com/svn',
    'libjingle':
         'http://libjingle.googlecode.com/svn',
    'cld2':
         'https://cld2.googlecode.com/svn',
    'jsr-305':
         'http://jsr-305.googlecode.com/svn',
    'angle_revision':
         '6df9b37d8e3aed3aea12058900b7932f911a152a',
    'bidichecker':
         'http://bidichecker.googlecode.com/svn',
    'git_url':
         'https://chromium.googlesource.com',
    'native_client':
         'http://src.chromium.org/native_client',
    'trace-viewer':
         'http://trace-viewer.googlecode.com/svn',
    'leveldb':
         'http://leveldb.googlecode.com/svn',
    'webkit_trunk':
         'http://src.chromium.org/blink/trunk',
    'googlemock':
         'http://googlemock.googlecode.com/svn',
    'grit-i18n':
         'http://grit-i18n.googlecode.com/svn',
    'pdfsqueeze':
         'http://pdfsqueeze.googlecode.com/svn',
    'protobuf':
         'http://protobuf.googlecode.com/svn',
    'smhasher':
         'http://smhasher.googlecode.com/svn',
    'google-toolbox-for-mac':
         'http://google-toolbox-for-mac.googlecode.com/svn',
    'libyuv':
         'http://libyuv.googlecode.com/svn',
    'rlz':
         'http://rlz.googlecode.com/svn',
    'v8':
         'http://v8.googlecode.com/svn',
    'octane-benchmark':
         'http://octane-benchmark.googlecode.com/svn',
    'sfntly':
         'http://sfntly.googlecode.com/svn',
    'sctp-refimpl':
         'https://sctp-refimpl.googlecode.com/svn',
    'libphonenumber':
         'http://libphonenumber.googlecode.com/svn',
    'pymox':
         'http://pymox.googlecode.com/svn',
    'pyftpdlib':
         'http://pyftpdlib.googlecode.com/svn',
    'google-safe-browsing':
         'http://google-safe-browsing.googlecode.com/svn',
    'clang_format_rev':
         '81edd558fea5dd7855d67a1dc61db34ae8c1fd63', # r223685
    'libcxx_revision':
         '48198f9110397fff47fe7c37cbfa296be7d44d3d',
    'libcxxabi_revision':
         '4ad1009ab3a59fa7a6896d74d5e4de5885697f95',
}

def Var(key): return vars[key]

deps = {
############# v8
  "v8/build/gyp":
    Var("git_url") + "/external/gyp.git" + "@" + "4a9b712d5cb4a5ba7a9950128a7219569caf7263",
  "v8/third_party/icu":
    Var("git_url") + "/chromium/deps/icu.git" + "@" + "eda9e75b1fa17f57ffa369ee3543a2301b68d0a9",
  "v8/buildtools":
    Var("git_url") + "/chromium/buildtools.git" + "@" + "d4dd4f79f60bf019625b3a1436979b0a42c892df",
  "v8/testing/gtest":
    Var("git_url") + "/external/googletest.git" + "@" + "be1868139ffe0ccd0e8e3b37292b84c821d9c8ad",
  "v8/testing/gmock":
    Var("git_url") + "/external/googlemock.git" + "@" + "29763965ab52f24565299976b936d1265cb6a271",  # from svn revision 501
  "v8/tools/clang":
    Var("git_url") + "/chromium/src/tools/clang.git" + "@" + "ed79fd57317ab9f09ce52a5e1c7424eebb80a73e",

############### rlz/DEPS
  "base":
    "http://src.chromium.org/svn/trunk/src/base" + Var("chrev"),

  "build":
    "http://src.chromium.org/svn/trunk/src/build" + Var("chrev"),

  "third_party/icu":
    "http://src.chromium.org/svn/trunk/deps/third_party/icu42" + Var("chrev"),

  "third_party/modp_b64":
    "http://src.chromium.org/svn/trunk/src/third_party/modp_b64" + Var("chrev"),

  "third_party/nss":
    "http://src.chromium.org/svn/trunk/deps/third_party/nss" + Var("chrev"),

  "third_party/sqlite":
    "http://src.chromium.org/svn/trunk/src/third_party/sqlite" + Var("chrev"),

  "third_party/wtl":
    "http://src.chromium.org/svn/trunk/src/third_party/wtl" + Var("chrev"),

  "third_party/zlib":
    "http://src.chromium.org/svn/trunk/src/third_party/zlib" + Var("chrev"),

  "testing":
    "http://src.chromium.org/svn/trunk/src/testing" + Var("chrev"),

  "testing/gmock":
    "http://googlemock.googlecode.com/svn/trunk@374",

  "testing/gtest":
    "http://googletest.googlecode.com/svn/trunk@492",

  "tools/gyp":
    "http://gyp.googlecode.com/svn/trunk@1233",

  "tools/win":
    "http://src.chromium.org/svn/trunk/src/tools/win" + Var("chrev"),
###################### native_client/DEPS
  "breakpad":
    Var("chromium_git") + "/external/google-breakpad.git@" +
    Var("breakpad_rev"),
  "buildtools":
    Var("chromium_git") + "/chromium/buildtools.git@" +
     Var("buildtools_revision"),
  "testing/gtest":
    Var("chromium_git") + "/external/googletest.git@" + Var("gtest_rev"),
  "third_party":
    Var("chromium_git") + "/native_client/src/third_party.git@" +
    Var("third_party_rev"),
  "validator_snapshots":
    (Var("chromium_git") + "/native_client/src/validator_snapshots.git@" +
     Var("validator_snapshots_rev")),
  "third_party/lcov":
    Var("chromium_git") + "/chromium/src/third_party/lcov.git@" +
    Var("lcov_rev"),
  "third_party/lss":
    Var("chromium_git") + "/external/linux-syscall-support/lss.git@" +
    Var("lss_rev"),
  "third_party/valgrind":
    Var("chromium_git") + "/chromium/deps/valgrind.git@" + Var("valgrind_rev"),
  "tools/clang":
    Var("chromium_git") + "/chromium/src/tools/clang.git@" + Var("clang_rev"),
  "tools/gyp":
    Var("chromium_git") + "/external/gyp.git@" + Var("gyp_rev"),
  "tools/valgrind":
    Var("chromium_git") + "/chromium/src/tools/valgrind.git@" +
    Var("tools_valgrind_rev"),
########################
    '.':
        Var('git_url') + '/chromium/src@42.0.2311.40',
    'build':
        Var('git_url') + '/chromium/tools/build.git@d2efd4ddb639ee19a02c3df5c04085250e7e0b81',
    'build/scripts/command_wrapper/bin':
        Var('git_url') + '/chromium/tools/command_wrapper/bin.git@2eeebba9a512cae9e4e9312f5ec728dbdad80bd0',
    'build/scripts/gsd_generate_index':
        Var('git_url') + '/chromium/tools/gsd_generate_index.git@d2f5d5a5d212d8fb337d751c0351644a6ac83ac8',
    'build/scripts/private/data/reliability':
        Var('git_url') + '/chromium/src/chrome/test/data/reliability.git@ba644102a2f81bb33582e9474a10812fef825389',
    'build/scripts/tools/deps2git':
        Var('git_url') + '/chromium/tools/deps2git.git@27ce444f50f3c6732982d225d3f4cf67f0979a98',
    'build/third_party/lighttpd':
        Var('git_url') + '/chromium/deps/lighttpd.git@9dfa55d15937a688a92cbf2b7a8621b0927d06eb',
    'depot_tools':
        Var('git_url') + '/chromium/tools/depot_tools.git@5b23e871ba4c195e0e068efaf1bb7e96f8d8f07b',
    'breakpad/src':
        Var('git_url') + '/external/google-breakpad/src.git@d5d1eacd7394325c27d715a83976a3bb7d4d237f',
    'buildtools':
        Var('git_url') + '/chromium/buildtools.git@93b3d0af1b30db55ee42bd2e983f7753153217db',
    'chrome/test/data/perf/canvas_bench':
        Var('git_url') + '/chromium/canvas_bench.git@a7b40ea5ae0239517d78845a5fc9b12976bfc732',
    'chrome/test/data/perf/frame_rate/content':
        Var('git_url') + '/chromium/frame_rate/content.git@c10272c88463efeef6bb19c9ec07c42bc8fe22b9',
    'media/cdm/ppapi/api':
        Var('git_url') + '/chromium/cdm.git@7b7c6cc620e13c8057b4b6bff19e5955feb2c8fa',
    'native_client':
        Var('git_url') + '/native_client/src/native_client.git@123e55671ed8929b6df469473a804259e640266e',
    'sdch/open-vcdiff':
        Var('git_url') + '/external/open-vcdiff.git@438f2a5be6d809bc21611a94cd37bfc8c28ceb33',
    'testing/gmock':
        Var('git_url') + '/external/googlemock.git@29763965ab52f24565299976b936d1265cb6a271',
    'testing/gtest':
        Var('git_url') + '/external/googletest.git@be1868139ffe0ccd0e8e3b37292b84c821d9c8ad',
    'third_party/WebKit':
        Var('webkit_url') + '' + Var('webkit_rev'),
    'third_party/angle':
        Var('git_url') + '/angle/angle.git' + '@' + Var('angle_revision'),
    'third_party/bidichecker':
        Var('git_url') + '/external/bidichecker/lib.git@97f2aa645b74c28c57eca56992235c79850fa9e0',
    'third_party/boringssl/src':
        'https://boringssl.googlesource.com/boringssl.git@938e03ed17144ad1d50380e52d53d106f76dd5c8',
    'src/third_party/brotli/src':
        Var('git_url') + '/external/font-compression-reference.git@8c9c83426beb4a58da34be76ea1fccb4054c4703',
    'third_party/cacheinvalidation/src':
        Var('git_url') + '/external/google-cache-invalidation-api/src.git@c91bd9d9fed06bf440be64f87b94a2effdb32bc4',
    'third_party/cld_2/src':
        Var('git_url') + '/external/cld2.git@14d9ef8d4766326f8aa7de54402d1b9c782d4481',
    'third_party/colorama/src':
        Var('git_url') + '/external/colorama.git@799604a1041e9b3bc5d2789ecbd7e8db2e18e6b8',
    'third_party/ffmpeg':
        Var('git_url') + '/chromium/third_party/ffmpeg.git@d4b1674dcd2f742403179a3ef8e6dd8d7aaecf1a',
    'third_party/flac':
        Var('git_url') + '/chromium/deps/flac.git@0635a091379d9677f1ddde5f2eec85d0f096f219',
    'third_party/hunspell':
        Var('git_url') + '/chromium/deps/hunspell.git@c956c0e97af00ef789afb2f64d02c9a5a50e6eb1',
    'third_party/hunspell_dictionaries':
        Var('git_url') + '/chromium/deps/hunspell_dictionaries.git@94eb94ce85661b54bb3c27bedeff5428b4a2798e',
    'third_party/icu':
        Var('git_url') + '/chromium/deps/icu.git@8d46830a11d9d1ee7815dbf217c840e74afb8e7e',
    'third_party/jsoncpp/source/include':
        Var('git_url') + '/external/jsoncpp/jsoncpp/include.git@b0dd48e02b6e6248328db78a65b5c601f150c349',
    'third_party/jsoncpp/source/src/lib_json':
        Var('git_url') + '/external/jsoncpp/jsoncpp/src/lib_json.git@a8caa51ba2f80971a45880425bf2ae864a786784',
    'third_party/leveldatabase/src':
        Var('git_url') + '/external/leveldb.git@251ebf5dc70129ad3c38193fe6c99a5b0ec6b9fa',
    'third_party/libaddressinput/src':
        Var('git_url') + '/external/libaddressinput.git@61f63da7ae6fa469138d60dec5d6bbecc6ab43d6',
    'third_party/libexif/sources':
        Var('git_url') + '/chromium/deps/libexif/sources.git@ed98343daabd7b4497f97fda972e132e6877c48a',
    'third_party/libjingle/source/talk':
        Var('git_url') + '/external/webrtc/trunk/talk.git@3b87adfbf3c061bb1c475a31f5967c3e12a7411c',
    'third_party/libjpeg_turbo':
        Var('git_url') + '/chromium/deps/libjpeg_turbo.git@034e9a9747e0983bc19808ea70e469bc8342081f',
    'third_party/libphonenumber/src/phonenumbers':
        Var('git_url') + '/external/libphonenumber/cpp/src/phonenumbers.git@0d6e3e50e17c94262ad1ca3b7d52b11223084bca',
    'third_party/libphonenumber/src/resources':
        Var('git_url') + '/external/libphonenumber/resources.git@b6dfdc7952571ff7ee72643cd88c988cbe966396',
    'third_party/libphonenumber/src/test':
        Var('git_url') + '/external/libphonenumber/cpp/test.git@f351a7e007f9c9995494499120bbc361ca808a16',
    'third_party/libsrtp':
        Var('git_url') + '/chromium/deps/libsrtp.git@6446144c7f083552f21cc4e6768e891bcb767574',
    'third_party/libvpx':
        Var('git_url') + '/chromium/deps/libvpx.git@33bbffe8b3fa6d240ab7720f4f46854bd98d7198',
    'third_party/libyuv':
        Var('git_url') + '/external/libyuv.git@d204db647e591ccf0e2589236ecea90330d65a66',
    'third_party/mesa/src':
        Var('git_url') + '/chromium/deps/mesa.git@071d25db04c23821a12a8b260ab9d96a097402f0',
    'third_party/openmax_dl':
        Var('git_url') + '/external/webrtc/deps/third_party/openmax.git@21c8abe416eb1cdf6f759cdce72e715e7f262282',
    'third_party/opus/src':
        Var('git_url') + '/chromium/deps/opus.git@cae696156f1e60006e39821e79a1811ae1933c69',
    'third_party/pdfium':
        'https://pdfium.googlesource.com/pdfium.git@58985096a7852263df68e87d9bfc335a3e2759bf',
    'third_party/py_trace_event/src':
        Var('git_url') + '/external/py_trace_event.git@dd463ea9e2c430de2b9e53dea57a77b4c3ac9b30',
    'third_party/pyftpdlib/src':
        Var('git_url') + '/external/pyftpdlib.git@2be6d65e31c7ee6320d059f581f05ae8d89d7e45',
    'third_party/pywebsocket/src':
        Var('git_url') + '/external/pywebsocket/src.git@cb349e87ddb30ff8d1fa1a89be39cec901f4a29c',
    'third_party/safe_browsing/testing':
        Var('git_url') + '/external/google-safe-browsing/testing.git@9d7e8064f3ca2e45891470c9b5b1dce54af6a9d6',
    'third_party/scons-2.0.1':
        Var('git_url') + '/native_client/src/third_party/scons-2.0.1.git@1c1550e17fc26355d08627fbdec13d8291227067',
    'third_party/sfntly/cpp/src':
        Var('git_url') + '/external/sfntly/cpp/src.git@1bdaae8fc788a5ac8936d68bf24f37d977a13dac',
    'third_party/skia':
        Var('git_url') + '/skia.git@5eb968c2f2b25f2e6701d70e29829a83587c76ed',
    'third_party/smhasher/src':
        Var('git_url') + '/external/smhasher.git@e87738e57558e0ec472b2fc3a643b838e5b6e88f',
    'third_party/snappy/src':
        Var('git_url') + '/external/snappy.git@762bb32f0c9d2f31ba4958c7c0933d22e80c20bf',
    'third_party/swig/Lib':
        Var('git_url') + '/chromium/deps/swig/Lib.git@f2a695d52e61e6a8d967731434f165ed400f0d69',
    'third_party/trace-viewer':
        Var('git_url') + '/external/trace-viewer.git@a9802a1384185f9c7ee250ce67d3d24d07b11141',
    'third_party/usrsctp/usrsctplib':
        Var('git_url') + '/external/usrsctplib.git@13718c7b9fd376fde092cbd3c5347d15059ac652',
    'third_party/webdriver/pylib':
        Var('git_url') + '/external/selenium/py.git@5fd78261a75fe08d27ca4835fb6c5ce4b42275bd',
    'third_party/webgl/src':
        Var('git_url') + '/external/khronosgroup/webgl.git@0c2bcf36a740181f50ce94a0eaad357219441dee',
    'third_party/webpagereplay':
        Var('git_url') + '/external/web-page-replay.git@532b413ff95e8595d5028e0dae75dcf3ba712d2e',
    'third_party/webrtc':
        Var('git_url') + '/external/webrtc/trunk/webrtc.git@96bdc6ffffbbea98925ebbd0e618934e0df35f59',
    'third_party/yasm/source/patched-yasm':
        Var('git_url') + '/chromium/deps/yasm/patched-yasm.git@4671120cd8558ce62ee8672ebf3eb6f5216f909b',
    'tools/deps2git':
        Var('git_url') + '/chromium/tools/deps2git.git@f04828eb0b5acd3e7ad983c024870f17f17b06d9',
    'tools/grit':
        Var('git_url') + '/external/grit-i18n.git@a5890a8118c0c80cc0560e6d8d5cf65e5d725509',
    'tools/gyp':
        Var('git_url') + '/external/gyp.git@34640080d08ab2a37665512e52142947def3056d',
    'tools/page_cycler/acid3':
        Var('git_url') + '/chromium/deps/acid3.git@6be0a66a1ebd7ebc5abc1b2f405a945f6d871521',
    'tools/swarming_client':
        Var('git_url') + '/external/swarming.client.git@1b7bfeca33abce319356fd1835a5cd2f74f1916a',
    'v8':
        Var('git_url') + '/v8/v8.git@555f5bc9de11e8f40ede03cb393899189450506f',
    'clang_format/script':
        Var('git_url') + '/chromium/llvm-project/cfe/tools/clang-format.git@' +
        Var('clang_format_rev'),
    'third_party/libc++/trunk':
        Var('git_url') + '/chromium/llvm-project/libcxx.git' + '@' +
        Var('libcxx_revision'),
    'third_party/libc++abi/trunk':
        Var('git_url') + '/chromium/llvm-project/libcxxabi.git' + '@' +
        Var('libcxxabi_revision'),

}

deps_os = {
    'android':
    {
############## native_client/DEPS
#   "third_party/android_tools":
#     Var("chromium_git") + "/android_tools.git@" + Var("android_tools_rev"),
################
        'pdf':
            None,
        'third_party/android_protobuf/src':
            Var('git_url') + '/external/android_protobuf.git@94f522f907e3f34f70d9e7816b947e62fddbb267',
#       'third_party/android_tools':
#           Var('git_url') + '/android_tools.git@fd5a8ec0c75d487635f7e6bd3bdc90eb23eba941',
        'third_party/apache-mime4j':
            Var('git_url') + '/chromium/deps/apache-mime4j.git@28cb1108bff4b6cf0a2e86ff58b3d025934ebe3a',
        'third_party/appurify-python/src':
            Var('git_url') + '/external/github.com/appurify/appurify-python.git@ee7abd5c5ae3106f72b2a0b9d2cb55094688e867',
        'third_party/elfutils/src':
            Var('git_url') + '/external/elfutils.git@249673729a7e5dbd5de4f3760bdcaa3d23d154d7',
        'third_party/findbugs':
            Var('git_url') + '/chromium/deps/findbugs.git@7f69fa78a6db6dc31866d09572a0e356e921bf12',
        'third_party/freetype':
            Var('git_url') + '/chromium/src/third_party/freetype.git@fd6919ac23f74b876c209aba5eaa2be662086391',
        'third_party/httpcomponents-client':
            Var('git_url') + '/chromium/deps/httpcomponents-client.git@285c4dafc5de0e853fa845dce5773e223219601c',
        'third_party/httpcomponents-core':
            Var('git_url') + '/chromium/deps/httpcomponents-core.git@9f7180a96f8fa5cab23f793c14b413356d419e62',
        'third_party/jarjar':
            Var('git_url') + '/chromium/deps/jarjar.git@2e1ead4c68c450e0b77fe49e3f9137842b8b6920',
        'third_party/jsr-305/src':
            Var('git_url') + '/external/jsr-305.git@642c508235471f7220af6d5df2d3210e3bfc0919',
        'third_party/junit/src':
            Var('git_url') + '/external/junit.git@45a44647e7306262162e1346b750c3209019f2e1',
        'third_party/lss':
            Var('git_url') + '/external/linux-syscall-support/lss.git@952107fa7cea0daaabead28c0e92d579bee517eb',
        'third_party/mockito/src':
            Var('git_url') + '/external/mockito/mockito.git@ed99a52e94a84bd7c467f2443b475a22fcc6ba8e',
        'third_party/requests/src':
            Var('git_url') + '/external/github.com/kennethreitz/requests.git@f172b30356d821d180fa4ecfa3e71c7274a32de4',
        'third_party/robolectric/lib':
            Var('git_url') + '/chromium/third_party/robolectric.git@6b63c99a8b6967acdb42cbed0adb067c80efc810',
    },
    'ios':
    {
        'src/chrome/test/data/perf/canvas_bench':
            None,
        'src/chrome/test/data/perf/frame_rate/content':
            None,
        'src/native_client':
            None,
        'src/testing/iossim/third_party/class-dump':
            Var('git_url') + '/chromium/deps/class-dump.git@89bd40883c767584240b4dade8b74e6f57b9bdab',
        'src/third_party/ffmpeg':
            None,
        'src/third_party/gcdwebserver/src':
            Var('git_url') + '/external/github.com/swisspol/GCDWebServer.git@18889793b75d7ee593d62ac88997caad850acdb6',
        'src/third_party/google_toolbox_for_mac/src':
            Var('git_url') + '/external/google-toolbox-for-mac.git@17eee6933bb4a978bf045ef1b12fc68f15b08cd2',
        'src/third_party/hunspell':
            None,
        'src/third_party/hunspell_dictionaries':
            None,
        'src/third_party/nss':
            Var('git_url') + '/chromium/deps/nss.git@bb4e75a43d007518ae7d618665ea2f25b0c60b63',
        'src/third_party/webgl':
            None,
    },
    'mac':
    {
        'src/chrome/installer/mac/third_party/xz/xz':
            Var('git_url') + '/chromium/deps/xz.git@eecaf55632ca72e90eb2641376bce7cdbc7284f7',
        'src/chrome/tools/test/reference_build/chrome_mac':
            Var('git_url') + '/chromium/reference_builds/chrome_mac.git@8dc181329e7c5255f83b4b85dc2f71498a237955',
        'src/third_party/google_toolbox_for_mac/src':
            Var('git_url') + '/external/google-toolbox-for-mac.git@17eee6933bb4a978bf045ef1b12fc68f15b08cd2',
        'src/third_party/lighttpd':
            Var('git_url') + '/chromium/deps/lighttpd.git@9dfa55d15937a688a92cbf2b7a8621b0927d06eb',
        'src/third_party/nss':
            Var('git_url') + '/chromium/deps/nss.git@bb4e75a43d007518ae7d618665ea2f25b0c60b63',
        'src/third_party/pdfsqueeze':
            Var('git_url') + '/external/pdfsqueeze.git@5936b871e6a087b7e50d4cbcb122378d8a07499f',
        'src/third_party/swig/mac':
            Var('git_url') + '/chromium/deps/swig/mac.git@1b182eef16df2b506f1d710b34df65d55c1ac44e',
    },
    'unix':
    {
        'build/third_party/cbuildbot_chromite':
            Var('git_url') + '/chromiumos/chromite.git@881f183fad9526c98e9bf948d7f3179029723462',
        'build/third_party/xvfb':
            Var('git_url') + '/chromium/tools/third_party/xvfb.git@aebb1aadf1422e4d81e831e13746b8f7ae322e07',
        'src/chrome/tools/test/reference_build/chrome_linux':
            Var('git_url') + '/chromium/reference_builds/chrome_linux64.git@033d053a528e820e1de3e2db766678d862a86b36',
        'src/third_party/chromite':
            Var('git_url') + '/chromiumos/chromite.git@fdc9440cb96f8de35202abc285ffb896e04292d3',
        'src/third_party/cros_system_api':
            Var('git_url') + '/chromiumos/platform/system_api.git@e22c1effdfaace2f904536f8a9953644ba90398c',
        'src/third_party/fontconfig/src':
            Var('git_url') + '/external/fontconfig.git@f16c3118e25546c1b749f9823c51827a60aeb5c1',
        'src/third_party/freetype2/src':
            Var('git_url') + '/chromium/src/third_party/freetype2.git@495a23fce9cd125f715dc20643d14fed226d76ac',
        'src/third_party/liblouis/src':
            Var('git_url') + '/external/liblouis-github.git@5f9c03f2a3478561deb6ae4798175094be8a26c2',
        'src/third_party/lss':
            Var('git_url') + '/external/linux-syscall-support/lss.git@952107fa7cea0daaabead28c0e92d579bee517eb',
        'src/third_party/pyelftools':
            Var('git_url') + '/chromiumos/third_party/pyelftools.git@19b3e610c86fcadb837d252c794cb5e8008826ae',
        'src/third_party/stp/src':
            Var('git_url') + '/external/github.com/stp/stp.git@fc94a599207752ab4d64048204f0c88494811b62',
        'src/third_party/swig/linux':
            Var('git_url') + '/chromium/deps/swig/linux.git@866b8e0e0e0cfe99ebe608260030916ca0c3f92d',
        'src/third_party/undoview':
            Var('git_url') + '/chromium/deps/undoview.git@3ba503e248f3cdbd81b78325a24ece0984637559',
        'src/third_party/xdg-utils':
            Var('git_url') + '/chromium/deps/xdg-utils.git@d80274d5869b17b8c9067a1022e4416ee7ed5e0d',
    },
    'win':
    {
        'src/chrome/tools/test/reference_build/chrome_win':
            Var('git_url') + '/chromium/reference_builds/chrome_win.git@f8a3a845dfc845df6b14280f04f86a61959357ef',
        'src/third_party/bison':
            Var('git_url') + '/chromium/deps/bison.git@083c9a45e4affdd5464ee2b224c2df649c6e26c3',
        'src/third_party/cygwin':
            Var('git_url') + '/chromium/deps/cygwin.git@c89e446b273697fadf3a10ff1007a97c0b7de6df',
        'src/third_party/gnu_binutils':
            Var('git_url') + '/native_client/deps/third_party/gnu_binutils.git@f4003433b61b25666565690caf3d7a7a1a4ec436',
        'src/third_party/gperf':
            Var('git_url') + '/chromium/deps/gperf.git@d892d79f64f9449770443fb06da49b5a1e5d33c1',
        'src/third_party/lighttpd':
            Var('git_url') + '/chromium/deps/lighttpd.git@9dfa55d15937a688a92cbf2b7a8621b0927d06eb',
        'src/third_party/mingw-w64/mingw/bin':
            Var('git_url') + '/native_client/deps/third_party/mingw-w64/mingw/bin.git@3cc8b140b883a9fe4986d12cfd46c16a093d3527',
        'src/third_party/nacl_sdk_binaries':
            Var('git_url') + '/chromium/deps/nacl_sdk_binaries.git@759dfca03bdc774da7ecbf974f6e2b84f43699a5',
        'src/third_party/nss':
            Var('git_url') + '/chromium/deps/nss.git@bb4e75a43d007518ae7d618665ea2f25b0c60b63',
        'src/third_party/omaha/src/omaha':
            Var('git_url') + '/external/omaha.git@098c7a3d157218dab4eed595e8f2fbe5a20a0bae',
        'src/third_party/pefile':
            Var('git_url') + '/external/pefile.git@72c6ae42396cb913bcab63c15585dc3b5c3f92f1',
        'src/third_party/perl':
            Var('git_url') + '/chromium/deps/perl.git@ac0d98b5cee6c024b0cffeb4f8f45b6fc5ccdb78',
        'src/third_party/psyco_win32':
            Var('git_url') + '/chromium/deps/psyco_win32.git@f5af9f6910ee5a8075bbaeed0591469f1661d868',
        'src/third_party/swig/win':
            Var('git_url') + '/chromium/deps/swig/win.git@986f013ba518541adf5c839811efb35630a31031',
        'src/third_party/yasm/binaries':
            Var('git_url') + '/chromium/deps/yasm/binaries.git@52f9b3f4b0aa06da24ef8b123058bb61ee468881',
    },
}

include_rules = [
    '+base',
    '+build',
    '+ipc',
    '+library_loaders',
    '+testing',
    '+third_party/icu/source/common/unicode',
    '+third_party/icu/source/i18n/unicode',
    '+url'
]

skip_child_includes = [
    'breakpad',
    'delegate_execute',
    'metro_driver',
    'native_client_sdk',
    'o3d',
    'sdch',
    'skia',
    'testing',
    'third_party',
    'v8',
    'win8'
]

hooks = [
    {
    'action':
         [
    'python',
    'src/build/landmines.py'
],
    'pattern':
         '.',
    'name':
         'landmines'
},
    {
    'action':
         [
    'python',
    'src/build/download_nacl_toolchains.py',
    '--mode',
    'nacl_core_sdk',
    'sync',
    '--extract'
],
    'pattern':
         '.',
    'name':
         'nacltools'
},
    {
    'action':
         [
    'python',
    'src/build/download_sdk_extras.py'
],
    'pattern':
         '.',
    'name':
         'sdkextras'
},
    {
    'action':
         [
    'python',
    'src/chrome/installer/linux/sysroot_scripts/install-debian.wheezy.sysroot.py',
    '--linux-only'
],
    'pattern':
         '.',
    'name':
         'sysroot'
},
    {
    'action':
         [
    'python',
    'src/build/vs_toolchain.py',
    'update'
],
    'pattern':
         '.',
    'name':
         'win_toolchain'
},
    {
    'action':
         [
    'python',
    'src/tools/clang/scripts/update.py',
    '--if-needed'
],
    'pattern':
         '.',
    'name':
         'clang'
},
    {
    'action':
         [
    'python',
    'src/build/util/lastchange.py',
    '-o',
    'src/build/util/LASTCHANGE'
],
    'pattern':
         '.',
    'name':
         'lastchange'
},
    {
    'action':
         [
    'python',
    'src/build/util/lastchange.py',
    '-s',
    'src/third_party/WebKit',
    '-o',
    'src/build/util/LASTCHANGE.blink'
],
    'pattern':
         '.',
    'name':
         'lastchange'
},
    {
    'action':
         [
    'download_from_google_storage',
    '--no_resume',
    '--platform=win32',
    '--no_auth',
    '--bucket',
    'chromium-gn',
    '-s',
    'src/buildtools/win/gn.exe.sha1'
],
    'pattern':
         '.',
    'name':
         'gn_win'
},
    {
    'action':
         [
    'download_from_google_storage',
    '--no_resume',
    '--platform=darwin',
    '--no_auth',
    '--bucket',
    'chromium-gn',
    '-s',
    'src/buildtools/mac/gn.sha1'
],
    'pattern':
         '.',
    'name':
         'gn_mac'
},
    {
    'action':
         [
    'download_from_google_storage',
    '--no_resume',
    '--platform=linux*',
    '--no_auth',
    '--bucket',
    'chromium-gn',
    '-s',
    'src/buildtools/linux32/gn.sha1'
],
    'pattern':
         '.',
    'name':
         'gn_linux32'
},
    {
    'action':
         [
    'download_from_google_storage',
    '--no_resume',
    '--platform=linux*',
    '--no_auth',
    '--bucket',
    'chromium-gn',
    '-s',
    'src/buildtools/linux64/gn.sha1'
],
    'pattern':
         '.',
    'name':
         'gn_linux64'
},
    {
    'action':
         [
    'download_from_google_storage',
    '--no_resume',
    '--platform=win32',
    '--no_auth',
    '--bucket',
    'chromium-clang-format',
    '-s',
    'src/buildtools/win/clang-format.exe.sha1'
],
    'pattern':
         '.',
    'name':
         'clang_format_win'
},
    {
    'action':
         [
    'download_from_google_storage',
    '--no_resume',
    '--platform=darwin',
    '--no_auth',
    '--bucket',
    'chromium-clang-format',
    '-s',
    'src/buildtools/mac/clang-format.sha1'
],
    'pattern':
         '.',
    'name':
         'clang_format_mac'
},
    {
    'action':
         [
    'download_from_google_storage',
    '--no_resume',
    '--platform=linux*',
    '--no_auth',
    '--bucket',
    'chromium-clang-format',
    '-s',
    'src/buildtools/linux64/clang-format.sha1'
],
    'pattern':
         '.',
    'name':
         'clang_format_linux'
},
    {
    'action':
         [
    'python',
    'src/third_party/binutils/download.py'
],
    'pattern':
         'src/third_party/binutils',
    'name':
         'binutils'
},
    {
    'action':
         [
    'download_from_google_storage',
    '--no_resume',
    '--platform=linux*',
    '--no_auth',
    '--bucket',
    'chromium-eu-strip',
    '-s',
    'src/build/linux/bin/eu-strip.sha1'
],
    'pattern':
         '.',
    'name':
         'eu-strip'
},
    {
    'action':
         [
    'download_from_google_storage',
    '--no_resume',
    '--platform=win32',
    '--no_auth',
    '--bucket',
    'chromium-drmemory',
    '-s',
    'src/third_party/drmemory/drmemory-windows-sfx.exe.sha1'
],
    'pattern':
         '.',
    'name':
         'drmemory'
},
    {
    'action':
         [
    'python',
    'src/build/get_syzygy_binaries.py',
    '--output-dir=src/third_party/syzygy/binaries',
    '--revision=79621b5523205997ae9f689efb7f299973c87a8c',
    '--overwrite'
],
    'pattern':
         '.',
    'name':
         'syzygy-binaries'
},
    {
    'action':
         [
    'python',
    'src/build/get_syzygy_binaries.py',
    '--output-dir=src/third_party/kasko',
    '--revision=33788dfa4e351db209915389a97eed31499c3206',
    '--resource=kasko.zip',
    '--resource=kasko_symbols.zip',
    '--overwrite'
],
    'pattern':
         '.',
    'name':
         'kasko'
},
    {
    'action':
         [
    'download_from_google_storage',
    '--no_resume',
    '--platform=win32',
    '--directory',
    '--recursive',
    '--no_auth',
    '--num_threads=16',
    '--bucket',
    'chromium-apache-win32',
    'src/third_party/apache-win32'
],
    'pattern':
         '\\.sha1',
    'name':
         'apache_win32'
},
    {
    'action':
         [
    'python',
    'src/third_party/mojo/src/mojo/public/tools/download_shell_binary.py',
    '--tools-directory=../../../../../../tools'
],
    'pattern':
         '',
    'name':
         'download_mojo_shell'
},
    {
    'action':
         [
    'python',
    'src/build/gyp_chromium'
],
    'pattern':
         '.',
    'name':
         'gyp'
},
    {
    'action':
         [
    'python',
    'src/tools/check_git_config.py',
    '--running-as-hook'
],
    'pattern':
         '.',
    'name':
         'check_git_config'
},
    {
    'action':
         [
    'python',
    'src/tools/remove_stale_pyc_files.py',
    'src/tools'
],
    'pattern':
         'src/tools/.*\\.py',
    'name':
         'remove_stale_pyc_files'
}
]

deps.update(deps_os['android'])

root_dir = os.getcwd()
for (directory, dependancy) in deps.iteritems():
    os.chdir(root_dir)
    try:
        os.makedirs(directory)
    except OSError:
        pass

    os.chdir(directory)
    if dependancy is None: continue
    if '@' in dependancy and (
         dependancy.startswith('https://chromium.googlesource.com/') or
         dependancy.startswith('http://src.chromium.org/') or
         dependancy.startswith('https://pdfium.googlesource.com/') or
         dependancy.startswith('https://boringssl.googlesource.com/')):

        source, filename = dependancy.rsplit('@')
        url = '%s/+archive/%s.tar.gz' % (source, filename)

        print 'Downloading: %s -> %s -> %s' % (directory, url, filename + '.tar.gz')
        if False:
            try:
                url_stream = urllib2.urlopen(urllib2.Request(url,
                    headers = {
                        "User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
                        "Accept-Encoding": "gzip"
                    }))
                output_file = file(filename + '.targz', 'wb')

                data = url_stream.read(1024 * 100)
                while data:
                    output_file.write(data)

                output_file.close()
                url_stream.close()

                sys.exit(0)

            except Exception, error:
                print 'Error downloading: %s -> %s\nError: %s' % (directory, url, str(error))

    else:
        raise RuntimeError('Source URL [%s] is not supported' % (dependancy))
