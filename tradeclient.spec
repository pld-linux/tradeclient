Summary:	TradeClient - Messaging and PIM Client (Gtk+)
Summary(pl):	TradeClient - program pocztowy oraz PIM (Gtk+)
Name:		tradeclient
Version:	0.7.1
%define		subver 1
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}-%{subver}.tar.gz
URL:		http://www.bynari.net/News___Events/Products/tradeclient/tradeclient.htm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gtk+-devel

%define		_prefix		/usr/X11R6

%description
Messaging and Personal Information Management Tool for Linux and UNIX.

%description -l pl
Program pocztowy oraz PIM (zarz±dzanie informacjami) dla Linuksa.

%prep
%setup -q -n %{name}-%{version}-%{subver}

%build
%{__make} \
	prefix=%{_prefix}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} 	\
	DOCINSTALLDIR="" 			\

gzip -9nf README CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
# there are no files here yet
##%{_datadir}/*
