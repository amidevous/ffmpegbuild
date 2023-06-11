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
Summary: Fraunhofer FDK AAC Codec Library
Name: xtreamui-fdk-aac
Version: 2.0.2
Release: 5%{?dist}
Source: https://github.com/mstorsjo/fdk-aac/archive/v%{version}/fdk-aac-%{version}.tar.gz
License: FDK-AAC
URL: https://github.com/mstorsjo/fdk-aac
%if 0%{?rhel} == 7
BuildRequires: devtoolset-8
%endif
BuildRequires: rpm-build make git gcc gcc-c++ gcc-gfortran gcc-objc gcc-objc++ libstdc++-devel
BuildRequires: autoconf automake libtool wget bzip2 gzip xz wget tar make pkgconfig patch m4 coreutils
BuildRequires: xtreamui-x265
Requires: xtreamui-x265
%description
The Fraunhofer FDK AAC Codec Library ("FDK AAC Codec") is software that
implements the MPEG Advanced Audio Coding ("AAC") encoding and decoding
scheme for digital audio.
%prep
%autosetup -n fdk-aac-%{version}
%build
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
#RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="%{_libdir}:$LD_LIBRARY_PATH"
export PATH="%{_bindir}:$PATH"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$RPM_OPT_FLAGS -I%{_includedir} -L%{_libdir}"
autoreconf -fiv
%configure --disable-silent-rules --disable-static
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post
chown -R xtreamcodes:xtreamcodes /home/xtreamcodes/
chown -R xtreamcodes:xtreamcodes /home/xtreamcodes/*
/sbin/ldconfig
%postun -p /sbin/ldconfig 

%files
%doc ChangeLog
%license NOTICE
%{_libdir}/fdk-aac/*.so.*
%doc documentation/*.pdf
%{_libdir}/pkgconfig/fdk-aac.pc
%{_includedir}/fdk-aac/

%changelog
* Tue Oct 18 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.0.2-5
- Rebuilt

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 04 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Leigh Scott <leigh123linux@googlemail.com> - 2.0.1-1
- Update to 2.0.1

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.0.0-1
- Update to 2.0.0

* Tue Sep 25 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.1.6-4
- Remove group tag

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.6-3
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.1.6-1
- Update to 1.6

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.1.5-1
- Update to 1.5

* Wed Sep 07 2016 Nicolas Chauvet <kwizart@gmail.com> - 0.1.5-0.1.gita0bd8aa
- Update to github snapshot
- Spec file clean-up

* Fri Nov 06 2015 Nicolas Chauvet <kwizart@gmail.com> - 0.1.4-1
- Update to 1.4

* Sun Jan 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.1.3-1
- Update to 1.3.0

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.1.2-1
- Update to 0.1.2

* Thu Mar 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.1.1-1
- Initial spec

