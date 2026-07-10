%global tl_name ascelike
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0
Release:	%{tl_revision}.1
Summary:	Bibliography style for the ASCE
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ascelike
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ascelike.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ascelike.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A document class and bibliographic style that prepares documents in the
style required by the American Society of Civil Engineers (ASCE). These
are unofficial files, not sanctioned by that organization, and the files
specifically give this caveat. Also included is a short
documentation/example of how to use the class.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/ascelike
%dir %{_datadir}/texmf-dist/doc/latex/ascelike
%dir %{_datadir}/texmf-dist/tex/latex/ascelike
%{_datadir}/texmf-dist/bibtex/bst/ascelike/ascelike.bst
%doc %{_datadir}/texmf-dist/doc/latex/ascelike/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/ascelike/ascexmpl.bib
%doc %{_datadir}/texmf-dist/doc/latex/ascelike/ascexmpl.pdf
%doc %{_datadir}/texmf-dist/doc/latex/ascelike/ascexmpl.tex
%{_datadir}/texmf-dist/tex/latex/ascelike/ascelike.bbx
%{_datadir}/texmf-dist/tex/latex/ascelike/ascelike.cbx
%{_datadir}/texmf-dist/tex/latex/ascelike/ascelike.cls
