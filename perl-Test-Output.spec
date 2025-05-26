%define modname	Test-Output
%bcond_without tests

Summary:	Utilities to test STDOUT and STDERR messages
Name:		perl-%{modname}
Version:	1.036
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Test::Output
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Output-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Tester)
%if %{with tests}
BuildRequires:	perl(Capture::Tiny)
%endif

%description
Test::Output provides a simple interface for testing output sent to STDOUT
or STDERR. A number of different utilies are included to try and be as
flexible as possible to the tester.

Originally this module was designed not to have external requirements, 
however, the features provided by L<Sub::Exporter> over what L<Exporter>
provides is just to great to pass up.

Test::Output ties STDOUT and STDERR using Test::Output::Tie.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%if %{with tests}
%check
%make_build test
%endif

%install
%make_install

%files
%doc Changes META.yml
%{perl_vendorlib}/*
%{_mandir}/man3/*
