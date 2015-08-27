syntax on
set tabstop=4
set shiftwidth=4
set expandtab
set backspace=2
" set colorcolumn=80

set autoindent
set number
set title
set hlsearch

set splitbelow
set splitright

set textwidth=0
set formatoptions-=cro

set fileformat=unix
set autoindent

map <C-J> <C-W>j
map <C-K> <C-W>k
map <C-H> <C-W>h
map <C-L> <C-W>l

" Use the below highlight group when displaying bad whitespace is desired.
highlight BadWhitespace ctermbg=red guibg=red

" Display tabs at the beginning of a line in Python mode as bad.
au BufRead,BufNewFile * match BadWhitespace /^\t\+/

" Make trailing whitespace be flagged as bad.
au BufRead,BufNewFile * match BadWhitespace /\s\+$/

" Remove trailing whitespace with 'Trim' command
command Trim %s/\s\+$//

