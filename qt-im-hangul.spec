Summary:	Input module of Qt for Korean using Hangul engine
Summary(pl.UTF-8):	Moduł wejściowy Qt dla języka koreańskiego wykorzystujący silnik Hangul
Name:		qt-im-hangul
Version:	0.2.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
#Source0Download: https://github.com/choehwanjin/qimhangul/releases
Source0:	https://github.com/choehwanjin/qimhangul/archive/qimhangul-%{version}.tar.gz
# Source0-md5:	c870f01b027b882d577cea98a55557c0
Patch0:		%{name}-sh.patch
URL:		https://github.com/choehwanjin/qimhangul
BuildRequires:	QtGui-devel >= 4.0.0
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake
BuildRequires:	libhangul-devel >= 0.0.12
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Input module of Qt for Korean using Hangul engine.

%description -l pl.UTF-8
Moduł wejściowy Qt dla języka koreańskiego wykorzystujący silnik
Hangul.

%package -n QtGui-inputmethod-hangul
Summary:	Input module of Qt 4 for Korean using Hangul engine
Summary(pl.UTF-8):	Moduł wejściowy Qt 4 dla języka koreańskiego wykorzystujący silnik Hangul
Group:		X11/Libraries
Requires:	QtGui >= 4.0.0
Requires:	libhangul >= 0.0.12

%description -n QtGui-inputmethod-hangul
Input module of Qt 4 for Korean using Hangul engine.

%description -n QtGui-inputmethod-hangul -l pl.UTF-8
Moduł wejściowy Qt 4 dla języka koreańskiego wykorzystujący silnik
Hangul.

%prep
%setup -q -n qimhangul-qimhangul-%{version}
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
PATH="%{_libdir}/qt4/bin:$PATH"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/qt4/plugins/inputmethods/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -n QtGui-inputmethod-hangul
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/qt4/plugins/inputmethods/libqimhangul.so
