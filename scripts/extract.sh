#!/bin/bash

function extract {
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1        ;;
      *.tar.gz)    tar xzf $1     ;;
      *.bz2)       bunzip2 $1       ;;
      *.rar)       unrar e $1     ;;
      *.gz)        gunzip $1     ;;
      *.tar)       tar xf $1        ;;
      *.tbz2)      tar xjf $1      ;;
      *.tgz)       tar xzf $1       ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1  ;;
      *.7z)        7z x $1    ;;
      *)           echo "Arquivo não suportado" ;;
    esac
  else
    echo "$1 não é um arquivo válido"
  fi
}

echo "Escolha uma opção para extrair o arquivo:"
echo "1. tar.bz2"
echo "2. tar.gz"
echo "3. bz2"
echo "4. rar"
echo "5. gz"
echo "6. tar"
echo "7. tbz2"
echo "8. tgz"
echo "9. zip"
echo "10. Z"
echo "11. 7z"

read -p "Opção: " opt

case $opt in
  1) extract *.tar.bz2;;
  2) extract *.tar.gz;;
  3) extract *.bz2;;
  4) extract *.rar;;
  5) extract *.gz;;
  6) extract *.tar;;
  7) extract *.tbz2;;
  8) extract *.tgz;;
  9) extract *.zip;;
  10) extract *.Z;;
  11) extract *.7z;;
  *) echo "Opção inválida";;
esac
