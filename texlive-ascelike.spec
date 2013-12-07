# revision 29129
# category Package
# catalog-ctan /macros/latex/contrib/ascelike
# catalog-date 2012-02-05 17:55:30 +0100
# catalog-license lppl
# catalog-version 2.2
Name:		texlive-ascelike
Version:	2.2
Release:	3
Summary:	Bibliography style for the ASCE
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ascelike
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascelike.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascelike.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A document class and bibliographic style that prepares
documents in the style required by the American Society of
Civil Engineers (ASCE). These are unofficial files, not
sanctioned by that organization, and the files specifically
give this caveat. Also included is a short
documentation/example of how to use the class.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/ascelike/ascelike.bst
%{_texmfdistdir}/tex/latex/ascelike/ascelike.cls
%doc %{_texmfdistdir}/doc/latex/ascelike/README
%doc %{_texmfdistdir}/doc/latex/ascelike/ascexmpl.bib
%doc %{_texmfdistdir}/doc/latex/ascelike/ascexmpl.pdf
%doc %{_texmfdistdir}/doc/latex/ascelike/ascexmpl.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
