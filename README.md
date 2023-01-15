# ffmpegbuild

auto build use

`bash <(wget --no-check-certificate -qO- https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/ffmpeg-build.sh)`

just install depot and dependencie


`bash <(wget --no-check-certificate -qO- https://raw.githubusercontent.com/amidevous/ffmpegbuild/main/addrepo.sh)`

for build require gcc 8.0 or + build variable


`export LD_LIBRARY_PATH="/root/ffmpeg_build/lib64:$LD_LIBRARY_PATH"`

`export PATH="/root/ffmpeg_build/bin:$PATH"`

`export PKG_CONFIG_PATH="/root/ffmpeg_build/lib64/pkgconfig:$PKG_CONFIG_PATH"`

`export CFLAGS="$CFLAGS -I/root/ffmpeg_build/include -L/root/ffmpeg_build/lib64"`

build prefix

`./configure --prefix=/root/ffmpeg_build --bindir=/root/ffmpeg_build/bin --sbindir=/root/ffmpeg_build/bin \`

`--libexecdir=/root/ffmpeg_build/libexec --sysconfdir=/root/ffmpeg_build/etc  --libdir=/root/ffmpeg_build/lib64 \`

`--includedir=/root/ffmpeg_build/include`


actual version dependencie include

openssl version = 3.0.7

gmp version = 6.2.1

nettle version = 3.8.1

libtasn1 version = 4.19.0

libffi version = 3.4.4

p11kit version = 0.24.1

libunistring version = 1.1

gnutls version = 3.6.16

nasm version = 2.16.01

yasm version = 1.3.0

x264 date build = 2023-01

x265 version = 3.5

fdk aac version = 2.0.2

lame version = 3.100

opus version = 1.3.1

libvpx version = 1.12.0

fribidi version = 1.0.12

harfbuzz version = 6.0.0

libass version = 0.17.0

theora version = 1.1.1

libogg version = 1.3.5

vorbis version = 1.3.7

xvid version = 1.3.7

xavs date build = 2023-01
