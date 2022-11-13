Name:		texlive-pst-graphicx
Version:	21717
Release:	1
Summary:	A pstricks-compatible graphicx for use with Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-graphicx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-graphicx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-graphicx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a version of graphicx that avoids loading
the graphics bundle's (original) keyval package, which clashes
with pstricks' use of xkeyval.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-graphicx/pst-graphicx.tex
%doc %{_texmfdistdir}/doc/generic/pst-graphicx/Changes
%doc %{_texmfdistdir}/doc/generic/pst-graphicx/README
%doc %{_texmfdistdir}/doc/generic/pst-graphicx/demo.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
