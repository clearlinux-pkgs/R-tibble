#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tibble
Version  : 1.3.0
Release  : 3
URL      : https://cran.r-project.org/src/contrib/tibble_1.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tibble_1.3.0.tar.gz
Summary  : Simple Data Frames
Group    : Development/Tools
License  : MIT
Requires: R-tibble-lib
Requires: R-Rcpp
Requires: R-lazyeval
Requires: R-microbenchmark
BuildRequires : R-Rcpp
BuildRequires : R-lazyeval
BuildRequires : R-microbenchmark
BuildRequires : clr-R-helpers

%description
tibble
======
[![Build Status](https://travis-ci.org/tidyverse/tibble.svg?branch=master)](https://travis-ci.org/tidyverse/tibble) [![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/tidyverse/tibble?branch=master&svg=true)](https://ci.appveyor.com/project/tidyverse/tibble) [![Coverage Status](https://img.shields.io/codecov/c/github/tidyverse/tibble/master.svg)](https://codecov.io/github/tidyverse/tibble?branch=master) [![CRAN\_Status\_Badge](http://www.r-pkg.org/badges/version/tibble)](https://cran.r-project.org/package=tibble)

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
export SOURCE_DATE_EPOCH=1493660656

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1493660656
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tibble
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library tibble || :


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
/usr/lib64/R/library/tibble/doc/formatting.R
/usr/lib64/R/library/tibble/doc/formatting.Rmd
/usr/lib64/R/library/tibble/doc/formatting.html
/usr/lib64/R/library/tibble/doc/index.html
/usr/lib64/R/library/tibble/doc/tibble.R
/usr/lib64/R/library/tibble/doc/tibble.Rmd
/usr/lib64/R/library/tibble/doc/tibble.html
/usr/lib64/R/library/tibble/help/AnIndex
/usr/lib64/R/library/tibble/help/aliases.rds
/usr/lib64/R/library/tibble/help/paths.rds
/usr/lib64/R/library/tibble/help/tibble.rdb
/usr/lib64/R/library/tibble/help/tibble.rdx
/usr/lib64/R/library/tibble/html/00Index.html
/usr/lib64/R/library/tibble/html/R.css
/usr/lib64/R/library/tibble/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tibble/libs/tibble.so
