# Steps for migrating PC
1. Make sure you update & upgrade packages in OLD_PC
2. Create packages list
OLD_PC: ``sudo dpkg --get-selections | sed "s/.*deinstall//" | sed "s/install$//g" > ~/pkglist``
3. Copy ``/etc/apt/sources.list``, ``.bashrc``, ``.vimrc``, ``~/.ssh/``, ``mount_perceptron.sh``, ``dgx_host.sh``
