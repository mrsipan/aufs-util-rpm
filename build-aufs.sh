#!/bin/bash -vex

printf "build aufs3-standalone\n"
rm -rf aufs3-standalone
git clone git://git.code.sf.net/p/aufs/aufs3-standalone

cd aufs3-standalone
git checkout aufs3.10
git archive aufs3.10 --prefix='aufs3-standalone-3.10/' --format=tar | gzip -9 > ../aufs3-standalone-3.10.tar.gz
cd ..
rm -rf aufs3-standalone


printf "build aufs3 user space tools\n"
git clone git://git.code.sf.net/p/aufs/aufs-util
cd aufs-util
git checkout remotes/origin/aufs3.2

# should do it in the rpm spec file
#sed -i 's/\(.*LDFLAGS.*static.*\)/# \1/g' Makefile
git archive remotes/origin/aufs3.2 --prefix='aufs-util-3.2/' --format=tar | gzip -9 > ../aufs-util-3.2.tar.gz
cd ..
rm -rf aufs-util

rpmbuild -bs --nodeps --define "_sourcedir ." --define "_srcrpmdir ." aufs-util.spec
