%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-lame
Version: xtream-ui-lameversion
Release: 1%{?dist}
Source: https://downloads.sourceforge.net/project/lame/lame/%{version}/lame-%{version}.tar.gz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-fdk-aac
Requires: xtream-ui-fdk-aac
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n lame-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --bindir="/root/ffmpeg_build/bin" --disable-shared --enable-nasm
make %{?_smp_mflags} all
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir

%files
/root/ffmpeg_build/bin/lame
/root/ffmpeg_build/include/lame/lame.h
/root/ffmpeg_build/lib64/libmp3lame.a
/root/ffmpeg_build/lib64/libmp3lame.la
/root/ffmpeg_build/share/doc/lame/html/about.html
/root/ffmpeg_build/share/doc/lame/html/abr.html
/root/ffmpeg_build/share/doc/lame/html/cbr.html
/root/ffmpeg_build/share/doc/lame/html/contact.html
/root/ffmpeg_build/share/doc/lame/html/contributors.html
/root/ffmpeg_build/share/doc/lame/html/detailed.html
/root/ffmpeg_build/share/doc/lame/html/history.html
/root/ffmpeg_build/share/doc/lame/html/index.html
/root/ffmpeg_build/share/doc/lame/html/introduction.html
/root/ffmpeg_build/share/doc/lame/html/links.html
/root/ffmpeg_build/share/doc/lame/html/list.html
/root/ffmpeg_build/share/doc/lame/html/ms_stereo.html
/root/ffmpeg_build/share/doc/lame/html/usage.html
/root/ffmpeg_build/share/doc/lame/html/vbr.html
/root/ffmpeg_build/share/man/man1/lame.1

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
