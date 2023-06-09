%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-libtasn1
Version: 4.19.0
Release: 1%{?dist}
Source: https://ftp.gnu.org/gnu/libtasn1/libtasn1-%{version}.tar.gz
License: ASL 2.0
URL: https://gnu.org
%if 0%{?rhel} == 7
BuildRequires: devtoolset-8
%endif
BuildRequires: rpm-build gcc gcc-c++ gcc-gfortran gcc-objc gcc-objc++ libstdc++-devel gcc-gnat wget bzip2 gzip xz wget tar make pkgconfig patch
BuildRequires: xtream-ui-nettle
Requires: xtream-ui-nettle
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -n libtasn1-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/home/xtreamcodes/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/home/xtreamcodes/iptv_xtream_codes/bin:$PATH"
export PKG_CONFIG_PATH="/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/home/xtreamcodes/ffmpeg_build/include -L/home/xtreamcodes/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix=/home/xtreamcodes/ffmpeg_build --bindir=/home/xtreamcodes/iptv_xtream_codes/bin --libdir=/home/xtreamcodes/ffmpeg_build/lib64
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/home/xtreamcodes/ffmpeg_build/share/info/dir

%files
/home/xtreamcodes/iptv_xtream_codes/bin/asn1Coding
/home/xtreamcodes/iptv_xtream_codes/bin/asn1Decoding
/home/xtreamcodes/iptv_xtream_codes/bin/asn1Parser
/home/xtreamcodes/ffmpeg_build/include/libtasn1.h
/home/xtreamcodes/ffmpeg_build/lib64/libtasn1.a
/home/xtreamcodes/ffmpeg_build/lib64/libtasn1.la
/home/xtreamcodes/ffmpeg_build/lib64/libtasn1.so
/home/xtreamcodes/ffmpeg_build/lib64/libtasn1.so.6
/home/xtreamcodes/ffmpeg_build/lib64/libtasn1.so.6.6.3
/home/xtreamcodes/ffmpeg_build/lib64/pkgconfig/libtasn1.pc
/home/xtreamcodes/ffmpeg_build/share/info/libtasn1.info
/home/xtreamcodes/ffmpeg_build/share/man/man1/asn1Coding.1
/home/xtreamcodes/ffmpeg_build/share/man/man1/asn1Decoding.1
/home/xtreamcodes/ffmpeg_build/share/man/man1/asn1Parser.1
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_array2tree.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_bit_der.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_check_version.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_copy_node.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_create_element.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_decode_simple_ber.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_decode_simple_der.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_delete_element.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_delete_structure.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_delete_structure2.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_der_coding.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_der_decoding.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_der_decoding2.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_der_decoding_element.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_der_decoding_startEnd.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_dup_node.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_encode_simple_der.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_expand_any_defined_by.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_expand_octet_string.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_find_node.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_find_structure_from_oid.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_get_bit_der.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_get_length_ber.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_get_length_der.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_get_object_id_der.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_get_octet_der.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_get_tag_der.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_length_der.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_number_of_elements.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_object_id_der.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_octet_der.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_parser2array.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_parser2tree.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_perror.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_print_structure.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_read_node_value.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_read_tag.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_read_value.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_read_value_type.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_strerror.3
/home/xtreamcodes/ffmpeg_build/share/man/man3/asn1_write_value.3
