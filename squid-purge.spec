%define name    squid-purge
%define version 20040201
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Squid pruger utility
License:    GPLv2+
Group:      Networking/Other
URL:        http://www.squid-cache.org/contrib/
Source:     http://www.squid-cache.org/contrib/purge-%{version}-src.tar.gz
Patch0:     purge-gcc4.patch
Patch1:     make-install.patch
#BuildRequires:  openssl-devel >= 0.9.7
#Requires:	apache
Requires:	openssl
Suggests:	webproxy
BuildRoot:  %{_tmppath}/%{name}-%{version}


%description
The purge tool is a kind of magnifying glass into your squid-2 cache. You
can use purge to have a look at what URLs are stored in which file within
your cache. The purge tool can also be used to release objects which URLs
match user specified regular expressions. A more troublesome feature is the
ability to remove files squid does not seem to know about any longer.

    USE AT YOUR OWN RISK! NO GUARANTEES, WHATSOEVER! DON'T BLAME US!
                         YOU HAVE BEEN WARNED!


%prep
%setup -q -n purge
%patch0 -p0 -b .gcc4
%patch1 -p0 -b .make

%build
%make CXX="g++ %optflags"


#%install

%makeinstall
mv purge squid-purge
install -d  %{buildroot}%{_sbindir}
install -m0700  squid-purge %{buildroot}%{_sbindir}/squid-purge


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0755,root,root)
%doc README
%{_sbindir}/squid-purge


