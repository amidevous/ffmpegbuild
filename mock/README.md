Mock Build config

install mock and config

`yum -y install mock`

or

`dnf -y install mock`


`wget --no-check-certificate -O "/etc/mock/templates/centos-7.tpl" "https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/mock/templates/centos-7.tpl"`

`wget --no-check-certificate -O "/etc/mock/templates/centos-stream-8.tpl" "https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/mock/templates/centos-stream-8.tpl"`

`wget --no-check-certificate -O "/etc/mock/templates/centos-stream-9.tpl" "https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/mock/templates/centos-stream-9.tpl"`

`wget --no-check-certificate -O "/etc/mock/templates/fedora-branched.tpl" "https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/mock/templates/fedora-branched.tpl"`

`wget --no-check-certificate -O "/etc/mock/templates/rpmfusion-el.tpl" "https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/mock/templates/rpmfusion-el.tpl"`

`wget --no-check-certificate -O "/etc/mock/templates/rpmfusion-fc.tpl" "https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/mock/templates/rpmfusion-fc.tpl"`

`wget --no-check-certificate -O "/etc/mock/centos+epel-7+rpmfusion-x86_64.cfg" "https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/mock/centos+epel-7+rpmfusion-x86_64.cfg"`

`wget --no-check-certificate -O "/etc/mock/centos-stream+epel-8+rpmfusion-x86_64.cfg" "https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/mock/centos-stream+epel-8+rpmfusion-x86_64.cfg"`


`wget --no-check-certificate -O "/etc/mock/centos-stream+epel-9+rpmfusion-x86_64.cfg" "https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/mock/centos-stream+epel-9+rpmfusion-x86_64.cfg"`


`wget --no-check-certificate -O "/etc/mock/fedora-35+rpmfusion-x86_64.cfg" "https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/mock/fedora-35+rpmfusion-x86_64.cfg"`


`wget --no-check-certificate -O "/etc/mock/fedora-36+rpmfusion-x86_64.cfg" "https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/mock/fedora-36+rpmfusion-x86_64.cfg"`


`wget --no-check-certificate -O "/etc/mock/fedora-37+rpmfusion-x86_64.cfg" "https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/mock/fedora-37+rpmfusion-x86_64.cfg"`


example use for build on CentOS 7

`mock -r "/etc/mock/centos+epel-7+rpmfusion-x86_64.cfg" --clean`

`mock -r "/etc/mock/centos+epel-7+rpmfusion-x86_64.cfg" --init`

`mock -r "/etc/mock/centos+epel-7+rpmfusion-x86_64.cfg" --enable-network --shell`

`cd /root`

`export HOME=/root`

`bash <(wget --no-check-certificate -qO- https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/ffmpeg-build.sh)`
