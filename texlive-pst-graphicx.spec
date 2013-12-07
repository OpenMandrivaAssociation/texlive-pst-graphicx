# revision 21717
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-graphicx
# catalog-date 2011-03-14 10:28:00 +0100
# catalog-license lppl
# catalog-version 0.02
Name:		texlive-pst-graphicx
Version:	0.02
Release:	5
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.02-2
+ Revision: 755315
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.02-1
+ Revision: 719359
- texlive-pst-graphicx
- texlive-pst-graphicx
- texlive-pst-graphicx
- texlive-pst-graphicx

