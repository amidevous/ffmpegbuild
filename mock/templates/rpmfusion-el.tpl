config_opts['chroot_setup_cmd'] = 'install @core distribution-gpg-keys rpmfusion-free-release rpmfusion-nonfree-release'

config_opts['yum.conf'] += """

[rpmfusion-free-updates]
name=RPM Fusion for EL $releasever - Free - Updates
baseurl=http://download1.rpmfusion.org/free/el/updates/$releasever/$basearch/
#mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-el-updates-released-$releasever&arch=$basearch 
enabled=1
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/rpmfusion/RPM-GPG-KEY-rpmfusion-free-el-$releasever

[rpmfusion-free-updates-source]
name=RPM Fusion for EL $releasever - Free - Updates Source
baseurl=http://download1.rpmfusion.org/free/el/updates/$releasever/SRPMS/
#mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-el-updates-released-source-$releasever&arch=$basearch 
enabled=0
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/rpmfusion/RPM-GPG-KEY-rpmfusion-free-el-$releasever

[rpmfusion-nonfree-updates]
name=RPM Fusion for EL $releasever - Nonfree - Updates
baseurl=http://download1.rpmfusion.org/nonfree/el/updates/$releasever/$basearch/
#mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-el-updates-released-$releasever&arch=$basearch
enabled=1
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/rpmfusion/RPM-GPG-KEY-rpmfusion-nonfree-el-$releasever

[rpmfusion-nonfree-updates-source]
name=RPM Fusion for EL $releasever - Nonfree - Updates Source
baseurl=http://download1.rpmfusion.org/nonfree/el/updates/$releasever/SRPMS/
#mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-el-updates-released-source-$releasever&arch=$basearch
enabled=0
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/rpmfusion/RPM-GPG-KEY-rpmfusion-nonfree-el-$releasever

"""
