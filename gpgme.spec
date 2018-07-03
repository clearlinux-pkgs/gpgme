#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x249B39D24F25E3B6 (dshaw@jabberwocky.com)
#
Name     : gpgme
Version  : 1.10.0
Release  : 19
URL      : ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-1.10.0.tar.bz2
Source0  : ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-1.10.0.tar.bz2
Source99 : ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-1.10.0.tar.bz2.sig
Summary  : GPGME - GnuPG Made Easy
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gpgme-bin
Requires: gpgme-python3
Requires: gpgme-lib
Requires: gpgme-data
Requires: gpgme-doc
Requires: gpgme-python
BuildRequires : gnupg
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : python3-dev
BuildRequires : swig

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG easier
for applications. It provides a High-Level Crypto API for encryption,
decryption, signing, signature verification and key management.

%package bin
Summary: bin components for the gpgme package.
Group: Binaries
Requires: gpgme-data

%description bin
bin components for the gpgme package.


%package data
Summary: data components for the gpgme package.
Group: Data

%description data
data components for the gpgme package.


%package dev
Summary: dev components for the gpgme package.
Group: Development
Requires: gpgme-lib
Requires: gpgme-bin
Requires: gpgme-data
Provides: gpgme-devel

%description dev
dev components for the gpgme package.


%package doc
Summary: doc components for the gpgme package.
Group: Documentation

%description doc
doc components for the gpgme package.


%package lib
Summary: lib components for the gpgme package.
Group: Libraries
Requires: gpgme-data

%description lib
lib components for the gpgme package.


%package python
Summary: python components for the gpgme package.
Group: Default
Requires: gpgme-python3

%description python
python components for the gpgme package.


%package python3
Summary: python3 components for the gpgme package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gpgme package.


%prep
%setup -q -n gpgme-1.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513279805
%configure --disable-static --disable-fd-passing --disable-gpgsm-test --enable-languages=cl,cpp,python3
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1513279805
rm -rf %{buildroot}
%make_install
## make_install_append content
cd lang/python
DESTDIR=%{buildroot} make install
rm -f %{buildroot}/usr/lib/python3.6/site-packages/gpg/install_files.txt
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/cmake/Gpgmepp/GpgmeppConfig.cmake
/usr/lib64/cmake/Gpgmepp/GpgmeppConfigVersion.cmake

%files bin
%defattr(-,root,root,-)
/usr/bin/gpgme-config
/usr/bin/gpgme-tool

%files data
%defattr(-,root,root,-)
/usr/share/common-lisp/source/gpgme/gpgme-package.lisp
/usr/share/common-lisp/source/gpgme/gpgme.asd
/usr/share/common-lisp/source/gpgme/gpgme.lisp

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/gpgme++/configuration.h
/usr/include/gpgme++/context.h
/usr/include/gpgme++/data.h
/usr/include/gpgme++/decryptionresult.h
/usr/include/gpgme++/defaultassuantransaction.h
/usr/include/gpgme++/editinteractor.h
/usr/include/gpgme++/encryptionresult.h
/usr/include/gpgme++/engineinfo.h
/usr/include/gpgme++/error.h
/usr/include/gpgme++/eventloopinteractor.h
/usr/include/gpgme++/exception.h
/usr/include/gpgme++/global.h
/usr/include/gpgme++/gpgadduserideditinteractor.h
/usr/include/gpgme++/gpgagentgetinfoassuantransaction.h
/usr/include/gpgme++/gpggencardkeyinteractor.h
/usr/include/gpgme++/gpgmefw.h
/usr/include/gpgme++/gpgmepp_export.h
/usr/include/gpgme++/gpgmepp_version.h
/usr/include/gpgme++/gpgsetexpirytimeeditinteractor.h
/usr/include/gpgme++/gpgsetownertrusteditinteractor.h
/usr/include/gpgme++/gpgsignkeyeditinteractor.h
/usr/include/gpgme++/importresult.h
/usr/include/gpgme++/interfaces/assuantransaction.h
/usr/include/gpgme++/interfaces/dataprovider.h
/usr/include/gpgme++/interfaces/passphraseprovider.h
/usr/include/gpgme++/interfaces/progressprovider.h
/usr/include/gpgme++/key.h
/usr/include/gpgme++/keygenerationresult.h
/usr/include/gpgme++/keylistresult.h
/usr/include/gpgme++/notation.h
/usr/include/gpgme++/result.h
/usr/include/gpgme++/scdgetinfoassuantransaction.h
/usr/include/gpgme++/signingresult.h
/usr/include/gpgme++/swdbresult.h
/usr/include/gpgme++/tofuinfo.h
/usr/include/gpgme++/trustitem.h
/usr/include/gpgme++/verificationresult.h
/usr/include/gpgme++/vfsmountresult.h
/usr/lib64/libgpgme.so
/usr/lib64/libgpgmepp.so
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgpgme.so.11
/usr/lib64/libgpgme.so.11.19.0
/usr/lib64/libgpgmepp.so.6
/usr/lib64/libgpgmepp.so.6.5.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
