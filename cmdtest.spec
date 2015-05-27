#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cmdtest
Version  : 0.14.orig
Release  : 3
URL      : http://code.liw.fi/debian/pool/main/c/cmdtest/cmdtest_0.14.orig.tar.gz
Source0  : http://code.liw.fi/debian/pool/main/c/cmdtest/cmdtest_0.14.orig.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: cmdtest-bin
Requires: cmdtest-python
Requires: cmdtest-doc
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-cliapp
BuildRequires : python-dev
BuildRequires : python-ttystatus
BuildRequires : setuptools

%description
==================
This project consists of two programs: the original `cmdtest`,
and the newer `yarn`. Both are black box testing tools for Unix
command line tools.

%package bin
Summary: bin components for the cmdtest package.
Group: Binaries

%description bin
bin components for the cmdtest package.


%package doc
Summary: doc components for the cmdtest package.
Group: Documentation

%description doc
doc components for the cmdtest package.


%package python
Summary: python components for the cmdtest package.
Group: Default

%description python
python components for the cmdtest package.


%prep
%setup -q -n cmdtest-0.14

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cmdtest
/usr/bin/yarn

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
