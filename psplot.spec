Summary:	A Fortran-callable Postscript plotting library
Summary(pl.UTF-8):	Działająca z Fortranem biblioteka rysująca w Postscripcie
Name:		psplot
Version:	0.1
Release:	1
License:	Freeware
Group:		Libraries
Source0:	ftp://student.ifpan.edu.pl/pub/psplot/%{name}-%{version}.tar.gz
# Source0-md5:	3704836929eae06c9419b339d6e4c5c4
Source1:	%{name}-Makefile
URL:		http://www.nova.edu/cwis/oceanography/psplot.html
BuildRequires:	gcc-g77
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The psplot library consists of Fortran-callable subroutines which can
be combined in a calling program to produce Postscript files. Since
the focus of the library is to produce technical drawing, many of the
'artistic' features of Postscript have not beed addressed. This
package is a shared library.

%description -l pl.UTF-8
Biblioteka psplot zawiera wywoływalne z Fortranu procedury do
produkcji plików postscriptowych. Ponieważ głównym zadaniem biblioteki
są rysunki techniczne, wiele "artystycznych" możliwości Postscriptu
nie jest wykorzystywanych. Ten pakiet zawiera bibliotekę
współdzieloną.

%package devel
Summary:	A Fortran-callable Postscript plotting library - header files
Summary(pl.UTF-8):	Pliki nagłówkowe do działającej z Fortranem biblioteki rysującej Postscript
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the psplot library.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki psplot.

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so

%files devel
%defattr(644,root,root,755)
%doc grmana4.ps *.txt *.for
%{_libdir}/lib%{name}.a
