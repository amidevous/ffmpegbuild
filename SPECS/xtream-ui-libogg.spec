%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-libogg
Version: xtream-ui-liboggversion
Release: 1%{?dist}
Source: https://github.com/xiph/ogg/releases/download/v%{version}/libogg-%{version}.tar.gz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-libass
Requires: xtream-ui-libass
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n libogg-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --enable-static
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/doc/

%files
/root/ffmpeg_build/include/ogg/config_types.h
/root/ffmpeg_build/include/ogg/ogg.h
/root/ffmpeg_build/include/ogg/os_types.h
/root/ffmpeg_build/lib64/libogg.a
/root/ffmpeg_build/lib64/libogg.la
/root/ffmpeg_build/lib64/libogg.so
/root/ffmpeg_build/lib64/libogg.so.0
/root/ffmpeg_build/lib64/libogg.so.0.8.5
/root/ffmpeg_build/lib64/pkgconfig/ogg.pc
/root/ffmpeg_build/share/aclocal/ogg.m4

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
