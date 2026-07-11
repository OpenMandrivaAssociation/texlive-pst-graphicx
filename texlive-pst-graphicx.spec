%global tl_name pst-graphicx
%global tl_revision 21717

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.02
Release:	%{tl_revision}.1
Summary:	A PSTricks-compatible graphicx for use with Plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-graphicx
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-graphicx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-graphicx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a version of graphicx that avoids loading the
graphics bundle's (original) keyval package, which clashes with
pstricks' use of xkeyval.

