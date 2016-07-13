%if 0%{?fedora}
%global with_python3 1
%endif

%global modname fabulous

Name:             python-fabulous
Version:          0.3.0
Release:          2%{?dist}
Summary:          Makes your terminal output totally fabulous
Group:            Development/Languages
License:          Apache 2.0 / OFL 
URL:              https://jart.github.io/%{modname}
Source0:          https://github.com/jart/fabulous/releases/download/%{version}/%{modname}-%{version}.tar.gz
Patch0:           python-fabulous-unbundle-fonts.patch
BuildArch:        noarch

BuildRequires:    dos2unix
BuildRequires:    gcc
BuildRequires:    make

%description
fabulous is a python module for producing fabulously colored terminal output.

Run the demo to see what's available::

    $ python -m fabulous.demo

%package -n python2-fabulous
Summary:          Makes your terminal output totally fabulous
Group:            Development/Languages
%{?python_provide:%python_provide python2-fabulous}

BuildRequires:    python2-devel
BuildRequires:    python-setuptools

Requires:         python-imaging
Requires:         python-grapefruit

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
%endif

%description -n python2-fabulous
fabulous is a python module for producing fabulously colored terminal output.

Run the demo to see what's available::

    $ python -m fabulous.demo

%if 0%{?with_python3}
%package -n python3-fabulous
Summary:          Makes your terminal output totally fabulous

Group:            Development/Languages

Requires:         python3-imaging

%description -n python3-fabulous
fabulous is a python module for producing fabulously colored terminal output.

Run the demo to see what's available::

    $ python3 -m fabulous.demo
%endif

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1
%{__rm} -f fabulous/fonts/*
%{__rm} fabulous/_xterm256.c
dos2unix README.rst

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%files -n python2-fabulous
%doc README.rst CONTRIBUTORS AUTHORS
%license LICENSE.txt
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{modname}-%{version}-*
%{_bindir}/fabulous-demo
%{_bindir}/fabulous-gotham
%{_bindir}/fabulous-image
%{_bindir}/fabulous-rotatingcube
%{_bindir}/fabulous-text

%if 0%{?with_python3}
%files -n python3-fabulous
%doc README.rst CONTRIBUTORS AUTHORS
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*
%{_bindir}/fabulous-demo
%{_bindir}/fabulous-gotham
%{_bindir}/fabulous-image
%{_bindir}/fabulous-rotatingcube
%{_bindir}/fabulous-text
%endif

%changelog
* Fri Jul 08 2016 Ralph Bean <rbean@redhat.com> - 0.2.1-1
- new version

* Thu Jul 07 2016 Ralph Bean <rbean@redhat.com> - 0.2.0-2
- Put balls.png in the right place.
  https://github.com/jart/fabulous/pull/10

* Tue Jul 05 2016 Ralph Bean <rbean@redhat.com> - 0.2.0-1
- new version
- Modernize python macros.
- Make explicit python2 subpackage.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 14 2014 Ralph Bean <rbean@redhat.com> - 0.1.5-9
- Rebuilt for epel7

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Ralph Bean <rbean@redhat.com> - 0.1.5-6
- Removed unnecssary defattr
- More specific directory ownership in files section

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 22 2012 Ralph Bean <rbean@redhat.com> - 0.1.5-4
- Built and included sphinx docs

* Sun Apr 22 2012 Ralph Bean <rbean@redhat.com> - 0.1.5-3
- Fresh .tar.gz from upstream.
- Run dos2unix on README.
- Remove _xterm256.c

* Sun Apr 22 2012 Ralph Bean <rbean@redhat.com> - 0.1.5-2
- Included README and COPYING in the doc macro
- Began using modname and version for upstream Source0 URL
- Patched out the bundled fonts.

* Thu Apr 05 2012 Ralph Bean <rbean@redhat.com> - 0.1.5-1
- initial package for Fedora
