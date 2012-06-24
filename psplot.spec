Summary:	A Fortran-callable Postscript plotting library
Summary(pl):	Dzia�aj�ca z Fortranem biblioteka rysuj�ca w Postscripcie
Name:		psplot
Version:	0.1
Release:	1
License:	Freeware
Group:		Libraries
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
Biblioteka psplot zawiera wywo�ywalne z Fortrana procedury do
produkcji plik�w postscriptowych. Poniewa� g��wnym zadaniem biblioteki
s� rysunki techniczne, wiele "artystycznych" mo�liwo�ci Postscriptu
nie jest wykorzystywanych. Ten pakiet zawiera bibliotek�
wsp�dzielon�.

%package devel
Summary:	A Fortran-callable Postscript plotting library - header files
Summary(pl):	Pliki nag��wkowe do dzia�aj�cej z Fortranem biblioteki rysuj�cej Postscript
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for the psplot library.

%description devel -l pl
Pliki nag��wkowe do biblioteki psplot.

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

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so

%files devel
%defattr(644,root,root,755)
%doc grmana4.ps *.txt *.for
%{_libdir}/lib%{name}.a
