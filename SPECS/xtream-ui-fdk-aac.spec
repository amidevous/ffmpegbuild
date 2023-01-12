%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-fdk-aac
Version: xtream-ui-fdk-aacversion
Release: 1%{?dist}
# wget -O /root/rpmbuild/SOURCES/fdk-aac-2.0.2.tar.gz https://github.com/mstorsjo/fdk-aac/archive/refs/tags/v2.0.2.tar.gz
Source: fdk-aac-%{version}.tar.gz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-x265
Requires: xtream-ui-x265
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n fdk-aac-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
autoreconf -fiv
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --disable-shared
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir

%files
/root/ffmpeg_build/include/fdk-aac/FDK_audio.h
/root/ffmpeg_build/include/fdk-aac/aacdecoder_lib.h
/root/ffmpeg_build/include/fdk-aac/aacenc_lib.h
/root/ffmpeg_build/include/fdk-aac/genericStds.h
/root/ffmpeg_build/include/fdk-aac/machine_type.h
/root/ffmpeg_build/include/fdk-aac/syslib_channelMapDescr.h
/root/ffmpeg_build/lib64/libfdk-aac.a
/root/ffmpeg_build/lib64/libfdk-aac.la
/root/ffmpeg_build/lib64/pkgconfig/fdk-aac.pc

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
