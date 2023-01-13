%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-harfbuzz
Version: xtream-ui-harfbuzzversion
Release: 1%{?dist}
Source: https://github.com/harfbuzz/harfbuzz/releases/download/%{version}/harfbuzz-%{version}.tar.xz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-fribidi
Requires: xtream-ui-fribidi
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n harfbuzz-%{version}
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
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/gtk-doc/
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/include/harfbuzz/hb-ft.h
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/bin/hb-ot-shape-closure
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/bin/hb-shape
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/bin/hb-subset
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/include/harfbuzz/hb-glib.h
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/include/harfbuzz/hb-icu.h
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/lib64/libharfbuzz-icu.a
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/lib64/libharfbuzz-icu.la
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/lib64/libharfbuzz-icu.so
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/lib64/libharfbuzz-icu.so.0
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/lib64/libharfbuzz-icu.so.0.60000.0
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/lib64/pkgconfig/harfbuzz-icu.pc


%files
/root/ffmpeg_build/include/harfbuzz/hb-aat-layout.h
/root/ffmpeg_build/include/harfbuzz/hb-aat.h
/root/ffmpeg_build/include/harfbuzz/hb-blob.h
/root/ffmpeg_build/include/harfbuzz/hb-buffer.h
/root/ffmpeg_build/include/harfbuzz/hb-common.h
/root/ffmpeg_build/include/harfbuzz/hb-cplusplus.hh
/root/ffmpeg_build/include/harfbuzz/hb-deprecated.h
/root/ffmpeg_build/include/harfbuzz/hb-draw.h
/root/ffmpeg_build/include/harfbuzz/hb-face.h
/root/ffmpeg_build/include/harfbuzz/hb-font.h
/root/ffmpeg_build/include/harfbuzz/hb-map.h
/root/ffmpeg_build/include/harfbuzz/hb-ot-color.h
/root/ffmpeg_build/include/harfbuzz/hb-ot-deprecated.h
/root/ffmpeg_build/include/harfbuzz/hb-ot-font.h
/root/ffmpeg_build/include/harfbuzz/hb-ot-layout.h
/root/ffmpeg_build/include/harfbuzz/hb-ot-math.h
/root/ffmpeg_build/include/harfbuzz/hb-ot-meta.h
/root/ffmpeg_build/include/harfbuzz/hb-ot-metrics.h
/root/ffmpeg_build/include/harfbuzz/hb-ot-name.h
/root/ffmpeg_build/include/harfbuzz/hb-ot-shape.h
/root/ffmpeg_build/include/harfbuzz/hb-ot-var.h
/root/ffmpeg_build/include/harfbuzz/hb-ot.h
/root/ffmpeg_build/include/harfbuzz/hb-set.h
/root/ffmpeg_build/include/harfbuzz/hb-shape-plan.h
/root/ffmpeg_build/include/harfbuzz/hb-shape.h
/root/ffmpeg_build/include/harfbuzz/hb-style.h
/root/ffmpeg_build/include/harfbuzz/hb-subset-repacker.h
/root/ffmpeg_build/include/harfbuzz/hb-subset.h
/root/ffmpeg_build/include/harfbuzz/hb-unicode.h
/root/ffmpeg_build/include/harfbuzz/hb-version.h
/root/ffmpeg_build/include/harfbuzz/hb.h
/root/ffmpeg_build/lib64/cmake/harfbuzz/harfbuzz-config.cmake
/root/ffmpeg_build/lib64/libharfbuzz-subset.a
/root/ffmpeg_build/lib64/libharfbuzz-subset.la
/root/ffmpeg_build/lib64/libharfbuzz-subset.so
/root/ffmpeg_build/lib64/libharfbuzz-subset.so.0
/root/ffmpeg_build/lib64/libharfbuzz-subset.so.0.60000.0
/root/ffmpeg_build/lib64/libharfbuzz.a
/root/ffmpeg_build/lib64/libharfbuzz.la
/root/ffmpeg_build/lib64/libharfbuzz.so
/root/ffmpeg_build/lib64/libharfbuzz.so.0
/root/ffmpeg_build/lib64/libharfbuzz.so.0.60000.0
/root/ffmpeg_build/lib64/pkgconfig/harfbuzz-subset.pc
/root/ffmpeg_build/lib64/pkgconfig/harfbuzz.pc

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
