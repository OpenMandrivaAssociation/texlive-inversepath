%global tl_name inversepath
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Calculate inverse file paths
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/inversepath
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inversepath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inversepath.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inversepath.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package calculates inverse relative paths. Such things may be
useful, for example, when writing an auxiliary file to a different
directory.

