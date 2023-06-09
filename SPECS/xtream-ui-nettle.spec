%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-nettle
Version: 3.9.1
Release: 1%{?dist}
Source: https://ftp.gnu.org/gnu/nettle/nettle-%{version}.tar.gz
License: ASL 2.0
URL: https://gnu.org/gnu/nettle
%if 0%{?rhel} == 7
BuildRequires: devtoolset-8
%endif
BuildRequires: rpm-build gcc gcc-c++ gcc-gfortran gcc-objc gcc-objc++ libstdc++-devel gcc-gnat wget bzip2 gzip xz wget tar make pkgconfig patch
BuildRequires: xtream-ui-gmp
Requires: xtream-ui-gmp
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n nettle-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/home/xtreamcodes/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/home/xtreamcodes/iptv_xtream_codes/bin:$PATH"
export PKG_CONFIG_PATH="/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/home/xtreamcodes/ffmpeg_build/include -L/home/xtreamcodes/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix=/home/xtreamcodes/ffmpeg_build --bindir=/root/ffmpeg_build/bin --sbindir=/root/ffmpeg_build/bin \
--libexecdir=/home/xtreamcodes/ffmpeg_build/libexec --sysconfdir=/home/xtreamcodes/ffmpeg_build/etc  --libdir=/home/xtreamcodes/ffmpeg_build/lib64 \
--includedir=/home/xtreamcodes/ffmpeg_build/include --with-include-path=/home/xtreamcodes/ffmpeg_build/include --with-lib-path=/home/xtreamcodes/ffmpeg_build/lib64 \
 --enable-mini-gmp
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/

%files
/home/xtreamcodes/iptv_xtream_codes/bin/nettle-hash
/home/xtreamcodes/iptv_xtream_codes/bin/nettle-lfib-stream
/home/xtreamcodes/iptv_xtream_codes/bin/nettle-pbkdf2
/home/xtreamcodes/iptv_xtream_codes/bin/pkcs1-conv
/home/xtreamcodes/iptv_xtream_codes/bin/sexp-conv
/home/xtreamcodes/ffmpeg_build/include/nettle/aes.h
/home/xtreamcodes/ffmpeg_build/include/nettle/arcfour.h
/home/xtreamcodes/ffmpeg_build/include/nettle/arctwo.h
/home/xtreamcodes/ffmpeg_build/include/nettle/asn1.h
/home/xtreamcodes/ffmpeg_build/include/nettle/base16.h
/home/xtreamcodes/ffmpeg_build/include/nettle/base64.h
/home/xtreamcodes/ffmpeg_build/include/nettle/bignum.h
/home/xtreamcodes/ffmpeg_build/include/nettle/blowfish.h
/home/xtreamcodes/ffmpeg_build/include/nettle/buffer.h
/home/xtreamcodes/ffmpeg_build/include/nettle/camellia.h
/home/xtreamcodes/ffmpeg_build/include/nettle/cast128.h
/home/xtreamcodes/ffmpeg_build/include/nettle/cbc.h
/home/xtreamcodes/ffmpeg_build/include/nettle/ccm.h
/home/xtreamcodes/ffmpeg_build/include/nettle/cfb.h
/home/xtreamcodes/ffmpeg_build/include/nettle/chacha-poly1305.h
/home/xtreamcodes/ffmpeg_build/include/nettle/chacha.h
/home/xtreamcodes/ffmpeg_build/include/nettle/cmac.h
/home/xtreamcodes/ffmpeg_build/include/nettle/ctr.h
/home/xtreamcodes/ffmpeg_build/include/nettle/curve25519.h
/home/xtreamcodes/ffmpeg_build/include/nettle/curve448.h
/home/xtreamcodes/ffmpeg_build/include/nettle/des.h
/home/xtreamcodes/ffmpeg_build/include/nettle/dsa-compat.h
/home/xtreamcodes/ffmpeg_build/include/nettle/dsa.h
/home/xtreamcodes/ffmpeg_build/include/nettle/eax.h
/home/xtreamcodes/ffmpeg_build/include/nettle/ecc-curve.h
/home/xtreamcodes/ffmpeg_build/include/nettle/ecc.h
/home/xtreamcodes/ffmpeg_build/include/nettle/ecdsa.h
/home/xtreamcodes/ffmpeg_build/include/nettle/eddsa.h
/home/xtreamcodes/ffmpeg_build/include/nettle/gcm.h
/home/xtreamcodes/ffmpeg_build/include/nettle/gostdsa.h
/home/xtreamcodes/ffmpeg_build/include/nettle/gosthash94.h
/home/xtreamcodes/ffmpeg_build/include/nettle/hkdf.h
/home/xtreamcodes/ffmpeg_build/include/nettle/hmac.h
/home/xtreamcodes/ffmpeg_build/include/nettle/knuth-lfib.h
/home/xtreamcodes/ffmpeg_build/include/nettle/macros.h
/home/xtreamcodes/ffmpeg_build/include/nettle/md2.h
/home/xtreamcodes/ffmpeg_build/include/nettle/md4.h
/home/xtreamcodes/ffmpeg_build/include/nettle/md5-compat.h
/home/xtreamcodes/ffmpeg_build/include/nettle/md5.h
/home/xtreamcodes/ffmpeg_build/include/nettle/memops.h
/home/xtreamcodes/ffmpeg_build/include/nettle/memxor.h
/home/xtreamcodes/ffmpeg_build/include/nettle/mini-gmp.h
/home/xtreamcodes/ffmpeg_build/include/nettle/nettle-meta.h
/home/xtreamcodes/ffmpeg_build/include/nettle/nettle-types.h
/home/xtreamcodes/ffmpeg_build/include/nettle/nist-keywrap.h
/home/xtreamcodes/ffmpeg_build/include/nettle/pbkdf2.h
/home/xtreamcodes/ffmpeg_build/include/nettle/pgp.h
/home/xtreamcodes/ffmpeg_build/include/nettle/pkcs1.h
/home/xtreamcodes/ffmpeg_build/include/nettle/poly1305.h
/home/xtreamcodes/ffmpeg_build/include/nettle/pss-mgf1.h
/home/xtreamcodes/ffmpeg_build/include/nettle/pss.h
/home/xtreamcodes/ffmpeg_build/include/nettle/realloc.h
/home/xtreamcodes/ffmpeg_build/include/nettle/ripemd160.h
/home/xtreamcodes/ffmpeg_build/include/nettle/rsa.h
/home/xtreamcodes/ffmpeg_build/include/nettle/salsa20.h
/home/xtreamcodes/ffmpeg_build/include/nettle/serpent.h
/home/xtreamcodes/ffmpeg_build/include/nettle/sexp.h
/home/xtreamcodes/ffmpeg_build/include/nettle/sha.h
/home/xtreamcodes/ffmpeg_build/include/nettle/sha1.h
/home/xtreamcodes/ffmpeg_build/include/nettle/sha2.h
/home/xtreamcodes/ffmpeg_build/include/nettle/sha3.h
/home/xtreamcodes/ffmpeg_build/include/nettle/siv-cmac.h
/home/xtreamcodes/ffmpeg_build/include/nettle/sm3.h
/home/xtreamcodes/ffmpeg_build/include/nettle/streebog.h
/home/xtreamcodes/ffmpeg_build/include/nettle/twofish.h
/home/xtreamcodes/ffmpeg_build/include/nettle/umac.h
/home/xtreamcodes/ffmpeg_build/include/nettle/version.h
/home/xtreamcodes/ffmpeg_build/include/nettle/xts.h
/home/xtreamcodes/ffmpeg_build/include/nettle/yarrow.h
/home/xtreamcodes/ffmpeg_build/lib64/libhogweed.a
/home/xtreamcodes/ffmpeg_build/lib64/libhogweed.so
/home/xtreamcodes/ffmpeg_build/lib64/libhogweed.so.6
/home/xtreamcodes/ffmpeg_build/lib64/libhogweed.so.6.6
/home/xtreamcodes/ffmpeg_build/lib64/libnettle.a
/home/xtreamcodes/ffmpeg_build/lib64/libnettle.so
/home/xtreamcodes/ffmpeg_build/lib64/libnettle.so.8
/home/xtreamcodes/ffmpeg_build/lib64/libnettle.so.8.6
/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig/hogweed.pc
/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig/nettle.pc

