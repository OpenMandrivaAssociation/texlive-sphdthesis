Name:		texlive-sphdthesis
Version:	34374
Release:	2
Summary:	LaTeX template for writing PhD Thesis
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sphdthesis
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sphdthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sphdthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a LaTeX document class for writing a PhD
thesis. The author developed it while writing his PhD thesis in
School of Computing (SoC), National University of Singapore
(NUS). By default, the class adheres to the NUS Guidelines on
Format of Research Thesis Submitted For Examination. However,
the class for conformation to a different guideline should not
be difficult.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/sphdthesis
%doc %{_texmfdistdir}/doc/latex/sphdthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
