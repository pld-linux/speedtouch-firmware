Summary:	Alcatel SpeedTouch USB ADSL modem firmware
Summary(pl):	Firmware dla modemu ADSL Alcatel SpeedTouch w wersji USB
Name:		speedtouch-firmware
Version:	1.3.4
Release:	2
License:	restricted, non-distributable
Group:		Libraries
# get it from Alcatel at http://www.speedtouchdsl.com/dvrreg_lx.htm (requires registration)
# or from Neostrada CD (Linux/ThomsonST330/pliki.tar.gz#utar:drivers)
Source0:	speedmgmt.tar.gz
# NoSource0-md5: 102dc7a457c3942ee21dc834db68eac2
NoSource:	0
URL:		http://www.speedtouchdsl.com/
Requires:	speedtouch >= 1.2-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alcatel SpeedTouch USB ADSL modem firmware, needed for modem_run
utility (speedtouch package). Load it by:

modem_run [-k] -m -f /usr/share/speedtouch/mgmt.o

(-k if you are using kernel driver from Linux 2.4.22+/2.6 instead of
userspace pppoa utility).

%description -l pl
Firmware dla modemu ADSL Alcatel SpeedTouch w wersji USB - potrzebne
dla narzêdzia modem_run (z pakietu speedtouch). Wczytuje siê je
poprzez:

modem_run [-k] -m -f /usr/share/speedtouch/mgmt.o

(-k nale¿y dodawaæ w przypadku u¿ywania sterownika w przestrzeni j±dra
dostêpnego w Linuksie 2.4.22+/2.6 zamiast narzêdzia pppoa dzia³ajacego
w przestrzeni u¿ytkownika).

%prep
%setup -q -n mgmt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/speedtouch

install mgmt.o $RPM_BUILD_ROOT%{_datadir}/speedtouch

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE speedtch.usermap
%{_datadir}/speedtouch/mgmt.o
