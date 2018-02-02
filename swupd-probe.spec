#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swupd-probe
Version  : 2
Release  : 9
URL      : https://github.com/clearlinux/swupd-probe/archive/v2.tar.gz
Source0  : https://github.com/clearlinux/swupd-probe/archive/v2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: swupd-probe-bin
Requires: swupd-probe-autostart
Requires: swupd-probe-config
Requires: swupd-probe-doc
BuildRequires : pkgconfig(systemd)

%description
## swupd-probe
This project creates an interface between swupd-client and
telemetrics-client. The goal of the project is to provide
highly reliable and safe telemetry of swupd-client events
to telemetrics-client.

%package autostart
Summary: autostart components for the swupd-probe package.
Group: Default

%description autostart
autostart components for the swupd-probe package.


%package bin
Summary: bin components for the swupd-probe package.
Group: Binaries
Requires: swupd-probe-config

%description bin
bin components for the swupd-probe package.


%package config
Summary: config components for the swupd-probe package.
Group: Default

%description config
config components for the swupd-probe package.


%package doc
Summary: doc components for the swupd-probe package.
Group: Documentation

%description doc
doc components for the swupd-probe package.


%prep
%setup -q -n swupd-probe-2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1509422756
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1509422756
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../swupd-probe.path %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/swupd-probe.path
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/swupd-probe.path

%files bin
%defattr(-,root,root,-)
/usr/bin/swupd-probe

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/swupd-probe.path
/usr/lib/systemd/system/swupd-probe.path
/usr/lib/systemd/system/swupd-probe.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
