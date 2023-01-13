%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-vorbis
Version: xtream-ui-vorbisversion
Release: 1%{?dist}
Source: https://github.com/xiph/vorbis/releases/download/v%{version}/libvorbis-%{version}.tar.gz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-theora
Requires: xtream-ui-theora
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n libvorbis-%{version}
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
/root/ffmpeg_build/include/vorbis/codec.h
/root/ffmpeg_build/include/vorbis/vorbisenc.h
/root/ffmpeg_build/include/vorbis/vorbisfile.h
/root/ffmpeg_build/lib64/libvorbis.a
/root/ffmpeg_build/lib64/libvorbis.la
/root/ffmpeg_build/lib64/libvorbis.so
/root/ffmpeg_build/lib64/libvorbis.so.0
/root/ffmpeg_build/lib64/libvorbis.so.0.4.9
/root/ffmpeg_build/lib64/libvorbisenc.a
/root/ffmpeg_build/lib64/libvorbisenc.la
/root/ffmpeg_build/lib64/libvorbisenc.so
/root/ffmpeg_build/lib64/libvorbisenc.so.2
/root/ffmpeg_build/lib64/libvorbisenc.so.2.0.12
/root/ffmpeg_build/lib64/libvorbisfile.a
/root/ffmpeg_build/lib64/libvorbisfile.la
/root/ffmpeg_build/lib64/libvorbisfile.so
/root/ffmpeg_build/lib64/libvorbisfile.so.3
/root/ffmpeg_build/lib64/libvorbisfile.so.3.3.8
/root/ffmpeg_build/lib64/pkgconfig/vorbis.pc
/root/ffmpeg_build/lib64/pkgconfig/vorbisenc.pc
/root/ffmpeg_build/lib64/pkgconfig/vorbisfile.pc
/root/ffmpeg_build/share/aclocal/vorbis.m4

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
