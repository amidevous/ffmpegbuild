%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
%global _prefix /home/xtreamcodes/ffmpeg_build
%global _sysconfdir %{_prefix}/etc
%global _includedir %{_prefix}/include
%global _bindir /home/xtreamcodes/iptv_xtream_codes/bin
%global _sbindir %{_bindir}
%global _libdir %{_prefix}/%{_lib}
%global _libexecdir %{_prefix}/libexec
%global _datarootdir %{_prefix}/share
%global _datadir %{_datarootdir}
%global _infodir %{_datarootdir}/info
%global _mandir %{_datarootdir}/man
%global _docdir %{_datadir}/doc
%global _rundir %{_prefix}/run
%global _localstatedir %{_prefix}/var
%global _sharedstatedir %{_prefix}/var/lib
%global _usrsrc %{_prefix}/src
%global _initddir %{_sysconfdir}/rc.d/init.d
%global _initrddir %{_initddir}
# Use old cmake macro
%global __cmake_in_source_build 1

%global     _so_version 199

Summary:    H.265/HEVC encoder
Name:       xtreamui-x265
Version:    3.5
Release:    5%{?dist}
URL:        http://x265.org/
# source/Lib/TLibCommon - BSD
# source/Lib/TLibEncoder - BSD
# everything else - GPLv2+
License:    GPLv2+ and BSD
Source0:    https://bitbucket.org/multicoreware/x265_git/downloads/x265_%{version}.tar.gz

# fix building as PIC
Patch0:     https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-x265/x265-pic.patch
Patch1:     https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-x265/x265-high-bit-depth-soname.patch
Patch2:     https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-x265/x265-detect_cpu_armhfp.patch
Patch3:     https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-x265/x265-arm-cflags.patch
Patch4:     https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/SPECS/xtreamui-x265/x265-pkgconfig_path_fix.patch

%if 0%{?rhel} == 7
BuildRequires: devtoolset-8
%endif
BuildRequires: rpm-build make git gcc gcc-c++ gcc-gfortran gcc-objc gcc-objc++ libstdc++-devel
BuildRequires: autoconf automake libtool wget bzip2 gzip xz wget tar make pkgconfig patch m4 coreutils
BuildRequires:  git
BuildRequires:  cmake3
%{?el7:BuildRequires: epel-rpm-macros}
BuildRequires:  xtreamui-nasm
BuildRequires:  ninja-build

%ifnarch armv7hl armv7hnl s390 s390x
BuildRequires:  numactl-devel
%endif
BuildRequires:  xtreamui-x264
Requires:  xtreamui-x264

%description
The primary objective of x265 is to become the best H.265/HEVC encoder
available anywhere, offering the highest compression efficiency and the highest
performance on a wide variety of hardware platforms.


%prep
%autosetup -p1 -n x265_%{version}

%build
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
#RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="%{_libdir}:$LD_LIBRARY_PATH"
export PATH="%{_bindir}:$PATH"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$RPM_OPT_FLAGS -I%{_includedir} -L%{_libdir}"
# High depth libraries (from source/h265.h):
#   If the requested bitDepth is not supported by the linked libx265,
#   it will attempt to dynamically bind x265_api_get() from a shared
#   library with an appropriate name:
#     8bit:  libx265_main.so
#     10bit: libx265_main10.so

build() {
%cmake3 -Wno-dev -G "Ninja" \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DCMAKE_SKIP_RPATH:BOOL=YES \
    -DENABLE_PIC:BOOL=ON \
    -DENABLE_SHARED=ON \
    -DENABLE_TESTS:BOOL=ON \
    -DENABLE_HDR10_PLUS=YES \
    -DCMAKE_ASM_NASM_FLAGS=-w-macro-params-legacy \
    -DBIN_INSTALL_DIR:PATH=%{_bindir} \
    -DLIB_INSTALL_DIR:PATH=%{_libdir} \
    $* \
    ../source
%cmake3_build
}

# High depth 10/12 bit libraries are supported only on 64 bit. They require
# disabled AltiVec instructions for building on ppc64/ppc64le.
%ifarch x86_64 aarch64 ppc64 ppc64le
mkdir 10bit; pushd 10bit
    build \
    -DENABLE_CLI=OFF \
    -DENABLE_ALTIVEC=OFF \
    -DHIGH_BIT_DEPTH=ON
popd

mkdir 12bit; pushd 12bit
    build \
    -DENABLE_CLI=OFF \
    -DENABLE_ALTIVEC=OFF \
    -DHIGH_BIT_DEPTH=ON \
    -DMAIN12=ON
popd
%endif

# 8 bit base library + encoder
mkdir 8bit; pushd 8bit
    build
popd

%install
for i in 8 10 12; do
    if [ -d ${i}bit ]; then
        pushd ${i}bit
            %cmake3_install
            # Remove unversioned library, should not be linked to
            rm -f %{buildroot}%{_libdir}/libx265_main${i}.so
        popd
    fi
done

find %{buildroot} -name "*.a" -delete

%check
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
#RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="%{_libdir}:$LD_LIBRARY_PATH"
export PATH="%{_bindir}:$PATH"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$RPM_OPT_FLAGS -I%{_includedir} -L%{_libdir}"
for i in 8 10 12; do
    if [ -d ${i}bit ]; then
        pushd ${i}bit
            test/TestBench || :
        popd
    fi
done

%post
chown -R xtreamcodes:xtreamcodes /home/xtreamcodes/
chown -R xtreamcodes:xtreamcodes /home/xtreamcodes/*
/sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_bindir}/x265
%license COPYING
%{_libdir}/libhdr10plus.so
%{_libdir}/libx265.so.%{_so_version}
%ifarch x86_64 aarch64 ppc64 ppc64le
%{_libdir}/libx265_main10.so.%{_so_version}
%{_libdir}/libx265_main12.so.%{_so_version}
%endif
%doc doc/*
%{_includedir}/hdr10plus.h
%{_includedir}/x265.h
%{_includedir}/x265_config.h
%{_libdir}/libx265.so
%{_libdir}/pkgconfig/x265.pc

%changelog
* Thu Dec 29 2022 Nicolas Chauvet <kwizart@gmail.com> - 3.5-5
- Enable ENABLE_HDR10_PLUS everywhere rfbz#6454

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Apr 13 2021 Leigh Scott <leigh123linux@gmail.com> - 3.5-1
- Update to 3.5

* Tue Mar 16 2021 Leigh Scott <leigh123linux@gmail.com> - 3.4-5
- Enable HDR10+.

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Leigh Scott <leigh123linux@gmail.com> - 3.4-2
- Use old cmake macro

* Sun May 31 2020 Leigh Scott <leigh123linux@gmail.com> - 3.4-1
- Update to 3.4

* Wed Mar 11 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.3-2
- Rebuilt for i686

* Sun Feb 23 2020 Leigh Scott <leigh123linux@googlemail.com> - 3.3-1
- Update to 3.3

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 3.2.1-1
- Update to 3.2.1
- Switch upstream source url

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Aug 04 2019 Leigh Scott <leigh123linux@googlemail.com> - 3.1.2-1
- Update to 3.1.2

* Fri Jun 28 2019 Nicolas Chauvet <kwizart@gmail.com> - 3.1-1
- Update to 3.1
- Switch to github mirror

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Feb 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 3.0-1
- Update to 3.0

* Sun Dec 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.9-3
- Rebuild against newer nasm on el7 (rfbz #5128)

* Wed Nov 21 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.9-2
- Rebuild for ffmpeg-3.* on el7

* Sun Nov 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.9-1
- Update to 2.9

* Thu Oct 04 2018 Sérgio Basto <sergio@serjux.com> - 2.8-1
- Update to 2.8 more 2 patches to fix builds on non-x86 and arm
  https://bitbucket.org/multicoreware/x265/issues/404/28-fails-to-build-on-ppc64le-gnu-linux
  https://bitbucket.org/multicoreware/x265/issues/406/arm-assembly-fail-to-compile-on-18

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.7-5
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 08 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.7-3
- Fix pkgconfig file (rfbz #4853)

* Tue Feb 27 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.7-2
- Fix CFLAGS on ARM

* Tue Feb 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.7-1
- update to 2.7
- Drop shared test patch as it causes nasm build to fail
- Fix scriptlets
- Use ninja to build

* Sat Dec 30 2017 Sérgio Basto <sergio@serjux.com> - 2.6-1
- Update x265 to 2.6

* Mon Oct 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.5-1
- update to 2.5

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.4-1
- update to 2.4

* Mon Apr 10 2017 Simone Caronni <negativo17@gmail.com> - 2.2-3
- Use source from multicoreware website.
- Clean up SPEC file a bit (formatting, 80 char wide descriptions).
- Enable shared 10/12 bit libraries on 64 bit architectures.

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Dominik Mierzejewski <rpm@greysector.net> - 2.2-1
- update to 2.2
- spell out SO version in file list
- fix typo in patch

* Mon Nov 07 2016 Sérgio Basto <sergio@serjux.com> - 2.1-1
- Update to 2.1

* Thu Aug 18 2016 Sérgio Basto <sergio@serjux.com> - 1.9-3
- Clean spec, Vascom patches series, rfbz #4199, add license tag

* Tue Jul 19 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.9-2
- use https for source URL
- enable NUMA support
- make sure Fedora compiler flags are used on ARM

* Fri Apr 08 2016 Adrian Reber <adrian@lisas.de> - 1.9-1
- Update to 1.9

* Sun Oct 25 2015 Dominik Mierzejewski <rpm@greysector.net> 1.8-2
- fix building as PIC
- update SO version in file list

* Sat Oct 24 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.8-1
- Update to 1.8
- Avoid tests for now

* Wed Apr 15 2015 Dominik Mierzejewski <rpm@greysector.net> 1.6-1
- update to 1.6 (ABI bump, rfbz#3593)
- release tarballs are now hosted on videolan.org
- drop obsolete patches

* Thu Dec 18 2014 Dominik Mierzejewski <rpm@greysector.net> 1.2-6
- fix build on armv7l arch (partially fix rfbz#3361, patch by Nicolas Chauvet)
- don't run tests on ARM for now (rfbz#3361)

* Sun Aug 17 2014 Dominik Mierzejewski <rpm@greysector.net> 1.2-5
- don't include contributor agreement in doc
- make sure /usr/share/doc/x265 is owned
- add a comment noting which files are BSD-licenced

* Fri Aug 08 2014 Dominik Mierzejewski <rpm@greysector.net> 1.2-4
- don't create bogus soname (patch by Xavier)

* Thu Jul 17 2014 Dominik Mierzejewski <rpm@greysector.net> 1.2-3
- fix tr call to remove DOS EOL
- build the library with -fPIC on arm and i686, too

* Sun Jul 13 2014 Dominik Mierzejewski <rpm@greysector.net> 1.2-2
- use version in source URL
- update License tag
- fix EOL in drag-uncrustify.bat
- don't link test binaries with shared binary on x86 (segfault)

* Thu Jul 10 2014 Dominik Mierzejewski <rpm@greysector.net> 1.2-1
- initial build
- fix pkgconfig file install location
- link test binaries with shared library
