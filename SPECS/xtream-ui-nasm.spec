%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-nasm
Version: 2.16.01
Release: 1%{?dist}
Source: https://www.nasm.us/pub/nasm/releasebuilds/%{version}/nasm-%{version}.tar.bz2
License: ASL 2.0
URL: https://www.nasm.us
%if 0%{?rhel} == 7
BuildRequires: devtoolset-8
%endif
BuildRequires: rpm-build gcc gcc-c++ gcc-gfortran gcc-objc gcc-objc++ libstdc++-devel gcc-gnat wget bzip2 gzip xz wget tar make pkgconfig patch
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n nasm-%{version}
%build
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/home/xtreamcodes/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/home/xtreamcodes/iptv_xtream_codes/bin:$PATH"
export PKG_CONFIG_PATH="/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/home/xtreamcodes/ffmpeg_build/include -L/home/xtreamcodes/ffmpeg_build/lib64"
./autogen.sh
./configure --prefix="/home/xtreamcodes/ffmpeg_build" --bindir="/home/xtreamcodes/iptv_xtream_codes/bin"
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/home/xtreamcodes/ffmpeg_build/share/info/dir

%post
chown -R xtreamcodes:xtreamcodes /home/xtreamcodes/
chown -R xtreamcodes:xtreamcodes /home/xtreamcodes/*

%files
/home/xtreamcodes/iptv_xtream_codes/bin/nasm
/home/xtreamcodes/iptv_xtream_codes/bin/ndisasm
/home/xtreamcodes/ffmpeg_build/share/man/man1/nasm.1
/home/xtreamcodes/ffmpeg_build/share/man/man1/ndisasm.1

