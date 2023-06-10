mkdir -p $(rpm --eval %_topdir)/SPECS
mkdir -p $(rpm --eval %_topdir)/SOURCES
wget https://ftp.gnu.org/gnu/gmp/gmp-6.2.1.tar.xz -O $(rpm --eval %_topdir)/SOURCES/gmp-6.2.1.tar.xz
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-gmp/gmp.h -O $(rpm --eval %_topdir)/SOURCES/gmp.h
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-gmp/gmp-mparam.h -O $(rpm --eval %_topdir)/SOURCES/gmp-mparam.h
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-gmp/gmp-6.0.0-debuginfo.patch -O $(rpm --eval %_topdir)/SOURCES/gmp-6.0.0-debuginfo.patch
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-gmp/gmp-intel-cet.patch -O $(rpm --eval %_topdir)/SOURCES/gmp-intel-cet.patch
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-gmp/xtreamui-gmp.spec -O $(rpm --eval %_topdir)/SPECS/xtreamui-gmp.spec
rpmbuild -ba $(rpm --eval %_topdir)/SPECS/xtreamui-gmp.spec
dnf -y install $(find $(rpm --eval %_topdir)/RPMS -name 'xtreamui-gmp-6.2.1-4.*.rpm')
wget https://www.zlib.net/zlib-1.2.13.tar.xz -O $(rpm --eval %_topdir)/SOURCES/zlib-1.2.13.tar.xz
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-zlib/zlib-1.2.5-minizip-fixuncrypt.patch -O $(rpm --eval %_topdir)/SOURCES/zlib-1.2.5-minizip-fixuncrypt.patch
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-zlib/zlib-1.2.13-optimized-s390.patch -O $(rpm --eval %_topdir)/SOURCES/zlib-1.2.13-optimized-s390.patch
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-zlib/zlib-1.2.13-Fix-bug-in-deflateBound.patch -O $(rpm --eval %_topdir)/SOURCES/zlib-1.2.13-Fix-bug-in-deflateBound.patch
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-zlib/zlib-1.2.13-power-optimizations.patch -O $(rpm --eval %_topdir)/SOURCES/zlib-1.2.13-power-optimizations.patch
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-zlib/zlib-1.2.13-IBM-Z-hw-accelerated-deflate.patch -O $(rpm --eval %_topdir)/SOURCES/zlib-1.2.13-IBM-Z-hw-accelerated-deflate.patch
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-zlib/zlib-1.2.13-s390x-vectorize-crc32.patch -O $(rpm --eval %_topdir)/SOURCES/zlib-1.2.13-s390x-vectorize-crc32.patch
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-zlib/zlib-1.2.11-covscan-issues.patch -O $(rpm --eval %_topdir)/SOURCES/zlib-1.2.11-covscan-issues.patch
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-zlib/zlib-1.2.11-covscan-issues-rhel9.patch -O $(rpm --eval %_topdir)/SOURCES/zlib-1.2.11-covscan-issues-rhel9.patch
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-zlib/xtreamui-zlib.spec -O $(rpm --eval %_topdir)/SPECS/xtreamui-zlib.spec
rpmbuild -ba $(rpm --eval %_topdir)/SPECS/xtreamui-zlib.spec
dnf -y install $(find $(rpm --eval %_topdir)/RPMS -name 'xtreamui-zlib-1.2.13-3.*.rpm')

















wget https://github.com/silnrsi/teckit/releases/download/v2.5.11/teckit-2.5.11.tar.gz -O $(rpm --eval %_topdir)/SOURCES/teckit-2.5.11.tar.gz
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-gettext/xtreamui-teckit.spec -O $(rpm --eval %_topdir)/SPECS/xtreamui-teckit.spec













wget https://ftp.gnu.org/pub/gnu/gettext/gettext-0.21.1.tar.gz -O $(rpm --eval %_topdir)/SOURCES/gettext-0.21.1.tar.gz
wget https://ftp.gnu.org/pub/gnu/gettext/msghack.py -O $(rpm --eval %_topdir)/SOURCES/msghack.py
wget https://ftp.gnu.org/pub/gnu/gettext/msghack.1 -O $(rpm --eval %_topdir)/SOURCES/msghack.1
wget https://ftp.gnu.org/pub/gnu/gettext/gettext-0.21.1-disable-libtextstyle.patch -O $(rpm --eval %_topdir)/SOURCES/gettext-0.21.1-disable-libtextstyle.patch
wget https://ftp.gnu.org/pub/gnu/gettext/gettext-0.21.1-covscan.patch -O $(rpm --eval %_topdir)/SOURCES/gettext-0.21.1-covscan.patch
wget https://ftp.gnu.org/pub/gnu/gettext/gettext-java17-2062407.patch -O $(rpm --eval %_topdir)/SOURCES/gettext-java17-2062407.patch
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-gettext/xtreamui-gettext.spec -O $(rpm --eval %_topdir)/SPECS/xtreamui-gettext.spec










