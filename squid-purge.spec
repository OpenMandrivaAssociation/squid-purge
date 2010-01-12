%define name    squid-purge
%define version 20040201
%define release %mkrel 3

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
Patch2:     purge-conf.patch
BuildRequires:  gcc-c++
#Requires:	apache
Suggests:	webproxy
BuildRoot:  %{_tmppath}/%{name}-%{version}


%description
The purge tool is a kind of magnifying glass into your squid-2 cache. You
can use purge to have a look at what URLs are stored in which file within
your cache. The purge tool can also be used to release objects which URLs
match user specified regular expressions. A more troublesome feature is the
ability to remove files squid does not seem to know about any longer.

%prep
%setup -q -n purge
%patch0 -p0 -b .gcc4
%patch1 -p0 -b .make
%patch2 -p0 -b .etc

%build
%make CXX="g++ %optflags" OPT_NORM="" SOCKLEN=socklen_t EXTRALIB="-lstdc++"


%install
#%makeinstall
mv purge squid-purge
install -d  %{buildroot}%{_sbindir}
install -m0700  squid-purge %{buildroot}%{_sbindir}/squid-purge


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0755,root,root)
%doc README
%{_sbindir}/squid-purge


