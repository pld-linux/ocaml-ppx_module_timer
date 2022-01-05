#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	A ppx extension to record module startup times
Summary(pl.UTF-8):	Rozszerzenie ppx to zapisywania czasów startu modułów
Name:		ocaml-ppx_module_timer
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_module_timer/tags
Source0:	https://github.com/janestreet/ppx_module_timer/archive/v%{version}/ppx_module_timer-%{version}.tar.gz
# Source0-md5:	2f4e90c784241a0f01fa56e56433e02a
URL:		https://github.com/janestreet/ppx_module_timer
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_base-devel >= 0.14
BuildRequires:	ocaml-ppx_base-devel < 0.15
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
BuildRequires:	ocaml-stdio-devel >= 0.14
BuildRequires:	ocaml-stdio-devel < 0.15
BuildRequires:	ocaml-time_now-devel >= 0.14
BuildRequires:	ocaml-time_now-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Ppx rewriter that records top-level module startup times.

This package contains files needed to run bytecode executables using
ppx_module_timer library.

%description -l pl.UTF-8
Moduł przepisujący ppx zapisujący czasy startu modułów górnego
poziomu.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_module_timer.

%package devel
Summary:	A ppx extension to record module startup times - development part
Summary(pl.UTF-8):	Rozszerzenie ppx to zapisywania czasów startu modułów - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppx_base-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0
Requires:	ocaml-stdio-devel >= 0.14
Requires:	ocaml-time_now-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
ppx_module_timer library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_module_timer.

%prep
%setup -q -n ppx_module_timer-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_module_timer/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_module_timer/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_module_timer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_module_timer
%attr(755,root,root) %{_libdir}/ocaml/ppx_module_timer/ppx.exe
%{_libdir}/ocaml/ppx_module_timer/META
%{_libdir}/ocaml/ppx_module_timer/*.cma
%dir %{_libdir}/ocaml/ppx_module_timer/runtime
%{_libdir}/ocaml/ppx_module_timer/runtime/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_module_timer/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_module_timer/runtime/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_module_timer/*.cmi
%{_libdir}/ocaml/ppx_module_timer/*.cmt
%{_libdir}/ocaml/ppx_module_timer/*.cmti
%{_libdir}/ocaml/ppx_module_timer/*.mli
%{_libdir}/ocaml/ppx_module_timer/runtime/*.cmi
%{_libdir}/ocaml/ppx_module_timer/runtime/*.cmt
%{_libdir}/ocaml/ppx_module_timer/runtime/*.cmti
%{_libdir}/ocaml/ppx_module_timer/runtime/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_module_timer/ppx_module_timer.a
%{_libdir}/ocaml/ppx_module_timer/*.cmx
%{_libdir}/ocaml/ppx_module_timer/*.cmxa
%{_libdir}/ocaml/ppx_module_timer/runtime/ppx_module_timer_runtime.a
%{_libdir}/ocaml/ppx_module_timer/runtime/*.cmx
%{_libdir}/ocaml/ppx_module_timer/runtime/*.cmxa
%endif
%{_libdir}/ocaml/ppx_module_timer/dune-package
%{_libdir}/ocaml/ppx_module_timer/opam
