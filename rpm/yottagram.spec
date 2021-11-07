Name:       yottagram

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Yottagram
Version:    0.2.0
Release:    1
Group:      Qt/Qt
License:    GPLv3
URL:        http://verdanditeam.com/
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:  tdlib = 1.7.0
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(connman-qt5)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(nemonotifications-qt5)
BuildRequires:  tdlib = 1.7.0
BuildRequires:  desktop-file-utils

%description
Short description of my Sailfish OS Application

%prep
%setup -q -n %{name}-%{version}

%build
#export CFLAGS='-O0 -g -pipe -Wall -fexceptions -fstack-protector --param=ssp-buffer-size=4 -Wformat -Wformat-security -fmessage-length=0 -march=armv7-a -mfloat-abi=hard -mfpu=neon -mthumb -Wno-psabi'
#export CXXFLAGS='-O0 -g -pipe -Wall -fexceptions -fstack-protector --param=ssp-buffer-size=4 -Wformat -Wformat-security -fmessage-length=0 -march=armv7-a -mfloat-abi=hard -mfpu=neon -mthumb -Wno-psabi'
%qtc_qmake5 

%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/com.verdanditeam.yottagram.service
%{_datadir}/lipstick/notificationcategories/x-verdanditeam.yottagram.im.conf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
