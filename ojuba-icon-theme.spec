Name:           ojuba-icon-theme
Version:        5
Release:        1%{?dist}
Summary:        ojuba icon theme
Group:          User Interface/Desktops
License:        Waqf
URL:            http://www.ojuba.org
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires(post): gtk2 >= 2.6.0
Requires(postun): gtk2 >= 2.6.0
# requires gnome-themes for Mist
Requires:       gnome-themes
Provides:       system-icon-theme

%description
This package contains the ojuba icon theme.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
rm ojuba-crystal/scalable/places/start-here.svg
rm Ojuba/scalable/places/start-here.svg
./render.sh
mkdir -p %{buildroot}%{_datadir}/icons
for i in ojuba-crystal Ojuba;do
  cp -r --preserve=timestamps $i %{buildroot}%{_datadir}/icons
  touch %{buildroot}%{_datadir}/icons/$i/icon-theme.cache
done

%post
for i in ojuba-crystal Ojuba;do
touch --no-create %{_datadir}/icons/$i || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache -f --quiet %{_datadir}/icons/$i || :
fi
done

%postun
for i in ojuba-crystal Ojuba;do
touch --no-create %{_datadir}/icons/$i || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache -f --quiet %{_datadir}/icons/$i || :
fi
done

%clean
rm -rf %{buildroot}


%files
%defattr(0644,root,root,0755)
%doc LICENSE
%{_datadir}/icons/*
%ghost %{_datadir}/icons/*/icon-theme.cache


%changelog
* Thu Jun 15 2010  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 4-6
- update for ojuba 4

* Mon Jul 20 2009  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 3-1
- update for ojuba 3
- render png images using render.sh

* Wed Jan 21 2009  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 1-6
- fix "Inherits"

* Fri Jul 04 2008  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 1-5
- fix index.theme files

* Fri Jul 04 2008  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 1-4
- Add Ojuba Mist icons

* Fri Jul 04 2008  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 1-3
- Add a crystal folder

* Wed Jun 25 2008 Muayyad Saleh AlSadi <alsadi@ojuba.org> - 1-2
- minor changes

* Wed Jun 25 2008 Muayyad Saleh AlSadi <alsadi@ojuba.org> - 1-1
- Initial RPM.

