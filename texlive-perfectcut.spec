%global tl_name perfectcut
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3
Release:	%{tl_revision}.1
Summary:	Nested delimiters that consistently grow regardless of the contents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/perfectcut
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/perfectcut.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/perfectcut.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines the command \perfectcut#1#2 which displays a
bracket <#1||#2>. Various other delimiters are similarly defined
(parentheses, square brackets ...). The effect of these commands is to
let the delimiters grow according to the number of nested
\perfectcommands (regardless of the size of the contents). The package
was originally intended for solving a notational issue for direct-style
continuation calculi in proof theory. For general use, the package also
defines commands for defining other sorts of delimiters which will
behave in the same way (see example in the documentation). The package
also offers a robust reimplementation of \big, \bigg, etc.

