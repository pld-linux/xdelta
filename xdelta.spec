Summary:	XDELTA - version control system
Summary(pl):	XDELTA - system kontroli wersji
Name:		xdelta
Version:	1.1.1
Release:	3
Copyright:	GPL
Group:		Development/Version Control
Group(pl):	Programowanie/Kontrola Wersji
Source:		ftp://www.xcf.berkeley.edu/pub/xdelta/%{name}-%{version}.tar.gz
URL:		http://www.XCF.Berkeley.EDU/~jmacd/xdelta.html
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	zlib-devel
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

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform}\
	--prefix=%{_prefix} \
	--x-includes=/usr/X11R6/lib/glib/include
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

make DESTDIR=$RPM_BUILD_ROOT install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	NEWS READ* ChangeLog

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdelta
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc {NEWS,READ*,ChangeLog}.gz

%attr(755,root,root) %{_bindir}/xdelta-config
%{_includedir}/*

%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
