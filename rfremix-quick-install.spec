Summary:	RFRemix kickstarts and repos
Name:		rfremix-quick-install
Version:	17
Release:	0.1%{?dist}

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
install -d -m 755 %{buildroot}%{_sysconfdir}/quick-install/repos
install -d -m 755 %{buildroot}%{_sysconfdir}/quick-install/ks

install -m 644 *.cfg %{buildroot}%{_sysconfdir}/quick-install/ks
install -m 644 *.repo %{buildroot}%{_sysconfdir}/quick-install/repos

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_sysconfdir}/quick-install/repos/*.repo
%{_sysconfdir}/quick-install/ks/*.cfg


%changelog
* Fri Mar  9 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 17-0.1.R
- initial build
