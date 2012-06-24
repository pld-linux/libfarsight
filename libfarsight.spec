Summary:	An audio/video conferencing framework
Summary(pl):	Szkielet do konferencji audio/video
Name:		libfarsight
Version:	0.1.8
Release:	0.1
License:	GPL
Group:		Libraries
Source0:  	%{name}-%{version}.tar.bz2
# Source0-md5:	7bab6f21b231262d36c58a37c82d3807
URL:		http://farsight.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gnet-devel >= 2.0.7
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gtk-doc
BuildRequires:	libjingle-devel
BuildRequires:	libtool
BuildRequires:	sofia-sip-devel >= 0.11.5
Requires:	glib2 >= 1:2.6.0
Requires:	gnet >= 2.0.7
Requires:	sofia-sip >= 0.11.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FarSight is an audio/video conferencing framework specifically
designed for Instant Messengers. It aims to provide a code
structure that will be able to absorb as many video conferencing
protocols as possible. It also offers an interface to those Instant
Messengers, allowing them to embed the video feeds and controls into
them.

FarSight is not a standalone application. It provides two APIs, one
for interfacing with the different "protocol modules" and one for
interfacing with the Instant Messenger GUI. There will also be a
default GUI for those who don't wish to embed the feeds into their
Instant Messenger's GUI.

%description -l pl
FarSight to szkielet do konferencji audio/video zaprojektowany
szczeg�lnie z my�l� o komunikatorach. Jego celem jest zapewnienie
struktury kodu b�d�cego w stanie obj�� jak najwi�cej protoko��w
konferencyjnych z obrazem. Oferuje tak�e interfejs do tych
komunikator�w, pozwalaj�c osadza� ich feedy i sterowanie obrazem.

FarSight nie jest samodzieln� aplikacj�. Udost�pnia dwa API: jedno do
wsp�pracy z r�nymi "modu�ami protoko��w" i jedno do wsp�pracy z
graficznym interfejsem komunikatora. B�dzie tak�e domy�lne GUI dla
tych, kt�rzy nie chc� osadza� feed�w w GUI komunikatora.

%package devel
Summary:	Headers for development using FarSight framework
Summary(pl):	Pliki nag��wkowe szkieletu FarSight
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers of FarSight for development.

%description devel -l pl
Pliki nag��wkowe szkieletu FarSight.

%prep
%setup -q -n farsight-%{version}

%build
%{__aclocal} -I m4
%{__libtoolize}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_sysconfdir}/farsight
%dir %{_libdir}/farsight-0.1
%attr(755,root,root) %{_libdir}/farsight-0.1/lib*.so
# rm if not needed
%{_libdir}/farsight-0.1/lib*.la

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc
