Summary:	A Fortran-callable Postscript plotting library
Summary(pl):	Dzia≥aj±ca z Fortranem biblioteka rysuj±ca w Postscripcie
Name:		psplot
Version:	0.1
Release:	1
License:	Freeware
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://student.ifpan.edu.pl/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}-Makefile
URL:		http://www.nova.edu/ocean/psplot.html
Buildrequires:	gcc-g77
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The psplot library consists of Fortran-callable subroutines which can
be combined in a calling program to produce Postscript files. Since
the focus of the library is to produce technical drawing, many of the
'artistic' features of Postscript have not beed addressed. This
package is a shared library.

%description -l pl
Biblioteka psplot zawiera wywo≥ywalne z Fortrana procedury do
produkcji plikÛw postscriptowych. Poniewaø g≥Ûwnym zadaniem biblioteki
s± rysunki techniczne, wiele "artystycznych" moøliwo∂ci Postscriptu
nie jest wykorzystywanych. Ten pakiet zawiera bibliotekÍ
wspÛ≥dzielon±.

%package devel
Summary:	A Fortran-callable Postscript plotting library - header files
Summary(pl):	Pliki nag≥Ûwkowe do dzia≥aj±cej z Fortranem biblioteki rysuj±cej Postscript
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
Header files for the psplot library.

%description devel -l pl
Pliki nag≥Ûwkowe do biblioteki psplot.

%prep
%setup -q -n %{name}

%build
cp -f %{SOURCE1} Makefile
%{__make} "CFLAGS=%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install libpsplot.so $RPM_BUILD_ROOT%{_libdir}
install libpsplot.a $RPM_BUILD_ROOT%{_libdir}

gzip -9nf grmana4.ps *.txt *.for

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so

%files devel
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/lib%{name}.a
