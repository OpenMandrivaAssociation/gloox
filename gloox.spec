#define _requires_exceptions libresolv.so.2(GLIBC_PRIVATE)

%define lib_major       17
%define lib_name        %mklibname %{name} %{lib_major}
%define lib_name_d      %mklibname %{name} -d
%define lib_name_d_s    %mklibname %{name} -d -s

%bcond_with     gnutls

Name:           gloox
Version:        1.0.22
Release:        1
Summary:        C++ Jabber/XMPP library
URL:            http://camaya.net/gloox/
Source0:	http://camaya.net/download/%{name}-%{version}.tar.bz2
License:        GPLv2+
Group:          Networking/Remote access
BuildRequires:  libidn-devel
BuildRequires:  pkgconfig(iksemel)
%if %with gnutls
BuildRequires:  libgnutls-devel
%else
BuildRequires:  pkgconfig(openssl)
%endif

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

# 11/11/2009 fix underlinking
export PTHREAD_LIBS="-lpthread"

%{configure2_5x} \
%if %with gnutls
        --with-gnutls      \
%else
        --without-gnutls       \
%endif
        --enable-static

%make_build

%install
%make_install


%files -n %{lib_name}
%defattr(-,root,root)
%doc AUTHORS COPYING 
%{_libdir}/lib*%{name}.so.%{lib_major}*

%files -n %{lib_name_d}
%defattr(-,root,root)
%{_bindir}/gloox-config
%{_includedir}/gloox/
%{_libdir}/lib*%{name}.so
%{_libdir}/pkgconfig/gloox.pc

%files -n %{lib_name_d_s}
%defattr(-,root,root)
%{_libdir}/lib*%{name}*.a


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdv2011.0
+ Revision: 610864
- rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 1.0-2mdv2010.1
+ Revision: 537298
- rebuild

* Thu Nov 12 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 1.0-1mdv2010.1
+ Revision: 465106
- update to new version 1.0
- fix underlinking

* Wed Sep 23 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.9.9-1mdv2010.0
+ Revision: 447919
- Update to new version 0.9.9.9

* Wed Jun 10 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 0.9.9.7-1mdv2010.0
+ Revision: 384927
- update to new (bugfix) version 0.9.9.7

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 16 2008 Funda Wang <fwang@mandriva.org> 0.9.9.5-1mdv2009.0
+ Revision: 194514
- New version 0.9.9.5

* Sun Jan 20 2008 David Walluck <walluck@mandriva.org> 0.9.9.3-1mdv2008.1
+ Revision: 155178
- 0.9.9.3

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 09 2007 Funda Wang <fwang@mandriva.org> 0.9.8-1mdv2008.1
+ Revision: 116646
- New version 0.9.8

* Sun Nov 18 2007 Funda Wang <fwang@mandriva.org> 0.9.7-2mdv2008.1
+ Revision: 109833
- fix typo of obsoletes

* Sun Nov 18 2007 Funda Wang <fwang@mandriva.org> 0.9.7-1mdv2008.1
+ Revision: 109812
- New version 0.9.7
- fix obosleted of devel package

* Fri Oct 26 2007 Funda Wang <fwang@mandriva.org> 0.9.6.1-1mdv2008.1
+ Revision: 102255
- New version 0.9.6.1

* Thu Sep 27 2007 David Walluck <walluck@mandriva.org> 0.9.5-1mdv2008.1
+ Revision: 93389
- 0.9.5

* Wed Aug 15 2007 Funda Wang <fwang@mandriva.org> 0.9.4.1-1mdv2008.0
+ Revision: 63703
- New version
- New devel package policy

* Sat Jul 21 2007 David Walluck <walluck@mandriva.org> 0.9.3-1mdv2008.0
+ Revision: 54249
- 0.9.3

* Sun Jun 24 2007 David Walluck <walluck@mandriva.org> 0.9.2-1mdv2008.0
+ Revision: 43545
- 0.9.2

* Thu Jun 21 2007 David Walluck <walluck@mandriva.org> 0.9.1-1mdv2008.0
+ Revision: 41969
- 0.9.1

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 0.8.8-3mdv2008.0
+ Revision: 36162
- rebuild with correct optflags

  + David Walluck <walluck@mandriva.org>
    - add _requires_exceptions libresolv.so.2(GLIBC_PRIVATE)
    - fix lib major (should be 4, not 0)
    - use %%mklibname for package names
    - fix gnutls conditional support
    - add %%bcond_with gnutls option
    - provide gloox in main lib package
    - correct devel provides
    - build static library
    - major spec file cleanup

* Wed Apr 25 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.8.8-1mdv2008.0
+ Revision: 18132
- New release 0.8.8


* Mon Mar 19 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.8.7-1mdv2007.1
+ Revision: 146408
- New release

* Fri Mar 09 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.8.6-1mdv2007.1
+ Revision: 139482
- Add BR
- Fix Build
- New release 0.8.6
- New release 0.8.4
- Import gloox

* Mon Jul 31 2006 Jerome Soyer <saispo@mandriva.org> 0.8.1-1mdv2007.0
- New release 0.8.1

* Mon Jul 24 2006 Olivier Blin <blino@mandriva.com> 0.8-2mdv2007.0
- rebuild for new glibc

* Fri Apr 14 2006 Jerome Soyer <saispo@mandriva.org> 0.8-1mdk
- New release 0.8

* Thu Apr 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.7.6.1-1mdk
- New release 0.7.6.1
- use mkrel

* Fri May 13 2005 Emmanuel Blindauer <blindauer@mandriva.org> 0.7.3-1mdk
- First Mandrakelinux release

