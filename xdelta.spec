Summary:	XDELTA - version control system
Summary(pl):	XDELTA - system kontroli wersji
Name:		xdelta
Version:	1.0.0
Release:	3d
Copyright:	GPL
Group:		Development/Version Control
Group(pl):	Programowanie/Kontrola Wersji
Source:		ftp://www.xcf.berkeley.edu/pub/xdelta/%{name}-%{version}.tar.gz                                  
Patch0:         xdelta-info.patch
URL:		http://www.XCF.Berkeley.EDU/~jmacd/xdelta.html                                                   
PreReq:		/sbin/install-info
BuildRoot:	/tmp/%{name}-%{version}-root

%description
XDELTA (`X' for XCF) is a version-control library and file-format designed as
a replacement for RCS.  The XDELTA library performs its work independently of
the actual file-format used to encode the version-file and is intended to be
used by various higher-level programs such as PRCS.

XDELTA uses a binary file-delta algorithm to replace the standard diff
program used by RCS.

%description -l pl
XDELTA (`X' od XCF) jest bibliotek± systemu kontroli wersji tworzona jako
zamiennik RCS. Biblioteka XDELTA wykonuje ró¿ne czynno¶ci niezale¿nie od
bierz±cego formatu plików, u¿ywanych do kodowania plików baz danych, systemu
kontroli wersji i zaprojektowana jest do u¿ywania w ró¿nych wysoko-poziomowych
systemach kontroli wersji jak PRCS.

XDELTA u¿ywa binarnego formatu zamiast standardowego diif-a u¿ywanego przez
RCS.

%package devel
Summary:	XDELTA - header files
Summary(pl):	XDELTA - pliki nag³ówkowe
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package contains the XDELTA header files required to develop
XDELTA-based applications.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe potrzebne przy tworzeniu aplikacji
bazuj±cych na XDELTA.

%package static
Summary:	XDELTA - static library
Summary(pl):	XDELTA - biblioteka statyczna
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This package contains the XDELTA static libraries

%description -l pl static
Pakiet ten zawiera bibliotekê statyczn± XDELTA.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--x-includes=/usr/X11R6/lib/glib/include
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/info

make prefix=$RPM_BUILD_ROOT/usr install-strip

install doc/xdelta.info $RPM_BUILD_ROOT/usr/info

gzip -9nf $RPM_BUILD_ROOT/usr/{info/*.info*,man/man1/*}

bzip2 -9 NEWS READ* xdelta.magic ChangeLog

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info /usr/info/xdelta.info.gz /etc/info-dir

%preun devel
if [ $1 = 0 ]; then
	/sbin/install-info --delete /usr/info/xdelta.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/lib/*.so.*
%attr(644,root, man) /usr/man/man1/*

%files devel
%defattr(644,root,root,755)
%doc NEWS.bz2 READ* xdelta.magic.bz2 ChangeLog.bz2

/usr/include/*
/usr/info/xdelta.*

%attr(755,root,root) /usr/lib/*.so

%files static
%attr(755,root,root) /usr/lib/lib*.a

%changelog
* Sat Jan 23 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-3d]
- removed xdelta.magic from doc (this is now included in latest file packa).
- changed --x-includes to /usr/X11R6/lib/glib/include,
- standarized {un}registering info pages (added xdelta-info.patch),
- gzipping instead bzipping2 man pages.

* Sat Jan 23 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- added Group(pl),  
- compressed man pages && documentation (bizp2),
- fixed %post && %preun,
- fixed static-subpackage.

* Wed Dec 23 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-3]
- standarized {un}registering info pages,
- xdelta info pages moved to section "Version Control:",
- added gzipping man pages,
- added URL,
- added using LDFLAGS="-s" to ./configure enviroment.

* Thu Nov 26 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-2]
- fixed: removed /usr/info/dir from devel,
- removed xdelta.magic and non existing doc/xdelta.txt from %doc,
- fixed --entry text on {un}registering info page for libtool in %post
  %preun in devel.

* Sat Oct 03 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.23-1d]
- build against Tornado,
- fixed pl translation,
- fixed files permissions,
- minor modifications of the spec file.

* Mon Aug 10 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
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

* Sun Jun  7 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.19-3]
- fixed configuring sources by add --x-includes=/usr/lib/glib/include
  configure parameter (for glibconfig.h),
- changed Source url to ftp://www.xcf.berkeley.edu/pub/xdelta/
- fixed %defattr macros (thanks to René Wuttke <Rene.Wuttke@gmx.net>).

* Wed May  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.19-2]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added -q %setup parameter,
- added using %%{name} macro in Buildroot, Source and Rquires in devel
  fields.

* Sun May 03 1998 Arne Coucheron <arneco@online.no>
  [0.19-1]
- removed some older changelogs

* Wed Apr 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
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
