Name:		texlive-inversepath
Version:	15878
Release:	1
Summary:	Calculate inverse file paths
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/inversepath
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inversepath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inversepath.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inversepath.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
