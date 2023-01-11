%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-p11-kit
Version: xtream-ui-p11-kitversion
Release: 1%{?dist}
Source: https://github.com/p11-glue/p11-kit/releases/download/%{version}/p11-kit-%{version}.tar.xz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-libffi
Requires: xtream-ui-libffi
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n p11-kit-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix=/root/ffmpeg_build --libdir=/root/ffmpeg_build/lib64 --without-systemd --disable-nls
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir

%files
/root/ffmpeg_build/bin/p11-kit
/root/ffmpeg_build/bin/trust
/root/ffmpeg_build/etc/pkcs11/pkcs11.conf.example
/root/ffmpeg_build/include/p11-kit-1/p11-kit/deprecated.h
/root/ffmpeg_build/include/p11-kit-1/p11-kit/iter.h
/root/ffmpeg_build/include/p11-kit-1/p11-kit/p11-kit.h
/root/ffmpeg_build/include/p11-kit-1/p11-kit/pin.h
/root/ffmpeg_build/include/p11-kit-1/p11-kit/pkcs11.h
/root/ffmpeg_build/include/p11-kit-1/p11-kit/pkcs11x.h
/root/ffmpeg_build/include/p11-kit-1/p11-kit/remote.h
/root/ffmpeg_build/include/p11-kit-1/p11-kit/uri.h
/root/ffmpeg_build/lib64/libp11-kit.la
/root/ffmpeg_build/lib64/libp11-kit.so
/root/ffmpeg_build/lib64/libp11-kit.so.0
/root/ffmpeg_build/lib64/libp11-kit.so.0.3.0
/root/ffmpeg_build/lib64/p11-kit-proxy.so
/root/ffmpeg_build/lib64/pkcs11/p11-kit-client.la
/root/ffmpeg_build/lib64/pkcs11/p11-kit-client.so
/root/ffmpeg_build/lib64/pkcs11/p11-kit-trust.la
/root/ffmpeg_build/lib64/pkcs11/p11-kit-trust.so
/root/ffmpeg_build/lib64/pkgconfig/p11-kit-1.pc
/root/ffmpeg_build/libexec/p11-kit/p11-kit-remote
/root/ffmpeg_build/libexec/p11-kit/p11-kit-server
/root/ffmpeg_build/libexec/p11-kit/trust-extract-compat
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/config-example.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/config-files.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/config.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/devel-building-style.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/devel-building.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/devel-commands.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/devel-debugging.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/devel-paths.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/devel-testing.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/devel.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/gtk-doc.css
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/home.png
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/index.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/left-insensitive.png
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/left.png
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit-Deprecated.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit-Future.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit-Modules.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit-PIN-Callbacks.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit-URIs.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit-Utilities.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit.devhelp2
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/pkcs11-conf.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/reference.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/remoting.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/right-insensitive.png
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/right.png
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/sharing-managed.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/sharing.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/style.css
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/tools.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/trust-disable.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/trust-glib-networking.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/trust-module.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/trust-nss.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/trust.html
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/up-insensitive.png
/root/ffmpeg_build/share/gtk-doc/html/p11-kit/up.png
/root/ffmpeg_build/share/p11-kit/modules/p11-kit-trust.module
/usr/share/bash-completion/completions/p11-kit
/usr/share/bash-completion/completions/trust


%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
