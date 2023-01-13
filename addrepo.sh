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
"$OS" = "CentOS-Stream" && "$VER" = "9" && "$ARCH" == "x86_64" || "$OS" = "Fedora" && "$VER" = "35" && "$ARCH" == "x86_64" ||
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
	echo "CentOS Stream Version 9 (LTS)"
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
$PACKAGE_INSTALLER autoconf automake $bzip2devel cmake $freetypedevel gcc $cpp $freetypedevel git libtool make \
$pkgconfig $zlibdevel wget curl gpg unzip nano doxygen subversion info dash $gettext patch m4 $lksctptools $harness ca-certificates \
$testsimple $bigint $complex $localemaketext $maketextsimple $corelist $moduleload $metadata \
$check $perlversion $digest $sha $utils $cmd $bigrat $html $hires $bignum perl $repo $fontconfig $rtmpdump
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
$PACKAGE_INSTALLER xtream-ui-xavs
