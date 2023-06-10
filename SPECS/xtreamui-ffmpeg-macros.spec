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
%global _var %{_prefix}/var
%global _usr %{_prefix}
%global _usrsrc %{_prefix}/src
%global _initddir %{_sysconfdir}/rc.d/init.d
%global _initrddir %{_initddir}
Summary: macros for ffmpeg build for xtreamui
Name: xtreamui-ffmpeg-macros
Version: 1.0.0
Release: 1%{?dist}
License: ASL 2.0
URL: https://github.com/amidevous/ffmpegbuild
BuildRequires: rpm-build gcc gcc-c++ gcc-gfortran gcc-objc gcc-objc++ libstdc++-devel gcc-gnat wget bzip2 gzip xz wget tar make pkgconfig patch
%description
macros for ffmpeg build for xtreamui
%prep
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="%{_libdir}:$LD_LIBRARY_PATH"
export PATH="%{_bindir}:$PATH"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I%{_includedir} -L%{_libdir}"


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
cat > %{_prefix}/macros <<EOF
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
%global _var %{_prefix}/var
%global _usr %{_prefix}
%global _usrsrc %{_prefix}/src
%global _initddir %{_sysconfdir}/rc.d/init.d
%global _initrddir %{_initddir}
EOF

%files
%{_prefix}/macros
