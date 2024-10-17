%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             hibernate-commons-annotations
Version:          4.0.4
Release:          1.3
Summary:          Hibernate Annotations
Group:            Development/Java
# For details see:
# - https://github.com/hibernate/hibernate-commons-annotations/commit/4a902b4f97f923f9044a4127357b44fe5dc39cdc
# - https://github.com/hibernate/hibernate-commons-annotations/commit/a11c44cd65dadcedaf8981379b94a2c4e31428d1
License:          LGPLv2
URL:              https://www.hibernate.org/
Source0:          https://github.com/hibernate/hibernate-commons-annotations/archive/%{namedversion}.tar.gz
Source1:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/hibernate/common/hibernate-commons-annotations/%{namedversion}/hibernate-commons-annotations-%{namedversion}.pom

BuildArch:        noarch

BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools >= 1.2.0
BuildRequires:    junit
BuildRequires:    slf4j
BuildRequires:    apache-commons-logging
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-processor-plugin
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-injection-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-source-plugin
BuildRequires:    maven-surefire-plugin

%description
Following the DRY (Don't Repeat Yourself) principle, 
Hibernate Validator let's you express your domain 
constraints once (and only once) and ensure their 
compliance at various level of your system 
automatically.

Common reflection code used in support of annotation processing.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n hibernate-commons-annotations-%{namedversion}

cp %{SOURCE1} pom.xml

%pom_add_dep org.jboss.logging:jboss-logging-processor:1.2.0:provided
%pom_add_dep junit:junit:4:test

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc changelog.txt lgpl.txt readme.txt

%files javadoc -f .mfiles-javadoc
%doc lgpl.txt

%changelog
* Mon Sep 09 2013 Marek Goldmann <mgoldman@redhat.com> - 4.0.3-1
- Upstream release 4.0.3.Final

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 4.0.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 22 2012 gil cattaneo <puntogil@libero.it> 4.0.1-1
- update to 4.0.1.Final
- adapt to current guideline
- add backward compatibility in depmap

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 01 2011 Marek Goldmann <mgoldman@redhat.com> 3.2.0-3
- Fixed license
- Using source from git

* Mon May 23 2011 Marek Goldmann <mgoldman@redhat.com> 3.2.0-2
- Moved to hibernate subdirectory

* Fri May 20 2011 Marek Goldmann <mgoldman@redhat.com> 3.2.0-1
- Initial packaging

