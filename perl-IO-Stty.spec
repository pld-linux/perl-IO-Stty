%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	Stty
Summary:	IO::Stty Perl module
Summary(cs):	Modul IO::Stty pro Perl
Summary(da):	Perlmodul IO::Stty
Summary(de):	IO::Stty Perl Modul
Summary(es):	Módulo de Perl IO::Stty
Summary(fr):	Module Perl IO::Stty
Summary(it):	Modulo di Perl IO::Stty
Summary(ja):	IO::Stty Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	IO::Stty ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul IO::Stty
Summary(pl):	Modu³ perla IO::Stty
Summary(pt_BR):	Módulo Perl IO::Stty
Summary(pt):	Módulo de Perl IO::Stty
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl IO::Stty
Summary(sv):	IO::Stty Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl IO::Stty
Summary(zh_CN):	IO::Stty Perl Ä£¿é
Name:		perl-IO-Stty
Version:	02
Release:	7
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-.%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Stty is a module for setting terminal parameters.

%description -l pl
IO::Stty jest modu³em s³u¿±cym do ustawiania parametrów terminala.

%prep
%setup -q -n %{pdir}-%{pnam}-.%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README stty.txt
%{perl_vendorlib}/IO/Stty.pm
%attr(755,root,root) %{perl_vendorlib}/IO/stty.pl
