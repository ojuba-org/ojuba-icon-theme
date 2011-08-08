#! /bin/bash

for t in ojuba-crystal Ojuba;do
  pushd $t
  for i in 16 22 24 32 36 48;do
    mkdir ${i}x${i}
    # render png files
    for f in $(find scalable/ -type f -iname '*.svg');do
      p=${f/.svg/.png}
      p=${p/scalable/${i}x${i}}
      mkdir -p $(dirname $p)
      convert -background none -resize ${i}x${i} $f $p
    done
    # create links
    for f in $(find scalable/ -type l -iname '*.svg');do
      p=${f/.svg/.png}
      p=${p/scalable/${i}x${i}}
      fl=$(readlink $f)
      pl=${fl/.svg/.png}
      pl=${pl/scalable/${i}x${i}} # just to be sure
      mkdir -p $(dirname $p)
      ln -s $pl $p
    done
  done
  popd
done



