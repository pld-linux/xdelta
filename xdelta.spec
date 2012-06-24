Summary:	XDELTA - version control system
Summary(es):	patch y diff para archivos binarios
Summary(pl):	XDELTA - system kontroli wersji
Summary(pt_BR):	patch e diff para arquivos bin�rios
Name:		xdelta
Version:	1.1.3
Release:	3
License:	GPL
Group:		Development/Version Control
Source0:	http://dl.sourceforge.net/xdelta/%{name}-%{version}.tar.gz
# Source0-md5:	08e964c28541605b6fe61c0dd6595516
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-use_sys_getopt.patch
Patch2:		%{name}-am15.patch
Patch3:		%{name}-ac25x.patch
Patch4:		%{name}-am18.patch
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
output of XDelta is not expressed in a human-readable format - XDelta
can also also apply these deltas to a copy of the original file(s).
XDelta uses a fast, linear algorithm and performs well on both binary
and text files. XDelta typically outperforms GNU diff in both time and
generated-delta-size, even for plain text files. XDelta also includes
a simple implementation of the Rsync algorithm and several advanced
features for implementing RCS-like file-archival with.

The XDelta library performs its work independently of the actual
format used to encode the file and is intended to be used by various
higher-level programs such as XCF's Project Revision Control System
(PRCS). PRCS is a front end for a version control toolset. Xdelta uses
a binary file delta algorithm to replace the standard diff program
used by RCS.

%description -l es
xdelta es como las �rdenes patch y diff, pero tambi�n funciona con
archivos binarios.

%description -l pl
XDelta (`X' od XCF - eXperimental Computing Facility w Berkeley) jest
bibliotek� i generatorem binarnych delt (r�nic podobnych do tych
tworzonych przez program diff, ale dla binari�w) oraz systemem
kontroli wersji. Te zmiany (delty) s� podobne do wyj�cia programu diff
tak�e w tym, �e mog� by� u�ywane do przechowywania i transmisji tylko
zmian mi�dzy plikami. Jednak, w przeciwie�stwie do diffa, wyj�cie
XDelty nie jest wyra�one w postaci czytelnej dla cz�owieka; XDelta
mo�e tak�e nanie�� te zmiany na kopi� oryginalnego pliku (plik�w).
XDelta u�ywa szybkiego, liniowego algorytmu i dobrze si� sprawdza
zar�wno na binarnych, jak i tekstowych plikach. Algorytm XDelta zwykle
jest wydajniejszy od GNU diffa zar�wno pod wzgl�dem czasu jak i
rozmiaru wygenerowanych r�nic, nawet dla plik�w czysto tekstowych.
XDelta zawiera tak�e przyk�adow� implementacj� algorytmy Rsync i kilka
zaawansowanych mo�liwo�ci do implementowania archiwizacji plik�w
podobnej do RCS.

Biblioteka XDelta dzia�a dobrze niezale�nie od formatu u�ytego przy
kodowaniu pliku i jest przeznaczona do u�ywania w r�nych
wysokopoziomowych programach takich jak system kontroli wersji z XCF
(PRCS - Project Revision Control System), b�d�cy frontendem do
zbioru narz�dzi s�u��cych do kontroli wersji, w kt�rym jest u�ywany
algorytm binarnych r�nic XDelta zamiast standardowego diffa u�ywanego
przez RCS.

%description -l pt_BR
xdelta � como os comandos patch e diff, mas tamb�m funciona com
arquivos bin�rios.

%package devel
Summary:	XDELTA - header files
Summary(pl):	XDELTA - pliki nag��wkowe
Summary(pt_BR):	Arquivos de desenvolvimento xdelta
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains the XDELTA header files required to develop
XDELTA-based applications.

%description devel -l pl
Pakiet ten zawiera pliki nag��wkowe potrzebne przy tworzeniu aplikacji
bazuj�cych na XDELTA.

%description devel -l pt_BR
Esse pacote cont�m os arquivos de desenvolvimento do xdelta.

%package static
Summary:	XDELTA - static library
Summary(pl):	XDELTA - biblioteka statyczna
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com xdelta
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains the XDELTA static libraries.

%description static -l pl
Pakiet ten zawiera bibliotek� statyczn� XDELTA.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com xdelta.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS READ*
%attr(755,root,root) %{_bindir}/xdelta
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/xdelta-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_aclocaldir}/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
