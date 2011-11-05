# revision 21717
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-graphicx
# catalog-date 2011-03-14 10:28:00 +0100
# catalog-license lppl
# catalog-version 0.02
Name:		texlive-pst-graphicx
Version:	0.02
Release:	1
Summary:	A pstricks-compatible graphicx for use with Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-graphicx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-graphicx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-graphicx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a version of graphicx that avoids loading
the graphics bundle's (original) keyval package, which clashes
with pstricks' use of xkeyval.

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
%{_texmfdistdir}/tex/generic/pst-graphicx/pst-graphicx.tex
%doc %{_texmfdistdir}/doc/generic/pst-graphicx/Changes
%doc %{_texmfdistdir}/doc/generic/pst-graphicx/README
%doc %{_texmfdistdir}/doc/generic/pst-graphicx/demo.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
