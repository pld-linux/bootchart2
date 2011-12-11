Summary:	Boot Process Performance Visualization
Summary(pl.UTF-8):	Wizualizacja wydajności procesu startu systemu
Name:		bootchart2
Version:	0.14.2
Release:	0.1
License:	GPL v2
Group:		Base
Source0:	https://github.com/downloads/mmeeks/bootchart/%{name}-%{version}.tar.bz2
# Source0-md5:	298487b2bda897e974f9862f0a0ad0ee
URL:		https://github.com/mmeeks/bootchart
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool for performance analysis and visualization of the GNU/Linux
boot process. Resource utilization and process information are
collected during the boot process and are later rendered in a PNG, SVG
or EPS encoded chart.

%description -l pl.UTF-8
Narzędzie do analizy i wizualizacji wydajności procesu startu systemu
GNU/Linux. Podczas startu systemu zbirane są informacje o procesach i
wykorzystaniu zasobów, a następnie są przedstawiane w postaci wykresu
w formacie PNG, SVG lub EPS.

%package gui
Summary:	GUI for bootchart2
Group:		Base

%description gui
A tool for performance analysis and visualization of the GNU/Linux
boot process. Resource utilization and process information are
collected during the boot process and are later rendered in a PNG, SVG
or EPS encoded chart.

%prep
%setup -q

%build
%{__make} \
	SYSTEMD_UNIT_DIR=%{systemdunitdir} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/bootchartd
%attr(755,root,root) /lib/bootchart/bootchart-collector
%{_sysconfdir}/bootchartd.conf
%{systemdunitdir}/bootchart-done.service
%{systemdunitdir}/bootchart-done.timer
%{systemdunitdir}/bootchart.service
%{_mandir}/man1/bootchart2.1*
%{_mandir}/man1/bootchartd.1*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pybootchartgui
%{_mandir}/man1/pybootchartgui.1*
%{py_sitescriptdir}/pybootchartgui
