%include	/usr/lib/rpm/macros.perl
Summary:	IO::Stty perl module
Summary(pl):	Modu� perla IO::Stty
Name:		perl-IO-Stty
Version:	02
Release:	6
License:	unknown
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/IO/IO-Stty-.%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Stty is a module for setting terminal parameters.

%description -l pl
IO::Stty jest modu�em s�u��cym do ustawiania parametr�w terminala.

%prep
%setup -q -n IO-Stty-.%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README stty.txt
%{perl_sitelib}/IO/Stty.pm
%{perl_sitelib}/IO/stty.pl
