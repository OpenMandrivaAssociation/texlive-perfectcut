# revision 32861
# category Package
# catalog-ctan /macros/latex/contrib/perfectcut
# catalog-date 2014-02-03 14:43:47 +0100
# catalog-license lppl1.3
# catalog-version 1.9
Name:		texlive-perfectcut
Version:	1.9
Release:	2
Summary:	Brackets whose size adjusts to the nesting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/perfectcut
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/perfectcut.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/perfectcut.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines the command \perfectcut#1#2 which displays
a bracket <#1||#2>. Its effect is to determine the size of the
bracket depending on the number of nested \perfectcut
(regardless of the contents). The command is intended for use:
In proof theory, for term notations of sequent calculus, In
computer science, for the modeling of abstract machines. The
package also offers a reimplementation of \big, \bigg, etc.,
into arbitrary-size variants.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/perfectcut/perfectcut.sty
%doc %{_texmfdistdir}/doc/latex/perfectcut/README
%doc %{_texmfdistdir}/doc/latex/perfectcut/perfectcut.pdf
%doc %{_texmfdistdir}/doc/latex/perfectcut/perfectcut.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
