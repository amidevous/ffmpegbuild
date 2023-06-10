#!/bin/bash
echo -e "\nChecking that minimal requirements are ok"
# Ensure the OS is compatible with the launcher
if [ -f /etc/centos-release ]; then
    inst() {
       rpm -q --queryformat '%{Version}-%{Release}' "$1"
    } 
    if (inst "centos-stream-repos"); then
    OS="CentOS-Stream"
    else
    OS="CentOs"
    fi    
    VERFULL=$(sed 's/^.*release //;s/ (Fin.*$//' /etc/centos-release) VER=${VERFULL:0:1} # return 6, 7, 8, 9 etc
elif [ -f /etc/fedora-release ]; then
    inst() {
       rpm -q --queryformat '%{Version}-%{Release}' "$1"
    } 
    OS="Fedora" VERFULL=$(sed 's/^.*release //;s/ (Fin.*$//' /etc/fedora-release) VER=${VERFULL:0:2} # return 34, 35, 36,37 etc
elif [ -f /etc/lsb-release ]; then
    OS=$(grep DISTRIB_ID /etc/lsb-release | sed 's/^.*=//') VER=$(grep DISTRIB_RELEASE /etc/lsb-release | sed 's/^.*=//')
	inst() {
       dpkg-query --showformat='${Version}' --show "$1"
    }
elif [ -f /etc/os-release ]; then
    OS=$(grep -w ID /etc/os-release | sed 's/^.*=//') VER=$(grep VERSION_ID /etc/os-release | sed 's/^.*"\(.*\)"/\1/' | head -n 1 | tail -n 1)
 else
    OS=$(uname -s) VER=$(uname -r)
fi
ARCH=$(uname -m)
echo "Detected : $OS  $VER  $ARCH"
# this part must be updated every 6 months
if [[ "$OS" = "CentOs" && "$VER" = "7" && "$ARCH" == "x86_64" || "$OS" = "CentOS-Stream" && "$VER" = "8" && "$ARCH" == "x86_64" ||
"$OS" = "CentOS-Stream" && "$VER" = "9" && "$ARCH" == "x86_64" || "$OS" = "Fedora" && "$VER" = "37" && "$ARCH" == "x86_64" ||
 "$OS" = "Fedora" && "$VER" = "38" && "$ARCH" == "x86_64"  ]] ; then
    echo "Ok."
else
    echo "Sorry, this OS is not supported."
	echo "This script is online for Linux x86_64 Stable Version"
	echo "Only aviable for :"
	echo "Centos Version 7"
	echo "CentOS Stream Version 8"
	echo "CentOS Stream Version 9"
	echo "Fedora Version 37"
	echo "Fedora Version 38"
    exit 1
fi
# define Package Variable
if [[ "$OS" = "CentOs" ]] ; then
		yum -y install epel-release
		yum -y update
		yum -y install dnf
    dnf -y install centos-release-scl
    dnf -y install devtoolset-8
fi
dnf -y install rpm-build make git gcc gcc-c++ gcc-gfortran gcc-objc gcc-objc++ libstdc++-devel cmake3 \
autoconf automake libtool wget bzip2-devel gzip xz-devel wget tar make pkgconfig patch m4 coreutils
rm -rf $(rpm --eval %_topdir)/SPECS $(rpm --eval %_topdir)/SOURCES
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
dnf -y install unzip $(find $(rpm --eval %_topdir)/RPMS -name 'xtreamui-zlib-1.2.13-3.*.rpm')






xtreamui-libxml2.spec





xtreamui-docbook-dtd.spec








xtreamui-docbook-style-xsl.spec





xtreamui-xmlto.spec










wget "https://github.com/libexpat/libexpat/archive/R_2_5_0.tar.gz#/expat-2.5.0.tar.gz" -O $(rpm --eval %_topdir)/SOURCES/expat-2.5.0.tar.gz
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-expat/xtreamui-expat.spec -O $(rpm --eval %_topdir)/SPECS/xtreamui-expat.spec
rpmbuild -ba $(rpm --eval %_topdir)/SPECS/xtreamui-expat.spec
dnf -y install $(find $(rpm --eval %_topdir)/RPMS -name 'xtreamui-zlib-1.2.13-3.*.rpm')









wget "https://github.com/libexpat/libexpat/archive/R_2_5_0.tar.gz#/expat-2.5.0.tar.gz" -O $(rpm --eval %_topdir)/SOURCES/expat-2.5.0.tar.gz
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-expat/xtreamui-expat.spec -O $(rpm --eval %_topdir)/SPECS/xtreamui-expat.spec
rpmbuild -ba $(rpm --eval %_topdir)/SPECS/xtreamui-expat.spec
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










