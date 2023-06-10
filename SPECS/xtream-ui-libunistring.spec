%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-libunistring
Version: 1.1
Release: 1%{?dist}
Source: https://ftp.gnu.org/gnu/libunistring/libunistring-%{version}.tar.xz
License: ASL 2.0
URL: https://gnu.org
%if 0%{?rhel} == 7
BuildRequires: devtoolset-8
%endif
BuildRequires: rpm-build gcc gcc-c++ gcc-gfortran gcc-objc gcc-objc++ libstdc++-devel gcc-gnat wget bzip2 gzip xz wget tar make pkgconfig patch
BuildRequires: xtream-ui-p11-kit
Requires: xtream-ui-p11-kit
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -n libunistring-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/home/xtreamcodes/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/home/xtreamcodes/ffmpeg_build/include -L/home/xtreamcodes/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix=/home/xtreamcodes/ffmpeg_build --libdir=/home/xtreamcodes/ffmpeg_build/lib64
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir

%files
/home/xtreamcodes/ffmpeg_build/include/unicase.h
/home/xtreamcodes/ffmpeg_build/include/uniconv.h
/home/xtreamcodes/ffmpeg_build/include/unictype.h
/home/xtreamcodes/ffmpeg_build/include/unigbrk.h
/home/xtreamcodes/ffmpeg_build/include/unilbrk.h
/home/xtreamcodes/ffmpeg_build/include/uniname.h
/home/xtreamcodes/ffmpeg_build/include/uninorm.h
/home/xtreamcodes/ffmpeg_build/include/unistdio.h
/home/xtreamcodes/ffmpeg_build/include/unistr.h
/home/xtreamcodes/ffmpeg_build/include/unistring/cdefs.h
/home/xtreamcodes/ffmpeg_build/include/unistring/iconveh.h
/home/xtreamcodes/ffmpeg_build/include/unistring/inline.h
/home/xtreamcodes/ffmpeg_build/include/unistring/localcharset.h
/home/xtreamcodes/ffmpeg_build/include/unistring/stdbool.h
/home/xtreamcodes/ffmpeg_build/include/unistring/stdint.h
/home/xtreamcodes/ffmpeg_build/include/unistring/version.h
/home/xtreamcodes/ffmpeg_build/include/unistring/woe32dll.h
/home/xtreamcodes/ffmpeg_build/include/unitypes.h
/home/xtreamcodes/ffmpeg_build/include/uniwbrk.h
/home/xtreamcodes/ffmpeg_build/include/uniwidth.h
/home/xtreamcodes/ffmpeg_build/lib64/libunistring.a
/home/xtreamcodes/ffmpeg_build/lib64/libunistring.la
/home/xtreamcodes/ffmpeg_build/lib64/libunistring.so
/home/xtreamcodes/ffmpeg_build/lib64/libunistring.so.5
/home/xtreamcodes/ffmpeg_build/lib64/libunistring.so.5.0.0
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_1.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_10.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_11.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_12.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_13.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_14.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_15.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_16.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_17.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_18.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_19.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_2.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_20.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_21.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_22.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_3.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_4.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_5.html
/home/xtreamcodes/ffmpeg_build/share/doc/libunistring/libunistring_6.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_7.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_8.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_9.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_abt.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_toc.html
/root/ffmpeg_build/share/info/libunistring.info
