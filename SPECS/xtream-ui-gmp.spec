%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-gmp
Version: xtream-ui-gmpversion
Release: 1%{?dist}
Source: https://ftp.gnu.org/gnu/gmp/gmp-%{version}.tar.xz
License: ASL 2.0
URL: https://gnu.org
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n gmp-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix=/root/ffmpeg_build --libdir=/root/ffmpeg_build/lib64 --enable-cxx --enable-fat
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install

%files
/root/ffmpeg_build/include/gmp.h
/root/ffmpeg_build/include/gmpxx.h
/root/ffmpeg_build/lib64/libgmp.a
/root/ffmpeg_build/lib64/libgmp.la
/root/ffmpeg_build/lib64/libgmp.so
/root/ffmpeg_build/lib64/libgmp.so.10
/root/ffmpeg_build/lib64/libgmp.so.10.4.1
/root/ffmpeg_build/lib64/libgmpxx.a
/root/ffmpeg_build/lib64/libgmpxx.la
/root/ffmpeg_build/lib64/libgmpxx.so
/root/ffmpeg_build/lib64/libgmpxx.so.4
/root/ffmpeg_build/lib64/libgmpxx.so.4.6.1
/root/ffmpeg_build/lib64/pkgconfig/gmp.pc
/root/ffmpeg_build/lib64/pkgconfig/gmpxx.pc
/root/ffmpeg_build/share/info/dir
/root/ffmpeg_build/share/info/gmp.info
/root/ffmpeg_build/share/info/gmp.info-1
/root/ffmpeg_build/share/info/gmp.info-2

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
