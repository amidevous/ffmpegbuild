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
#PACKAGE_INSTALLER="yum -y install" PACKAGE_INSTALLER_LOCAL="yum -y --enablerepo ffmpeg-local install" PACKAGE_BININSTALLER="rpm -i"
#	PACKAGE_REMOVER="yum -y remove" PACKAGE_UPDATER="yum -y update" PACKAGE_UPDGRADER="yum -y  upgrade" PACKAGE_UTILS="yum-utils"
#    PACKAGE_GROUPINSTALL="yum -y groupinstall" PACKAGE_SOURCEDOWNLOAD="yumdownloader --source"
#    PACKAGE_BUILDDEP="yum-builddep -y"
#elif [[ "$OS" = "Fedora" || "$OS" = "CentOS-Stream"  ]]; then
#    PACKAGE_INSTALLER="dnf -y install" PACKAGE_INSTALLER_LOCAL="dnf -y --enablerepo ffmpeg-local install"
#	PACKAGE_BININSTALLER="rpm -i" PACKAGE_REMOVER="dnf -y remove"
#    PACKAGE_UPDATER="dnf -y update" PACKAGE_UPDGRADER="dnf -y upgrade" PACKAGE_UTILS="dnf-utils"
#    PACKAGE_GROUPINSTALL="dnf -y groupinstall"PACKAGE_SOURCEDOWNLOAD="dnf download --source"
#    PACKAGE_BUILDDEP="dnf build-dep -y"
fi
dnf -y install rpm-build gcc gcc-c++ gcc-gfortran gcc-objc gcc-objc++ libstdc++-devel gcc-gnat wget bzip2 gzip xz wget tar make pkgconfig patch m4
mkdir -p $rpm --eval %_topdir)/SPECS
mkdir -p $(rpm --eval %_topdir)/SOURCES
wget https://ftp.gnu.org/gnu/gmp/gmp-6.2.1.tar.xz -O $(rpm --eval %_topdir)/SOURCES/gmp-6.2.1.tar.xz
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtream-ui-gmp.spec -O $(rpm --eval %_topdir)/SPECS/xtream-ui-gmp.spec
rpmbuild -ba $(rpm --eval %_topdir)/SPECS/xtream-ui-gmp.spec
dnf -y install $(find $(rpm --eval %_topdir) -name 'xtream-ui-gmp-6.2.1-1.el7.x86_64.rpm')
wget https://ftp.gnu.org/gnu/nettle/nettle-3.9.1.tar.gz -O $(rpm --eval %_topdir)/SOURCES/nettle-3.9.1.tar.gz
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtream-ui-nettle.spec -O $(rpm --eval %_topdir)/SPECS/xtream-ui-nettle.spec
rpmbuild -ba $(rpm --eval %_topdir)/SPECS/xtream-ui-nettle.spec
dnf -y install $(find $(rpm --eval %_topdir) -name 'xtream-ui-nettle-3.9.1-1.el7.x86_64.rpm')
wget https://ftp.gnu.org/gnu/libtasn1/libtasn1-4.19.0.tar.gz -O $(rpm --eval %_topdir)/SOURCES/libtasn1-4.19.0.tar.gz
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtream-ui-libtasn1.spec -O $(rpm --eval %_topdir)/SPECS/xtream-ui-libtasn1.spec
rpmbuild -ba $(rpm --eval %_topdir)/SPECS/xtream-ui-libtasn1.spec
dnf -y install $(find $(rpm --eval %_topdir) -name 'xtream-ui-libtasn1-4.19.0-1.el7.x86_64.rpm')











wget https://www.nasm.us/pub/nasm/releasebuilds/2.16.01/nasm-2.16.01.tar.bz2 -O $(rpm --eval %_topdir)/SOURCES/nasm-2.16.01.tar.bz2
wget https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtream-ui-nasm.spec -O $(rpm --eval %_topdir)/SPECS/xtream-ui-nasm.spec
rpmbuild -ba $(rpm --eval %_topdir)/SPECS/xtream-ui-nasm.spec
dnf -y install $(find $(rpm --eval %_topdir) -name 'xtream-ui-nasm-2.16.01-1.el7.x86_64.rpm')


























