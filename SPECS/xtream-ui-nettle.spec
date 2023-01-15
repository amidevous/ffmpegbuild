%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-nettle
Version: xtream-ui-nettleversion
Release: 1%{?dist}
Source: https://ftp.gnu.org/gnu/nettle/nettle-%{version}.tar.gz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-gmp
Requires: xtream-ui-gmp
Provides: libhogweed.so.6()(64bit), libhogweed.so.6(HOGWEED_6)(64bit), libnettle.so.8()(64bit), libnettle.so.8(NETTLE_8)(64bit)
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n nettle-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix=/root/ffmpeg_build --bindir=/root/ffmpeg_build/bin --sbindir=/root/ffmpeg_build/bin \
--libexecdir=/root/ffmpeg_build/libexec --sysconfdir=/root/ffmpeg_build/etc  --libdir=/root/ffmpeg_build/lib64 \
--includedir=/root/ffmpeg_build/include --with-include-path=/root/ffmpeg_build/include --with-lib-path=/root/ffmpeg_build/lib64 \
 --enable-mini-gmp --host=x86_64 --disable-pic --disable-shared
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/

%files
/root/ffmpeg_build/bin/nettle-hash
/root/ffmpeg_build/bin/nettle-lfib-stream
/root/ffmpeg_build/bin/nettle-pbkdf2
/root/ffmpeg_build/bin/pkcs1-conv
/root/ffmpeg_build/bin/sexp-conv
/root/ffmpeg_build/include/nettle/aes.h
/root/ffmpeg_build/include/nettle/arcfour.h
/root/ffmpeg_build/include/nettle/arctwo.h
/root/ffmpeg_build/include/nettle/asn1.h
/root/ffmpeg_build/include/nettle/base16.h
/root/ffmpeg_build/include/nettle/base64.h
/root/ffmpeg_build/include/nettle/bignum.h
/root/ffmpeg_build/include/nettle/blowfish.h
/root/ffmpeg_build/include/nettle/buffer.h
/root/ffmpeg_build/include/nettle/camellia.h
/root/ffmpeg_build/include/nettle/cast128.h
/root/ffmpeg_build/include/nettle/cbc.h
/root/ffmpeg_build/include/nettle/ccm.h
/root/ffmpeg_build/include/nettle/cfb.h
/root/ffmpeg_build/include/nettle/chacha-poly1305.h
/root/ffmpeg_build/include/nettle/chacha.h
/root/ffmpeg_build/include/nettle/cmac.h
/root/ffmpeg_build/include/nettle/ctr.h
/root/ffmpeg_build/include/nettle/curve25519.h
/root/ffmpeg_build/include/nettle/curve448.h
/root/ffmpeg_build/include/nettle/des.h
/root/ffmpeg_build/include/nettle/dsa-compat.h
/root/ffmpeg_build/include/nettle/dsa.h
/root/ffmpeg_build/include/nettle/eax.h
/root/ffmpeg_build/include/nettle/ecc-curve.h
/root/ffmpeg_build/include/nettle/ecc.h
/root/ffmpeg_build/include/nettle/ecdsa.h
/root/ffmpeg_build/include/nettle/eddsa.h
/root/ffmpeg_build/include/nettle/gcm.h
/root/ffmpeg_build/include/nettle/gostdsa.h
/root/ffmpeg_build/include/nettle/gosthash94.h
/root/ffmpeg_build/include/nettle/hkdf.h
/root/ffmpeg_build/include/nettle/hmac.h
/root/ffmpeg_build/include/nettle/knuth-lfib.h
/root/ffmpeg_build/include/nettle/macros.h
/root/ffmpeg_build/include/nettle/md2.h
/root/ffmpeg_build/include/nettle/md4.h
/root/ffmpeg_build/include/nettle/md5-compat.h
/root/ffmpeg_build/include/nettle/md5.h
/root/ffmpeg_build/include/nettle/memops.h
/root/ffmpeg_build/include/nettle/memxor.h
/root/ffmpeg_build/include/nettle/mini-gmp.h
/root/ffmpeg_build/include/nettle/nettle-meta.h
/root/ffmpeg_build/include/nettle/nettle-types.h
/root/ffmpeg_build/include/nettle/nist-keywrap.h
/root/ffmpeg_build/include/nettle/pbkdf2.h
/root/ffmpeg_build/include/nettle/pgp.h
/root/ffmpeg_build/include/nettle/pkcs1.h
/root/ffmpeg_build/include/nettle/poly1305.h
/root/ffmpeg_build/include/nettle/pss-mgf1.h
/root/ffmpeg_build/include/nettle/pss.h
/root/ffmpeg_build/include/nettle/realloc.h
/root/ffmpeg_build/include/nettle/ripemd160.h
/root/ffmpeg_build/include/nettle/rsa.h
/root/ffmpeg_build/include/nettle/salsa20.h
/root/ffmpeg_build/include/nettle/serpent.h
/root/ffmpeg_build/include/nettle/sexp.h
/root/ffmpeg_build/include/nettle/sha.h
/root/ffmpeg_build/include/nettle/sha1.h
/root/ffmpeg_build/include/nettle/sha2.h
/root/ffmpeg_build/include/nettle/sha3.h
/root/ffmpeg_build/include/nettle/siv-cmac.h
/root/ffmpeg_build/include/nettle/sm3.h
/root/ffmpeg_build/include/nettle/streebog.h
/root/ffmpeg_build/include/nettle/twofish.h
/root/ffmpeg_build/include/nettle/umac.h
/root/ffmpeg_build/include/nettle/version.h
/root/ffmpeg_build/include/nettle/xts.h
/root/ffmpeg_build/include/nettle/yarrow.h
/root/ffmpeg_build/lib64/libhogweed.a
/root/ffmpeg_build/lib64/libhogweed.so
/root/ffmpeg_build/lib64/libhogweed.so.6
/root/ffmpeg_build/lib64/libhogweed.so.6.6
/root/ffmpeg_build/lib64/libnettle.a
/root/ffmpeg_build/lib64/libnettle.so
/root/ffmpeg_build/lib64/libnettle.so.8
/root/ffmpeg_build/lib64/libnettle.so.8.6
/root/ffmpeg_build/lib64/pkgconfig/hogweed.pc
/root/ffmpeg_build/lib64/pkgconfig/nettle.pc

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
