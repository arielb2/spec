%if 0%{?fedora}
%global with_python3 1
%endif

%global modname grapefruit
%global snapshot_date 20110710
%global snapshot_revision 31

Name:		python-grapefruit
Version:	0.1a3
Release:	1%{?dist}
Summary:	Python module for easy manipulation of color information

Group:		Development/Libraries
License:	ASL 2.0
URL:	        https://github.com/xav/%{modname}%	
Source0:	https://github.com/downloads/xav/Grapefruit/%{modname}-%{version}.tar.tar.gz
BuildArch:	noarch
BuildRequires:	python2-devel
%description
GrapeFruit is a pure python module that let you easily manipulate and convert
color information. It's primary goal is to be natural and flexible.

%if 0%{?with_python3}
%package -n python3-grapefruit
Summary:        Python module for easy manipulation of color information

Group:          Development/Libraries
BuildRequires:  python3-devel
%description -n python3-grapefruit
GrapeFruit is a pure python module that let you easily manipulate and convert
color information. It's primary goal is to be natural and flexible.

%endif
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%prep
%setup -q -c %{modname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%if 0%{?with_python3}
#pushd %{py3dir}
#CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
#popd
%py3_build
%endif

%install
%{__python} setup.py install --skip-build --root="$RPM_BUILD_ROOT"
chmod 655 $RPM_BUILD_ROOT%{python_sitelib}/grapefruit.py
sed -i 's/\r//' CHANGES LICENSE TODO doc/Makefile doc/index.rst doc/conf.py doc/makedoc.cmd

%if 0%{?with_python3}
#pushd %{py3dir}
#%{__python3} setup.py install --skip-build --root="$RPM_BUILD_ROOT"
%py3_install
chmod 655 $RPM_BUILD_ROOT%{python3_sitelib}/grapefruit.py
sed -i 's/\r//' CHANGES LICENSE TODO doc/Makefile doc/index.rst doc/conf.py doc/makedoc.cmd
#popd
%endif

%files
%doc doc/ CHANGES COPYING README LICENSE TODO
%{python_sitelib}/*.egg-info
%{python_sitelib}/grapefruit.py*

%if 0%{?with_python3}
%files -n python3-grapefruit
%doc doc/ CHANGES COPYING README LICENSE TODO
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/grapefruit.py*
%endif
%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1a3-9.20110710svn31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1a3-8.20110710svn31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1a3-7.20110710svn31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1a3-6.20110710svn31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1a3-5.20110710svn31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1a3-4.20110710svn31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1a3-3.20110710svn31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.1a3-2.20110710svn31
- Fix summary to be shorter than 80 characters
- Clean up spec file

* Sun Jul 10 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.1a3-1.20110710svn31
- Initial RPM release
