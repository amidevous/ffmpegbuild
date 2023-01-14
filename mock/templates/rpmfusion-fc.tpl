config_opts['chroot_setup_cmd'] = 'install @core rpmfusion-free-release rpmfusion-nonfree-release'

config_opts['yum.conf'] += """

[rpmfusion-free]
name=RPM Fusion for Fedora $releasever - Free
baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/$basearch/os/
#metalink=https://mirrors.rpmfusion.org/metalink?repo=free-fedora-$releasever&arch=$basearch 
enabled=1
enabled_metadata=1
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///usr/share/distribution-gpg-keys/rpmfusion/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever

[rpmfusion-free-source]
name=RPM Fusion for Fedora $releasever - Free - Source 
baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/source/SRPMS/ 
#metalink=https://mirrors.rpmfusion.org/metalink?repo=free-fedora-source-$releasever&arch=$basearch
enabled=0
enabled_metadata=1
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///usr/share/distribution-gpg-keys/rpmfusion/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever

[rpmfusion-free-updates]
name=RPM Fusion for Fedora $releasever - Free - Updates
baseurl=http://download1.rpmfusion.org/free/fedora/updates/$releasever/$basearch/
#metalink=https://mirrors.rpmfusion.org/metalink?repo=free-fedora-updates-released-$releasever&arch=$basearch
enabled=1
enabled_metadata=1
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///usr/share/distribution-gpg-keys/rpmfusion/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever


[rpmfusion-free-updates-source]
name=RPM Fusion for Fedora $releasever - Free - Updates Source
baseurl=http://download1.rpmfusion.org/free/fedora/updates/$releasever/SRPMS/
#metalink=https://mirrors.rpmfusion.org/metalink?repo=free-fedora-updates-released-source-$releasever&arch=$basearch
enabled=0
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///usr/share/distribution-gpg-keys/rpmfusion/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever

[rpmfusion-nonfree]
name=RPM Fusion for Fedora $releasever - Nonfree
baseurl=http://download1.rpmfusion.org/nonfree/fedora/releases/$releasever/Everything/$basearch/os/
#metalink=https://mirrors.rpmfusion.org/metalink?repo=nonfree-fedora-$releasever&arch=$basearch
enabled=1
enabled_metadata=1
metadata_expire=14d
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///usr/share/distribution-gpg-keys/rpmfusion/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$releasever

[rpmfusion-nonfree-source]
name=RPM Fusion for Fedora $releasever - Nonfree - Source
baseurl=http://download1.rpmfusion.org/nonfree/fedora/releases/$releasever/Everything/source/SRPMS/
#metalink=https://mirrors.rpmfusion.org/metalink?repo=nonfree-fedora-source-$releasever&arch=$basearch
enabled=0
metadata_expire=7d
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///usr/share/distribution-gpg-keys/rpmfusion/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$releasever


[rpmfusion-nonfree-updates]
name=RPM Fusion for Fedora $releasever - Nonfree - Updates
baseurl=http://download1.rpmfusion.org/nonfree/fedora/updates/$releasever/$basearch/
#metalink=https://mirrors.rpmfusion.org/metalink?repo=nonfree-fedora-updates-released-$releasever&arch=$basearch
enabled=1
enabled_metadata=1
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///usr/share/distribution-gpg-keys/rpmfusion/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$releasever

[rpmfusion-nonfree-updates-source]
name=RPM Fusion for Fedora $releasever - Nonfree - Updates Source
baseurl=http://download1.rpmfusion.org/nonfree/fedora/updates/$releasever/SRPMS/
#metalink=https://mirrors.rpmfusion.org/metalink?repo=nonfree-fedora-updates-released-source-$releasever&arch=$basearch
enabled=0
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///usr/share/distribution-gpg-keys/rpmfusion/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$releasever


"""
