%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-p11-kit
Version: 0.24.1
Release: 1%{?dist}
Source: https://github.com/p11-glue/p11-kit/releases/download/%{version}/p11-kit-%{version}.tar.xz
License: ASL 2.0
URL: https://gnu.org
%if 0%{?rhel} == 7
BuildRequires: devtoolset-8
%endif
BuildRequires: rpm-build gcc gcc-c++ gcc-gfortran gcc-objc gcc-objc++ libstdc++-devel gcc-gnat wget bzip2 gzip xz wget tar make pkgconfig patch
BuildRequires: xtream-ui-libffi
Requires: xtream-ui-libffi
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -n p11-kit-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/home/xtreamcodes/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/home/xtreamcodes/iptv_xtream_codes/bin:$PATH"
export PKG_CONFIG_PATH="/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/home/xtreamcodes/ffmpeg_build/include -L/home/xtreamcodes/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix=/home/xtreamcodes/ffmpeg_build --libdir=/home/xtreamcodes/ffmpeg_build/lib64 --bindir=/home/xtreamcodes/iptv_xtream_codes/bin --without-systemd --disable-nls
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir
rm -rf $RPM_BUILD_ROOT/usr


%files
/home/xtreamcodes/iptv_xtream_codes/bin/p11-kit
/home/xtreamcodes/iptv_xtream_codes/bin/trust
/home/xtreamcodes/ffmpeg_build/etc/pkcs11/pkcs11.conf.example
/home/xtreamcodes/ffmpeg_build/include/p11-kit-1/p11-kit/deprecated.h
/home/xtreamcodes/ffmpeg_build/include/p11-kit-1/p11-kit/iter.h
/home/xtreamcodes/ffmpeg_build/include/p11-kit-1/p11-kit/p11-kit.h
/home/xtreamcodes/ffmpeg_build/include/p11-kit-1/p11-kit/pin.h
/home/xtreamcodes/ffmpeg_build/include/p11-kit-1/p11-kit/pkcs11.h
/home/xtreamcodes/ffmpeg_build/include/p11-kit-1/p11-kit/pkcs11x.h
/home/xtreamcodes/ffmpeg_build/include/p11-kit-1/p11-kit/remote.h
/home/xtreamcodes/ffmpeg_build/include/p11-kit-1/p11-kit/uri.h
/home/xtreamcodes/ffmpeg_build/lib64/libp11-kit.la
/home/xtreamcodes/ffmpeg_build/lib64/libp11-kit.so
/home/xtreamcodes/ffmpeg_build/lib64/libp11-kit.so.0
/home/xtreamcodes/ffmpeg_build/lib64/libp11-kit.so.0.3.0
/home/xtreamcodes/ffmpeg_build/lib64/p11-kit-proxy.so
/home/xtreamcodes/ffmpeg_build/lib64/pkcs11/p11-kit-client.la
/home/xtreamcodes/ffmpeg_build/lib64/pkcs11/p11-kit-client.so
/home/xtreamcodes/ffmpeg_build/lib64/pkcs11/p11-kit-trust.la
/home/xtreamcodes/ffmpeg_build/lib64/pkcs11/p11-kit-trust.so
/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig/p11-kit-1.pc
/home/xtreamcodes/ffmpeg_build/libexec/p11-kit/p11-kit-remote
/home/xtreamcodes/ffmpeg_build/libexec/p11-kit/p11-kit-server
/home/xtreamcodes/ffmpeg_build/libexec/p11-kit/trust-extract-compat
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/config-example.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/config-files.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/config.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/devel-building-style.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/devel-building.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/devel-commands.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/devel-debugging.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/devel-paths.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/devel-testing.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/devel.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/gtk-doc.css
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/home.png
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/index.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/left-insensitive.png
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/left.png
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit-Deprecated.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit-Future.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit-Modules.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit-PIN-Callbacks.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit-URIs.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit-Utilities.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit.devhelp2
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/p11-kit.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/pkcs11-conf.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/reference.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/remoting.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/right-insensitive.png
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/right.png
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/sharing-managed.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/sharing.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/style.css
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/tools.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/trust-disable.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/trust-glib-networking.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/trust-module.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/trust-nss.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/trust.html
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/up-insensitive.png
/home/xtreamcodes/ffmpeg_build/share/gtk-doc/html/p11-kit/up.png
/home/xtreamcodes/ffmpeg_build/share/p11-kit/modules/p11-kit-trust.module
