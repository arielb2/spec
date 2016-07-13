%if 0%{?fedora}
%global with_python3 1
%endif

%global modname fabulous

Name:             python-fabulous
Version:          0.1.5
Release:          11%{?dist}
Summary:          Makes your terminal output totally fabulous

Group:            Development/Languages
License:          MIT
URL:              http://pypi.python.org/pypi/%{modname}
Source0:          http://lobstertech.com/media/file/%{modname}/%{modname}-%{version}.tar.gz
Patch0:           0001-Unbundle-fonts.patch

BuildArch:        noarch

BuildRequires:    dos2unix
BuildRequires:    gcc
BuildRequires:    make
BuildRequires:    python2-devel
BuildRequires:    python-setuptools
BuildRequires:    python-sphinx

Requires:         python-imaging
Requires:         python-grapefruit

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
%endif

%description
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

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1
%{__rm} -f fabulous/fonts/*
%{__rm} fabulous/_xterm256.c
dos2unix README

%build
%{__python} setup.py build 

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

PYTHONPATH=$(pwd) make -C docs html
%{__rm} -f docs/_build/html/.buildinfo


%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
%endif

%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc README COPYING docs/_build/html

%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-*

%if 0%{?with_python3}
%files -n python3-fabulous
%doc README COPYING docs/_build/html
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*
%endif

%changelog
* Thu Jun 30 2016 Ariel O. Barria <ariel.o.barria@gmail.com> - 0.1.5-12
- Rebuilt for Python3

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
