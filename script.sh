#!/bin/bash

apt update
wget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.2.12.tar.xz
tar xvf linux-6.2.12.tar.xz
apt install -y gcc make bash binutils flex bison pahole util-linux kmod e2fsprogs jfsutils reiserfsprogs xfsprogs squashfs-tools btrfs-progs pcmciautils quota PPP nfs-common udev grub procps iptables openssl bc cpio
apt install -y libncurses-dev gawk libssl-dev dkms libelf-dev libudev-dev libpci-dev libiberty-dev autoconf llvm
systemctl daemon-reload
cd linux-6.2.12
scripts/config --disable SYSTEM_TRUSTED_KEYS
scripts/config --disable SYSTEM_REVOCATION_KEYS
cp /boot/config-5.15.0-71-generic ./.config
make oldconfig
make -j8 
make modules_install
make install

