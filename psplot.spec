
Name:		psplot
Version:	0.1
Release:	1
URL:		http://www.nova.edu/ocean/psplot.html
Source0:	ftp://student.ifpan.edu.pl/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}-Makefile
Summary:	A Fortran-callable Postscript plotting library
License:	Freeware
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Buildrequires:	gcc-g77
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The psplot library consists of Fortran-callable subroutines which can
be combined in a calling program to produce Postscript files. Since
the focus of the library is to produce technical drawing, many of the
'artistic' features of Postscript have not beed addressed. This
package is a shared library.

%package devel
Summary:	A Fortran-callable Postscript plotting library - header files
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
Header files for the psplot library.

%package static
Summary:	A Fortran-callable Postscript plotting library - static version
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Static psplot libraries.

%prep
%setup -q -n %{name}

%build
cp %{SOURCE1} Makefile
%{__make} "CFLAGS=%{rpmcflags}"
ln -s libpsplot.so libpsplot.so.link

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install libpsplot.so $RPM_BUILD_ROOT%{_libdir}/libpsplot.so.%{version}
cp -a libpsplot.so.link $RPM_BUILD_ROOT%{_libdir}/libpsplot.so
install libpsplot.a $RPM_BUILD_ROOT%{_libdir}/libpsplot.a

gzip -9nf grmana4.ps *.txt *.for 

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so.*.*
%files devel
%defattr(644,root,root,755)
%doc *.gz
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so
%files static
%defattr(644,root,root,755)
%{_libdir}/lib%{name}.a
