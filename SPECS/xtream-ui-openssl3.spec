%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-openssl3
Version: xtream-ui-openssl3version
Release: 1%{?dist}
# We have to remove certain patented algorithms from the openssl source
# tarball with the hobble-openssl script which is included below.
# The original openssl upstream tarball cannot be shipped in the .src.rpm.
Source: http://artfiles.org/openssl.org/source/openssl-%{version}.tar.gz

License: ASL 2.0
URL: http://www.openssl.org/
AutoReq: no
BuildRequires: gcc
BuildRequires: coreutils, perl-interpreter, sed, zlib-devel, /usr/bin/cmp
BuildRequires: lksctp-tools-devel
BuildRequires: /usr/bin/rename
BuildRequires: /usr/bin/pod2man
BuildRequires: /usr/sbin/sysctl
BuildRequires: perl(Test::Harness), perl(Test::More), perl(Math::BigInt)
BuildRequires: perl(Module::Load::Conditional), perl(File::Temp)
BuildRequires: perl(Time::HiRes), perl(IPC::Cmd), perl(Pod::Html), perl(Digest::SHA)
BuildRequires: perl(FindBin), perl(lib), perl(File::Compare), perl(File::Copy), perl(bigint)
BuildRequires: git-core
Requires: coreutils

%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

%prep
%autosetup -S git -n openssl-%{version}

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"

export HASHBANGPERL=/usr/bin/perl
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
sslarch=%{_os}-%{_target_cpu}
%ifarch %ix86
sslarch=linux-elf
if ! echo %{_target} | grep -q i686 ; then
	sslflags="no-asm 386"
fi
%endif
%ifarch x86_64
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch sparcv9
sslarch=linux-sparcv9
sslflags=no-asm
%endif
%ifarch sparc64
sslarch=linux64-sparcv9
sslflags=no-asm
%endif
%ifarch alpha alphaev56 alphaev6 alphaev67
sslarch=linux-alpha-gcc
%endif
%ifarch s390 sh3eb sh4eb
sslarch="linux-generic32 -DB_ENDIAN"
%endif
%ifarch s390x
sslarch="linux64-s390x"
%endif
%ifarch %{arm}
sslarch=linux-armv4
%endif
%ifarch aarch64
sslarch=linux-aarch64
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch sh3 sh4
sslarch=linux-generic32
%endif
%ifarch ppc64 ppc64p7
sslarch=linux-ppc64
%endif
%ifarch ppc64le
sslarch="linux-ppc64le"
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch mips mipsel
sslarch="linux-mips32 -mips32r2"
%endif
%ifarch mips64 mips64el
sslarch="linux64-mips64 -mips64r2"
%endif
%ifarch mips64el
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch riscv64
sslarch=linux-generic64
%endif
./Configure --prefix=/root/ffmpeg_build --openssldir=/root/ffmpeg_build/etc/pki/tls shared zlib ${sslarch} $RPM_OPT_FLAGS

# Do not run this in a production package the FIPS symbols must be patched-in
#util/mkdef.pl crypto update

make %{?_smp_mflags}

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/doc/openssl
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/man

%files
/root/ffmpeg_build/bin/c_rehash
/root/ffmpeg_build/bin/openssl
/root/ffmpeg_build/etc/pki/tls/ct_log_list.cnf
/root/ffmpeg_build/etc/pki/tls/ct_log_list.cnf.dist
/root/ffmpeg_build/etc/pki/tls/misc/CA.pl
/root/ffmpeg_build/etc/pki/tls/misc/tsget
/root/ffmpeg_build/etc/pki/tls/misc/tsget.pl
/root/ffmpeg_build/etc/pki/tls/openssl.cnf
/root/ffmpeg_build/etc/pki/tls/openssl.cnf.dist
/root/ffmpeg_build/include/openssl/aes.h
/root/ffmpeg_build/include/openssl/asn1.h
/root/ffmpeg_build/include/openssl/asn1_mac.h
/root/ffmpeg_build/include/openssl/asn1err.h
/root/ffmpeg_build/include/openssl/asn1t.h
/root/ffmpeg_build/include/openssl/async.h
/root/ffmpeg_build/include/openssl/asyncerr.h
/root/ffmpeg_build/include/openssl/bio.h
/root/ffmpeg_build/include/openssl/bioerr.h
/root/ffmpeg_build/include/openssl/blowfish.h
/root/ffmpeg_build/include/openssl/bn.h
/root/ffmpeg_build/include/openssl/bnerr.h
/root/ffmpeg_build/include/openssl/buffer.h
/root/ffmpeg_build/include/openssl/buffererr.h
/root/ffmpeg_build/include/openssl/camellia.h
/root/ffmpeg_build/include/openssl/cast.h
/root/ffmpeg_build/include/openssl/cmac.h
/root/ffmpeg_build/include/openssl/cmp.h
/root/ffmpeg_build/include/openssl/cmp_util.h
/root/ffmpeg_build/include/openssl/cmperr.h
/root/ffmpeg_build/include/openssl/cms.h
/root/ffmpeg_build/include/openssl/cmserr.h
/root/ffmpeg_build/include/openssl/comp.h
/root/ffmpeg_build/include/openssl/comperr.h
/root/ffmpeg_build/include/openssl/conf.h
/root/ffmpeg_build/include/openssl/conf_api.h
/root/ffmpeg_build/include/openssl/conferr.h
/root/ffmpeg_build/include/openssl/configuration.h
/root/ffmpeg_build/include/openssl/conftypes.h
/root/ffmpeg_build/include/openssl/core.h
/root/ffmpeg_build/include/openssl/core_dispatch.h
/root/ffmpeg_build/include/openssl/core_names.h
/root/ffmpeg_build/include/openssl/core_object.h
/root/ffmpeg_build/include/openssl/crmf.h
/root/ffmpeg_build/include/openssl/crmferr.h
/root/ffmpeg_build/include/openssl/crypto.h
/root/ffmpeg_build/include/openssl/cryptoerr.h
/root/ffmpeg_build/include/openssl/cryptoerr_legacy.h
/root/ffmpeg_build/include/openssl/ct.h
/root/ffmpeg_build/include/openssl/cterr.h
/root/ffmpeg_build/include/openssl/decoder.h
/root/ffmpeg_build/include/openssl/decodererr.h
/root/ffmpeg_build/include/openssl/des.h
/root/ffmpeg_build/include/openssl/dh.h
/root/ffmpeg_build/include/openssl/dherr.h
/root/ffmpeg_build/include/openssl/dsa.h
/root/ffmpeg_build/include/openssl/dsaerr.h
/root/ffmpeg_build/include/openssl/dtls1.h
/root/ffmpeg_build/include/openssl/e_os2.h
/root/ffmpeg_build/include/openssl/ebcdic.h
/root/ffmpeg_build/include/openssl/ec.h
/root/ffmpeg_build/include/openssl/ecdh.h
/root/ffmpeg_build/include/openssl/ecdsa.h
/root/ffmpeg_build/include/openssl/ecerr.h
/root/ffmpeg_build/include/openssl/encoder.h
/root/ffmpeg_build/include/openssl/encodererr.h
/root/ffmpeg_build/include/openssl/engine.h
/root/ffmpeg_build/include/openssl/engineerr.h
/root/ffmpeg_build/include/openssl/err.h
/root/ffmpeg_build/include/openssl/ess.h
/root/ffmpeg_build/include/openssl/esserr.h
/root/ffmpeg_build/include/openssl/evp.h
/root/ffmpeg_build/include/openssl/evperr.h
/root/ffmpeg_build/include/openssl/fips_names.h
/root/ffmpeg_build/include/openssl/fipskey.h
/root/ffmpeg_build/include/openssl/hmac.h
/root/ffmpeg_build/include/openssl/http.h
/root/ffmpeg_build/include/openssl/httperr.h
/root/ffmpeg_build/include/openssl/idea.h
/root/ffmpeg_build/include/openssl/kdf.h
/root/ffmpeg_build/include/openssl/kdferr.h
/root/ffmpeg_build/include/openssl/lhash.h
/root/ffmpeg_build/include/openssl/macros.h
/root/ffmpeg_build/include/openssl/md2.h
/root/ffmpeg_build/include/openssl/md4.h
/root/ffmpeg_build/include/openssl/md5.h
/root/ffmpeg_build/include/openssl/mdc2.h
/root/ffmpeg_build/include/openssl/modes.h
/root/ffmpeg_build/include/openssl/obj_mac.h
/root/ffmpeg_build/include/openssl/objects.h
/root/ffmpeg_build/include/openssl/objectserr.h
/root/ffmpeg_build/include/openssl/ocsp.h
/root/ffmpeg_build/include/openssl/ocsperr.h
/root/ffmpeg_build/include/openssl/opensslconf.h
/root/ffmpeg_build/include/openssl/opensslv.h
/root/ffmpeg_build/include/openssl/ossl_typ.h
/root/ffmpeg_build/include/openssl/param_build.h
/root/ffmpeg_build/include/openssl/params.h
/root/ffmpeg_build/include/openssl/pem.h
/root/ffmpeg_build/include/openssl/pem2.h
/root/ffmpeg_build/include/openssl/pemerr.h
/root/ffmpeg_build/include/openssl/pkcs12.h
/root/ffmpeg_build/include/openssl/pkcs12err.h
/root/ffmpeg_build/include/openssl/pkcs7.h
/root/ffmpeg_build/include/openssl/pkcs7err.h
/root/ffmpeg_build/include/openssl/prov_ssl.h
/root/ffmpeg_build/include/openssl/proverr.h
/root/ffmpeg_build/include/openssl/provider.h
/root/ffmpeg_build/include/openssl/rand.h
/root/ffmpeg_build/include/openssl/randerr.h
/root/ffmpeg_build/include/openssl/rc2.h
/root/ffmpeg_build/include/openssl/rc4.h
/root/ffmpeg_build/include/openssl/rc5.h
/root/ffmpeg_build/include/openssl/ripemd.h
/root/ffmpeg_build/include/openssl/rsa.h
/root/ffmpeg_build/include/openssl/rsaerr.h
/root/ffmpeg_build/include/openssl/safestack.h
/root/ffmpeg_build/include/openssl/seed.h
/root/ffmpeg_build/include/openssl/self_test.h
/root/ffmpeg_build/include/openssl/sha.h
/root/ffmpeg_build/include/openssl/srp.h
/root/ffmpeg_build/include/openssl/srtp.h
/root/ffmpeg_build/include/openssl/ssl.h
/root/ffmpeg_build/include/openssl/ssl2.h
/root/ffmpeg_build/include/openssl/ssl3.h
/root/ffmpeg_build/include/openssl/sslerr.h
/root/ffmpeg_build/include/openssl/sslerr_legacy.h
/root/ffmpeg_build/include/openssl/stack.h
/root/ffmpeg_build/include/openssl/store.h
/root/ffmpeg_build/include/openssl/storeerr.h
/root/ffmpeg_build/include/openssl/symhacks.h
/root/ffmpeg_build/include/openssl/tls1.h
/root/ffmpeg_build/include/openssl/trace.h
/root/ffmpeg_build/include/openssl/ts.h
/root/ffmpeg_build/include/openssl/tserr.h
/root/ffmpeg_build/include/openssl/txt_db.h
/root/ffmpeg_build/include/openssl/types.h
/root/ffmpeg_build/include/openssl/ui.h
/root/ffmpeg_build/include/openssl/uierr.h
/root/ffmpeg_build/include/openssl/whrlpool.h
/root/ffmpeg_build/include/openssl/x509.h
/root/ffmpeg_build/include/openssl/x509_vfy.h
/root/ffmpeg_build/include/openssl/x509err.h
/root/ffmpeg_build/include/openssl/x509v3.h
/root/ffmpeg_build/include/openssl/x509v3err.h
/root/ffmpeg_build/lib64/engines-3/capi.so
/root/ffmpeg_build/lib64/engines-3/loader_attic.so
/root/ffmpeg_build/lib64/engines-3/padlock.so
/root/ffmpeg_build/lib64/libcrypto.a
/root/ffmpeg_build/lib64/libcrypto.so
/root/ffmpeg_build/lib64/libcrypto.so.3
/root/ffmpeg_build/lib64/libssl.a
/root/ffmpeg_build/lib64/libssl.so
/root/ffmpeg_build/lib64/libssl.so.3
/root/ffmpeg_build/lib64/ossl-modules/legacy.so
/root/ffmpeg_build/lib64/pkgconfig/libcrypto.pc
/root/ffmpeg_build/lib64/pkgconfig/libssl.pc
/root/ffmpeg_build/lib64/pkgconfig/openssl.pc

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
