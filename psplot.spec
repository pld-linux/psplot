Summary:	A Fortran-callable Postscript plotting library
Summary(pl):	Dzia³aj±ca z Fortranem biblioteka rysuj±ca w Postscripcie
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
Biblioteka psplot zawiera wywo³ywalne z Fortrana procedury do
produkcji plików postscriptowych. Poniewa¿ g³ównym zadaniem biblioteki
s± rysunki techniczne, wiele "artystycznych" mo¿liwo¶ci Postscriptu
nie jest wykorzystywanych. Ten pakiet zawiera bibliotekê
wspó³dzielon±.

%package devel
Summary:	A Fortran-callable Postscript plotting library - header files
Summary(pl):	Pliki nag³ówkowe do dzia³aj±cej z Fortranem biblioteki rysuj±cej Postscript
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for the psplot library.

%description devel -l pl
Pliki nag³ówkowe do biblioteki psplot.

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
