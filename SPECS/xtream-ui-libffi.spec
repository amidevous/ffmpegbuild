%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-libffi
Version: 3.4.4
Release: 1%{?dist}
Source: https://github.com/libffi/libffi/releases/download/v%{version}/libffi-%{version}.tar.gz
License: ASL 2.0
URL: https://gnu.org
%if 0%{?rhel} == 7
BuildRequires: devtoolset-8
%endif
BuildRequires: rpm-build gcc gcc-c++ gcc-gfortran gcc-objc gcc-objc++ libstdc++-devel gcc-gnat wget bzip2 gzip xz wget tar make pkgconfig patch
BuildRequires: xtream-ui-libtasn1
Requires: xtream-ui-libtasn1
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n libffi-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/home/xtreamcodes/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/home/xtreamcodes/iptv_xtream_codes/bin:$PATH"
export PKG_CONFIG_PATH="/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/home/xtreamcodes/ffmpeg_build/include -L/home/xtreamcodes/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix=/home/xtreamcodes/ffmpeg_build --libdir=//home/xtreamcodes/ffmpeg_build/lib64 --disable-multi-os-directory
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/home/xtreamcodes/ffmpeg_build/share/info/dir

%files
/home/xtreamcodes/ffmpeg_build/include/ffi.h
/home/xtreamcodes/ffmpeg_build/include/ffitarget.h
/home/xtreamcodes/ffmpeg_build/lib64/libffi.a
/home/xtreamcodes/ffmpeg_build/lib64/libffi.la
/home/xtreamcodes/ffmpeg_build/lib64/libffi.so
/home/xtreamcodes/ffmpeg_build/lib64/libffi.so.8
/home/xtreamcodes/ffmpeg_build/lib64/libffi.so.8.1.2
/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig/libffi.pc
/home/xtreamcodes/ffmpeg_build/share/info/libffi.info
/home/xtreamcodes/ffmpeg_build/share/man/man3/ffi.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/ffi_call.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/ffi_prep_cif.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/ffi_prep_cif_var.3
