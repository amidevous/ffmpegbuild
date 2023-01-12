%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-gnutls
Version: xtream-ui-gnutlsversion
Release: 1%{?dist}
Source: https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/gnutls-%{version}.tar.xz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-libunistring
Requires: xtream-ui-libunistring
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n gnutls-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
autoreconf -ifv
./configure --prefix=/root/ffmpeg_build --libdir=/root/ffmpeg_build/lib64 --disable-hardware-acceleration \
--disable-doc --disable-nls --disable-rpath
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir

%files
/root/ffmpeg_build/bin/certtool
/root/ffmpeg_build/bin/gnutls-cli
/root/ffmpeg_build/bin/gnutls-cli-debug
/root/ffmpeg_build/bin/gnutls-serv
/root/ffmpeg_build/bin/ocsptool
/root/ffmpeg_build/bin/p11tool
/root/ffmpeg_build/bin/psktool
/root/ffmpeg_build/bin/srptool
/root/ffmpeg_build/include/gnutls/abstract.h
/root/ffmpeg_build/include/gnutls/compat.h
/root/ffmpeg_build/include/gnutls/crypto.h
/root/ffmpeg_build/include/gnutls/dtls.h
/root/ffmpeg_build/include/gnutls/gnutls.h
/root/ffmpeg_build/include/gnutls/gnutlsxx.h
/root/ffmpeg_build/include/gnutls/ocsp.h
/root/ffmpeg_build/include/gnutls/openpgp.h
/root/ffmpeg_build/include/gnutls/pkcs11.h
/root/ffmpeg_build/include/gnutls/pkcs12.h
/root/ffmpeg_build/include/gnutls/pkcs7.h
/root/ffmpeg_build/include/gnutls/self-test.h
/root/ffmpeg_build/include/gnutls/socket.h
/root/ffmpeg_build/include/gnutls/system-keys.h
/root/ffmpeg_build/include/gnutls/tpm.h
/root/ffmpeg_build/include/gnutls/urls.h
/root/ffmpeg_build/include/gnutls/x509-ext.h
/root/ffmpeg_build/include/gnutls/x509.h
/root/ffmpeg_build/lib64/libgnutls.la
/root/ffmpeg_build/lib64/libgnutls.so
/root/ffmpeg_build/lib64/libgnutls.so.30
/root/ffmpeg_build/lib64/libgnutls.so.30.28.2
/root/ffmpeg_build/lib64/libgnutlsxx.la
/root/ffmpeg_build/lib64/libgnutlsxx.so
/root/ffmpeg_build/lib64/libgnutlsxx.so.28
/root/ffmpeg_build/lib64/libgnutlsxx.so.28.1.0
/root/ffmpeg_build/lib64/pkgconfig/gnutls.pc

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
