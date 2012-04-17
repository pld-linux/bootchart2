Summary:	Boot Process Performance Visualization
Summary(pl.UTF-8):	Wizualizacja wydajności procesu startu systemu
Name:		bootchart2
Version:	0.14.2
Release:	2
License:	GPL v2
Group:		Base
Source0:	https://github.com/downloads/mmeeks/bootchart/%{name}-%{version}.tar.bz2
# Source0-md5:	298487b2bda897e974f9862f0a0ad0ee
URL:		https://github.com/mmeeks/bootchart
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.641
Requires(post,preun,postun):	systemd-units >= 38
Requires:	systemd-units >= 38
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
Requires:	python-pycairo
Requires:	python-pygobject
Requires:	python-pygtk-gtk

%description gui
A tool which renders the output of the boot-logger tool bootchart2 to
either the screen or files in PNG, SVF or EPS encoded chart.

%description -l pl.UTF-8
Narzędzie tworzące wykres wyświetlany na ekranie lub zapisywany do
plików w formacie PNG, SVG lub EPS na podstawie danych dostarczonych
przez bootchart2.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	NO_PYTHON_COMPILE=1 \
	PY_LIBDIR=%{py_scriptdir} \
	SYSTEMD_UNIT_DIR=%{systemdunitdir} \
	DESTDIR=$RPM_BUILD_ROOT

%post
%systemd_post bootchart.service

%preun
%systemd_preun bootchart.service

%postun
%systemd_reload

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) /sbin/bootchartd
%dir /lib/bootchart
%dir /lib/bootchart/tmpfs
%attr(755,root,root) /lib/bootchart/bootchart-collector
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bootchartd.conf
%{systemdunitdir}/bootchart-done.service
%{systemdunitdir}/bootchart-done.timer
%{systemdunitdir}/bootchart.service
%{_mandir}/man1/bootchart2.1*
%{_mandir}/man1/bootchartd.1*

%files gui
%defattr(644,root,root,755)
%doc README.pybootchart
%attr(755,root,root) %{_bindir}/pybootchartgui
%{_mandir}/man1/pybootchartgui.1*
%{py_sitescriptdir}/pybootchartgui
