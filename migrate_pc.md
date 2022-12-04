# Steps for migrating PC
1. Make sure you update & upgrade packages in OLD_PC
2. Create packages list

OLD_PC: ``sudo dpkg --get-selections | sed "s/.*deinstall//" | sed "s/install$//g" > ~/pkglist``

and copy ``pkglist`` to NEW_PC

NEW_PC: ``sudo apt update && cat pkglist | xargs sudo apt install -y`` and ``sudo apt autoremove``

3. Copy ``/etc/apt/sources.list``, ``.bashrc``, ``.vimrc``, ``~/.ssh/``, ``mount_perceptron.sh``, ``dgx_host.sh``
