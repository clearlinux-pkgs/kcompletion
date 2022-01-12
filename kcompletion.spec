#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kcompletion
Version  : 5.90.0
Release  : 46
URL      : https://download.kde.org/stable/frameworks/5.90/kcompletion-5.90.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.90/kcompletion-5.90.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.90/kcompletion-5.90.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1
Requires: kcompletion-data = %{version}-%{release}
Requires: kcompletion-lib = %{version}-%{release}
Requires: kcompletion-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kwidgetsaddons-dev

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
%setup -q -n kcompletion-5.90.0
cd %{_builddir}/kcompletion-5.90.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641969338
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1641969338
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcompletion
cp %{_builddir}/kcompletion-5.90.0/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcompletion/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/kcompletion-5.90.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcompletion/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/kcompletion-5.90.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcompletion/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kcompletion-5.90.0/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kcompletion/6f1f675aa5f6a2bbaa573b8343044b166be28399
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/as/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/az/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/be/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/br/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/de/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/el/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/es/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/et/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/he/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/id/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/is/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/it/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/km/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/or/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/se/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/si/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/te/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/th/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kcompletion5_qt.qm
/usr/share/qlogging-categories5/kcompletion.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KCompletion/KComboBox
/usr/include/KF5/KCompletion/KCompletion
/usr/include/KF5/KCompletion/KCompletionBase
/usr/include/KF5/KCompletion/KCompletionBox
/usr/include/KF5/KCompletion/KCompletionMatches
/usr/include/KF5/KCompletion/KHistoryComboBox
/usr/include/KF5/KCompletion/KLineEdit
/usr/include/KF5/KCompletion/KPixmapProvider
/usr/include/KF5/KCompletion/KSortableList
/usr/include/KF5/KCompletion/kcombobox.h
/usr/include/KF5/KCompletion/kcompletion.h
/usr/include/KF5/KCompletion/kcompletion_export.h
/usr/include/KF5/KCompletion/kcompletionbase.h
/usr/include/KF5/KCompletion/kcompletionbox.h
/usr/include/KF5/KCompletion/kcompletionmatches.h
/usr/include/KF5/KCompletion/khistorycombobox.h
/usr/include/KF5/KCompletion/klineedit.h
/usr/include/KF5/KCompletion/kpixmapprovider.h
/usr/include/KF5/KCompletion/ksortablelist.h
/usr/include/KF5/kcompletion_version.h
/usr/lib64/cmake/KF5Completion/KF5CompletionConfig.cmake
/usr/lib64/cmake/KF5Completion/KF5CompletionConfigVersion.cmake
/usr/lib64/cmake/KF5Completion/KF5CompletionTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Completion/KF5CompletionTargets.cmake
/usr/lib64/libKF5Completion.so
/usr/lib64/qt5/mkspecs/modules/qt_KCompletion.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Completion.so.5
/usr/lib64/libKF5Completion.so.5.90.0
/usr/lib64/qt5/plugins/designer/kcompletion5widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcompletion/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kcompletion/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kcompletion/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kcompletion/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
