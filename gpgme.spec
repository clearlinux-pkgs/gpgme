#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x249B39D24F25E3B6
#
Name     : gpgme
Version  : 1.12.0
Release  : 29
URL      : https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-1.12.0.tar.bz2
Source0  : https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-1.12.0.tar.bz2
Source99 : https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-1.12.0.tar.bz2.sig
Summary  : GPGME - GnuPG Made Easy
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gpgme-bin
Requires: gpgme-python3
Requires: gpgme-lib
Requires: gpgme-data
Requires: gpgme-license
Requires: gpgme-python
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-kde
BuildRequires : doxygen
BuildRequires : gnupg
BuildRequires : graphviz
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : python3-dev
BuildRequires : qtbase-dev
BuildRequires : swig

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG easier
for applications. It provides a High-Level Crypto API for encryption,
decryption, signing, signature verification and key management.

%package bin
Summary: bin components for the gpgme package.
Group: Binaries
Requires: gpgme-data = %{version}-%{release}
Requires: gpgme-license = %{version}-%{release}

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
Requires: gpgme-lib = %{version}-%{release}
Requires: gpgme-bin = %{version}-%{release}
Requires: gpgme-data = %{version}-%{release}
Provides: gpgme-devel = %{version}-%{release}

%description dev
dev components for the gpgme package.


%package doc
Summary: doc components for the gpgme package.
Group: Documentation

%description doc
doc components for the gpgme package.


%package extras
Summary: extras components for the gpgme package.
Group: Default

%description extras
extras components for the gpgme package.


%package lib
Summary: lib components for the gpgme package.
Group: Libraries
Requires: gpgme-data = %{version}-%{release}
Requires: gpgme-license = %{version}-%{release}

%description lib
lib components for the gpgme package.


%package license
Summary: license components for the gpgme package.
Group: Default

%description license
license components for the gpgme package.


%package python
Summary: python components for the gpgme package.
Group: Default
Requires: gpgme-python3 = %{version}-%{release}

%description python
python components for the gpgme package.


%package python3
Summary: python3 components for the gpgme package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gpgme package.


%prep
%setup -q -n gpgme-1.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539053149
%configure --disable-static --disable-fd-passing --disable-gpgsm-test --enable-languages=cl,cpp,python3,qt
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1539053149
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/gpgme
cp COPYING %{buildroot}/usr/share/doc/gpgme/COPYING
cp COPYING.LESSER %{buildroot}/usr/share/doc/gpgme/COPYING.LESSER
%make_install
## install_append content
cd lang/python
DESTDIR=%{buildroot} make install
rm -f %{buildroot}/usr/lib/python3.6/site-packages/gpg/install_files.txt
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gpgme-config
/usr/bin/gpgme-json
/usr/bin/gpgme-tool

%files data
%defattr(-,root,root,-)
/usr/share/common-lisp/source/gpgme/gpgme-package.lisp
/usr/share/common-lisp/source/gpgme/gpgme.asd
/usr/share/common-lisp/source/gpgme/gpgme.lisp

%files dev
%defattr(-,root,root,-)
%exclude /usr/lib64/libqgpgme.so
/usr/include/*.h
/usr/include/QGpgME/AbstractImportJob
/usr/include/QGpgME/AddUserIDJob
/usr/include/QGpgME/ChangeExpiryJob
/usr/include/QGpgME/ChangeOwnerTrustJob
/usr/include/QGpgME/ChangePasswdJob
/usr/include/QGpgME/CryptoConfig
/usr/include/QGpgME/DN
/usr/include/QGpgME/DataProvider
/usr/include/QGpgME/DecryptJob
/usr/include/QGpgME/DecryptVerifyJob
/usr/include/QGpgME/DefaultKeyGenerationJob
/usr/include/QGpgME/DeleteJob
/usr/include/QGpgME/DownloadJob
/usr/include/QGpgME/EncryptJob
/usr/include/QGpgME/ExportJob
/usr/include/QGpgME/HierarchicalKeyKistJob
/usr/include/QGpgME/ImportFromKeyserverJob
/usr/include/QGpgME/ImportJob
/usr/include/QGpgME/Job
/usr/include/QGpgME/KeyForMailboxJob
/usr/include/QGpgME/KeyGenerationJob
/usr/include/QGpgME/KeyListJob
/usr/include/QGpgME/ListAllKeysJob
/usr/include/QGpgME/MultiDeleteJob
/usr/include/QGpgME/Protocol
/usr/include/QGpgME/QGpgMENewCryptoConfig
/usr/include/QGpgME/QuickJob
/usr/include/QGpgME/RefreshKeysJob
/usr/include/QGpgME/SignEncryptJob
/usr/include/QGpgME/SignJob
/usr/include/QGpgME/SignKeyJob
/usr/include/QGpgME/SpecialJob
/usr/include/QGpgME/TofuPolicyJob
/usr/include/QGpgME/VerifyDetachedJob
/usr/include/QGpgME/VerifyOpaqueJob
/usr/include/QGpgME/WKSPublishJob
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
/usr/include/qgpgme/abstractimportjob.h
/usr/include/qgpgme/adduseridjob.h
/usr/include/qgpgme/changeexpiryjob.h
/usr/include/qgpgme/changeownertrustjob.h
/usr/include/qgpgme/changepasswdjob.h
/usr/include/qgpgme/cryptoconfig.h
/usr/include/qgpgme/dataprovider.h
/usr/include/qgpgme/decryptjob.h
/usr/include/qgpgme/decryptverifyjob.h
/usr/include/qgpgme/defaultkeygenerationjob.h
/usr/include/qgpgme/deletejob.h
/usr/include/qgpgme/dn.h
/usr/include/qgpgme/downloadjob.h
/usr/include/qgpgme/encryptjob.h
/usr/include/qgpgme/exportjob.h
/usr/include/qgpgme/hierarchicalkeylistjob.h
/usr/include/qgpgme/importfromkeyserverjob.h
/usr/include/qgpgme/importjob.h
/usr/include/qgpgme/job.h
/usr/include/qgpgme/keyformailboxjob.h
/usr/include/qgpgme/keygenerationjob.h
/usr/include/qgpgme/keylistjob.h
/usr/include/qgpgme/listallkeysjob.h
/usr/include/qgpgme/multideletejob.h
/usr/include/qgpgme/protocol.h
/usr/include/qgpgme/qgpgme_export.h
/usr/include/qgpgme/qgpgme_version.h
/usr/include/qgpgme/qgpgmenewcryptoconfig.h
/usr/include/qgpgme/quickjob.h
/usr/include/qgpgme/refreshkeysjob.h
/usr/include/qgpgme/signencryptjob.h
/usr/include/qgpgme/signjob.h
/usr/include/qgpgme/signkeyjob.h
/usr/include/qgpgme/specialjob.h
/usr/include/qgpgme/tofupolicyjob.h
/usr/include/qgpgme/verifydetachedjob.h
/usr/include/qgpgme/verifyopaquejob.h
/usr/include/qgpgme/wkspublishjob.h
/usr/lib64/cmake/Gpgmepp/GpgmeppConfig.cmake
/usr/lib64/cmake/Gpgmepp/GpgmeppConfigVersion.cmake
/usr/lib64/cmake/QGpgme/QGpgmeConfig.cmake
/usr/lib64/cmake/QGpgme/QGpgmeConfigVersion.cmake
/usr/lib64/libgpgme.so
/usr/lib64/libgpgmepp.so
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

%files extras
%defattr(-,root,root,-)
/usr/lib64/libqgpgme.so
/usr/lib64/libqgpgme.so.7
/usr/lib64/libqgpgme.so.7.3.2

%files lib
%defattr(-,root,root,-)
%exclude /usr/lib64/libqgpgme.so.7
%exclude /usr/lib64/libqgpgme.so.7.3.2
/usr/lib64/libgpgme.so.11
/usr/lib64/libgpgme.so.11.21.0
/usr/lib64/libgpgmepp.so.6
/usr/lib64/libgpgmepp.so.6.8.0

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/gpgme/COPYING
/usr/share/doc/gpgme/COPYING.LESSER

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
