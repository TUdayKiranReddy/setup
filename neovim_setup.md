## Install packages
```
sudo apt install neovim ranger libxtst-dev libx11-dev python3-pynvim
```

## Installing vim-plug
```
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

curl -fLo ~/.config/nvim/init.vim --create-dirs https://raw.githubusercontent.com/gadepall/termux/main/neovim/init.vim
```

## Enter plugin
```
nvim ~/.config/nvim/init.vim       
:PlugInstall
:qa!
```

## For installing a plugin add the follwing lines in `~/.config/nvim/init.vim `
```
call plug#begin('~/.config/nvim/plugged') 
Plug 'lervag/vimtex' 
call plug#end()
```
To Install 
```
nvim
:PlugInstall
```

# Add the below configuration for vimTeX
```
" This is necessary for VimTeX to load properly. The "indent" is optional.
" Note that most plugin managers will do this automatically.
filetype plugin indent on

" This enables Vim's and neovim's syntax-related features. Without this, some
" VimTeX features will not work (see ":help vimtex-requirements" for more
" info).
syntax enable

" Viewer options: One may configure the viewer either by specifying a built-in
" viewer method:
let g:vimtex_view_method = 'zathura'

" Or with a generic interface:
let g:vimtex_view_general_viewer = 'okular'
let g:vimtex_view_general_options = '--unique file:@pdf\#src:@line@tex'

" VimTeX uses latexmk as the default compiler backend. If you use it, which is
" strongly recommended, you probably don't need to configure anything. If you
" want another compiler backend, you can change it as follows. The list of
" supported backends and further explanation is provided in the documentation,
" see ":help vimtex-compiler".
let g:vimtex_compiler_method = 'latexrun'

" Most VimTeX mappings rely on localleader and this can be changed with the
" following line. The default is usually fine and is the symbol "\".
let maplocalleader = ","
```
