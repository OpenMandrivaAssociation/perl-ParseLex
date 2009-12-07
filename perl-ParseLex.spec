%define upstream_name    ParseLex
%define upstream_version 2.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2
Summary:	Generator of lexical analyzers 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/P/PV/PVERD/%{upstream_name}-%{upstream_version}.tar.bz2
Obsoletes: perl-Parse-Lex
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

# make test won't work...
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README examples
%{perl_vendorlib}/Parse
%{_mandir}/*/*
