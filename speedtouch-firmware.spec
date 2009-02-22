Summary:	Alcatel SpeedTouch USB ADSL modem firmware
Summary(pl.UTF-8):	Firmware dla modemu ADSL Alcatel SpeedTouch w wersji USB
Name:		speedtouch-firmware
Version:	3.012
Release:	3
License:	restricted, non-distributable
Group:		Libraries
Source0:	http://www.speedtouch.com/download/drivers/USB/SpeedTouch330_firmware_3012.zip
# NoSource0-md5:	2551ce46ef785642f2c6768511f70ff3
Source1:	http://www.linux-usb.org/SpeedTouch/firmware/firmware-extractor.tar.gz
# Source1-md5:	752e33faf0b62176114e757dfc1e7191
NoSource:	0
URL:		http://www.thomson.net/GlobalEnglish/Products/dsl-modems-gateways/residential_wired/other_supported_products/thomson_st330/Pages/default.aspx
BuildRequires:	unzip
Obsoletes:	speedtouch-firmware-userspace
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alcatel SpeedTouch USB ADSL modem firmware loaded by Linux kernel
firmware loader (recent Linux 2.6.x with udev or hotplug).

%description -l pl.UTF-8
Firmware dla modemu ADSL Alcatel SpeedTouch w wersji USB do
wczytywania przez mechanizm jądra (w nowych wersjach Linuksa 2.6.x
z narzędziem udev lub hotplug).

%prep
%setup -q -c -a1

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
install -d $RPM_BUILD_ROOT/lib/firmware

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
