%global pkg_name maven-invoker-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.8
Release:        8.13%{?dist}
Summary:        Maven Invoker Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-invoker-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
Patch0:         pom-xml.patch

BuildArch: noarch

# Basic stuff
BuildRequires: %{?scl_prefix_java_common}javapackages-tools
# Maven and its dependencies
BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix}maven-resources-plugin
BuildRequires: %{?scl_prefix}maven-plugin-plugin
BuildRequires: %{?scl_prefix}maven-script-interpreter
BuildRequires: %{?scl_prefix}maven-invoker
BuildRequires: %{?scl_prefix}mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires: %{?scl_prefix}mvn(org.apache.maven.doxia:doxia-site-renderer)

# Others
BuildRequires: %{?scl_prefix}groovy


%description
The Maven Invoker Plugin is used to run a set of Maven projects. The plugin 
can determine whether each project execution is successful, and optionally 
can verify the output generated from a given project execution.
  

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%patch0

%pom_add_dep org.apache.maven:maven-plugin-registry
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-8.13
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.8-8.12
- Mass rebuild 2015-01-13

* Tue Jan 13 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-8.11
- Add POM dependency on maven-plugin-registry

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 1.8-8.10
- Rebuild to regenerate requires from java-common

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.8-8.9
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-8.8
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-8.7
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-8.6
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-8.5
- Remove requires on java

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-8.4
- Rebuild to fix incorrect auto-requires

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-8.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.8-8
- Mass rebuild 2013-12-27

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 1.8-7
- Migrate away from mvn-rpmbuild (Resolves: #997508)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue Apr  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-5
- Fix Requires and BuildRequires on Doxia; resolves: rhbz#950061
- Remove unneeded BR

* Sat Feb 16 2013 Michal Srb <msrb@redhat.com> - 1.8-4
- Migrate from maven-doxia to doxia subpackages (Resolves: #909238)
- Remove unnecessary BR on maven-doxia-tools

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.8-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jan 18 2013 Weinan Li <weli@redhat.com> 1.8-1
- Upgrade to 1.8

* Fri Jan 4 2013 David Xie <david.scriptfan@gmail.com> 1.7-2
- Add LICENSE and NOTICE files.

* Tue Oct 23 2012 Alexander Kurtakov <akurtako@redhat.com> 1.7-1
- Update to latest upstream.

* Tue Aug 21 2012 Tomas Radej <tradej@redhat.com> - 1.6-1
- Updated to v1.6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 9 2011 Alexander Kurtakov <akurtako@redhat.com> 1.5-5
- Build with maven 3.x.
- Use upstream source.
- Guidelines fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 Weinan Li <weli@redhat.com> -1.5-3
- R: maven-shared-invoker
- R: maven-shared-reporting-api
- R: maven-shared-reporting-impl
- Remove BR: maven2-plugin-changes
- Add BR: maven-shared-invoker

* Mon Jun 7 2010 Weinan Li <weli@redhat.com> - 1.5-2
- Fix incoherent version in changelog
- BR: maven-javadoc-plugin

* Thu Jun 3 2010 Weinan Li <weli@redhat.com> - 1.5-1
- Initial Package
