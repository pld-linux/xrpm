Summary:	An alternative package manager for RPMS
Summary(pl):	Zarz±dca plików RPM dla X
Name:		xrpm
Version:	2.2
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	ftp://www.cc.mala.bc.ca/pub/Linux/%{name}-%{version}.tar.gz
# Source0-md5:	455ad8849eb18d2aabe76f02a1511305
Source1:	%{name}.pld
Source2:	%{name}-ftp-sites.pld
URL:		http://www.gmsys.com/xrpm.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
Requires:	tix
Requires:	tkinter

%description
XRPM-2.2 is an alternative tool for manipulating software packages
built with RedHat's RPM package management tool. XRPM will allow you
to list and install packages from directories and FTP sites.

%description -l pl
XRPM jest ca³kiem przyjemnym narzêdziem do nadzoru, instalacji oraz
deinstalacji paczek RPM.

%prep

%setup -q -a0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/bin
install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/ftp-sites
cp xrpm.conf $RPM_BUILD_ROOT%{_sysconfdir}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/xrpm
chmod 755 $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/xrpm
cp file.gif $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp findrpm.py $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp ftputil.py $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp gmsgui.py $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp gmsutil.py $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp gui.py $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp help.py $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp info.gif $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp install.gif $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp menu.py $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp quit.gif $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp remove.gif $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp rpm.py $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm
cp xrpm.py $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/xrpm

#(cd $RPM_BUILD_ROOT
#mkdir -p ./usr/X11R6/lib/menu
#cat > ./usr/X11R6/lib/menu/%{name} <<EOF
#?package(%{name}):\
#command="/usr/X11R6/bin/xrpm"\
#title="Xrpm"\
#longtitle="Tool for manipulating software packages"\
#needs="x11"\
#section="Configuration/Packaging"
#EOF
#)

%clean
rm -rf $RPM_BUILD_ROOT/

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE NEWS todo license manual
%config %{_sysconfdir}/ftp-sites
%config(noreplace) %{_sysconfdir}/xrpm.conf
%{_prefix}/X11R6/bin/xrpm
%{_prefix}/X11R6/lib/xrpm/*
