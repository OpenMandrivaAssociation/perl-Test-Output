%define modname	Test-Output
%define modver 1.033

Summary:	Utilities to test STDOUT and STDERR messages
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Test::Output
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Output-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Tester)

%description
Test::Output provides a simple interface for testing output sent to STDOUT
or STDERR. A number of different utilies are included to try and be as
flexible as possible to the tester.

Originally this module was designed not to have external requirements, 
however, the features provided by L<Sub::Exporter> over what L<Exporter>
provides is just to great to pass up.

Test::Output ties STDOUT and STDERR using Test::Output::Tie.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{perl_vendorlib}/*
%{_mandir}/man3/*
