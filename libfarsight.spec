Summary:	An audio/video conferencing framework
Summary(pl.UTF-8):   Szkielet do konferencji audio/video
Name:		libfarsight
Version:	0.1.8
Release:	0.1
License:	GPL
Group:		Libraries
Source0:  	%{name}-%{version}.tar.bz2
# Source0-md5:	7bab6f21b231262d36c58a37c82d3807
URL:		http://farsight.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gnet-devel >= 2.0.7
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gtk-doc >= 1.5
BuildRequires:	libjingle-devel >= 0.3
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sofia-sip-devel >= 1.11.6
Requires:	glib2 >= 1:2.6.0
Requires:	gnet >= 2.0.7
Requires:	sofia-sip >= 1.11.6
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

%description -l pl.UTF-8
FarSight to szkielet do konferencji audio/video zaprojektowany
szczególnie z myślą o komunikatorach. Jego celem jest zapewnienie
struktury kodu będącego w stanie objąć jak najwięcej protokołów
konferencyjnych z obrazem. Oferuje także interfejs do tych
komunikatorów, pozwalając osadzać ich feedy i sterowanie obrazem.

FarSight nie jest samodzielną aplikacją. Udostępnia dwa API: jedno do
współpracy z różnymi "modułami protokołów" i jedno do współpracy z
graficznym interfejsem komunikatora. Będzie także domyślne GUI dla
tych, którzy nie chcą osadzać feedów w GUI komunikatora.

%package devel
Summary:	Headers for development using FarSight framework
Summary(pl.UTF-8):   Pliki nagłówkowe szkieletu FarSight
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.6.0
Requires:	gstreamer-devel >= 0.10

%description devel
Headers of FarSight for development.

%description devel -l pl.UTF-8
Pliki nagłówkowe szkieletu FarSight.

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

rm -f $RPM_BUILD_ROOT%{_libdir}/farsight-0.1/*.la

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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc
