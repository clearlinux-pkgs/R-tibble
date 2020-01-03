#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tibble
Version  : 2.1.3
Release  : 43
URL      : https://cran.r-project.org/src/contrib/tibble_2.1.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tibble_2.1.3.tar.gz
Summary  : Simple Data Frames
Group    : Development/Tools
License  : MIT
Requires: R-tibble-lib = %{version}-%{release}
Requires: R-cli
Requires: R-crayon
Requires: R-dplyr
Requires: R-fansi
Requires: R-htmltools
Requires: R-import
Requires: R-pillar
Requires: R-pkgconfig
Requires: R-rlang
BuildRequires : R-cli
BuildRequires : R-crayon
BuildRequires : R-dplyr
BuildRequires : R-fansi
BuildRequires : R-htmltools
BuildRequires : R-import
BuildRequires : R-markdown
BuildRequires : R-microbenchmark
BuildRequires : R-pillar
BuildRequires : R-pkgconfig
BuildRequires : R-rlang
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
stricter checking and better formatting than the traditional data frame.

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
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569295612

%install
export SOURCE_DATE_EPOCH=1569295612
rm -rf %{buildroot}
export LANG=C.UTF-8
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tibble || :


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
/usr/lib64/R/library/tibble/help/paths.rds
/usr/lib64/R/library/tibble/help/tibble.rdb
/usr/lib64/R/library/tibble/help/tibble.rdx
/usr/lib64/R/library/tibble/html/00Index.html
/usr/lib64/R/library/tibble/html/R.css
/usr/lib64/R/library/tibble/tests/testthat.R
/usr/lib64/R/library/tibble/tests/testthat/helper-api.R
/usr/lib64/R/library/tibble/tests/testthat/helper-data.R
/usr/lib64/R/library/tibble/tests/testthat/helper-encoding.R
/usr/lib64/R/library/tibble/tests/testthat/helper-error.R
/usr/lib64/R/library/tibble/tests/testthat/helper-output.R
/usr/lib64/R/library/tibble/tests/testthat/helper-type-sum.R
/usr/lib64/R/library/tibble/tests/testthat/helper-unknown-rows.R
/usr/lib64/R/library/tibble/tests/testthat/output/glimpse/5.txt
/usr/lib64/R/library/tibble/tests/testthat/output/glimpse/all-35.txt
/usr/lib64/R/library/tibble/tests/testthat/output/glimpse/all-50.txt
/usr/lib64/R/library/tibble/tests/testthat/output/glimpse/all-70.txt
/usr/lib64/R/library/tibble/tests/testthat/output/glimpse/iris-70-na-nrow.txt
/usr/lib64/R/library/tibble/tests/testthat/output/glimpse/iris-70.txt
/usr/lib64/R/library/tibble/tests/testthat/output/glimpse/iris-empty-70.txt
/usr/lib64/R/library/tibble/tests/testthat/output/glimpse/iris-nested-df-70.txt
/usr/lib64/R/library/tibble/tests/testthat/output/glimpse/iris-nested-tbl-70.txt
/usr/lib64/R/library/tibble/tests/testthat/output/glimpse/mtcars-70.txt
/usr/lib64/R/library/tibble/tests/testthat/output/glimpse/non-syntactic.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/POSIXlt-8-60.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/all--30.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/all--300.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/all-1-30-0.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/all-1-30-2.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/iris--70.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/iris-3-5.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/iris-5-30.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/iris-inf-30.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/iris-neg-30.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/iris_10_unk-10-70.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/iris_11_unk-10-70.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/iris_9_unk-10-70.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/iris_unk-10-70.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/long-5-30.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/long_unk-5-30.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/mtcars-8-30.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/newline.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/non-syntactic.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/wide-8-60.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/zero-cols_unk-5-30.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/zero-rows_unk-5-30.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/zero_cols-5-30.txt
/usr/lib64/R/library/tibble/tests/testthat/output/trunc_mat/zero_rows--30.txt
/usr/lib64/R/library/tibble/tests/testthat/test-add.R
/usr/lib64/R/library/tibble/tests/testthat/test-data-frame.R
/usr/lib64/R/library/tibble/tests/testthat/test-enframe.R
/usr/lib64/R/library/tibble/tests/testthat/test-glimpse.R
/usr/lib64/R/library/tibble/tests/testthat/test-has-name.R
/usr/lib64/R/library/tibble/tests/testthat/test-lst.R
/usr/lib64/R/library/tibble/tests/testthat/test-matrix.R
/usr/lib64/R/library/tibble/tests/testthat/test-msg-format.R
/usr/lib64/R/library/tibble/tests/testthat/test-msg.R
/usr/lib64/R/library/tibble/tests/testthat/test-name-repair.R
/usr/lib64/R/library/tibble/tests/testthat/test-options.R
/usr/lib64/R/library/tibble/tests/testthat/test-rownames.R
/usr/lib64/R/library/tibble/tests/testthat/test-string-to-indices.R
/usr/lib64/R/library/tibble/tests/testthat/test-syntactic-names.R
/usr/lib64/R/library/tibble/tests/testthat/test-tbl-df.R
/usr/lib64/R/library/tibble/tests/testthat/test-tidy_names.R
/usr/lib64/R/library/tibble/tests/testthat/test-tribble.R
/usr/lib64/R/library/tibble/tests/testthat/test-trunc-mat.R
/usr/lib64/R/library/tibble/tests/testthat/test-type_sum.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tibble/libs/tibble.so
/usr/lib64/R/library/tibble/libs/tibble.so.avx2
/usr/lib64/R/library/tibble/libs/tibble.so.avx512
