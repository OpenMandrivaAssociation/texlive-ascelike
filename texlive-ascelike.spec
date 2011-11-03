# revision 23704
# category Package
# catalog-ctan /macros/latex/contrib/ascelike
# catalog-date 2011-08-24 08:41:41 +0200
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-ascelike
Version:	2.1
Release:	1
Summary:	Bibliography style for the ASCE
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ascelike
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascelike.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascelike.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A document class and bibliographic style that prepares
documents in the style required by the American Society of
Civil Engineers (ASCE). These are unofficial files, not
sanctioned by that organization, and the files specifically
give this caveat. Also included is a short
documentation/example of how to use the class.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/ascelike/ascelike.bst
%{_texmfdistdir}/tex/latex/ascelike/ascelike.cls
%doc %{_texmfdistdir}/doc/latex/ascelike/README
%doc %{_texmfdistdir}/doc/latex/ascelike/ascexmpl.bib
%doc %{_texmfdistdir}/doc/latex/ascelike/ascexmpl.pdf
%doc %{_texmfdistdir}/doc/latex/ascelike/ascexmpl.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
