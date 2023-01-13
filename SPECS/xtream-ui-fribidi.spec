%global debug_package %{nil}
%define __arch_install_post %{nil}
%global __brp_check_rpaths %{nil}
%global __check_rpaths %{nil}
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtream-ui-fribidi
Version: xtream-ui-fribidiversion
Release: 1%{?dist}
Source: https://github.com/fribidi/fribidi/releases/download/v%{version}/fribidi-%{version}.tar.xz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtream-ui-libvpx
Requires: xtream-ui-libvpx
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n fribidi-%{version}
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

%files
/root/ffmpeg_build/bin/fribidi
/root/ffmpeg_build/include/fribidi/fribidi-arabic.h
/root/ffmpeg_build/include/fribidi/fribidi-begindecls.h
/root/ffmpeg_build/include/fribidi/fribidi-bidi-types-list.h
/root/ffmpeg_build/include/fribidi/fribidi-bidi-types.h
/root/ffmpeg_build/include/fribidi/fribidi-bidi.h
/root/ffmpeg_build/include/fribidi/fribidi-brackets.h
/root/ffmpeg_build/include/fribidi/fribidi-char-sets-list.h
/root/ffmpeg_build/include/fribidi/fribidi-char-sets.h
/root/ffmpeg_build/include/fribidi/fribidi-common.h
/root/ffmpeg_build/include/fribidi/fribidi-config.h
/root/ffmpeg_build/include/fribidi/fribidi-deprecated.h
/root/ffmpeg_build/include/fribidi/fribidi-enddecls.h
/root/ffmpeg_build/include/fribidi/fribidi-flags.h
/root/ffmpeg_build/include/fribidi/fribidi-joining-types-list.h
/root/ffmpeg_build/include/fribidi/fribidi-joining-types.h
/root/ffmpeg_build/include/fribidi/fribidi-joining.h
/root/ffmpeg_build/include/fribidi/fribidi-mirroring.h
/root/ffmpeg_build/include/fribidi/fribidi-shape.h
/root/ffmpeg_build/include/fribidi/fribidi-types.h
/root/ffmpeg_build/include/fribidi/fribidi-unicode-version.h
/root/ffmpeg_build/include/fribidi/fribidi-unicode.h
/root/ffmpeg_build/include/fribidi/fribidi.h
/root/ffmpeg_build/lib64/libfribidi.a
/root/ffmpeg_build/lib64/libfribidi.la
/root/ffmpeg_build/lib64/libfribidi.so
/root/ffmpeg_build/lib64/libfribidi.so.0
/root/ffmpeg_build/lib64/libfribidi.so.0.4.0
/root/ffmpeg_build/lib64/pkgconfig/fribidi.pc
/root/ffmpeg_build/share/man/man3/fribidi_charset_to_unicode.3
/root/ffmpeg_build/share/man/man3/fribidi_debug_status.3
/root/ffmpeg_build/share/man/man3/fribidi_get_bidi_type.3
/root/ffmpeg_build/share/man/man3/fribidi_get_bidi_type_name.3
/root/ffmpeg_build/share/man/man3/fribidi_get_bidi_types.3
/root/ffmpeg_build/share/man/man3/fribidi_get_bracket.3
/root/ffmpeg_build/share/man/man3/fribidi_get_bracket_types.3
/root/ffmpeg_build/share/man/man3/fribidi_get_joining_type.3
/root/ffmpeg_build/share/man/man3/fribidi_get_joining_type_name.3
/root/ffmpeg_build/share/man/man3/fribidi_get_joining_types.3
/root/ffmpeg_build/share/man/man3/fribidi_get_mirror_char.3
/root/ffmpeg_build/share/man/man3/fribidi_get_par_direction.3
/root/ffmpeg_build/share/man/man3/fribidi_get_par_embedding_levels.3
/root/ffmpeg_build/share/man/man3/fribidi_get_par_embedding_levels_ex.3
/root/ffmpeg_build/share/man/man3/fribidi_get_type.3
/root/ffmpeg_build/share/man/man3/fribidi_get_type_internal.3
/root/ffmpeg_build/share/man/man3/fribidi_join_arabic.3
/root/ffmpeg_build/share/man/man3/fribidi_log2vis.3
/root/ffmpeg_build/share/man/man3/fribidi_log2vis_get_embedding_levels.3
/root/ffmpeg_build/share/man/man3/fribidi_mirroring_status.3
/root/ffmpeg_build/share/man/man3/fribidi_parse_charset.3
/root/ffmpeg_build/share/man/man3/fribidi_remove_bidi_marks.3
/root/ffmpeg_build/share/man/man3/fribidi_reorder_line.3
/root/ffmpeg_build/share/man/man3/fribidi_reorder_nsm_status.3
/root/ffmpeg_build/share/man/man3/fribidi_set_debug.3
/root/ffmpeg_build/share/man/man3/fribidi_set_mirroring.3
/root/ffmpeg_build/share/man/man3/fribidi_set_reorder_nsm.3
/root/ffmpeg_build/share/man/man3/fribidi_shape.3
/root/ffmpeg_build/share/man/man3/fribidi_shape_arabic.3
/root/ffmpeg_build/share/man/man3/fribidi_shape_mirroring.3
/root/ffmpeg_build/share/man/man3/fribidi_unicode_to_charset.3

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
