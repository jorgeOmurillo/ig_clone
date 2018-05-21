let SessionLoad = 1
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/ig_clone
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +30 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/ig_clone/settings.py
badd +2933 term://.//27933:zsh\ \#\ django\ server\ console
badd +150 term://.//29248:zsh\ \#\ terminal\ console
badd +1 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/feed/templates/feed/profile_settings.html
badd +37 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/feed/templates/feed/follow_list.html
badd +9 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/feed/templates/feed/explore.html
badd +33 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/feed/templates/feed/profile.html
badd +11 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/feed/templates/feed/home.html
badd +38 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/templates/header.html
badd +4 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/templates/footer.html
badd +3 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/templates/base.html
badd +19 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/static/js/index.js
badd +1 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/static/css/strap.css
badd +29 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/feed/views.py
badd +12 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/feed/urls.py
badd +53 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/feed/models.py
badd +26 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/ig_clone/urls.py
badd +4 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/static/js/jquery-3.1.0.min.js
badd +23 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/static/js/ajax-csrf-auth.js
badd +9 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/templates/registration/login.html
badd +4 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/feed/templatetags/custom_tags.py
badd +1 ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/media/profile_pics/IMG_3563.JPG
argglobal
silent! argdel *
$argadd settings.py
edit ~/Dropbox/Code/Python/Django/ig_clone/ig_clone/static/css/strap.css
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd t
set winminheight=1 winminwidth=1 winheight=1 winwidth=1
exe '1resize ' . ((&lines * 29 + 20) / 41)
exe '2resize ' . ((&lines * 9 + 20) / 41)
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 89 - ((0 * winheight(0) + 14) / 29)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
89
normal! 07|
lcd ~/Dropbox/Code/Python/Django/ig_clone/ig_clone
wincmd w
argglobal
if bufexists('term://.//27933:zsh\ \#\ django\ server\ console') | buffer term://.//27933:zsh\ \#\ django\ server\ console | else | edit term://.//27933:zsh\ \#\ django\ server\ console | endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 9881 - ((8 * winheight(0) + 4) / 9)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
9881
normal! 0
lcd ~/Dropbox/Code/Python/Django/ig_clone/ig_clone
wincmd w
exe '1resize ' . ((&lines * 29 + 20) / 41)
exe '2resize ' . ((&lines * 9 + 20) / 41)
tabnext 1
if exists('s:wipebuf') && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 winminheight=1 winminwidth=1 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
