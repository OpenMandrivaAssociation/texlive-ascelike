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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A document class and bibliographic style that prepares documents in the
style required by the American Society of Civil Engineers (ASCE). These
are unofficial files, not sanctioned by that organization, and the files
specifically give this caveat. Also included is a short
documentation/example of how to use the class.

