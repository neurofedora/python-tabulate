%global modname tabulate

Name:           python-%{modname}
Version:        0.7.5
Release:        1%{?dist}
Summary:        Pretty-print tabular data in Python, a library and a command-line utility

License:        MIT
URL:            https://pypi.python.org/pypi/tabulate
Source0:        https://bitbucket.org/astanin/%{name}/get/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
The main use cases of the library are:

* printing small tables without hassle: just one function call, formatting is
  guided by the data itself
* authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
* readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python2-setuptools
# Test deps
BuildRequires:  python2-nose
%if 0%{?fedora} > 23
BuildRequires:  python2-numpy
%else
BuildRequires:  numpy
%endif

%description -n python2-%{modname}
The main use cases of the library are:

* printing small tables without hassle: just one function call, formatting is
  guided by the data itself
* authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
* readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools
# Test deps
BuildRequires:  python3-nose
BuildRequires:  python3-numpy

%description -n python3-%{modname}
The main use cases of the library are:

* printing small tables without hassle: just one function call, formatting is
  guided by the data itself
* authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
* readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point

Python 3 version.

%prep
%autosetup -n astanin-%{name}-3830da89c6c1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

pushd %{buildroot}%{_bindir}
  mv %{modname} %{modname}-%{python3_version}
  ln -s %{modname}-%{python3_version} %{modname}
  ln -s %{modname}-%{python3_version} %{modname}-3
  cp %{modname}-%{python3_version} %{modname}-%{python2_version}
  sed -i -e "1s/python3/python2/" %{modname}-%{python2_version}
  ln -s %{modname}-%{python2_version} %{modname}-2
popd

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{modname}
%license LICENSE
%doc README.rst
%{_bindir}/%{modname}-2
%{_bindir}/%{modname}-%{python2_version}
%{python2_sitelib}/%{modname}*.egg-info/
%{python2_sitelib}/%{modname}.py*

%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{_bindir}/%{modname}
%{_bindir}/%{modname}-3
%{_bindir}/%{modname}-%{python3_version}
%{python3_sitelib}/%{modname}*.egg-info/
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
* Tue Nov 24 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.5-1
- Initial package
