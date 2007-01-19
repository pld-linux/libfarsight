Summary:	An audio/video conferencing framework
Name:		libfarsight
Version:	0.1.8
Release:	0.1
License:	GPL
URL:		http://farsight.sourceforge.net/	
Group:		Networking/Instant messaging
Source0:  	%{name}-%{version}.tar.bz2
# Source0-md5:	7bab6f21b231262d36c58a37c82d3807
BuildRequires:  autoconf
BuildRequires:  automake >= 1.9
BuildRequires:  glib2-devel >= 2.6.0
BuildRequires:	gnet-devel >= 2.0.7
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:  gtk-doc
BuildRequires:	libjingle-devel
BuildRequires:	libtool
BuildRequires:	sofia-sip-devel >= 0.11.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FarSight is an audio/video conferencing framework 
specifically designed for Instant Messengers. It 
aims to provide a code structure that will be able 
to absorb as many video conferencing protocols as 
possible. It also offers an interface to those Instant 
Messengers, allowing them to embed the video feeds and 
controls into them.

FarSight is not a standalone application. It provides two 
APIs, one for interfacing with the different "protocol modules" 
and one for interfacing with the Instant Messenger GUI. There will 
also be a default GUI for those who don't wish to embed the feeds 
into their Instant Messenger's GUI.

%package devel
Summary:	Headers for development
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
Headers of farsight for development.

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
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_sysconfdir}/farsight
%dir %{_libdir}/farsight-0.1

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_pkgconfigdir}/*.pc
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/farsight-0.1/lib*.so
%{_libdir}/farsight-0.1/lib*.la
