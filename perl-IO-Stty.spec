%define		pdir	IO
%define		pnam	Stty
%include	/usr/lib/rpm/macros.perl
Summary:	IO::Stty Perl module
Summary(cs.UTF-8):	Modul IO::Stty pro Perl
Summary(da.UTF-8):	Perlmodul IO::Stty
Summary(de.UTF-8):	IO::Stty Perl Modul
Summary(es.UTF-8):	Módulo de Perl IO::Stty
Summary(fr.UTF-8):	Module Perl IO::Stty
Summary(it.UTF-8):	Modulo di Perl IO::Stty
Summary(ja.UTF-8):	IO::Stty Perl モジュール
Summary(ko.UTF-8):	IO::Stty 펄 모줄
Summary(nb.UTF-8):	Perlmodul IO::Stty
Summary(pl.UTF-8):	Moduł perla IO::Stty
Summary(pt_BR.UTF-8):	Módulo Perl IO::Stty
Summary(pt.UTF-8):	Módulo de Perl IO::Stty
Summary(ru.UTF-8):	Модуль для Perl IO::Stty
Summary(sv.UTF-8):	IO::Stty Perlmodul
Summary(uk.UTF-8):	Модуль для Perl IO::Stty
Summary(zh_CN.UTF-8):	IO::Stty Perl 模块
Name:		perl-IO-Stty
Version:	02
Release:	9
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-.%{version}.tar.gz
# Source0-md5:	db2919cf267fce93682f0f854359f04e
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/IO-Stty/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Stty is a module for setting terminal parameters.

%description -l pl.UTF-8
IO::Stty jest modułem służącym do ustawiania parametrów terminala.

%prep
%setup -q -n %{pdir}-%{pnam}-.%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README stty.txt
%{perl_vendorlib}/IO/Stty.pm
%attr(755,root,root) %{perl_vendorlib}/IO/stty.pl
