#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	ManyParams
Summary:	Test::ManyParams - module to test many params as one test
Summary(pl):	Test::ManyParams - modu³ do testowania wielu parametrów podczas jednego testu
Name:		perl-Test-ManyParams
Version:	0.08
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bd412fb68f57e4ab8d7d2cb8b79d35bd
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Readonly
BuildRequires:	perl-Set-CrossProduct
BuildRequires:	perl-Test-Builder-Tester
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module helps to tests many parameters at once. In general, it
calls the given subroutine with every combination of the given
parameter values. The combinations are created with building a cross
product.

%description -l pl
Ten modu³ jest pomocny przy testowania wielu parametrów naraz.
Ogólnie, wywo³uje on podan± funkcjê we wszystkich kombinacjach
podanych warto¶ci parametrów. Kombinacje s± tworzone poprzez iloczyn
kartezjañski.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
