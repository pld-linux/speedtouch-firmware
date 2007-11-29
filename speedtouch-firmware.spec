Summary:	Alcatel SpeedTouch USB ADSL modem firmware
Summary(pl.UTF-8):	Firmware dla modemu ADSL Alcatel SpeedTouch w wersji USB
Name:		speedtouch-firmware
Version:	3.012
Release:	2
License:	restricted, non-distributable
Group:		Libraries
Source0:	http://www.speedtouch.com/download/drivers/USB/SpeedTouch330_firmware_3012.zip
# NoSource0-md5:	2551ce46ef785642f2c6768511f70ff3
Source1:	http://download.ethomson.com/download/speedmgmt.tar.gz
# NoSource1-md5:	102dc7a457c3942ee21dc834db68eac2
Source2:	http://www.linux-usb.org/SpeedTouch/firmware/firmware-extractor.tar.gz
# Source2-md5:	752e33faf0b62176114e757dfc1e7191
NoSource:	0
NoSource:	1
URL:		http://www.speedtouchdsl.com/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alcatel SpeedTouch USB ADSL modem firmware loaded by Linux kernel
firmware loader (recent Linux 2.6.x with udev or hotplug).

%description -l pl.UTF-8
Firmware dla modemu ADSL Alcatel SpeedTouch w wersji USB do
wczytywania przez mechanizm jądra (w nowych wersjach Linuksa 2.6.x
z narzędziem udev lub hotplug).

%package userspace
Summary:	Alcatel SpeedTouch USB ADSL modem firmware for modem_run loader
Summary(pl.UTF-8):	Firmware modemu ADSL Alcatel SpeedTouch USB dla narzędzia modem_run
Group:		Libraries
Requires:	speedtouch >= 1.2-1

%description userspace
Alcatel SpeedTouch USB ADSL modem firmware, needed for modem_run
utility (speedtouch package). Load it by:

modem_run [-k] -f /usr/share/speedtouch/mgmt.o

(-k if you are using kernel driver from Linux 2.4.22+/2.6 instead of
userspace pppoa utility).

%description userspace -l pl.UTF-8
Firmware dla modemu ADSL Alcatel SpeedTouch w wersji USB - potrzebne
dla narzędzia modem_run (z pakietu speedtouch). Wczytuje się je
poprzez:

modem_run [-k] -f /usr/share/speedtouch/mgmt.o

(-k należy dodawać w przypadku używania sterownika w przestrzeni jądra
dostępnego w Linuksie 2.4.22+/2.6 zamiast narzędzia pppoa działającego
w przestrzeni użytkownika).

%prep
%setup -q -c -a1 -a2

%build
%{__cc} %{rpmcflags} -o fextractor firmware-extractor/firmware.c

# for a "silver" (revision 4) modem
./fextractor ZZZL_%{version}
mv -f speedtch-1.bin{,.4.00}
mv -f speedtch-2.bin{,.4.00}

# for an old "green" (revision 0) or a "purple" (revision 2) modem
# (colours-revision mapping is not so strict, there exist silver modems rev. 2)
./fextractor KQD6_%{version}
mv -f speedtch-1.bin{,.0.00}
mv -f speedtch-2.bin{,.0.00}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/speedtouch,/lib/firmware}

install mgmt/mgmt.o $RPM_BUILD_ROOT%{_datadir}/speedtouch
install speedtch-* $RPM_BUILD_ROOT/lib/firmware
ln -s speedtch-1.bin.0.00 $RPM_BUILD_ROOT/lib/firmware/speedtch-1.bin.2.00
ln -s speedtch-2.bin.0.00 $RPM_BUILD_ROOT/lib/firmware/speedtch-2.bin.2.00

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/speedtch-1.bin.0.00
/lib/firmware/speedtch-2.bin.0.00
/lib/firmware/speedtch-1.bin.2.00
/lib/firmware/speedtch-2.bin.2.00
/lib/firmware/speedtch-1.bin.4.00
/lib/firmware/speedtch-2.bin.4.00

%files userspace
%defattr(644,root,root,755)
%{_datadir}/speedtouch/mgmt.o
