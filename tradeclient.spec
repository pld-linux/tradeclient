Summary:	TradeClient - Messaging and PIM Client (Gtk+)
Summary(pl.UTF-8):	TradeClient - program pocztowy oraz PIM (Gtk+)
Name:		tradeclient
Version:	0.9.0
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	365d4f0029cc43ecc9a47c2a5a28ac17
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-include_time_h.patch
Patch1:		%{name}-openldap2.patch
URL:		http://www.bynari.net/News___Events/Products/tradeclient/tradeclient.htm
BuildRequires:	gtk+-devel
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Messaging and Personal Information Management Tool for Linux and UNIX.

%description -l pl.UTF-8
Program pocztowy oraz PIM (zarządzanie informacjami) dla Linuksa.

%prep
%setup -q
gzip -dc imap-4.7c.tar.Z | tar xfv -
%patch -P0 -p1
%patch -P1 -p0

%build
# Set the "right" optflags
perl -pi -e 's|^(\s*CFLAGS\+=)-m486|$1%{rpmcflags}|' Makefile

%{__make} \
	prefix=%{_prefix}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_applnkdir}/Office/PIMs} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	DOCINSTALLDIR=""

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Office/PIMs
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Office/PIMs/*
%{_pixmapsdir}/*
# there are no files here yet
#%%{_datadir}/*
