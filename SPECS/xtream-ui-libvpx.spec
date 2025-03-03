%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-libvpx
Version: xtream-ui-libvpxversion
Release: 1%{?dist}
# wget -O /root/rpmbuild/SOURCES/libvpx-$libvpxversion.tar.gz https://chromium.googlesource.com/webm/libvpx/+archive/$libvpxcheckout.tar.gz
Source: libvpx-%{version}.tar.gz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-opus
Requires: xtream-ui-opus
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n libvpx-%{version} -c
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 \
--disable-examples --disable-unit-tests --enable-vp9-highbitdepth --as=yasm
make %{?_smp_mflags} all
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir

%files
/root/ffmpeg_build/include/vpx/vp8.h
/root/ffmpeg_build/include/vpx/vp8cx.h
/root/ffmpeg_build/include/vpx/vp8dx.h
/root/ffmpeg_build/include/vpx/vpx_codec.h
/root/ffmpeg_build/include/vpx/vpx_decoder.h
/root/ffmpeg_build/include/vpx/vpx_encoder.h
/root/ffmpeg_build/include/vpx/vpx_ext_ratectrl.h
/root/ffmpeg_build/include/vpx/vpx_frame_buffer.h
/root/ffmpeg_build/include/vpx/vpx_image.h
/root/ffmpeg_build/include/vpx/vpx_integer.h
/root/ffmpeg_build/lib64/libvpx.a
/root/ffmpeg_build/lib64/pkgconfig/vpx.pc

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
