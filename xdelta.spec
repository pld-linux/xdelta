Summary:	XDELTA - version control system
Summary(es):	patch y diff para archivos binarios
Summary(pl):	XDELTA - system kontroli wersji
Summary(pt_BR):	patch e diff para arquivos binários
Name:		xdelta
Version:	1.1.1
Release:	12
License:	GPL
Group:		Development/Version Control
Group(de):	Entwicklung/Versionkontrolle
Group(pl):	Programowanie/Zarz±dzanie wersjami
Source0:	ftp://www.xcf.berkeley.edu/pub/xdelta/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		xdelta-ac_fixes.patch
Patch2:		xdelta-use_sys_getopt.patch
URL:		http://www.XCF.Berkeley.EDU/~jmacd/xdelta.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	zlib-devel
Requires:	glib >= 1.2.0
Requires(post):		/sbin/ldconfig
Requires(postun):	/sbin/ldconfig
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
xdelta es como las órdenes patch y diff, pero también funciona con
archivos binarios.

%description -l pl
XDELTA (`X' od XCF) jest bibliotek± systemu kontroli wersji tworzona
jako zamiennik RCS. Biblioteka XDELTA wykonuje ró¿ne czynno¶ci
niezale¿nie od bierz±cego formatu plików, u¿ywanych do kodowania
plików baz danych, systemu kontroli wersji i zaprojektowana jest do
u¿ywania w ró¿nych wysoko-poziomowych systemach kontroli wersji jak
PRCS.

%description -l pt_BR
xdelta é como os comandos patch e diff, mas também funciona com
arquivos binários.

%package devel
Summary:	XDELTA - header files
Summary(pl):	XDELTA - pliki nag³ówkowe
Summary(pt_BR):	Arquivos de desenvolvimento xdelta
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
This package contains the XDELTA header files required to develop
XDELTA-based applications.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe potrzebne przy tworzeniu aplikacji
bazuj±cych na XDELTA.

%description -l pt_BR devel
Esse pacote contém os arquivos de desenvolvimento do xdelta.

%package static
Summary:	XDELTA - static library
Summary(pl):	XDELTA - biblioteka statyczna
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com xdelta
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
This package contains the XDELTA static libraries.

%description -l pl static
Pakiet ten zawiera bibliotekê statyczn± XDELTA.

%description -l pt_BR static
Bibliotecas estáticas para desenvolvimento com xdelta.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
libtoolize -c -f
aclocal
autoconf
%configure \
	--x-includes=%{_prefix}/X11R6/lib/glib/include
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf NEWS READ* ChangeLog

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
