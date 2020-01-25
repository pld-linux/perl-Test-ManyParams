#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Test
%define		pnam	ManyParams
Summary:	Test::ManyParams - module to test many params as one test
Summary(pl.UTF-8):	Test::ManyParams - moduł do testowania wielu parametrów podczas jednego testu
Name:		perl-Test-ManyParams
Version:	0.10
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ba8534916c50206985beda77720c671b
URL:		http://search.cpan.org/dist/Test-ManyParams/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Readonly
BuildRequires:	perl-Set-CrossProduct
BuildRequires:	perl-Test-Builder-Tester
BuildRequires:	perl-Test-Differences
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module helps to tests many parameters at once. In general, it
calls the given subroutine with every combination of the given
parameter values. The combinations are created with building a cross
product.

%description -l pl.UTF-8
Ten moduł jest pomocny przy testowania wielu parametrów naraz.
Ogólnie, wywołuje on podaną funkcję we wszystkich kombinacjach
podanych wartości parametrów. Kombinacje są tworzone poprzez iloczyn
kartezjański.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
