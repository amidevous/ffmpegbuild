%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-gmp
Version: 6.2.1
Release: 1%{?dist}
Source: https://ftp.gnu.org/gnu/gmp/gmp-%{version}.tar.xz
License: ASL 2.0
URL: https://gnu.org/gnu
%if 0%{?rhel} == 7
BuildRequires: devtoolset-8
%endif
BuildRequires: rpm-build gcc gcc-c++ gcc-gfortran gcc-objc gcc-objc++ libstdc++-devel gcc-gnat wget bzip2 gzip xz wget tar make pkgconfig patch
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -n gmp-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/home/xtreamcodes/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/home/xtreamcodes/iptv_xtream_codes/bin:$PATH"
export PKG_CONFIG_PATH="/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/home/xtreamcodes/ffmpeg_build/include -L/home/xtreamcodes/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix=/home/xtreamcodes/ffmpeg_build --libdir=/home/xtreamcodes/ffmpeg_build/lib64 --enable-cxx --enable-fat
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install


%files
/home/xtreamcodes/ffmpeg_build/include/gmp.h
/home/xtreamcodes/ffmpeg_build/include/gmpxx.h
/home/xtreamcodes/ffmpeg_build/lib64/libgmp.a
/home/xtreamcodes/ffmpeg_build/lib64/libgmp.la
/home/xtreamcodes/ffmpeg_build/lib64/libgmp.so
/home/xtreamcodes/ffmpeg_build/lib64/libgmp.so.10
/home/xtreamcodes/ffmpeg_build/lib64/libgmp.so.10.4.1
/home/xtreamcodes/ffmpeg_build/lib64/libgmpxx.a
/home/xtreamcodes/ffmpeg_build/lib64/libgmpxx.la
/home/xtreamcodes/ffmpeg_build/lib64/libgmpxx.so
/home/xtreamcodes/ffmpeg_build/lib64/libgmpxx.so.4
/home/xtreamcodes/ffmpeg_build/lib64/libgmpxx.so.4.6.1
/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig/gmp.pc
/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig/gmpxx.pc
/home/xtreamcodes/ffmpeg_build/share/info/dir
/home/xtreamcodes/ffmpeg_build/share/info/gmp.info
/home/xtreamcodes/ffmpeg_build/share/info/gmp.info-1
/home/xtreamcodes/ffmpeg_build/share/info/gmp.info-2
