Summary:	XDELTA - version control system
Summary(es):	patch y diff para archivos binarios
Summary(pl):	XDELTA - system kontroli wersji
Summary(pt_BR):	patch e diff para arquivos bin·rios
Name:		xdelta
Version:	1.1.3
Release:	1
License:	GPL
Group:		Development/Version Control
Group(de):	Entwicklung/Versionkontrolle
Group(pl):	Programowanie/Zarz±dzanie wersjami
Source0:	http://prdownloads.sourceforge.net/xdelta/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-use_sys_getopt.patch
Patch2:		%{name}-am15.patch
URL:		http://www.XCF.Berkeley.EDU/~jmacd/xdelta.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XDelta (X for XCF: the eXperimental Computing Facility at Berkeley) is
a library interface and binary delta generator (like a diff program
for binaries) and an RCS. These changes (deltas) are similar to the
output of the "diff" program in that they may be used to store and
transmit only the changes between files. However, unlike diff, the
output of XDelta is not expressed in a human-readable format--XDelta
can also also apply these deltas to a copy of the original file(s).
XDelta uses a fast, linear algorithm and performs well on both binary
and text files. XDelta typically outperforms GNU diff in both time and
generated-delta-size, even for plain text files. XDelta also includes
a simple implementation of the Rsync algorithm and several advanced
features for implementing RCS-like file-archival with.

The Xdelta library performs its work independently of the actual
format used to encode the file and is intended to be used by various
higher-level programs such as XCF's Project Revision Control System
(PRCS). PRCS is a front end for a version control toolset. Xdelta uses
a binary file delta algorithm to replace the standard diff program
used by RCS.

%description -l es
xdelta es como las Ûrdenes patch y diff, pero tambiÈn funciona con
archivos binarios.

%description -l pl
XDELTA (`X' od XCF) jest bibliotek± systemu kontroli wersji tworzona
jako zamiennik RCS. Biblioteka XDELTA wykonuje rÛøne czynno∂ci
niezaleønie od bierz±cego formatu plikÛw, uøywanych do kodowania
plikÛw baz danych, systemu kontroli wersji i zaprojektowana jest do
uøywania w rÛønych wysoko-poziomowych systemach kontroli wersji jak
PRCS.

%description -l pt_BR
xdelta È como os comandos patch e diff, mas tambÈm funciona com
arquivos bin·rios.

%package devel
Summary:	XDELTA - header files
Summary(pl):	XDELTA - pliki nag≥Ûwkowe
Summary(pt_BR):	Arquivos de desenvolvimento xdelta
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
This package contains the XDELTA header files required to develop
XDELTA-based applications.

%description -l pl devel
Pakiet ten zawiera pliki nag≥Ûwkowe potrzebne przy tworzeniu aplikacji
bazuj±cych na XDELTA.

%description -l pt_BR devel
Esse pacote contÈm os arquivos de desenvolvimento do xdelta.

%package static
Summary:	XDELTA - static library
Summary(pl):	XDELTA - biblioteka statyczna
Summary(pt_BR):	Bibliotecas est·ticas para desenvolvimento com xdelta
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
This package contains the XDELTA static libraries.

%description -l pl static
Pakiet ten zawiera bibliotekÍ statyczn± XDELTA.

%description -l pt_BR static
Bibliotecas est·ticas para desenvolvimento com xdelta.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure \
	--x-includes=%{_prefix}/X11R6/lib/glib/include
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf NEWS READ* ChangeLog

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
%attr(755,root,root) %{_libdir}/lib*.so
%{_aclocaldir}/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
