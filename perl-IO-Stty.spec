%include	/usr/lib/rpm/macros.perl
Summary:	IO-Stty perl module
Summary(pl):	Modu³ perla IO-Stty
Name:		perl-IO-Stty
Version:	02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/IO-Stty-.%{version}.tar.gz
Patch:		perl-IO-Stty-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO-Stty is a module for setting terminal parameters. 

%description -l pl
IO-Stty jest modu³em s³u¿±cym do ustawiania parametrów terminala.

%prep
%setup -q -n IO-Stty-.%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/IO/Stty
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf README *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,stty.txt}.gz

%{perl_sitelib}/IO/Stty.pm
%{perl_sitelib}/IO/stty.pl
%{perl_sitearch}/auto/IO/Stty
