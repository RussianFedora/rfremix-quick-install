#!/bin/sh
NR=$(rpm -q --specfile *.spec --qf "%{name}-%{version}")

rm -rf $NR
cp -r rfremix-quick-install $NR
tar cjf $NR.tar.bz2 $NR --exclude=.git
rm -rf $NR
