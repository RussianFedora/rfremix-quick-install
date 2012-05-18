Summary:	RFRemix kickstarts and repos
Name:		rfremix-quick-install
Version:	17
Release:	0.3%{?dist}

License:	GPLv2
Group:		System Environment/Base
URL:		http://russianfedora.ru
Source:		%{name}-%{version}.tar.bz2

BuildArch:	noarch

%description
It is kickstart files and netinstall repos for lorax and
Anaconda only.

%prep
%setup -q


%build
# Nothing to build


%install
rm -rf %{buildroot}

# Install rfremixconf
install -d -m 755 %{buildroot}%{_sysconfdir}/yum.repos.d

install -m 644 *.cfg %{buildroot}
install -m 644 *.repo %{buildroot}%{_sysconfdir}/yum.repos.d

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_sysconfdir}/yum.repos.d/*
/*.cfg


%changelog
* Fri May 18 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 17-0.3.R
- do not include @office to kde ks quick install file. We use
  @desktop-minimal

* Sat Mar 10 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 17-0.2.R
- place files to another directories

* Fri Mar  9 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 17-0.1.R
- initial build
