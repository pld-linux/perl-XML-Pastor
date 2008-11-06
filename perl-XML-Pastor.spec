#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Pastor
Summary:	XML::Pastor - Generate Perl classes with XML bindings starting from a W3C XSD Schema
#Summary(pl.UTF-8):	
Name:		perl-XML-Pastor
Version:	1.0.3
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	419a54a422a883d59925ea5723dd4ca1
URL:		http://search.cpan.org/dist/XML-Pastor/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Data::HashArray)
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Class-Data-Inheritable
BuildRequires:	perl-File-chdir
BuildRequires:	perl-libwww
BuildRequires:	perl-URI
BuildRequires:	perl-XML-LibXML >= 1.66
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Pastor is able to generate Perl classes either offline or at
run-time starting from a W3C XSD Schema.

The generated classes correspond to the global elements, complex and
simple type declarations in the schema. The generated classes have
full XML binding, meaning objects belonging to them can be read from
and written to XML. Accessor methods for attributes and child elements
will be generated automatically.

Furthermore it is possible to validate the objects of generated
classes against the original schema although the schema is typically
no longer accessible.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/XML/*.pm
%{perl_vendorlib}/XML/Pastor
%{_mandir}/man3/*
%{_mandir}/man1/*
