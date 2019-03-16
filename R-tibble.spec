#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tibble
Version  : 2.0.1
Release  : 32
URL      : https://cran.r-project.org/src/contrib/tibble_2.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tibble_2.0.1.tar.gz
Summary  : Provides a 'tbl_df' class (the 'tibble') that provides stricter checking and better formatting than the traditional data frame.
Group    : Development/Tools
License  : MIT
Requires: R-tibble-lib = %{version}-%{release}
Requires: R-cli
Requires: R-dplyr
Requires: R-fansi
Requires: R-import
Requires: R-pillar
Requires: R-pkgconfig
Requires: R-rlang
BuildRequires : R-cli
BuildRequires : R-dplyr
BuildRequires : R-fansi
BuildRequires : R-import
BuildRequires : R-markdown
BuildRequires : R-microbenchmark
BuildRequires : R-pillar
BuildRequires : R-pkgconfig
BuildRequires : R-rlang
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
# tibble <img src="man/figures/logo.png" align="right" />
[![Build
Status](https://travis-ci.org/tidyverse/tibble.svg?branch=master)](https://travis-ci.org/tidyverse/tibble)
[![AppVeyor Build
Status](https://ci.appveyor.com/api/projects/status/github/tidyverse/tibble?branch=master&svg=true)](https://ci.appveyor.com/project/tidyverse/tibble)
[![codecov](https://codecov.io/gh/tidyverse/tibble/branch/master/graph/badge.svg)](https://codecov.io/gh/tidyverse/tibble)
[![CRAN\_Status\_Badge](https://www.r-pkg.org/badges/version/tibble)](https://cran.r-project.org/package=tibble)
[![Life
cycle](https://img.shields.io/badge/lifecycle-stable-brightgreen.svg)](https://www.tidyverse.org/lifecycle/)

%package lib
Summary: lib components for the R-tibble package.
Group: Libraries

%description lib
lib components for the R-tibble package.


%prep
%setup -q -c -n tibble

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547339297

%install
export SOURCE_DATE_EPOCH=1547339297
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tibble
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tibble
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tibble
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library tibble|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tibble/DESCRIPTION
/usr/lib64/R/library/tibble/INDEX
/usr/lib64/R/library/tibble/LICENSE
/usr/lib64/R/library/tibble/Meta/Rd.rds
/usr/lib64/R/library/tibble/Meta/features.rds
/usr/lib64/R/library/tibble/Meta/hsearch.rds
/usr/lib64/R/library/tibble/Meta/links.rds
/usr/lib64/R/library/tibble/Meta/nsInfo.rds
/usr/lib64/R/library/tibble/Meta/package.rds
/usr/lib64/R/library/tibble/Meta/vignette.rds
/usr/lib64/R/library/tibble/NAMESPACE
/usr/lib64/R/library/tibble/NEWS.md
/usr/lib64/R/library/tibble/R/tibble
/usr/lib64/R/library/tibble/R/tibble.rdb
/usr/lib64/R/library/tibble/R/tibble.rdx
/usr/lib64/R/library/tibble/doc/extending.R
/usr/lib64/R/library/tibble/doc/extending.Rmd
/usr/lib64/R/library/tibble/doc/extending.html
/usr/lib64/R/library/tibble/doc/index.html
/usr/lib64/R/library/tibble/doc/tibble.R
/usr/lib64/R/library/tibble/doc/tibble.Rmd
/usr/lib64/R/library/tibble/doc/tibble.html
/usr/lib64/R/library/tibble/help/AnIndex
/usr/lib64/R/library/tibble/help/aliases.rds
/usr/lib64/R/library/tibble/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/tibble/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/tibble/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/tibble/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/tibble/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/tibble/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/tibble/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/tibble/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/tibble/help/figures/logo.png
/usr/lib64/R/library/tibble/help/figures/logo.svg
/usr/lib64/R/library/tibble/help/paths.rds
/usr/lib64/R/library/tibble/help/tibble.rdb
/usr/lib64/R/library/tibble/help/tibble.rdx
/usr/lib64/R/library/tibble/html/00Index.html
/usr/lib64/R/library/tibble/html/R.css
/usr/lib64/R/library/tibble/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tibble/libs/tibble.so
/usr/lib64/R/library/tibble/libs/tibble.so.avx2
/usr/lib64/R/library/tibble/libs/tibble.so.avx512
