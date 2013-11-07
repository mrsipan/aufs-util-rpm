Name: aufs-util		
Version: 3.2
Release:	1%{?dist}
Summary: user tools for aufs file system	

AutoReqProv: no

Group: Applications/Internet
License: GPL
URL: http://aufs.sourceforge.net		
Source0: aufs-util-3.2.tar.gz	
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: gcc-c++	
#Requires:	hi

%description
user tools for aufs


%prep
%setup


%build
#make %{?_smp_mflags}
sed -i 's/\(.*static.*\)/# \1/g' Makefile
sed -i 's/\(Install = install\).*/\1/g' Makefile
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/etc/default/aufs
/sbin/auibusy
/sbin/auplink
/sbin/mount.aufs
/sbin/umount.aufs
/usr/bin/aubrsync
/usr/bin/aubusy
/usr/bin/auchk
/usr/lib/libau.so
/usr/lib/libau.so.2
/usr/lib/libau.so.2.7
/usr/share/man/man5/aufs.5.gz


%changelog
* Mon Nov 07 2013 Ben Sanchez - 3.2-1
- initial rpm
