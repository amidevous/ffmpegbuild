%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-x265
Version: xtream-ui-x265version
Release: 1%{?dist}
Source: https://bitbucket.org/multicoreware/x265_git/downloads/x265_%{version}.tar.gz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-x264
Requires: xtream-ui-x264
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n x265_%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
cd build/linux
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="/root/ffmpeg_build" -DLIB_INSTALL_DIR=lib64 -DENABLE_SHARED:bool=off ../../source
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
cd build/linux
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir

%files
/root/ffmpeg_build/bin/x265
/root/ffmpeg_build/include/x265.h
/root/ffmpeg_build/include/x265_config.h
/root/ffmpeg_build/lib64/libx265.a

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
