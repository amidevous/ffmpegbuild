%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-libunistring
Version: xtream-ui-libunistringversion
Release: 1%{?dist}
Source: https://ftp.gnu.org/gnu/libunistring/libunistring-%{version}.tar.xz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-p11-kit
Requires: xtream-ui-p11-kit
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n libunistring-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix=/root/ffmpeg_build --libdir=/root/ffmpeg_build/lib64
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir

%files
/root/ffmpeg_build/include/unicase.h
/root/ffmpeg_build/include/uniconv.h
/root/ffmpeg_build/include/unictype.h
/root/ffmpeg_build/include/unigbrk.h
/root/ffmpeg_build/include/unilbrk.h
/root/ffmpeg_build/include/uniname.h
/root/ffmpeg_build/include/uninorm.h
/root/ffmpeg_build/include/unistdio.h
/root/ffmpeg_build/include/unistr.h
/root/ffmpeg_build/include/unistring/cdefs.h
/root/ffmpeg_build/include/unistring/iconveh.h
/root/ffmpeg_build/include/unistring/inline.h
/root/ffmpeg_build/include/unistring/localcharset.h
/root/ffmpeg_build/include/unistring/stdbool.h
/root/ffmpeg_build/include/unistring/stdint.h
/root/ffmpeg_build/include/unistring/version.h
/root/ffmpeg_build/include/unistring/woe32dll.h
/root/ffmpeg_build/include/unitypes.h
/root/ffmpeg_build/include/uniwbrk.h
/root/ffmpeg_build/include/uniwidth.h
/root/ffmpeg_build/lib64/libunistring.a
/root/ffmpeg_build/lib64/libunistring.la
/root/ffmpeg_build/lib64/libunistring.so
/root/ffmpeg_build/lib64/libunistring.so.5
/root/ffmpeg_build/lib64/libunistring.so.5.0.0
/root/ffmpeg_build/share/doc/libunistring/libunistring_1.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_10.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_11.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_12.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_13.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_14.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_15.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_16.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_17.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_18.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_19.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_2.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_20.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_21.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_22.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_3.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_4.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_5.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_6.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_7.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_8.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_9.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_abt.html
/root/ffmpeg_build/share/doc/libunistring/libunistring_toc.html
/root/ffmpeg_build/share/info/libunistring.info

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
