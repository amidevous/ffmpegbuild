config_opts['chroot_setup_cmd'] = 'install @core wget nano'
config_opts['dist'] = 'el9'  # only useful for --resultdir variable subst
config_opts['releasever'] = '9'
config_opts['package_manager'] = 'dnf'
config_opts['extra_chroot_dirs'] = [ '/run/lock', ]

config_opts['bootstrap_image'] = 'quay.io/centos/centos:stream9'

config_opts['dnf.conf'] = """
[main]
keepcache=1
debuglevel=2
reposdir=/dev/null
logfile=/var/log/yum.log
retries=20
obsoletes=1
gpgcheck=0
assumeyes=1
syslog_ident=mock
syslog_device=
best=1
install_weak_deps=0
protected_packages=
module_platform_id=platform:el9
user_agent={{ user_agent }}

{% if koji_primary_repo != None and koji_primary_repo != "centos-stream" %}
[local-centos-stream]
{% else %}
[local]
{% endif %}
name=CentOS Stream $releasever - Koji Local - BUILDROOT ONLY!
baseurl=https://kojihub.stream.centos.org/kojifiles/repos/c{{ releasever }}s-build/latest/$basearch/
cost=2000
enabled=0
skip_if_unavailable=False

[baseos]
name=CentOS Stream $releasever - BaseOS
#baseurl=http://mirror.stream.centos.org/$releasever-stream/BaseOS/$basearch/os/
metalink=https://mirrors.centos.org/metalink?repo=centos-baseos-$releasever-stream&arch=$basearch
gpgkey=file:///usr/share/distribution-gpg-keys/centos/RPM-GPG-KEY-CentOS-Official
gpgcheck=1
enabled=1
skip_if_unavailable=False

[appstream]
name=CentOS Stream $releasever - AppStream
#baseurl=http://mirror.stream.centos.org/$releasever-stream/AppStream/$basearch/os/
metalink=https://mirrors.centos.org/metalink?repo=centos-appstream-$releasever-stream&arch=$basearch
gpgkey=file:///usr/share/distribution-gpg-keys/centos/RPM-GPG-KEY-CentOS-Official
gpgcheck=1
enabled=1
skip_if_unavailable=False

[crb]
name=CentOS Stream $releasever - CRB
#baseurl=http://mirror.stream.centos.org/$releasever-stream/CRB/$basearch/os/
metalink=https://mirrors.centos.org/metalink?repo=centos-crb-$releasever-stream&arch=$basearch
gpgkey=file:///usr/share/distribution-gpg-keys/centos/RPM-GPG-KEY-CentOS-Official
gpgcheck=1
enabled=1
skip_if_unavailable=False

[highavailability]
name=CentOS Stream $releasever - HighAvailability
#baseurl=http://mirror.stream.centos.org/$releasever-stream/HighAvailability/$basearch/os/
metalink=https://mirrors.centos.org/metalink?repo=centos-highavailability-$releasever-stream&arch=$basearch
gpgkey=file:///usr/share/distribution-gpg-keys/centos/RPM-GPG-KEY-CentOS-Official
gpgcheck=1
enabled=0

[nfv]
name=CentOS Stream $releasever - NFV
#baseurl=http://mirror.stream.centos.org/$releasever-stream/NFV/$basearch/os/
metalink=https://mirrors.centos.org/metalink?repo=centos-nfv-$releasever-stream&arch=$basearch
gpgkey=file:///usr/share/distribution-gpg-keys/centos/RPM-GPG-KEY-CentOS-Official
gpgcheck=1
enabled=0

[rt]
name=CentOS Stream $releasever - RT
#baseurl=http://mirror.stream.centos.org/$releasever-stream/RT/$basearch/os/
metalink=https://mirrors.centos.org/metalink?repo=centos-rt-$releasever-stream&arch=$basearch
gpgkey=file:///usr/share/distribution-gpg-keys/centos/RPM-GPG-KEY-CentOS-Official
gpgcheck=1
enabled=0

[resilientstorage]
name=CentOS Stream $releasever - ResilientStorage
#baseurl=http://mirror.stream.centos.org/$releasever-stream/ResilientStorage/$basearch/os/
metalink=https://mirrors.centos.org/metalink?repo=centos-resilientstorage-$releasever-stream&arch=$basearch
gpgkey=file:///usr/share/distribution-gpg-keys/centos/RPM-GPG-KEY-CentOS-Official
gpgcheck=1
enabled=0

[extras-common]
name=CentOS Stream $releasever - Extras packages
#baseurl=http://mirror.stream.centos.org/SIGs/$releasever-stream/extras/$basearch/extras-common/
metalink=https://mirrors.centos.org/metalink?repo=centos-extras-sig-extras-common-$releasever-stream&arch=$basearch
gpgkey=file:///usr/share/distribution-gpg-keys/centos/RPM-GPG-KEY-CentOS-SIG-Extras-SHA512
gpgcheck=1
enabled=1
skip_if_unavailable=False

[ffmpeg-local]
name=ffmpeg local
baseurl=file:///root/ffmpeg_package/CentOS-Stream/9/x86_64
gpgcheck=0
enabled=0
enabled_metadata=1
metadata_expire=1m

"""
