%define upstream_name    ParseLex
%define upstream_version 2.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Generator of lexical analyzers 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PV/PVERD/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Parse::Template)

BuildArch:	noarch

%description
The Parse::Lex.pm module for perl5 is an object-oriented generator of
lexical analyzers.

This distribution includes Parse::YYLex (writed by Vladimir Alexiev)
a lexer generator that you can use with yacc parsers.

A collection of examples demonstrating various
Parse::Lex/Parse::LevEvent features can be found in the "examples"
directory.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README examples
%{perl_vendorlib}/Parse
%{_mandir}/*/*

%changelog
* Mon Aug 16 2010 Jérôme Quelin <jquelin@mandriva.org> 2.200.0-1mdv2011.0
+ Revision: 570553
- update to 2.20

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 2.190.0-2mdv2011.0
+ Revision: 528236
- adding missing buildrequires:
- rebuild
- update to 2.19
- update to 2.18

* Sun Feb 28 2010 Jérôme Quelin <jquelin@mandriva.org> 2.180.0-1mdv2010.1
+ Revision: 512598
- update to 2.18

* Mon Jan 11 2010 Jérôme Quelin <jquelin@mandriva.org> 2.170.0-1mdv2010.1
+ Revision: 489642
- update to 2.17

* Mon Dec 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.150.0-2mdv2010.1
+ Revision: 474512
- no tabs in spec file
- fix package name
- package renaming according to perl packaging policvy
- rename the package to perl-ParseLex, as perl perl packaging policy
- fix package naming

  + Jérôme Quelin <jquelin@mandriva.org>
    - renamed package to perl-Parse-Lex
    - renamed perl-ParseLex to perl-Parse-Lex

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 2.150.0-1mdv2010.0
+ Revision: 399727
- forgot to change real rpm name
- renamed package perl-ParseLex to perl-Parse-Lex
- renamed package to perl-Parse-Lex to follow mandriva conventions (yes,
  author is brain-dead)
- using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.15-5mdv2009.0
+ Revision: 258191
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.15-4mdv2009.0
+ Revision: 246269
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.15-2mdv2008.1
+ Revision: 136330
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.15-2mdv2008.0
+ Revision: 86785
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 2.15-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.15-1mdk
- initial Mandriva package

