# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/inversepath
# catalog-date 2008-08-19 23:32:24 +0200
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-inversepath
Version:	0.2
Release:	10
Summary:	Calculate inverse file paths
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/inversepath
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inversepath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inversepath.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inversepath.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package calculates inverse relative paths. Such things may
be useful, for example, when writing an auxiliary file to a
different directory.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/inversepath/inversepath.sty
%doc %{_texmfdistdir}/doc/latex/inversepath/README
%doc %{_texmfdistdir}/doc/latex/inversepath/inversepath.pdf
#- source
%doc %{_texmfdistdir}/source/latex/inversepath/inversepath.dtx
%doc %{_texmfdistdir}/source/latex/inversepath/inversepath.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 752802
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 718728
- texlive-inversepath
- texlive-inversepath
- texlive-inversepath
- texlive-inversepath

