#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: e738c51
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kcompletion
Version  : 6.0.0
Release  : 75
URL      : https://download.kde.org/stable/frameworks/6.0/kcompletion-6.0.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.0/kcompletion-6.0.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.0/kcompletion-6.0.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1
Requires: kcompletion-data = %{version}-%{release}
Requires: kcompletion-lib = %{version}-%{release}
Requires: kcompletion-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KCompletion
Powerful completion framework, including completion-enabled lineedit and combobox.

%package data
Summary: data components for the kcompletion package.
Group: Data

%description data
data components for the kcompletion package.


%package dev
Summary: dev components for the kcompletion package.
Group: Development
Requires: kcompletion-lib = %{version}-%{release}
Requires: kcompletion-data = %{version}-%{release}
Provides: kcompletion-devel = %{version}-%{release}
Requires: kcompletion = %{version}-%{release}

%description dev
dev components for the kcompletion package.


%package lib
Summary: lib components for the kcompletion package.
Group: Libraries
Requires: kcompletion-data = %{version}-%{release}
Requires: kcompletion-license = %{version}-%{release}

%description lib
lib components for the kcompletion package.


%package license
Summary: license components for the kcompletion package.
Group: Default

%description license
license components for the kcompletion package.


%prep
%setup -q -n kcompletion-6.0.0
cd %{_builddir}/kcompletion-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709233228
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1709233228
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcompletion
cp %{_builddir}/kcompletion-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcompletion/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kcompletion-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcompletion/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kcompletion-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcompletion/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kcompletion-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kcompletion/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/as/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ast/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/az/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/be/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/br/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/da/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/de/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/el/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/es/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/et/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/he/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/id/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/is/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/it/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/km/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/or/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/sa/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/se/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/si/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/te/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/th/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kcompletion6_qt.qm
/usr/share/qlogging-categories6/kcompletion.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KCompletion/KComboBox
/usr/include/KF6/KCompletion/KCompletion
/usr/include/KF6/KCompletion/KCompletionBase
/usr/include/KF6/KCompletion/KCompletionBox
/usr/include/KF6/KCompletion/KCompletionMatches
/usr/include/KF6/KCompletion/KEmailValidator
/usr/include/KF6/KCompletion/KHistoryComboBox
/usr/include/KF6/KCompletion/KLineEdit
/usr/include/KF6/KCompletion/KSortableList
/usr/include/KF6/KCompletion/kcombobox.h
/usr/include/KF6/KCompletion/kcompletion.h
/usr/include/KF6/KCompletion/kcompletion_export.h
/usr/include/KF6/KCompletion/kcompletion_version.h
/usr/include/KF6/KCompletion/kcompletionbase.h
/usr/include/KF6/KCompletion/kcompletionbox.h
/usr/include/KF6/KCompletion/kcompletionmatches.h
/usr/include/KF6/KCompletion/kemailvalidator.h
/usr/include/KF6/KCompletion/khistorycombobox.h
/usr/include/KF6/KCompletion/klineedit.h
/usr/include/KF6/KCompletion/ksortablelist.h
/usr/lib64/cmake/KF6Completion/KF6CompletionConfig.cmake
/usr/lib64/cmake/KF6Completion/KF6CompletionConfigVersion.cmake
/usr/lib64/cmake/KF6Completion/KF6CompletionTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Completion/KF6CompletionTargets.cmake
/usr/lib64/libKF6Completion.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6Completion.so.6.0.0
/V3/usr/lib64/qt6/plugins/designer/kcompletion6widgets.so
/usr/lib64/libKF6Completion.so.6
/usr/lib64/libKF6Completion.so.6.0.0
/usr/lib64/qt6/plugins/designer/kcompletion6widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcompletion/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kcompletion/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kcompletion/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kcompletion/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
