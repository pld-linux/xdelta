Summary:	XDELTA - version control system
Summary(pl):	XDELTA - system kontroli wersji
Name:		xdelta
Version:	1.1.1
Release:	2
Copyright:	GPL
Group:		Development/Version Control
Group(pl):	Programowanie/Kontrola Wersji
Source:		ftp://www.xcf.berkeley.edu/pub/xdelta/%{name}-%{version}.tar.gz
URL:		http://www.XCF.Berkeley.EDU/~jmacd/xdelta.html
BuildPrereq:	glib-devel >= 1.2.0
BuildPrereq:	zlib-devel
Requires:	glib >= 1.2.0
BuildRoot:	/tmp/%{name}-%{version}-root

%description
XDELTA (`X' for XCF) is a version-control library and file-format designed as
a replacement for RCS.  The XDELTA library performs its work independently of
the actual file-format used to encode the version-file and is intended to be
used by various higher-level programs such as PRCS.

XDELTA uses a binary file-delta algorithm to replace the standard diff
program used by RCS.

%description -l pl
XDELTA (`X' od XCF) jest bibliotek� systemu kontroli wersji tworzona jako
zamiennik RCS. Biblioteka XDELTA wykonuje r�ne czynno�ci niezale�nie od
bierz�cego formatu plik�w, u�ywanych do kodowania plik�w baz danych, systemu
kontroli wersji i zaprojektowana jest do u�ywania w r�nych wysoko-poziomowych
systemach kontroli wersji jak PRCS.

XDELTA u�ywa binarnego formatu zamiast standardowego diif-a u�ywanego przez
RCS.

%package devel
Summary:	XDELTA - header files
Summary(pl):	XDELTA - pliki nag��wkowe
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
PreReq:		/sbin/install-info
Requires:	%{name} = %{version}

%description devel
This package contains the XDELTA header files required to develop
XDELTA-based applications.

%description -l pl devel
Pakiet ten zawiera pliki nag��wkowe potrzebne przy tworzeniu aplikacji
bazuj�cych na XDELTA.

%package static
Summary:	XDELTA - static library
Summary(pl):	XDELTA - biblioteka statyczna
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This package contains the XDELTA static libraries

%description -l pl static
Pakiet ten zawiera bibliotek� statyczn� XDELTA.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target}\
	--prefix=/usr \
	--x-includes=/usr/X11R6/lib/glib/include
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

make prefix=$RPM_BUILD_ROOT/usr install-strip

strip --strip-unneeded $RPM_BUILD_ROOT/usr/lib/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	NEWS READ* ChangeLog

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/xdelta
%attr(755,root,root) /usr/lib/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc {NEWS,READ*,ChangeLog}.gz

%attr(755,root,root) /usr/bin/xdelta-config
/usr/include/*

%attr(755,root,root) /usr/lib/lib*.so

%files static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%changelog
* Wed Apr 21 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [1.1.1-2]
- recompiled on rpm 3.

  by Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>:
- updated to 1.1.1,
- strip with --strip-unneeded shared libraries,
- gzipping %doc instead bzippng2,
- removed %post, %postun.

* Sun Mar 21 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.6-1]
- fix: "PreReq: /sbin/install-info" moved to devel,
- strip with --strip-unneeded shared libraries.

* Mon Mar  1 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.3-1]
- removed xdelta.magic from %doc (it is integrated in current file package),
- added "Requires: glib = 1.2.0" to main,
- /usr/bin/xdelta-config moved to devel,
- removed xdelta info pages (it is empty .. contain only GPL licence text),
- removed man group from man pages.

* Fri Feb 05 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.0.2-1d]
- updated to 1.0.2,
- fixed permission of static library.

* Sat Jan 23 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-3d]
- removed xdelta.magic from doc (this is now included in latest file packa).
- changed --x-includes to /usr/X11R6/lib/glib/include,
- standarized {un}registering info pages (added xdelta-info.patch),
- gzipping instead bzipping2 man pages.

* Sat Jan 23 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
- added Group(pl),  
- compressed man pages && documentation (bizp2),
- fixed %post && %preun,
- fixed static-subpackage.

* Wed Dec 23 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-3]
- standarized {un}registering info pages,
- xdelta info pages moved to section "Version Control:",
- added gzipping man pages,
- added URL,
- added using LDFLAGS="-s" to ./configure enviroment.

* Thu Nov 26 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-2]
- fixed: removed %{_infodir}/dir from devel,
- removed xdelta.magic and non existing doc/xdelta.txt from %doc,
- fixed --entry text on {un}registering info page for libtool in %post
  %preun in devel.

* Sat Oct 03 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [0.23-1d]
- build against Tornado,
- fixed pl translation,
- fixed files permissions,
- minor modifications of the spec file.

* Mon Aug 10 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.22-2]
- added pl translation,
- added static subpackage,
- all %doc moved to devel,
- cosmetic changes in %files.

* Tue Jul 07 1998 Arne Coucheron <arneco@online.no>
  [0.22-1]
- removed running of automake, problem fixed in sources

* Sat Jul 04 1998 Arne Coucheron <arneco@online.no>
  [0.21-1]
- added xdelta.magic to %doc
- added running of automake before configure to make this version build
- changed %defattr

* Sat Jun 27 1998 Arne Coucheron <arneco@online.no>
  [0.20-1]

* Sun Jun  7 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.19-3]
- fixed configuring sources by add --x-includes=/usr/lib/glib/include
  configure parameter (for glibconfig.h),
- changed Source url to ftp://www.xcf.berkeley.edu/pub/xdelta/
- fixed %defattr macros (thanks to Ren� Wuttke <Rene.Wuttke@gmx.net>).

* Wed May  6 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.19-2]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added -q %setup parameter,
- added using %%{name} macro in Buildroot, Source and Rquires in devel
  fields.

* Sun May 03 1998 Arne Coucheron <arneco@online.no>
  [0.19-1]
- removed some older changelogs

* Wed Apr 28 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.18-2]
- removed COPYING from %doc (copyright statment is in Copyright field),
- /sbin/ldconfig is now -p parameter in %post, %postun,
- replaced "mkdir -p" with "install -d" in %install,
- added "Requires: xdelta = %%{PACKAGE_VERSION}" for devel,
- added using %defattr macro in %files (requires rpm >= 2.4.99),
- added using predefined macro %%{PACKAGE_VERSION} instead %{version},
- changed permission on /usr/lib/lib*.so links to 644,
- removed /usr/lib/libxdelta.la from devel,
- added striping /usr/lib/lib*.so.*.* libs,
- Buildroot changed to /tmp/xdelta-%%{PACKAGE_VERSION}-root.

* Fri Apr 24 1998 Arne Coucheron <arneco@online.no>
  [0.18-1]
- removed the fakeglib patch

* Wed Apr 08 1998 Arne Coucheron <arneco@online.no>
  [0.15-2]
- splitted the package into a main and devel package

* Sat Apr 04 1998 Arne Coucheron <arneco@online.no>
  [0.15-1]
