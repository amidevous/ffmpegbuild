%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-libtasn1
Version: xtream-ui-libtasn1version
Release: 1%{?dist}
Source: https://ftp.gnu.org/gnu/libtasn1/libtasn1-%{version}.tar.gz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-nettle
Requires: xtream-ui-nettle
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n libtasn1-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix=/root/ffmpeg_build --libdir=/root/ffmpeg_build/lib64
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir

%files
/root/ffmpeg_build/bin/asn1Coding
/root/ffmpeg_build/bin/asn1Decoding
/root/ffmpeg_build/bin/asn1Parser
/root/ffmpeg_build/include/libtasn1.h
/root/ffmpeg_build/lib64/libtasn1.a
/root/ffmpeg_build/lib64/libtasn1.la
/root/ffmpeg_build/lib64/libtasn1.so
/root/ffmpeg_build/lib64/libtasn1.so.6
/root/ffmpeg_build/lib64/libtasn1.so.6.6.3
/root/ffmpeg_build/lib64/pkgconfig/libtasn1.pc
/root/ffmpeg_build/share/info/libtasn1.info
/root/ffmpeg_build/share/man/man1/asn1Coding.1
/root/ffmpeg_build/share/man/man1/asn1Decoding.1
/root/ffmpeg_build/share/man/man1/asn1Parser.1
/root/ffmpeg_build/share/man/man3/asn1_array2tree.3
/root/ffmpeg_build/share/man/man3/asn1_bit_der.3
/root/ffmpeg_build/share/man/man3/asn1_check_version.3
/root/ffmpeg_build/share/man/man3/asn1_copy_node.3
/root/ffmpeg_build/share/man/man3/asn1_create_element.3
/root/ffmpeg_build/share/man/man3/asn1_decode_simple_ber.3
/root/ffmpeg_build/share/man/man3/asn1_decode_simple_der.3
/root/ffmpeg_build/share/man/man3/asn1_delete_element.3
/root/ffmpeg_build/share/man/man3/asn1_delete_structure.3
/root/ffmpeg_build/share/man/man3/asn1_delete_structure2.3
/root/ffmpeg_build/share/man/man3/asn1_der_coding.3
/root/ffmpeg_build/share/man/man3/asn1_der_decoding.3
/root/ffmpeg_build/share/man/man3/asn1_der_decoding2.3
/root/ffmpeg_build/share/man/man3/asn1_der_decoding_element.3
/root/ffmpeg_build/share/man/man3/asn1_der_decoding_startEnd.3
/root/ffmpeg_build/share/man/man3/asn1_dup_node.3
/root/ffmpeg_build/share/man/man3/asn1_encode_simple_der.3
/root/ffmpeg_build/share/man/man3/asn1_expand_any_defined_by.3
/root/ffmpeg_build/share/man/man3/asn1_expand_octet_string.3
/root/ffmpeg_build/share/man/man3/asn1_find_node.3
/root/ffmpeg_build/share/man/man3/asn1_find_structure_from_oid.3
/root/ffmpeg_build/share/man/man3/asn1_get_bit_der.3
/root/ffmpeg_build/share/man/man3/asn1_get_length_ber.3
/root/ffmpeg_build/share/man/man3/asn1_get_length_der.3
/root/ffmpeg_build/share/man/man3/asn1_get_object_id_der.3
/root/ffmpeg_build/share/man/man3/asn1_get_octet_der.3
/root/ffmpeg_build/share/man/man3/asn1_get_tag_der.3
/root/ffmpeg_build/share/man/man3/asn1_length_der.3
/root/ffmpeg_build/share/man/man3/asn1_number_of_elements.3
/root/ffmpeg_build/share/man/man3/asn1_object_id_der.3
/root/ffmpeg_build/share/man/man3/asn1_octet_der.3
/root/ffmpeg_build/share/man/man3/asn1_parser2array.3
/root/ffmpeg_build/share/man/man3/asn1_parser2tree.3
/root/ffmpeg_build/share/man/man3/asn1_perror.3
/root/ffmpeg_build/share/man/man3/asn1_print_structure.3
/root/ffmpeg_build/share/man/man3/asn1_read_node_value.3
/root/ffmpeg_build/share/man/man3/asn1_read_tag.3
/root/ffmpeg_build/share/man/man3/asn1_read_value.3
/root/ffmpeg_build/share/man/man3/asn1_read_value_type.3
/root/ffmpeg_build/share/man/man3/asn1_strerror.3
/root/ffmpeg_build/share/man/man3/asn1_write_value.3

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
