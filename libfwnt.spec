# see m4/${libname}.m4 />= for required version of particular library
%define		libcdata_ver	20230108
%define		libcerror_ver	20120425
%define		libcnotify_ver	20120425
%define		libcthreads_ver	20160404
Summary:	Library to support Windows NT specific formats
Summary(pl.UTF-8):	Biblioteka wspierająca formaty specyficzne dla Windows NT
Name:		libfwnt
Version:	20240126
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libfwnt/releases
Source0:	https://github.com/libyal/libfwnt/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	9f593c47477f9860fa66b31105d82240
URL:		https://github.com/libyal/libfwnt/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
%{?with_python2:BuildRequires:	python-devel >= 2}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
BuildRequires:	rpm-pythonprov
Requires:	libcdata >= %{libcdata_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcstring >= 20120425
Requires:	libcthreads >= %{libcthreads_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libfwnt is a library to support Windows NT specific formats.

%description -l pl.UTF-8
libfwnt to biblioteka wspierająca formaty specyficzne dla Windows NT.

%package devel
Summary:	Header files for libfwnt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libfwnt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcdata-devel >= %{libcdata_ver}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libcnotify-devel >= %{libcnotify_ver}
Requires:	libcstring-devel >= 20120425
Requires:	libcthreads-devel >= %{libcthreads_ver}

%description devel
Header files for libfwnt library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libfwnt.

%package static
Summary:	Static libfwnt library
Summary(pl.UTF-8):	Statyczna biblioteka libfwnt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libfwnt library.

%description static -l pl.UTF-8
Statyczna biblioteka libfwnt.

%package -n python-pyfwnt
Summary:	Python 2 interface to libfwnt
Summary(pl.UTF-8):	Interfejs Pythona 2 do libfwnt
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-pyfwnt
Python 2 interface to libfwnt.

%description -n python-pyfwnt -l pl.UTF-8
Interfejs Pythona 2 do libfwnt.

%package -n python3-pyfwnt
Summary:	Python 3 interface to libfwnt
Summary(pl.UTF-8):	Interfejs Pythona 3 do libfwnt
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-pyfwnt
Python 3 interface to libfwnt.

%description -n python3-pyfwnt -l pl.UTF-8
Interfejs Pythona 3 do libfwnt.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_python2:--enable-python2} \
	%{?with_python3:--enable-python3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfwnt.la

%if %{with python2}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pyfwnt.{la,a}
%endif
%if %{with python3}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/pyfwnt.{la,a}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libfwnt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfwnt.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfwnt.so
%{_includedir}/libfwnt
%{_includedir}/libfwnt.h
%{_pkgconfigdir}/libfwnt.pc
%{_mandir}/man3/libfwnt.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libfwnt.a

%if %{with python2}
%files -n python-pyfwnt
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/pyfwnt.so
%endif

%if %{with python3}
%files -n python3-pyfwnt
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/pyfwnt.so
%endif
