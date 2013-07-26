%define upstream_name    Test-Output
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.02
Release:	1

Summary:	Utilities to test STDOUT and STDERR messages
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Output-1.02.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Tester)
BuildArch:	noarch

%description
Test::Output provides a simple interface for testing output sent to STDOUT
or STDERR. A number of different utilies are included to try and be as
flexible as possible to the tester.

Originally this module was designed not to have external requirements, 
however, the features provided by L<Sub::Exporter> over what L<Exporter>
provides is just to great to pass up.

Test::Output ties STDOUT and STDERR using Test::Output::Tie.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 662212
- update to new version 1.01

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.160.0-2
+ Revision: 658428
- rebuild for updates rpm-setup

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 401519
- rebuild using %%perl_convert_version
- fixed license field

* Sat May 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.16-1mdv2010.0
+ Revision: 376345
- update to new version 0.16

* Wed May 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.15-1mdv2010.0
+ Revision: 375276
- update to new version 0.15

* Tue May 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.14-1mdv2010.0
+ Revision: 374887
- updated to 0.14

* Tue Mar 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.13-1mdv2009.1
+ Revision: 353458
- update to new version 0.13

* Sun Oct 26 2008 Jérôme Quelin <jquelin@mandriva.org> 0.12-1mdv2009.1
+ Revision: 297381
- update to new version 0.12

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.10-4mdv2009.0
+ Revision: 258575
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.10-3mdv2009.0
+ Revision: 246545
- rebuild
- fix summary-ended-with-dot

* Mon Jan 07 2008 Jérôme Quelin <jquelin@mandriva.org> 0.10-1mdv2008.1
+ Revision: 146316
- import perl-Test-Output



