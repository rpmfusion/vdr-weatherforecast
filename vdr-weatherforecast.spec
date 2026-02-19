%global pname   weatherforecast

# Set vdr_version based on Fedora version
# Default
%global vdr_version 2.6.9

%if 0%{?fedora} == 42
%global vdr_version 2.7.4
%elif 0%{?fedora} == 43
%global vdr_version 2.7.7
%elif 0%{?fedora} >= 44
%global vdr_version 2.7.9
%endif

Name:           vdr-weatherforecast
Version:        0.2.0
Release:        41%{?dist}
Summary:        A VDR plugin which provides a weather forecast 
License:        GPL-2.0-or-later AND BSD-2-Clause
URL:            https://github.com/vdr-projects/vdr-plugin-weatherforecast
Source0:        https://github.com/vdr-projects/vdr-plugin-%{pname}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  libcurl-devel
BuildRequires:  jansson-devel
BuildRequires:  libskindesignerapi-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
WeatherForecast provides a weather forecast based on forecast.io data.

%prep
%setup -q -n vdr-plugin-%{pname}-%{version}

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC"

%install
%make_install
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
* Mon Feb 09 2026 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-41
- Rebuilt for new VDR API version 2.7.9

* Tue Feb 03 2026 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-40
- Rebuilt for new VDR API version 2.7.8

* Mon Feb 02 2026 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Aug 01 2025 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-38
- Rebuilt for new VDR API version 2.7.7

* Sun Jul 27 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jun 21 2025 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-36
- Rebuilt for new VDR API version 2.7.6

* Tue May 27 2025 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-35
- Rebuilt for new VDR API version 2.7.5

* Sun Mar 16 2025 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-34
- Rebuilt for new VDR API version 2.7.4

* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-32
- Rebuilt for new VDR API version 2.7.3

* Fri Jul 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-31
- Rebuilt for new VDR API version 2.6.9

* Sun Apr 21 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-30
- Rebuilt for new VDR API version

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-28
- Rebuilt for new VDR API version

* Tue Jan 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-27
- Rebuilt for new VDR API version
- Add BR gettext for rawhide

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Dec 18 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-25
- Rebuilt for new VDR API version

* Sat Dec 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-24
- Update URL address
- Rebuilt for new VDR API version

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Mon Apr 11 2022 Sérgio Basto <sergio@serjux.com> - 0.2.0-22
- Rebuilt for VDR 2.6.1

* Sat Feb 05 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-21
- Rebuilt for new VDR API version

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-20
- Rebuilt for new VDR API version

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-17
- Rebuilt for new VDR API version

* Wed Oct 21 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-16
- Rebuilt for new VDR API version

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-15
- Rebuilt for new VDR API version

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-11
- Rebuilt for new VDR API version 2.4.1

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-10
- Rebuilt for new VDR API version

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-8
- Add BR gcc-c++

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.2.0-7
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-5
- Rebuilt for vdr-2.4.0

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

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

