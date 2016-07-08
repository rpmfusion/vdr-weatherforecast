%global pname   weatherforecast

Name:           vdr-weatherforecast
Version:        0.2.0
Release:        1%{?dist}
Summary:        A VDR plugin which provides a weather forecast 

Group:          Applications/Multimedia
License:        GPLv2+ and BSD
URL:            http://projects.vdr-developer.org/projects/plg-weatherforecast
Source0:        http://projects.vdr-developer.org/git/vdr-plugin-%{pname}.git/snapshot/vdr-plugin-%{pname}-%{version}.tar.bz2
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf

BuildRequires:  vdr-devel >= 1.7.22
BuildRequires:  libcurl-devel
BuildRequires:  jansson-devel
BuildRequires:  libskindesignerapi-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
WeatherForecast provides a weather forecast based on forecast.io data.

%prep
%setup -q -n vdr-plugin-%{pname}-%{version}

%build
make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" %{?_smp_mflags} all

%install
make install DESTDIR=%{buildroot}
# weatherforecast.conf
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf


%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}


%changelog
* Sun Jan 31 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Sat Oct 03 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.1-2
- added BSD to the License tag

* Sun Apr 12 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1
- added BR libskindesignerapi-devel

* Fri Mar 13 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.0.3-1
- Update to 0.0.3

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.0.2-3
- Rebuild

* Mon Feb 02 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.0.2-2
- Mark license files as %%license where available
- Defined global macro pname for program name

* Sat Jan 17 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.0.2-1
- Update to 0.0.2

* Thu Jan 15 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.0.1-1
- Initial build

