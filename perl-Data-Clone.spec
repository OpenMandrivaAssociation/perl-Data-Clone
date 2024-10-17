%define upstream_name    Data-Clone
%define upstream_version 0.003

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Polymorphic data cloning
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Devel::PPPort)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::ParseXS)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(XSLoader)
BuildRequires:	perl(parent)
BuildRequires:	perl-devel

%description
'Data::Clone' does data cloning, i.e. copies things recursively. This is
smart so that it works with not only non-blessed references, but also with
blessed references (i.e. objects). When 'clone()' finds an object, it calls
a 'clone' method of the object if the object has a 'clone', otherwise it
makes a surface copy of the object. That is, this module does polymorphic
data cloning.

Although there are several modules on CPAN which can clone data, this
module has a different cloning policy from almost all of them. See the
/Cloning policy manpage and the /Comparison to other cloning modules
manpage for details.

Cloning policy
    A cloning policy is a rule that how a cloning routine copies data. Here
    is the cloning policy of 'Data::Clone'.

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
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

