%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-opus
Version: xtream-ui-opusversion
Release: 1%{?dist}
Source: https://archive.mozilla.org/pub/opus/opus-%{version}.tar.gz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-lame
Requires: xtream-ui-lame
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n opus-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --disable-shared
make %{?_smp_mflags} all
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/man
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/doc

%files
/root/ffmpeg_build/include/opus/opus.h
/root/ffmpeg_build/include/opus/opus_defines.h
/root/ffmpeg_build/include/opus/opus_multistream.h
/root/ffmpeg_build/include/opus/opus_projection.h
/root/ffmpeg_build/include/opus/opus_types.h
/root/ffmpeg_build/lib64/libopus.a
/root/ffmpeg_build/lib64/libopus.la
/root/ffmpeg_build/lib64/pkgconfig/opus.pc
/root/ffmpeg_build/share/aclocal/opus.m4

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
