#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Glib
Version  : 1.3294
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/X/XA/XAOC/Glib-1.3294.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/X/XA/XAOC/Glib-1.3294.tar.gz
Summary  : 'Perl wrappers for the GLib utility and Object libraries'
Group    : Development/Tools
License  : LGPL-2.1
Requires: perl-Glib-license = %{version}-%{release}
Requires: perl-Glib-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Depends)
BuildRequires : perl(ExtUtils::PkgConfig)
BuildRequires : pkgconfig(gobject-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Glib
====
This module provides perl access to Glib and GLib's GObject libraries.
GLib is a portability and utility library; GObject provides a generic
type system with inheritance and a powerful signal system.  Together
these libraries are used as the foundation for many of the libraries
that make up the Gnome environment, and are used in many unrelated
projects.

%package dev
Summary: dev components for the perl-Glib package.
Group: Development
Provides: perl-Glib-devel = %{version}-%{release}
Requires: perl-Glib = %{version}-%{release}

%description dev
dev components for the perl-Glib package.


%package license
Summary: license components for the perl-Glib package.
Group: Default

%description license
license components for the perl-Glib package.


%package perl
Summary: perl components for the perl-Glib package.
Group: Default
Requires: perl-Glib = %{version}-%{release}

%description perl
perl components for the perl-Glib package.


%prep
%setup -q -n Glib-1.3294
cd %{_builddir}/Glib-1.3294
pushd ..
cp -a Glib-1.3294 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Glib
cp %{_builddir}/Glib-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Glib/9b5750f0d09684e6a1eef6e223cec8f2ae80eaeb || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Glib.3
/usr/share/man/man3/Glib::BookmarkFile.3
/usr/share/man/man3/Glib::Boxed.3
/usr/share/man/man3/Glib::Bytes.3
/usr/share/man/man3/Glib::CodeGen.3
/usr/share/man/man3/Glib::Error.3
/usr/share/man/man3/Glib::Flags.3
/usr/share/man/man3/Glib::GenPod.3
/usr/share/man/man3/Glib::KeyFile.3
/usr/share/man/man3/Glib::Log.3
/usr/share/man/man3/Glib::MainLoop.3
/usr/share/man/man3/Glib::MakeHelper.3
/usr/share/man/man3/Glib::Markup.3
/usr/share/man/man3/Glib::Object.3
/usr/share/man/man3/Glib::Object::Subclass.3
/usr/share/man/man3/Glib::OptionContext.3
/usr/share/man/man3/Glib::OptionGroup.3
/usr/share/man/man3/Glib::Param::Boolean.3
/usr/share/man/man3/Glib::Param::Double.3
/usr/share/man/man3/Glib::Param::Enum.3
/usr/share/man/man3/Glib::Param::Flags.3
/usr/share/man/man3/Glib::Param::GType.3
/usr/share/man/man3/Glib::Param::Int.3
/usr/share/man/man3/Glib::Param::Int64.3
/usr/share/man/man3/Glib::Param::String.3
/usr/share/man/man3/Glib::Param::UInt.3
/usr/share/man/man3/Glib::Param::UInt64.3
/usr/share/man/man3/Glib::Param::Unichar.3
/usr/share/man/man3/Glib::ParamSpec.3
/usr/share/man/man3/Glib::ParseXSDoc.3
/usr/share/man/man3/Glib::Signal.3
/usr/share/man/man3/Glib::Type.3
/usr/share/man/man3/Glib::Utils.3
/usr/share/man/man3/Glib::Variant.3
/usr/share/man/man3/Glib::VariantDict.3
/usr/share/man/man3/Glib::VariantType.3
/usr/share/man/man3/Glib::devel.3
/usr/share/man/man3/Glib::index.3
/usr/share/man/man3/Glib::version.3
/usr/share/man/man3/Glib::xsapi.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Glib/9b5750f0d09684e6a1eef6e223cec8f2ae80eaeb

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
