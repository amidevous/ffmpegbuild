#!/bin/bash
#define version
opensslversion=3.0.7 gmpversion=6.2.1 nettleversion=3.8.1 libtasn1version=4.19.0 libffiversion=3.4.4 p11kitversion=0.24.1
libunistringversion=1.1 gnutlsversion=3.6.16 gnutlsversionmin=${gnutlsversion:0:3} nasmversion=2.16.01 yasmversion=1.3.0
x264version=$(date +%Y.%m) x265version=3.5 fdkaacversion=2.0.2 lameversion=3.100 opusversion=1.3.1 libvpxversion=1.12.0
libvpxcheckout=03265cd42b3783532de72f2ded5436652e6f5ce3 fribidiversion=1.0.12 harfbuzzversion=6.0.0 libassversion=0.17.0
rtmpdumpversion=2.3 theoraversion=1.1.1 liboggversion=1.3.5 vorbisversion=1.3.7 xvidversion=1.3.7
xavsversion=$(date +%Y.%m)

ffmpegversion=5.1.2
echo -e "\nChecking that minimal requirements are ok"
# Ensure the OS is compatible with the launcher
if [ -f /etc/centos-release ]; then
    inst() {
       rpm -q --queryformat '%{Version}-%{Release}' "$1"
    } 
    if (inst "centos-stream-repos"); then
    OS="CentOS-Stream"
    else
    OS="CentOs"
    fi    
    VERFULL=$(sed 's/^.*release //;s/ (Fin.*$//' /etc/centos-release) VER=${VERFULL:0:1} # return 6, 7, 8, 9 etc
elif [ -f /etc/fedora-release ]; then
    inst() {
       rpm -q --queryformat '%{Version}-%{Release}' "$1"
    } 
    OS="Fedora" VERFULL=$(sed 's/^.*release //;s/ (Fin.*$//' /etc/fedora-release) VER=${VERFULL:0:2} # return 34, 35, 36,37 etc
elif [ -f /etc/lsb-release ]; then
    OS=$(grep DISTRIB_ID /etc/lsb-release | sed 's/^.*=//') VER=$(grep DISTRIB_RELEASE /etc/lsb-release | sed 's/^.*=//')
	inst() {
       dpkg-query --showformat='${Version}' --show "$1"
    }
elif [ -f /etc/os-release ]; then
    OS=$(grep -w ID /etc/os-release | sed 's/^.*=//') VER=$(grep VERSION_ID /etc/os-release | sed 's/^.*"\(.*\)"/\1/' | head -n 1 | tail -n 1)
 else
    OS=$(uname -s) VER=$(uname -r)
fi
ARCH=$(uname -m)
echo "Detected : $OS  $VER  $ARCH"
# this part must be updated every 6 months
if [[ "$OS" = "CentOs" && "$VER" = "7" && "$ARCH" == "x86_64" || "$OS" = "CentOS-Stream" && "$VER" = "8" && "$ARCH" == "x86_64" ||
"$OS" = "Fedora" && "$VER" = "35" && "$ARCH" == "x86_64" ||
"$OS" = "Fedora" && "$VER" = "36" && "$ARCH" == "x86_64" || "$OS" = "Fedora" && "$VER" = "37" && "$ARCH" == "x86_64" ||
"$OS" = "Ubuntu" && "$VER" = "18.04" && "$ARCH" == "x86_64" || "$OS" = "Ubuntu" && "$VER" = "20.04" && "$ARCH" == "x86_64" ||
"$OS" = "Ubuntu" && "$VER" = "22.04" && "$ARCH" == "x86_64" || "$OS" = "debian" && "$VER" = "10" && "$ARCH" == "x86_64" ||
"$OS" = "debian" && "$VER" = "11" && "$ARCH" == "x86_64" ]] ; then
    echo "Ok."
else
    echo "Sorry, this OS is not supported."
	echo "This script is online for Linux x86_64 Stable Version"
	echo "Only aviable for :"
	echo "Centos Version 7 (LTS)"
	echo "CentOS Stream Version 8 (LTS)"
	echo "Fedora Version 35 (Old Stable)"
	echo "Fedora Version 36 (Stable)"
	echo "Fedora Version 37 (Next Stable)"
	echo "Ubuntu Version 18.04 (LTS)"
	echo "Ubuntu Version 20.04 (LTS)"
	echo "Ubuntu Version 22.04 (LTS)"
	echo "Debian 10 (Old Stable)"
	echo "Debian 11 (Stable)"
    exit 1
fi
# define Package Variable
if [[ "$OS" = "CentOs" ]] ; then
    PACKAGE_INSTALLER="yum -y install" PACKAGE_BININSTALLER="rpm -i" PACKAGE_REMOVER="yum -y remove"
    PACKAGE_UPDATER="yum -y update" PACKAGE_UPDGRADER="yum -y  upgrade" PACKAGE_UTILS="yum-utils"
    PACKAGE_GROUPINSTALL="yum -y groupinstall" PACKAGE_SOURCEDOWNLOAD="yumdownloader --source"
    PACKAGE_BUILDDEP="yum-builddep -y"
elif [[ "$OS" = "Fedora" || "$OS" = "CentOS-Stream"  ]]; then
    PACKAGE_INSTALLER="dnf -y install" PACKAGE_BININSTALLER="rpm -i" PACKAGE_REMOVER="dnf -y remove"
    PACKAGE_UPDATER="dnf -y update" PACKAGE_UPDGRADER="dnf -y upgrade" PACKAGE_UTILS="dnf-utils"
    PACKAGE_GROUPINSTALL="dnf -y groupinstall"PACKAGE_SOURCEDOWNLOAD="dnf download --source"
    PACKAGE_BUILDDEP="dnf build-dep -y"
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
    PACKAGE_INSTALLER="apt-get -y install" PACKAGE_BININSTALLER="dpkg -i" PACKAGE_REMOVER="apt-get -y purge"
	PACKAGE_UPDATER="apt-get -y update" PACKAGE_UPDGRADER="apt-get -y dist-upgrade" PACKAGE_SOURCEDOWNLOAD="apt-get -y source"
	PACKAGE_BUILDDEP="apt-get -y build-dep"
fi
# Define diference package name
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
# minimal build require
bzip2devel="bzip2-devel" freetypedevel="freetype-devel" cpp="gcc-c++" zlibdevel=zlib-devel gettext=gettext-devel
pkgconfig=pkgconfig repo=createrepo fontconfig=fontconfig-devel
# openssl 3 build dependencie
lksctptools=lksctp-tools-devel harness=perl-Test-Harness testsimple=perl-Test-Simple bigint=perl-Math-BigInt
complex=perl-Math-Complex localemaketext=perl-Locale-Maketext maketextsimple=perl-Locale-Maketext-Simple
corelist=perl-Module-CoreList moduleload="perl-Module-Load perl-Module-Load-Conditional" metadata=perl-Module-Metadata
perlversion=perl-version check=perl-Params-Check digest=perl-Digest sha=perl-Digest-SHA utils=perl-ExtUtils-MM-Utils
cmd=perl-IPC-Cmd bigrat=perl-Math-BigRat html=perl-Pod-Html hires=perl-Time-HiRes bignum=perl-bignum
rtmpdump=librtmp-devel
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
# minimal build require
bzip2devel="libbz2-dev" freetypedevel="libfreetype6-dev" cpp="g++ build-essential" zlibdevel=zlib1g-dev gettext=gettext
pkgconfig=pkg-config repo=reprepro fontconfig=libfontconfig1-dev
# openssl 3 build dependencie
lksctptools=lksctp-tools harness=libtest-harness-perl testsimple=libtest-simple-perl bigint=libmath-bigint-perl
complex=libmath-complex-perl localemaketext=liblocale-maketext-gettext-perl maketextsimple=liblocale-maketext-lexicon-perl
corelist=libmodule-corelist-perl moduleload=libmodule-load-conditional-perl metadata=libdist-metadata-perl
check=libparams-validate-perl perlversion=libperl-version-perl digest=libio-digest-perl sha=libdigest-sha-perl
utils=perl-modules-5.* cmd=libipc-run-perl
#pod bigrat include on perl-doc
bigrat=perl-doc
#pod htlm include on perl-doc
html= hires=libtime-hires-perl bignum=libcrypt-openssl-bignum-perl
rtmpdump=librtmp-dev
fi
# Install Require Package for Build
# For CentOS and CentOS Stream install epel
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" ]]; then
$PACKAGE_INSTALLER epel-release
$PACKAGE_INSTALLER --nogpgcheck https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-$(rpm -E %rhel).noarch.rpm https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-$(rpm -E %rhel).noarch.rpm
if [[ "$VER" = "8" ]]; then
dnf config-manager --enable powertools
fi
$PACKAGE_INSTALLER @fedora-packager
$PACKAGE_INSTALLER rpm-build
elif [[ "$OS" = "Fedora" ]]; then
$PACKAGE_INSTALLER --nogpgcheck https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
$PACKAGE_INSTALLER @fedora-packager
$PACKAGE_INSTALLER rpm-build
fi
$PACKAGE_UPDATER
$PACKAGE_UPDGRADER
$PACKAGE_INSTALLER autoconf
$PACKAGE_INSTALLER automake
$PACKAGE_INSTALLER $bzip2devel
$PACKAGE_INSTALLER cmake
$PACKAGE_INSTALLER $freetypedevel
$PACKAGE_INSTALLER gcc
$PACKAGE_INSTALLER $cpp
$PACKAGE_INSTALLER $freetypedevel
$PACKAGE_INSTALLER git
$PACKAGE_INSTALLER libtool
$PACKAGE_INSTALLER make
$PACKAGE_INSTALLER $pkgconfig
$PACKAGE_INSTALLER $zlibdevel
$PACKAGE_INSTALLER wget
$PACKAGE_INSTALLER curl
$PACKAGE_INSTALLER gpg
$PACKAGE_INSTALLER unzip
$PACKAGE_INSTALLER nano
$PACKAGE_INSTALLER doxygen
$PACKAGE_INSTALLER subversion
$PACKAGE_INSTALLER info
$PACKAGE_INSTALLER dash
$PACKAGE_INSTALLER $gettext
$PACKAGE_INSTALLER patch
$PACKAGE_INSTALLER m4
$PACKAGE_INSTALLER $lksctptools
$PACKAGE_INSTALLER $harness
$PACKAGE_INSTALLER ca-certificates
$PACKAGE_INSTALLER $testsimple
$PACKAGE_INSTALLER $bigint
$PACKAGE_INSTALLER $complex
$PACKAGE_INSTALLER $localemaketext
$PACKAGE_INSTALLER $maketextsimple
$PACKAGE_INSTALLER $corelist
$PACKAGE_INSTALLER $moduleload
$PACKAGE_INSTALLER $metadata
$PACKAGE_INSTALLER $check
$PACKAGE_INSTALLER $perlversion
$PACKAGE_INSTALLER $digest
$PACKAGE_INSTALLER $sha
$PACKAGE_INSTALLER $utils
$PACKAGE_INSTALLER $cmd
$PACKAGE_INSTALLER $bigrat
$PACKAGE_INSTALLER $html
$PACKAGE_INSTALLER $hires
$PACKAGE_INSTALLER $bignum
$PACKAGE_INSTALLER perl
$PACKAGE_INSTALLER $repo
$PACKAGE_INSTALLER $fontconfig
$PACKAGE_INSTALLER $rtmpdump
# podman repository for ubuntu
if [[ "$OS" = "Ubuntu" && ("$VER" = "18.04" || "$VER" = "20.04" ) ]] ; then
echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_${VER}/ /" | tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list
wget --no-check-certificate -qO- "https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_${VER}/Release.key" | gpg --dearmor | tee /etc/apt/trusted.gpg.d/devel_kubic_libcontainers_stable.gpg > /dev/null
fi
$PACKAGE_UPDATER
$PACKAGE_INSTALLER podman
testgcc=$(gcc --version | awk '/gcc/ && ($3+0)<8.0{print "no"}')
if [[ "testgcc" = "no" ]]; then
# update gcc to < 8.0
if [[ "$OS" = "CentOs" && "$VER" == "7"  ]]; then
$PACKAGE_UPDATER
$PACKAGE_INSTALLER centos-release-scl
$PACKAGE_UPDATER
$PACKAGE_INSTALLER devtoolset-8
source /opt/rh/devtoolset-8/enable
elif [[ "$OS" = "Ubuntu" && "$VER" == "18.04"  ]]; then
$PACKAGE_UPDATER
$PACKAGE_INSTALLER software-properties-common
add-apt-repository -y ppa:ubuntu-toolchain-r/test
$PACKAGE_UPDATER
$PACKAGE_INSTALLER gcc-8 g++-8
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 270
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 270
update-alternatives --install /usr/bin/cpp cpp /usr/bin/cpp-7 270
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 180
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-8 180
update-alternatives --install /usr/bin/cpp cpp /usr/bin/cpp-8 180
update-alternatives --set gcc /usr/bin/gcc-8
update-alternatives --set g++ /usr/bin/g++-8
update-alternatives --set cpp /usr/bin/cpp-8
fi
fi
export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"
export PATH="/root/ffmpeg_build/bin:$PATH"
export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"
# local repo create and install
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
pkgarch=x86_64
mkdir -p /root/ffmpeg_package/$OS/$VER/$ARCH/
cat > /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd <<EOF
#!/bin/bash
NAMERPM=\$(rpm -pq --queryformat "%{NAME}" \$1)
MINRPM=\${NAMERPM::1}
mkdir -p /root/ffmpeg_package/$OS/$VER/$ARCH/Packages/\$MINRPM
mv \$1 /root/ffmpeg_package/$OS/$VER/$ARCH/Packages/\$MINRPM
$PACKAGE_REMOVER /lib64/libldap.so.2
createrepo --update /root/ffmpeg_package/$OS/$VER/$ARCH
EOF
chmod +x /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd
mkdir -p /etc/yum.repos.d/
cat > /etc/yum.repos.d/ffmpeg-local.repo <<EOF
[ffmpeg-local]
name=ffmpeg local
baseurl=file:///root/ffmpeg_package/$OS/$VER/$ARCH
gpgcheck=0
enabled=1
enabled_metadata=1
metadata_expire=1m
EOF
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
pkgarch=amd64
mkdir -p /root/ffmpeg_package/$OS/
mkdir -p /root/ffmpeg_package/$OS/conf
mkdir -p /root/ffmpeg_package/$OS/incoming
cat > /root/ffmpeg_package/$OS/conf/distributions <<EOF
Origin: ffmpeg local
Label: ffmpeg local
Suite: $(lsb_release -sc)
Codename: $(lsb_release -sc)
Version: $VER
Architectures: amd64
Components: main
Description: local repo for ffmpeg build
EOF
mkdir -p /root/ffmpeg_package/$OS/$VER/$ARCH/
cat > /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd <<EOF
#!/bin/bash
reprepro -Vb /root/ffmpeg_package/$OS/ includedeb $(lsb_release -sc) \$1
cp /root/ffmpeg_package/Ubuntu/dists/$(lsb_release -sc)/Release /root/ffmpeg_package/Ubuntu/dists/$(lsb_release -sc)/InRelease
chown -R _apt:root /root/ffmpeg_package/$OS/
chown -R _apt:root /root/ffmpeg_package/$OS/*
chmod -R 700 /root/ffmpeg_package/$OS/
chmod -R 700 /root/ffmpeg_package/$OS/*
EOF
chmod +x /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd
cat > /etc/apt/sources.list.d/ffmpeg-local.list <<EOF
deb [trusted=yes] file:/root/ffmpeg_package/$OS $(lsb_release -sc) main
EOF
fi
$PACKAGE_INSTALLER checkinstall
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" ]]; then
dist=el$VER
pack=rpm
elif [[ "$OS" = "Fedora" ]]; then
dist=fc$VER
pack=rpm
elif [[ "$OS" = "Ubuntu" ]]; then
dist=Ubuntu-$(lsb_release -sc)
pack=debian
elif [[ "$OS" = "debian" ]]; then
dist=debian-$(lsb_release -sc)
pack=debian
fi
cd
rm -rf /root/bin/* /root/ffmpeg_sources
mkdir -p /root/ffmpeg_sources
cd /root/ffmpeg_sources
$PACKAGE_UPDATER
$PACKAGE_REMOVER xtream-ui-openssl3
rm -rf /root/ffmpeg_build/
$PACKAGE_INSTALLER xtream-ui-openssl3
if [[ $(inst  "xtream-ui-openssl3") != "$opensslversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/openssl-$opensslversion.tar.gz http://artfiles.org/openssl.org/source/openssl-$opensslversion.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-openssl3.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-openssl3.spec
sed -i "s|xtream-ui-openssl3version|$opensslversion|" "/root/rpmbuild/SPECS/xtream-ui-openssl3.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-openssl3.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-openssl3-$opensslversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-openssl3
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O openssl-$opensslversion.tar.gz http://artfiles.org/openssl.org/source/openssl-$opensslversion.tar.gz
tar -xvf openssl-$opensslversion.tar.gz
cd /root/ffmpeg_sources/openssl-$opensslversion
./Configure --prefix=/root/ffmpeg_build --openssldir=/root/ffmpeg_build/etc/pki/tls shared zlib
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=openssl \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$opensslversion \
    --pkgrelease=1.$dist \
    --pkgname=xtream-ui-openssl3 \
    -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-gmp
if [[ $(inst  "xtream-ui-gmp") != "$gmpversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/gmp-$gmpversion.tar.xz https://ftp.gnu.org/gnu/gmp/gmp-$gmpversion.tar.xz
wget -O /root/rpmbuild/SPECS/xtream-ui-gmp.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-gmp.spec
sed -i "s|xtream-ui-gmpversion|$gmpversion|" "/root/rpmbuild/SPECS/xtream-ui-gmp.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-gmp.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-gmp-$gmpversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-gmp
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O gmp-$gmpversion.tar.xz https://ftp.gnu.org/gnu/gmp/gmp-$gmpversion.tar.xz
tar xf gmp-$gmpversion.tar.xz
cd /root/ffmpeg_sources/gmp-$gmpversion
./configure --prefix=/root/ffmpeg_build --libdir=/root/ffmpeg_build/lib64 --enable-cxx --enable-fat
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=gmp \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$gmpversion \
    --pkgrelease=1.$dist \
    --pkgname=xtream-ui-gmp \
    --requires=xtream-ui-openssl3 -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-nettle
if [[ $(inst  "xtream-ui-nettle") != "$nettleversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/nettle-$nettleversion.tar.gz https://ftp.gnu.org/gnu/nettle/nettle-$nettleversion.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-nettle.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-nettle.spec
sed -i "s|xtream-ui-nettleversion|$nettleversion|" "/root/rpmbuild/SPECS/xtream-ui-nettle.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-nettle.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-nettle-$nettleversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-nettle
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O nettle-$nettleversion.tar.gz https://ftp.gnu.org/gnu/nettle/nettle-$nettleversion.tar.gz
tar xf nettle-$nettleversion.tar.gz
cd /root/ffmpeg_sources/nettle-$nettleversion
./configure --prefix=/root/ffmpeg_build --bindir=/root/ffmpeg_build/bin --sbindir=/root/ffmpeg_build/bin \
--libexecdir=/root/ffmpeg_build/libexec --sysconfdir=/root/ffmpeg_build/etc  --libdir=/root/ffmpeg_build/lib64 \
--includedir=/root/ffmpeg_build/include --with-include-path=/root/ffmpeg_build/include --with-lib-path=/root/ffmpeg_build/lib \
 --enable-mini-gmp
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=nettle \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$nettleversion \
    --pkgrelease=1.$dist \
    --pkgname=xtream-ui-nettle \
    --requires=xtream-ui-gmp -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-libtasn1
if [[ $(inst  "xtream-ui-libtasn1") != "$libtasn1version-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/libtasn1-$libtasn1version.tar.gz https://ftp.gnu.org/gnu/libtasn1/libtasn1-$libtasn1version.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-libtasn1.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-libtasn1.spec
sed -i "s|xtream-ui-libtasn1version|$libtasn1version|" "/root/rpmbuild/SPECS/xtream-ui-libtasn1.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-libtasn1.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-libtasn1-$libtasn1version-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-libtasn1
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O libtasn1-$libtasn1version.tar.gz https://ftp.gnu.org/gnu/libtasn1/libtasn1-$libtasn1version.tar.gz
tar xf libtasn1-$libtasn1version.tar.gz
cd /root/ffmpeg_sources/libtasn1-$libtasn1version
./configure --prefix=/root/ffmpeg_build --libdir=/root/ffmpeg_build/lib64
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=libtasn1 \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$libtasn1version \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-libtasn1 \
    --requires=xtream-ui-nettle -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-libffi
if [[ $(inst  "xtream-ui-libffi") != "$libffiversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/libffi-$libffiversion.tar.gz https://github.com/libffi/libffi/releases/download/v$libffiversion/libffi-$libffiversion.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-libffi.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-libffi.spec
sed -i "s|xtream-ui-libffiversion|$libffiversion|" "/root/rpmbuild/SPECS/xtream-ui-libffi.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-libffi.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-libffi-$libffiversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-libffi
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O libffi-$libffiversion.tar.gz https://github.com/libffi/libffi/releases/download/v$libffiversion/libffi-$libffiversion.tar.gz
tar xf libffi-$libffiversion.tar.gz
cd /root/ffmpeg_sources/libffi-$libffiversion
./configure --prefix=/root/ffmpeg_build --libdir=/root/ffmpeg_build/lib64 --disable-multi-os-directory
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=libffi \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$libffiversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-libffi \
    --requires=xtream-ui-libtasn1 -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-p11-kit
if [[ $(inst  "xtream-ui-p11-kit") != "$p11kitversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/p11-kit-$p11kitversion.tar.xz https://github.com/p11-glue/p11-kit/releases/download/$p11kitversion/p11-kit-$p11kitversion.tar.xz
wget -O /root/rpmbuild/SPECS/xtream-ui-p11-kit.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-p11-kit.spec
sed -i "s|xtream-ui-p11-kitversion|$p11kitversion|" "/root/rpmbuild/SPECS/xtream-ui-p11-kit.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-p11-kit.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-p11-kit-$p11kitversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-p11-kit
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O p11-kit-$p11kitversion.tar.xz https://github.com/p11-glue/p11-kit/releases/download/$p11kitversion/p11-kit-$p11kitversion.tar.xz
tar xf p11-kit-$p11kitversion.tar.xz
cd /root/ffmpeg_sources/p11-kit-$p11kitversion
./configure --prefix=/root/ffmpeg_build --libdir=/root/ffmpeg_build/lib64 --without-systemd --disable-nls
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=p11-kit \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$p11kitversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-p11-kit \
    --requires=xtream-ui-libffi -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-libunistring
if [[ $(inst  "xtream-ui-libunistring") != "$libunistringversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/libunistring-$libunistringversion.tar.xz https://ftp.gnu.org/gnu/libunistring/libunistring-$libunistringversion.tar.xz
wget -O /root/rpmbuild/SPECS/xtream-ui-libunistring.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-libunistring.spec
sed -i "s|xtream-ui-libunistringversion|$libunistringversion|" "/root/rpmbuild/SPECS/xtream-ui-libunistring.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-libunistring.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-libunistring-$libunistringversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-libunistring
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O libunistring-$libunistringversion.tar.xz https://ftp.gnu.org/gnu/libunistring/libunistring-$libunistringversion.tar.xz
tar -xvf libunistring-$libunistringversion.tar.xz
cd /root/ffmpeg_sources/libunistring-$libunistringversion
./configure --prefix=/root/ffmpeg_build --libdir=/root/ffmpeg_build/lib64
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=libunistring \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$libunistringversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-libunistring \
    --requires=xtream-ui-p11-kit -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-gnutls
if [[ $(inst  "xtream-ui-gnutls") != "$gnutlsversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/gnutls-$gnutlsversion.tar.xz https://www.gnupg.org/ftp/gcrypt/gnutls/v$gnutlsversionmin/gnutls-$gnutlsversion.tar.xz
wget -O /root/rpmbuild/SPECS/xtream-ui-gnutls.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-gnutls.spec
sed -i "s|xtream-ui-gnutlsversion|$gnutlsversion|" "/root/rpmbuild/SPECS/xtream-ui-gnutls.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-gnutls.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-gnutls-$gnutlsversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-gnutls
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O gnutls-$gnutlsversion.tar.xz https://www.gnupg.org/ftp/gcrypt/gnutls/v$gnutlsversionmin/gnutls-$gnutlsversion.tar.xz
tar -xvf gnutls-$gnutlsversion.tar.xz
cd /root/ffmpeg_sources/gnutls-$gnutlsversion
autoreconf -ifv
./configure --prefix=/root/ffmpeg_build --libdir=/root/ffmpeg_build/lib64 --disable-hardware-acceleration \
--disable-doc --disable-nls --disable-rpath
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=gnutls \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$gnutlsversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-gnutls \
    --requires=xtream-ui-libunistring -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-nasm
if [[ $(inst  "xtream-ui-nasm") != "$nasmversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/nasm-$nasmversion.tar.bz2 https://www.nasm.us/pub/nasm/releasebuilds/$nasmversion/nasm-$nasmversion.tar.bz2
wget -O /root/rpmbuild/SPECS/xtream-ui-nasm.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-nasm.spec
sed -i "s|xtream-ui-nasmversion|$nasmversion|" "/root/rpmbuild/SPECS/xtream-ui-nasm.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-nasm.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-nasm-$nasmversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-nasm
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O nasm-$nasmversion.tar.bz2 https://www.nasm.us/pub/nasm/releasebuilds/$nasmversion/nasm-$nasmversion.tar.bz2
tar xjvf nasm-$nasmversion.tar.bz2
cd /root/ffmpeg_sources/nasm-$nasmversion
./autogen.sh
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --bindir="/root/ffmpeg_build/bin"
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=nasm \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$nasmversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-nasm \
    --requires=xtream-ui-gnutls -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-yasm
if [[ $(inst  "xtream-ui-yasm") != "$yasmversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/yasm-$yasmversion.tar.gz https://www.tortall.net/projects/yasm/releases/yasm-$yasmversion.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-yasm.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-yasm.spec
sed -i "s|xtream-ui-yasmversion|$yasmversion|" "/root/rpmbuild/SPECS/xtream-ui-yasm.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-yasm.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-yasm-$yasmversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-yasm
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O yasm-$yasmversion.tar.gz https://www.tortall.net/projects/yasm/releases/yasm-$yasmversion.tar.gz
tar xzvf yasm-$yasmversion.tar.gz
cd /root/ffmpeg_sources/yasm-$yasmversion
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --bindir="/root/ffmpeg_build/bin"
make
checkinstall \
	--type=$pack \
    --pkgsource=yasm \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$yasmversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-yasm \
    --requires=xtream-ui-nasm -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-x264
if [[ $(inst  "xtream-ui-x264") != "$x264version-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/x264-stable.tar.gz https://code.videolan.org/videolan/x264/-/archive/stable/x264-stable.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-x264.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-x264.spec
sed -i "s|xtream-ui-x264version|$x264version|" "/root/rpmbuild/SPECS/xtream-ui-x264.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-x264.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-x264-$x264version-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-x264
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O x264-stable.tar.gz https://code.videolan.org/videolan/x264/-/archive/stable/x264-stable.tar.gz
tar -xvf x264-stable.tar.gz
cd /root/ffmpeg_sources/x264-stable
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --bindir="/root/ffmpeg_build/bin" --enable-static
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=x264 \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$x264version \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-x264 \
    --requires=xtream-ui-yasm -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-x265
if [[ $(inst  "xtream-ui-x265") != "$x265version-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/x265_$x265version.tar.gz https://bitbucket.org/multicoreware/x265_git/downloads/x265_$x265version.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-x265.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-x265.spec
sed -i "s|xtream-ui-x265version|$x265version|" "/root/rpmbuild/SPECS/xtream-ui-x265.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-x265.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-x265-$x265version-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-x265
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O x265_$x265version.tar.gz https://bitbucket.org/multicoreware/x265_git/downloads/x265_$x265version.tar.gz
tar -xvf x265_$x265version.tar.gz
cd /root/ffmpeg_sources/x265_$x265version/build/linux
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="/root/ffmpeg_build" -DLIB_INSTALL_DIR=lib64 -DENABLE_SHARED:bool=off ../../source
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=x265 \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$x265version \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-x265 \
    --requires=xtream-ui-x264 -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
if [ ! -f /root/ffmpeg_build/lib64/pkgconfig/x265.pc ]
then
mkdir -p /root/ffmpeg_build/lib64/pkgconfig/
cat > /root/ffmpeg_build/lib64/pkgconfig/x265.pc <<EOF
prefix=/root/ffmpeg_build
exec_prefix=\${prefix}
libdir=\${exec_prefix}/lib64
includedir=\${prefix}/include

Name: x265
Description: H.265/HEVC video encoder
Version: 3.5
Libs: -L\${libdir} -lx265
Libs.private: -lstdc++ -lm -lrt -ldl
Cflags: -I\${includedir}
EOF
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-fdk-aac
if [[ $(inst  "xtream-ui-fdk-aac") != "$fdkaacversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/fdk-aac-$fdkaacversion.tar.gz https://github.com/mstorsjo/fdk-aac/archive/refs/tags/v$fdkaacversion.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-fdk-aac.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-fdk-aac.spec
sed -i "s|xtream-ui-fdk-aacversion|$fdkaacversion|" "/root/rpmbuild/SPECS/xtream-ui-fdk-aac.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-fdk-aac.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-fdk-aac-$fdkaacversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-fdk-aac
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O fdk-aac-$fdkaacversion.tar.gz https://github.com/mstorsjo/fdk-aac/archive/refs/tags/v$fdkaacversion.tar.gz
tar -xvf fdk-aac-$fdkaacversion.tar.gz
cd /root/ffmpeg_sources/fdk-aac-$fdkaacversion
autoreconf -fiv
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --disable-shared
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=fdk-aac \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$fdkaacversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-fdk-aac \
    --requires=xtream-ui-x265 -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-lame
if [[ $(inst  "xtream-ui-lame") != "$lameversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/lame-$lameversion.tar.gz https://downloads.sourceforge.net/project/lame/lame/$lameversion/lame-$lameversion.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-lame.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-lame.spec
sed -i "s|xtream-ui-lameversion|$lameversion|" "/root/rpmbuild/SPECS/xtream-ui-lame.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-lame.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-lame-$lameversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-lame
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O lame-$lameversion.tar.gz https://downloads.sourceforge.net/project/lame/lame/$lameversion/lame-$lameversion.tar.gz
tar xzvf lame-$lameversion.tar.gz
cd /root/ffmpeg_sources/lame-$lameversion
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --bindir="/root/ffmpeg_build/bin" --disable-shared --enable-nasm
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=lame \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$lameversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-lame \
    --requires=xtream-ui-fdk-aac -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-opus
if [[ $(inst  "xtream-ui-opus") != "$opusversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/opus-$opusversion.tar.gz https://archive.mozilla.org/pub/opus/opus-$opusversion.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-opus.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-opus.spec
sed -i "s|xtream-ui-opusversion|$opusversion|" "/root/rpmbuild/SPECS/xtream-ui-opus.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-opus.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-opus-$opusversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-opus
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O opus-$opusversion.tar.gz https://archive.mozilla.org/pub/opus/opus-$opusversion.tar.gz
tar xzvf opus-$opusversion.tar.gz
cd /root/ffmpeg_sources/opus-$opusversion
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --disable-shared
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=opus \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$opusversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-opus \
    --requires=xtream-ui-lame -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-libvpx
if [[ $(inst  "xtream-ui-libvpx") != "$libvpxversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/libvpx-$libvpxversion.tar.gz https://chromium.googlesource.com/webm/libvpx/+archive/$libvpxcheckout.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-libvpx.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-libvpx.spec
sed -i "s|xtream-ui-libvpxversion|$libvpxversion|" "/root/rpmbuild/SPECS/xtream-ui-libvpx.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-libvpx.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-libvpx-$libvpxversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-libvpx
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O libvpx-$libvpxversion.tar.gz https://chromium.googlesource.com/webm/libvpx/+archive/$libvpxcheckout.tar.gz
mkdir -p /root/ffmpeg_sources/libvpx-$libvpxversion
cd /root/ffmpeg_sources/libvpx-$libvpxversion
tar -xvf ../libvpx-$libvpxversion.tar.gz
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 \
--disable-examples --disable-unit-tests --enable-vp9-highbitdepth --as=yasm
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=libvpx \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$libvpxversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-libvpx \
    --requires=xtream-ui-opus -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-fribidi
if [[ $(inst  "xtream-ui-fribidi") != "$fribidiversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/fribidi-$fribidiversion.tar.xz https://github.com/fribidi/fribidi/releases/download/v$fribidiversion/fribidi-$fribidiversion.tar.xz
wget -O /root/rpmbuild/SPECS/xtream-ui-fribidi.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-fribidi.spec
sed -i "s|xtream-ui-fribidiversion|$fribidiversion|" "/root/rpmbuild/SPECS/xtream-ui-fribidi.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-fribidi.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-fribidi-$fribidiversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-fribidi
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O fribidi-$fribidiversion.tar.xz https://github.com/fribidi/fribidi/releases/download/v$fribidiversion/fribidi-$fribidiversion.tar.xz
tar -xvf fribidi-$fribidiversion.tar.xz
cd /root/ffmpeg_sources/fribidi-$fribidiversion
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --enable-static
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=fribidi \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$fribidiversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-fribidi \
    --requires=xtream-ui-libvpx -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
# harfbuzz version 6.0.0 require gcc 8.0 or + or build not work
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-harfbuzz
if [[ $(inst  "xtream-ui-harfbuzz") != "$harfbuzzversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/harfbuzz-$harfbuzzversion.tar.xz https://github.com/harfbuzz/harfbuzz/releases/download/$harfbuzzversion/harfbuzz-$harfbuzzversion.tar.xz
wget -O /root/rpmbuild/SPECS/xtream-ui-harfbuzz.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-harfbuzz.spec
sed -i "s|xtream-ui-harfbuzzversion|$harfbuzzversion|" "/root/rpmbuild/SPECS/xtream-ui-harfbuzz.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-harfbuzz.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-harfbuzz-$harfbuzzversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-harfbuzz
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O harfbuzz-$harfbuzzversion.tar.xz https://github.com/harfbuzz/harfbuzz/releases/download/$harfbuzzversion/harfbuzz-$harfbuzzversion.tar.xz
tar -xvf harfbuzz-$harfbuzzversion.tar.xz
cd /root/ffmpeg_sources/harfbuzz-$harfbuzzversion
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --enable-static
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=harfbuzz \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$harfbuzzversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-harfbuzz \
    --requires=xtream-ui-fribidi -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-libass
if [[ $(inst  "xtream-ui-libass") != "$libassversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/libass-$libassversion.tar.gz https://github.com/libass/libass/releases/download/$libassversion/libass-$libassversion.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-libass.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-libass.spec
sed -i "s|xtream-ui-libassversion|$libassversion|" "/root/rpmbuild/SPECS/xtream-ui-libass.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-libass.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-libass-$libassversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-libass
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O libass-$libassversion.tar.gz https://github.com/libass/libass/releases/download/$libassversion/libass-$libassversion.tar.gz
tar -xvf libass-$libassversion.tar.gz
cd /root/ffmpeg_sources/libass-$libassversion
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --enable-static
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=libass \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$libassversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-libass \
    --requires=xtream-ui-harfbuzz -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-libogg
if [[ $(inst  "xtream-ui-libogg") != "$liboggversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/libogg-$liboggversion.tar.gz https://github.com/xiph/ogg/releases/download/v$liboggversion/libogg-$liboggversion.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-libogg.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-libogg.spec
sed -i "s|xtream-ui-liboggversion|$liboggversion|" "/root/rpmbuild/SPECS/xtream-ui-libogg.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-libogg.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-libogg-$liboggversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-libogg
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O libogg-$liboggversion.tar.gz https://github.com/xiph/ogg/releases/download/v$liboggversion/libogg-$liboggversion.tar.gz
tar -xvf libogg-$liboggversion.tar.gz
cd /root/ffmpeg_sources/libogg-$liboggversion
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --enable-static
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=libogg \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$liboggversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-libogg \
    --requires=xtream-ui-libass -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-theora
if [[ $(inst  "xtream-ui-theora") != "$theoraversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/theora-$theoraversion.tar.gz https://github.com/xiph/theora/archive/refs/tags/v$theoraversion.tar.gz
#patch: png_sizeof no longer available (since libpng 1.6)
wget -O /root/rpmbuild/SOURCES/theora.patch https://gitlab.xiph.org/xiph/theora/-/commit/7288b539c52e99168488dc3a343845c9365617c8.patch
wget -O /root/rpmbuild/SPECS/xtream-ui-theora.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-theora.spec
sed -i "s|xtream-ui-theoraversion|$theoraversion|" "/root/rpmbuild/SPECS/xtream-ui-theora.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-theora.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-theora-$theoraversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-theora
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O theora-$theoraversion.tar.gz https://github.com/xiph/theora/archive/refs/tags/v$theoraversion.tar.gz
tar -xvf theora-$theoraversion.tar.gz
cd /root/ffmpeg_sources/theora-$theoraversion
./autogen.sh
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --enable-static
#patch: png_sizeof no longer available (since libpng 1.6) 
wget -O theora.patch https://gitlab.xiph.org/xiph/theora/-/commit/7288b539c52e99168488dc3a343845c9365617c8.patch
patch -p1 < theora.patch
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=theora \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$theoraversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-theora \
    --requires=xtream-ui-libogg -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-vorbis
if [[ $(inst  "xtream-ui-vorbis") != "$vorbisversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/libvorbis-$vorbisversion.tar.gz https://github.com/xiph/vorbis/releases/download/v$vorbisversion/libvorbis-$vorbisversion.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-vorbis.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-vorbis.spec
sed -i "s|xtream-ui-vorbisversion|$vorbisversion|" "/root/rpmbuild/SPECS/xtream-ui-vorbis.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-vorbis.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-vorbis-$vorbisversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-vorbis
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O libvorbis-$vorbisversion.tar.gz https://github.com/xiph/vorbis/releases/download/v$vorbisversion/libvorbis-$vorbisversion.tar.gz
tar -xvf libvorbis-$vorbisversion.tar.gz
cd /root/ffmpeg_sources/libvorbis-$vorbisversion
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64 --enable-static
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=libvorbis \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$vorbisversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-vorbis \
    --requires=xtream-ui-theora -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-xvid
if [[ $(inst  "xtream-ui-xvid") != "$xvidversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
wget -O /root/rpmbuild/SOURCES/xvidcore-$xvidversion.tar.gz https://downloads.xvid.com/downloads/xvidcore-$xvidversion.tar.gz
wget -O /root/rpmbuild/SPECS/xtream-ui-xvid.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-xvid.spec
sed -i "s|xtream-ui-xvidversion|$xvidversion|" "/root/rpmbuild/SPECS/xtream-ui-xvid.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-xvid.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-xvid-$xvidversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-xvid
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
wget -O xvidcore-$xvidversion.tar.gz https://downloads.xvid.com/downloads/xvidcore-$xvidversion.tar.gz
tar -xvf xvidcore-$xvidversion.tar.gz
cd /root/ffmpeg_sources/xvidcore/build/generic
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=xvidcore \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$xvidversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-xvid \
    --requires=xtream-ui-vorbis -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
cd /root/ffmpeg_sources
rm -rf *
$PACKAGE_UPDATER
$PACKAGE_INSTALLER xtream-ui-xavs
if [[ $(inst  "xtream-ui-xavs") != "xavsversion-1.$dist" ]]; then
if [[ "$OS" = "CentOs" || "$OS" = "CentOS-Stream" || "$OS" = "Fedora" ]]; then
mkdir -p /root/rpmbuild/SPECS /root/rpmbuild/SOURCES
svn checkout https://svn.code.sf.net/p/xavs/code/trunk xavs-$xavsversion
tar -czvf /root/rpmbuild/SOURCES/xavs-$xavsversion.tar.gz xavs-$xavsversion
rm -rf xavs-$xavsversion
wget -O /root/rpmbuild/SPECS/xtream-ui-xavs.spec https://github.com/amidevous/ffmpegbuild/raw/main/SPECS/xtream-ui-xavs.spec
sed -i "s|xtream-ui-xavsversion|$xavsversion|" "/root/rpmbuild/SPECS/xtream-ui-xavs.spec"
rpmbuild -ba /root/rpmbuild/SPECS/xtream-ui-xavs.spec
/root/ffmpeg_package/$OS/$VER/$ARCH/repoadd /root/rpmbuild/RPMS/x86_64/xtream-ui-xavs-$xavsversion-1.$dist.x86_64.rpm
sleep 60
$PACKAGE_INSTALLER xtream-ui-xavs
elif [[ "$OS" = "Ubuntu" || "$OS" = "debian" ]]; then
svn checkout https://svn.code.sf.net/p/xavs/code/trunk xavs-$xavsversion
cd /root/ffmpeg_sources/xavs-$xavsversion
./configure --prefix="/root/ffmpeg_build" --libdir=/root/ffmpeg_build/lib64
make -j$(nproc --all)
checkinstall \
	--type=$pack \
    --pkgsource=xavs \
    --pkglicense=GPL3 \
    --deldesc=no \
    --nodoc \
    --maintainer=amidevous@gmail.com \
    --pkgarch=$pkgarch \
    --pkgversion=$xavsversion \
    --pkgrelease=1.$dist \
	--exclude=/root/ffmpeg_build/share/info/dir \
    --pkgname=xtream-ui-xavs \
    --requires=xtream-ui-xvid -y
find /root/ffmpeg_sources -name '*.deb' -exec /root/ffmpeg_package/$OS/$VER/$ARCH/repoadd {} \;
fi
fi
