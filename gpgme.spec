#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v4
# autospec commit: 3d985eb
#
# Source0 file verified with key 0x528897B826403ADA
#
Name     : gpgme
Version  : 1.23.1
Release  : 84
URL      : https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-1.23.1.tar.bz2
Source0  : https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-1.23.1.tar.bz2
Source1  : https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-1.23.1.tar.bz2.sig
Summary  : GPGME - GnuPG Made Easy
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 MIT
Requires: gpgme-bin = %{version}-%{release}
Requires: gpgme-data = %{version}-%{release}
Requires: gpgme-info = %{version}-%{release}
Requires: gpgme-lib = %{version}-%{release}
Requires: gpgme-license = %{version}-%{release}
Requires: gpgme-python = %{version}-%{release}
Requires: gpgme-python3 = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : buildreq-kde
BuildRequires : gnupg
BuildRequires : graphviz
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libgpg-error-extras
BuildRequires : pypi(setuptools)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : qtbase-dev
BuildRequires : swig
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0003-Hack-in-a-version-number-setuptools-allows.patch
Patch2: 0004-Enable-passing-extra-opts-to-setup.py.patch

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
Requires: gpgme = %{version}-%{release}

%description dev
dev components for the gpgme package.


%package extras
Summary: extras components for the gpgme package.
Group: Default

%description extras
extras components for the gpgme package.


%package info
Summary: info components for the gpgme package.
Group: Default

%description info
info components for the gpgme package.


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
%setup -q -n gpgme-1.23.1
cd %{_builddir}/gpgme-1.23.1
%patch -P 1 -p1
%patch -P 2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710428833
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure --disable-static --disable-fd-passing \
--disable-gpgsm-test \
--enable-languages=cl,cpp,python,qt6
make  %{?_smp_mflags}

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710428833
rm -rf %{buildroot}
## install_prepend content
export SETUPTOOLS_USE_DISTUTILS=local
export SETUP_PY_EXTRA_OPTS="--single-version-externally-managed --root=/"
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/gpgme
cp %{_builddir}/gpgme-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gpgme/dfac199a7539a404407098a2541b9482279f690d || :
cp %{_builddir}/gpgme-%{version}/COPYING.LESSER %{buildroot}/usr/share/package-licenses/gpgme/0bf81afbc585fd8fa3a9267d33498831f5a5c9c2 || :
cp %{_builddir}/gpgme-%{version}/LICENSES %{buildroot}/usr/share/package-licenses/gpgme/7f6d7039cb982a2acec77a9d337942283a3875a0 || :
export GOAMD64=v2
GOAMD64=v2
%make_install
## install_append content
touch abifiles.list
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
/usr/share/common-lisp/source/gpgme/gpgme-grovel.lisp
/usr/share/common-lisp/source/gpgme/gpgme-package.lisp
/usr/share/common-lisp/source/gpgme/gpgme.asd
/usr/share/common-lisp/source/gpgme/gpgme.lisp

%files dev
%defattr(-,root,root,-)
/usr/include/QGpgME/AbstractImportJob
/usr/include/QGpgME/AddExistingSubkeyJob
/usr/include/QGpgME/AddUserIDJob
/usr/include/QGpgME/ChangeExpiryJob
/usr/include/QGpgME/ChangeOwnerTrustJob
/usr/include/QGpgME/ChangePasswdJob
/usr/include/QGpgME/CryptoConfig
/usr/include/QGpgME/DN
/usr/include/QGpgME/DataProvider
/usr/include/QGpgME/Debug
/usr/include/QGpgME/DecryptJob
/usr/include/QGpgME/DecryptVerifyArchiveJob
/usr/include/QGpgME/DecryptVerifyJob
/usr/include/QGpgME/DefaultKeyGenerationJob
/usr/include/QGpgME/DeleteJob
/usr/include/QGpgME/DownloadJob
/usr/include/QGpgME/EncryptArchiveJob
/usr/include/QGpgME/EncryptJob
/usr/include/QGpgME/ExportJob
/usr/include/QGpgME/FileListDataProvider
/usr/include/QGpgME/GpgCardJob
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
/usr/include/QGpgME/ReceiveKeysJob
/usr/include/QGpgME/RefreshKeysJob
/usr/include/QGpgME/RevokeKeyJob
/usr/include/QGpgME/SetPrimaryUserIDJob
/usr/include/QGpgME/SignArchiveJob
/usr/include/QGpgME/SignEncryptArchiveJob
/usr/include/QGpgME/SignEncryptJob
/usr/include/QGpgME/SignJob
/usr/include/QGpgME/SignKeyJob
/usr/include/QGpgME/SpecialJob
/usr/include/QGpgME/TofuPolicyJob
/usr/include/QGpgME/VerifyDetachedJob
/usr/include/QGpgME/VerifyOpaqueJob
/usr/include/QGpgME/WKDLookupJob
/usr/include/QGpgME/WKDLookupResult
/usr/include/QGpgME/WKDRefreshJob
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
/usr/include/gpgme++/gpgaddexistingsubkeyeditinteractor.h
/usr/include/gpgme++/gpgadduserideditinteractor.h
/usr/include/gpgme++/gpgagentgetinfoassuantransaction.h
/usr/include/gpgme++/gpggencardkeyinteractor.h
/usr/include/gpgme++/gpgmefw.h
/usr/include/gpgme++/gpgmepp_export.h
/usr/include/gpgme++/gpgmepp_version.h
/usr/include/gpgme++/gpgrevokekeyeditinteractor.h
/usr/include/gpgme++/gpgsetexpirytimeeditinteractor.h
/usr/include/gpgme++/gpgsetownertrusteditinteractor.h
/usr/include/gpgme++/gpgsignkeyeditinteractor.h
/usr/include/gpgme++/importresult.h
/usr/include/gpgme++/interfaces/assuantransaction.h
/usr/include/gpgme++/interfaces/dataprovider.h
/usr/include/gpgme++/interfaces/passphraseprovider.h
/usr/include/gpgme++/interfaces/progressprovider.h
/usr/include/gpgme++/interfaces/statusconsumer.h
/usr/include/gpgme++/key.h
/usr/include/gpgme++/keygenerationresult.h
/usr/include/gpgme++/keylistresult.h
/usr/include/gpgme++/notation.h
/usr/include/gpgme++/result.h
/usr/include/gpgme++/scdgetinfoassuantransaction.h
/usr/include/gpgme++/signingresult.h
/usr/include/gpgme++/statusconsumerassuantransaction.h
/usr/include/gpgme++/swdbresult.h
/usr/include/gpgme++/tofuinfo.h
/usr/include/gpgme++/trustitem.h
/usr/include/gpgme++/verificationresult.h
/usr/include/gpgme++/vfsmountresult.h
/usr/include/gpgme.h
/usr/include/qgpgme/abstractimportjob.h
/usr/include/qgpgme/addexistingsubkeyjob.h
/usr/include/qgpgme/adduseridjob.h
/usr/include/qgpgme/changeexpiryjob.h
/usr/include/qgpgme/changeownertrustjob.h
/usr/include/qgpgme/changepasswdjob.h
/usr/include/qgpgme/cryptoconfig.h
/usr/include/qgpgme/dataprovider.h
/usr/include/qgpgme/debug.h
/usr/include/qgpgme/decryptjob.h
/usr/include/qgpgme/decryptverifyarchivejob.h
/usr/include/qgpgme/decryptverifyjob.h
/usr/include/qgpgme/defaultkeygenerationjob.h
/usr/include/qgpgme/deletejob.h
/usr/include/qgpgme/dn.h
/usr/include/qgpgme/downloadjob.h
/usr/include/qgpgme/encryptarchivejob.h
/usr/include/qgpgme/encryptjob.h
/usr/include/qgpgme/exportjob.h
/usr/include/qgpgme/filelistdataprovider.h
/usr/include/qgpgme/gpgcardjob.h
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
/usr/include/qgpgme/receivekeysjob.h
/usr/include/qgpgme/refreshkeysjob.h
/usr/include/qgpgme/revokekeyjob.h
/usr/include/qgpgme/setprimaryuseridjob.h
/usr/include/qgpgme/signarchivejob.h
/usr/include/qgpgme/signencryptarchivejob.h
/usr/include/qgpgme/signencryptjob.h
/usr/include/qgpgme/signjob.h
/usr/include/qgpgme/signkeyjob.h
/usr/include/qgpgme/specialjob.h
/usr/include/qgpgme/tofupolicyjob.h
/usr/include/qgpgme/verifydetachedjob.h
/usr/include/qgpgme/verifyopaquejob.h
/usr/include/qgpgme/wkdlookupjob.h
/usr/include/qgpgme/wkdlookupresult.h
/usr/include/qgpgme/wkdrefreshjob.h
/usr/include/qgpgme/wkspublishjob.h
/usr/lib64/cmake/Gpgmepp/GpgmeppConfig.cmake
/usr/lib64/cmake/Gpgmepp/GpgmeppConfigVersion.cmake
/usr/lib64/cmake/QGpgmeQt6/QGpgmeQt6Config.cmake
/usr/lib64/cmake/QGpgmeQt6/QGpgmeQt6ConfigVersion.cmake
/usr/lib64/libgpgme.so
/usr/lib64/libgpgmepp.so
/usr/lib64/libqgpgmeqt6.so
/usr/lib64/pkgconfig/gpgme-glib.pc
/usr/lib64/pkgconfig/gpgme.pc
/usr/share/aclocal/*.m4

%files extras
%defattr(-,root,root,-)
/usr/lib64/libqgpgmeqt6.so.15
/usr/lib64/libqgpgmeqt6.so.15.5.0

%files info
%defattr(0644,root,root,0755)
/usr/share/info/gpgme.info
/usr/share/info/gpgme.info-1
/usr/share/info/gpgme.info-2

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgpgme.so.11
/usr/lib64/libgpgme.so.11.32.0
/usr/lib64/libgpgmepp.so.6
/usr/lib64/libgpgmepp.so.6.20.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gpgme/0bf81afbc585fd8fa3a9267d33498831f5a5c9c2
/usr/share/package-licenses/gpgme/7f6d7039cb982a2acec77a9d337942283a3875a0
/usr/share/package-licenses/gpgme/dfac199a7539a404407098a2541b9482279f690d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
