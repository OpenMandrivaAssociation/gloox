%define name gloox
%define version 0.8.8 
%define release %mkrel 1

%define lib_major 0
%define lib_name %mklibname %name %lib_major


# select between GNUTLS or OpenSSL
%define use_gnutls 0
%{?_with_gnutls: %global use_gnutls 1}


Summary: Gloox is a C++ Jabber/XMPP library
Name: %{name}
Version: %{version}
Release: %{release}
Source0:  http://camaya.net/download/%{name}-%{version}.tar.bz2
License: GPL
Group: Networking/Remote access
Url: http://camaya.net/gloox
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libiksemel-devel libidn-devel openssl-devel gnutls-devel
%if %use_gnutls
BuildRequires:  gnutls-devel
%endif




%description
gloox is a C++ Jabber/XMPP library which takes care of the
low-level protocol stuff. Additionally, it offers high-level
interfaces for interaction with an XMPP server. It is released
under the GNU GPL. Commercial licenses are available.

%clean
rm -rf $RPM_BUILD_ROOT
 
%prep
%setup -q

%build
%configure2_5x \
%if %use_gnutls
        --with-gnutls      \
%else
        --without-gnutls       \
%endif
	--disable-static

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%files
%defattr(-,root,root)
%doc AUTHORS COPYING 


%package -n %{lib_name}
Summary: Libraries for %name
Group: Networking/Instant messaging

%description -n %{lib_name}
%name librairies

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/lib*%{name}.so.*

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig




%package -n %{lib_name}-devel
Summary: Headers for %name
Group: Networking/Instant messaging
Provides: %lib_name = %version-%release
Provides: %lib_name-devel = %version-%release
Provides: lib%name-devel = %version-%release
Requires: %lib_name = %version-%release

%description -n %{lib_name}-devel
headers for %name librairies


%files -n %lib_name-devel
%defattr(-,root,root)
%{_includedir}/*
%exclude %{_libdir}/lib*%{name}*.la
%{_libdir}/lib*%{name}.so
%{_libdir}/pkgconfig/*
%{_bindir}/*
%post -n %{lib_name}-devel -p /sbin/ldconfig
%postun -n %{lib_name}-devel -p /sbin/ldconfig




#%package -n %{lib_name}-static-devel
#Summary: Static libraries for %name
#Group: Networking/Instant messaging

#%description -n %{lib_name}-static-devel
#headers for %name librairies

#%files -n %{lib_name}-static-devel
#%defattr(-,root,root)
#%{_libdir}/lib*%{name}*.a


