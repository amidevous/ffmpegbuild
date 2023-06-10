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
Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: xtreamui-yasm
Version: xtream-ui-yasmversion
Release: 1%{?dist}
Source: https://www.tortall.net/projects/yasm/releases/yasm-%{version}.tar.gz
License: ASL 2.0
URL: https://gnu.org
BuildRequires: xtreamui-nasm
Requires: xtreamui-nasm
%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.
%prep
%autosetup -S git -n yasm-%{version}
%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
if test -f "/opt/rh/devtoolset-8/enable"; then
source /opt/rh/devtoolset-8/enable
fi
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --bindir="/root/ffmpeg_build/bin"
make %{?_smp_mflags}
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%make_install
rm -rf $RPM_BUILD_ROOT/root/ffmpeg_build/share/info/dir

%files
/root/ffmpeg_build/bin/vsyasm
/root/ffmpeg_build/bin/yasm
/root/ffmpeg_build/bin/ytasm
/root/ffmpeg_build/include/libyasm-stdint.h
/root/ffmpeg_build/include/libyasm.h
/root/ffmpeg_build/include/libyasm/arch.h
/root/ffmpeg_build/include/libyasm/assocdat.h
/root/ffmpeg_build/include/libyasm/bitvect.h
/root/ffmpeg_build/include/libyasm/bytecode.h
/root/ffmpeg_build/include/libyasm/compat-queue.h
/root/ffmpeg_build/include/libyasm/coretype.h
/root/ffmpeg_build/include/libyasm/dbgfmt.h
/root/ffmpeg_build/include/libyasm/errwarn.h
/root/ffmpeg_build/include/libyasm/expr.h
/root/ffmpeg_build/include/libyasm/file.h
/root/ffmpeg_build/include/libyasm/floatnum.h
/root/ffmpeg_build/include/libyasm/hamt.h
/root/ffmpeg_build/include/libyasm/insn.h
/root/ffmpeg_build/include/libyasm/intnum.h
/root/ffmpeg_build/include/libyasm/inttree.h
/root/ffmpeg_build/include/libyasm/linemap.h
/root/ffmpeg_build/include/libyasm/listfmt.h
/root/ffmpeg_build/include/libyasm/md5.h
/root/ffmpeg_build/include/libyasm/module.h
/root/ffmpeg_build/include/libyasm/objfmt.h
/root/ffmpeg_build/include/libyasm/parser.h
/root/ffmpeg_build/include/libyasm/phash.h
/root/ffmpeg_build/include/libyasm/preproc.h
/root/ffmpeg_build/include/libyasm/section.h
/root/ffmpeg_build/include/libyasm/symrec.h
/root/ffmpeg_build/include/libyasm/valparam.h
/root/ffmpeg_build/include/libyasm/value.h
/root/ffmpeg_build/lib64/libyasm.a
/root/ffmpeg_build/share/man/man1/yasm.1
/root/ffmpeg_build/share/man/man7/yasm_arch.7
/root/ffmpeg_build/share/man/man7/yasm_dbgfmts.7
/root/ffmpeg_build/share/man/man7/yasm_objfmts.7
/root/ffmpeg_build/share/man/man7/yasm_parsers.7

%changelog
* Thu Nov 24 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.7-2
- Various provider-related imrovements necessary for PKCS#11 provider correct operations
  Resolves: rhbz#2142517
