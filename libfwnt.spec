Summary:	Library to support Windows NT specific formats
Summary(pl.UTF-8):	Biblioteka wspierająca formaty specyficzne dla Windows NT
Name:		libfwnt
Version:	20150104
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libfwnt/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	eb83116fd3a8eb9205be1c06049dec67
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libfwnt/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcdata-devel >= 20150102
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcnotify-devel >= 20120425
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libcthreads-devel >= 20130509
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcdata >= 20150102
Requires:	libcerror >= 20120425
Requires:	libcnotify >= 20120425
Requires:	libcstring >= 20120425
Requires:	libcthreads >= 20130509
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
Requires:	libcdata-devel >= 20150102
Requires:	libcerror-devel >= 20120425
Requires:	libcnotify-devel >= 20120425
Requires:	libcstring-devel >= 20120425
Requires:	libcthreads-devel >= 20130509

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

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfwnt.la

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
