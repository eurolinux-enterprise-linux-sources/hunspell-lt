Name: hunspell-lt
Summary: Lithuanian hunspell dictionaries
Version: 1.2.1
Release: 9%{?dist}
Source: ftp://ftp.akl.lt/ispell-lt/lt_LT-%{version}.zip
Group: Applications/Text
URL: ftp://ftp.akl.lt/ispell-lt/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: BSD
BuildArch: noarch

Requires: hunspell

%description
Lithuanian hunspell dictionaries.

%prep
%setup -q -n lt_LT-%{version}

%build
chmod -x *
for i in INSTRUKCIJOS.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.EN INSTRUKCIJOS.txt
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 1.2.1-4
- clean spec

* Fri Jul 10 2009 Caolan McNamara <caolanm@redhat.com> - 1.2.1-3
- clean spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 20 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.1-1
- latest version

* Sat Feb 16 2008 Caolan McNamara <caolanm@redhat.com> - 1.2-1
- next version

* Tue Jun 05 2007 Caolan McNamara <caolanm@redhat.com> - 1.1-1.20070510cvs
- next version

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 1.1-1.20061127cvs
- initial version
