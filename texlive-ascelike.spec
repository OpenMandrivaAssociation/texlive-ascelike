Name:		texlive-ascelike
Version:	29129
Release:	1
Summary:	Bibliography style for the ASCE
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ascelike
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascelike.r29129.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascelike.doc.r29129.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
