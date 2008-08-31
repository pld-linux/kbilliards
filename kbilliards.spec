Summary:	kbilliards - a funny billiards simulator
Summary(de.UTF-8):	kbilliards - ein lustiger Billiard Simulator
Summary(pl.UTF-8):	kbilliards - zabawny symulator bilarda
Name:		kbilliards
Version:	0.8.7
Release:	0.5
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.hostnotfound.it/kbilliards/%{name}-%{version}b.tar.bz2
# Source0-md5:	f773a0a860ac0cb678f5e736860a0fe9
Patch0:		%{name}-rand.patch
Patch1:		%{name}-am.patch
Patch2:		kde-ac260.patch
URL:		http://www.hostnotfound.it/kbilliards.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A funny billiards simulator game, under KDE.

%description -l de.UTF-8
Ein lustiger Billiard Simulator unter KDE.

%description -l pl.UTF-8
Zabawny symulator bilarda pod KDE.

%prep
%setup -q -n %{name}-%{version}b
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f Makefile.cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kbilliards*
%{_desktopdir}/kbilliards.desktop
%{_iconsdir}/hicolor/*/*/*.png
