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
%global with_srp 0%{?fedora} < 38

%global with_mingw 0
%if 0%{?fedora}
%global with_mingw 0%{!?_without_mingw:1}
%endif 

Version: 3.8.0
Release: 2%{?dist}
Patch: gnutls-3.2.7-rpath.patch

# Delete only after the kernel has been patched for thested systems
Patch: gnutls-3.7.8-ktls_disable_keyupdate_test.patch

# follow https://gitlab.com/gnutls/gnutls/-/issues/1443
Patch: gnutls-3.7.8-ktls_skip_tls12_chachapoly_test.patch


Summary: A TLS protocol implementation
Name: gnutls
# The libraries are LGPLv2.1+, utilities are GPLv3+
License: GPLv3+ and LGPLv2+
BuildRequires: p11-kit-devel >= 0.21.3, gettext-devel
BuildRequires: readline-devel, libtasn1-devel >= 4.3
BuildRequires: zlib-devel, brotli-devel, libzstd-devel
BuildRequires: automake, autoconf, gperf, libtool, texinfo
BuildRequires: xtreamui-nettle
BuildRequires: libidn2-devel
BuildRequires: libunistring-devel
BuildRequires: net-tools, datefudge, softhsm, gcc, gcc-c++
BuildRequires: gnupg2
BuildRequires: git-core

# for a sanity check on cert loading
BuildRequires: p11-kit-trust, ca-certificates
Requires: crypto-policies
Requires: p11-kit-trust
Requires: libtasn1 >= 4.3
Requires: xtreamui-nettle >= 3.4.1


BuildRequires: make gtk-doc

%if %{with_mingw}
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libtasn1 >= 4.3
BuildRequires:  mingw32-readline
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-p11-kit >= 0.23.1
BuildRequires:  mingw32-nettle >= 3.6
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libtasn1 >= 4.3
BuildRequires:  mingw64-readline
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-p11-kit >= 0.23.1
BuildRequires:  mingw64-nettle >= 3.6
%endif

URL: http://www.gnutls.org/
%define short_version %(echo %{version} | grep -m1 -o "[0-9]*\.[0-9]*" | head -1)
Source0: https://www.gnupg.org/ftp/gcrypt/gnutls/v%{short_version}/%{name}-%{version}.tar.xz
Source1: https://www.gnupg.org/ftp/gcrypt/gnutls/v%{short_version}/%{name}-%{version}.tar.xz.sig
Source2: https://gnutls.org/gnutls-release-keyring.gpg

# Wildcard bundling exception https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib) = 20130424

%package c++
Summary: The C++ interface to GnuTLS
Requires: %{name}%{?_isa} = %{version}-%{release}

%package devel
Summary: Development files for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-c++%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%package utils
License: GPLv3+
Summary: Command line tools for TLS protocol
Requires: %{name}%{?_isa} = %{version}-%{release}


%description
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 

%description c++
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 

%description devel
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 
This package contains files needed for developing applications with
the GnuTLS library.

%description utils
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 
This package contains command line TLS client and server and certificate
manipulation tools.


%if %{with_mingw}
%package -n mingw32-%{name}
Summary:        MinGW GnuTLS TLS/SSL encryption library
Requires:       pkgconfig
Requires:       mingw32-libtasn1 >= 4.3
BuildArch:      noarch

%description -n mingw32-gnutls
GnuTLS TLS/SSL encryption library.  This library is cross-compiled
for MinGW.

%package -n mingw64-%{name}
Summary:        MinGW GnuTLS TLS/SSL encryption library
Requires:       pkgconfig
Requires:       mingw64-libtasn1 >= 4.3
BuildArch:      noarch

%description -n mingw64-gnutls
GnuTLS TLS/SSL encryption library.  This library is cross-compiled
for MinGW.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -p1 -S git

%build
%define _lto_cflags %{nil}

autoreconf -fi

sed -i -e 's|sys_lib_dlsearch_path_spec="/lib /usr/lib|sys_lib_dlsearch_path_spec="/lib /usr/lib %{_libdir}|g' configure
rm -f lib/minitasn1/*.c lib/minitasn1/*.h

echo "SYSTEM=NORMAL" >> tests/system.prio

CCASFLAGS="$CCASFLAGS -Wa,--generate-missing-build-notes=yes"
export CCASFLAGS


mkdir native_build
pushd native_build
%global _configure ../configure
%configure \
	   --disable-gost \
%if %{with_srp}
           --enable-srp-authentication \
%endif
%ifarch %{ix86}
           --disable-year2038 \
%endif
	   --enable-sha1-support \
           --disable-static \
           --disable-openssl-compatibility \
           --disable-non-suiteb-curves \
           --with-system-priority-file=%{_sysconfdir}/crypto-policies/back-ends/gnutls.config \
           --with-default-trust-store-pkcs11="pkcs11:" \
           --without-tpm \
           --without-tpm2 \
           --enable-ktls \
           --htmldir=%{_docdir}/manual \
           --disable-libdane \
	   --with-zlib --with-brotli --with-zstd \
           --disable-rpath \
           --with-default-priority-string="@SYSTEM"

%make_build
popd

%if %{with_mingw}
# MinGW does not support CCASFLAGS
export CCASFLAGS=""
%mingw_configure \
%if %{with_srp}
    --enable-srp-authentication \
%endif
    --enable-sha1-support \
    --disable-static \
    --disable-openssl-compatibility \
    --disable-non-suiteb-curves \
    --disable-libdane \
    --disable-rpath \
    --disable-nls \
    --disable-cxx \
    --enable-local-libopts \
    --enable-shared \
    --without-tpm \
    --with-included-unistring \
    --disable-doc \
    --with-default-priority-string="@SYSTEM"
%mingw_make %{?_smp_mflags}
%endif

%install
%make_install -C native_build
pushd native_build
make -C doc install-html DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gnutls-dane.pc




%find_lang gnutls
popd

%if %{with_mingw}
%mingw_make_install

# Remove .la files
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

# The .def files aren't interesting for other binaries
rm -f $RPM_BUILD_ROOT%{mingw32_bindir}/*.def
rm -f $RPM_BUILD_ROOT%{mingw64_bindir}/*.def

# Remove info and man pages which duplicate stuff in Fedora already.
rm -rf $RPM_BUILD_ROOT%{mingw32_infodir}
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw32_docdir}/gnutls

rm -rf $RPM_BUILD_ROOT%{mingw64_infodir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_docdir}/gnutls

# Remove test libraries
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/crypt32.dll*
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/ncrypt.dll*
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/crypt32.dll*
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/ncrypt.dll*

%mingw_debug_install_post
%endif

%check
pushd native_build
make check %{?_smp_mflags} GNUTLS_SYSTEM_PRIORITY_FILE=/dev/null
popd

%files -f native_build/gnutls.lang
%{_libdir}/libgnutls.so.30*
%doc README.md AUTHORS NEWS THANKS
%license LICENSE doc/COPYING doc/COPYING.LESSER

%files c++
%{_libdir}/libgnutlsxx.so.*

%files devel
%{_includedir}/*
%{_libdir}/libgnutls*.so

%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
%{_infodir}/gnutls*
%{_infodir}/pkcs11-vision*
%{_docdir}/manual/*

%files utils
%{_bindir}/certtool
%{_bindir}/ocsptool
%{_bindir}/psktool
%{_bindir}/p11tool
%if %{with_srp}
%{_bindir}/srptool
%endif
%{_bindir}/gnutls*
%{_mandir}/man1/*
%doc doc/certtool.cfg



%if %{with_mingw}
%files -n mingw32-%{name}
%license LICENSE doc/COPYING doc/COPYING.LESSER
%{mingw32_bindir}/certtool.exe
%{mingw32_bindir}/gnutls-cli-debug.exe
%{mingw32_bindir}/gnutls-cli.exe
%{mingw32_bindir}/gnutls-serv.exe
%{mingw32_bindir}/libgnutls-30.dll
%{mingw32_bindir}/ocsptool.exe
%{mingw32_bindir}/p11tool.exe
%{mingw32_bindir}/psktool.exe
%if %{with_srp}
%{mingw32_bindir}/srptool.exe
%endif
%{mingw32_libdir}/libgnutls.dll.a
%{mingw32_libdir}/libgnutls-30.def
%{mingw32_libdir}/pkgconfig/gnutls.pc
%{mingw32_includedir}/gnutls/

%files -n mingw64-%{name}
%license LICENSE doc/COPYING doc/COPYING.LESSER
%{mingw64_bindir}/certtool.exe
%{mingw64_bindir}/gnutls-cli-debug.exe
%{mingw64_bindir}/gnutls-cli.exe
%{mingw64_bindir}/gnutls-serv.exe
%{mingw64_bindir}/libgnutls-30.dll
%{mingw64_bindir}/ocsptool.exe
%{mingw64_bindir}/p11tool.exe
%{mingw64_bindir}/psktool.exe
%if %{with_srp}
%{mingw64_bindir}/srptool.exe
%endif
%{mingw64_libdir}/libgnutls.dll.a
%{mingw64_libdir}/libgnutls-30.def
%{mingw64_libdir}/pkgconfig/gnutls.pc
%{mingw64_includedir}/gnutls/
%endif

%changelog
* Thu Mar 02 2023 Daniel P. Berrangé <berrange@redhat.com> - 3.8.0-2
- Disable GNULIB's year2038 support for 64-bit time_t

* Thu Feb 16 2023 Zoltan Fridrich <zfridric@redhat.com> - 3.8.0-1
- [packit] 3.8.0 upstream release

* Tue Feb 14 2023 Zoltan Fridrich <zfridric@redhat.com> - 3.7.8-14
- Prepare for release

* Fri Jan 20 2023 Frantisek Krenzelok <krenzelok.frantisek@gmail.com> - 3.7.8-13
- KTLS: disable ktls_keyupdate & tls1.2 chachapoly tests

* Fri Jan 20 2023 Frantisek Krenzelok <krenzelok.frantisek@gmail.com> - 3.7.8-12
- KTLS additional ciphersuites

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Frantisek Krenzelok <krenzelok.frantisek@gmail.com> - 3.7.8-10
- gcc-analyzer: suppress warnings

* Thu Oct 27 2022 Daniel P. Berrangé <berrange@redhat.com> - 3.7.8-9
- Cross-compiled mingw sub-RPMs should be 'noarch'

* Wed Oct 19 2022 Zoltan Fridrich <zfridric@redhat.com> - 3.7.8-8
- Add conditions for mingw

* Tue Oct 18 2022 Michael Cronenworth <mike@cchtml.com> - 3.7.8-6
- Initial MinGW package support

* Tue Oct 18 2022 Zoltan Fridrich <zfridric@redhat.com> - 3.7.8-5
- Use make macros

* Tue Oct 18 2022 Zoltan Fridrich <zfridric@redhat.com> - 3.7.8-4
- RPMAUTOSPEC: unresolvable merge
