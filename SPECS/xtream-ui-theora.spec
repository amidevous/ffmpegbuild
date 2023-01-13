%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-theora
Version: xtream-ui-theoraversion
Release: 1%{?dist}
# wget -O /root/rpmbuild/SOURCES/theora-$theoraversion.tar.gz https://github.com/xiph/theora/archive/refs/tags/v$theoraversion.tar.gz
Source: theora-%{version}.tar.gz
Patch1: theora.patch
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-libogg
Requires: xtream-ui-libogg
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n theora-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./autogen.sh
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --enable-static
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/doc/

%files
/root/ffmpeg_build/include/theora/codec.h
/root/ffmpeg_build/include/theora/theora.h
/root/ffmpeg_build/include/theora/theoradec.h
/root/ffmpeg_build/include/theora/theoraenc.h
/root/ffmpeg_build/lib64/libtheora.a
/root/ffmpeg_build/lib64/libtheora.la
/root/ffmpeg_build/lib64/libtheora.so
/root/ffmpeg_build/lib64/libtheora.so.0
/root/ffmpeg_build/lib64/libtheora.so.0.3.10
/root/ffmpeg_build/lib64/libtheoradec.a
/root/ffmpeg_build/lib64/libtheoradec.la
/root/ffmpeg_build/lib64/libtheoradec.so
/root/ffmpeg_build/lib64/libtheoradec.so.1
/root/ffmpeg_build/lib64/libtheoradec.so.1.1.4
/root/ffmpeg_build/lib64/libtheoraenc.a
/root/ffmpeg_build/lib64/libtheoraenc.la
/root/ffmpeg_build/lib64/libtheoraenc.so
/root/ffmpeg_build/lib64/libtheoraenc.so.1
/root/ffmpeg_build/lib64/libtheoraenc.so.1.1.2
/root/ffmpeg_build/lib64/pkgconfig/theora.pc
/root/ffmpeg_build/lib64/pkgconfig/theoradec.pc
/root/ffmpeg_build/lib64/pkgconfig/theoraenc.pc

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
