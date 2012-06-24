Summary:	Collection of tools to make administering DNS easier
Summary(pl):	Zestaw narz�dzi u�atwiaj�cych administrowanie DNS-em
Name:		dnsutl
Version:	1.8
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/dnsutl/%{name}-%{version}.tar.gz
# Source0-md5:	10f47572221b7376a07449ac0ff62fdc
URL:		http://dnsutl.sourceforge.net/
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir	%{_prefix}/sbin

%description
The dnsutl package is a collection tools to make administering DNS
easier.

These include:
- dns-rev: Take the forward DNS mapping and generate the reverse
  mapping. This is useful for producing a self-consistent DNS
  configuration.
- dns-ethers: By using a bogus record type, you can keep the MAC
  address with the IP address, and generate the /etc/ethers file.
- dns-hosts: Take the forward DNS mapping and generate the /etc/hosts
  file.
- dns-bootp: Using the MAC and IP information, you can generate the
  /etc/bootptab file.
- dns-ng: Take the forward DNS mapping and generate the /etc/netgroup
  file.
- dns-bootparams: Using the MAC and IP information, you can generate
  the Sun /etc/bootparams file.
- dns-boot-check: Check your named(8) configuration for self-
  consistency.
- dns-hosts-import: Turn your /etc/hosts file into a DNS forward map,
  as a first step to configuring your DNS server.
- dns-dhcp: Using the MAC and IP information, you can generate the
  /etc/dhcp.conf file.

All of these programs are both faster than shell scripts, and more
robust when faced with all the peculiar semantics of DNS resource
files. They even understand the $include directive.

%description -l pl
Pakiet dnsutl to zestaw narz�dzi u�atwiaj�cych administrowanie DNS-em.
Zawiera:
- dns-rev - generowanie odwrotnych odwzorowa� DNS na podstawie
  prostych; przydatne do tworzenia samodzielnej konfiguracji DNS.
- dns-ethers - u�ywaj�c fa�szywego rodzaju rekordu mo�na przechowywa�
  adresy MAC wraz z adresami IP i generowa� plik /etc/ethers.
- dns-hosts - pobieranie prostego odwzorowania DNS i generowanie pliku
  /etc/hosts.
- dns-bootp - generowanie pliku /etc/bootptab na podstawie informacji
  o adresach MAC i IP.
- dns-ng - pobieranie prostego odwzorowania DNS i generowanie pliku
  /etc/netgroup.
- dns-bootparams - przy u�yciu informacji o adresach MAC i IP pozwala
  generowa� plik /etc/bootparams dla Suna.
- dns-boot-check - sprawdzanie konfiguracji serwera named(8) pod k�tem
  samodzielno�ci.
- dns-hosts-import - zamiana pliku /etc/hosts na odwzorowanie proste
  DNS jako pierwszy krok do konfiguracji serwera DNS.
- dns-dhcp - przy u�yciu informacji o adresach MAC i IP pozwala
  generowa� plik /etc/dhcp.conf.

Wszystkie te programy s� szybsze ni� skrypty pow�oki i przydatniejsze
w po��czeniu ze szczeg�ln� semantyk� plik�w zasob�w DNS. Rozumiej�
nawet dyrektyw� $include.

%prep
%setup -q

%build
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
%{__make} install -j1 \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/dns-boot-check
%attr(755,root,root) %{_bindir}/dns-bootp
%attr(755,root,root) %{_bindir}/dns-bootparams
%attr(755,root,root) %{_bindir}/dns-dhcp
%attr(755,root,root) %{_bindir}/dns-ethers
%attr(755,root,root) %{_bindir}/dns-ethers-import
%attr(755,root,root) %{_bindir}/dns-filter
%attr(755,root,root) %{_bindir}/dns-hosts
%attr(755,root,root) %{_bindir}/dns-hosts-import
%attr(755,root,root) %{_bindir}/dns-ng
%attr(755,root,root) %{_bindir}/dns-rev
%{_mandir}/man1/dns-boot-check.1*
%{_mandir}/man1/dns-bootp.1*
%{_mandir}/man1/dns-bootparams.1*
%{_mandir}/man1/dns-dhcp.1*
%{_mandir}/man1/dns-ethers-import.1*
%{_mandir}/man1/dns-ethers.1*
%{_mandir}/man1/dns-filter.1*
%{_mandir}/man1/dns-hosts-import.1*
%{_mandir}/man1/dns-hosts.1*
%{_mandir}/man1/dns-license.1*
%{_mandir}/man1/dns-ng.1*
%{_mandir}/man1/dns-rev.1*
