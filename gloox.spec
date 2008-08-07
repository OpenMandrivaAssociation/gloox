#%define _requires_exceptions libresolv.so.2(GLIBC_PRIVATE)

%define lib_major       7
%define lib_name        %mklibname %{name} %{lib_major}
%define lib_name_d      %mklibname %{name} -d
%define lib_name_d_s    %mklibname %{name} -d -s

%bcond_with     gnutls

Name:           gloox
Version:        0.9.9.5
Release:        %mkrel 2
Summary:        C++ Jabber/XMPP library
URL:            http://camaya.net/gloox/
Source0:	http://camaya.net/download/%{name}-%{version}.tar.bz2
License:        GPLv2+
Group:          Networking/Remote access
BuildRequires:  libidn-devel
BuildRequires:  libiksemel-devel
%if %with gnutls
BuildRequires:  libgnutls-devel
%else
BuildRequires:  libopenssl-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
gloox is a C++ Jabber/XMPP library which takes care of the
low-level protocol stuff. Additionally, it offers high-level
interfaces for interaction with an XMPP server. It is released
under the GNU GPL. Commercial licenses are available.

%package -n %{lib_name}
Summary:        Libraries for %{name}
Group:          Networking/Instant messaging
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n %{lib_name}
%{name} librairies.

%package -n %{lib_name_d}
Summary:        Headers for %{name}
Group:          Networking/Instant messaging
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{lib_name} = %{version}-%{release}
Obsoletes:      %mklibname -d gloox 7
Obsoletes:	%mklibname -d gloox 4
Obsoletes:	%mklibname -d gloox 0

%description -n %{lib_name_d}
Headers for %{name} librairies.

%package -n %{lib_name_d_s}
Summary:        Static libraries for %{name}
Group:          Networking/Instant messaging
Provides:       lib%{name}-static-devel = %{version}-%{release}
Provides:       %{name}-static-devel = %{version}-%{release}
Requires:       %{lib_name_d} = %{version}-%{release}
Obsoletes:      %mklibname -d -s gloox 7
Obsoletes:      %mklibname -d -s gloox 4
Obsoletes:      %mklibname -d -s gloox 0

%description -n %{lib_name_d_s}
Headers for %{name} librairies.

%prep
%setup -q

%build
%{configure2_5x} \
%if %with gnutls
        --with-gnutls      \
%else
        --without-gnutls       \
%endif
        --enable-static

%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}
 
%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%defattr(-,root,root)
%doc AUTHORS COPYING 
%{_libdir}/lib*%{name}.so.%{lib_major}*

%files -n %{lib_name_d}
%defattr(-,root,root)
%{_bindir}/gloox-config
%{_includedir}/gloox/
%{_libdir}/lib*%{name}*.la
%{_libdir}/lib*%{name}.so
%{_libdir}/pkgconfig/gloox.pc

%files -n %{lib_name_d_s}
%defattr(-,root,root)
%{_libdir}/lib*%{name}*.a
