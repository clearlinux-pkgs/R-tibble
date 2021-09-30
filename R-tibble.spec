#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tibble
Version  : 3.1.5
Release  : 68
URL      : https://cran.r-project.org/src/contrib/tibble_3.1.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tibble_3.1.5.tar.gz
Summary  : Simple Data Frames
Group    : Development/Tools
License  : MIT
Requires: R-tibble-lib = %{version}-%{release}
Requires: R-ellipsis
Requires: R-fansi
Requires: R-lifecycle
Requires: R-magrittr
Requires: R-pillar
Requires: R-pkgconfig
Requires: R-rlang
Requires: R-vctrs
BuildRequires : R-ellipsis
BuildRequires : R-fansi
BuildRequires : R-lifecycle
BuildRequires : R-magrittr
BuildRequires : R-pillar
BuildRequires : R-pkgconfig
BuildRequires : R-rlang
BuildRequires : R-vctrs
BuildRequires : buildreq-R

%description
data frame.

%package lib
Summary: lib components for the R-tibble package.
Group: Libraries

%description lib
lib components for the R-tibble package.


%prep
%setup -q -c -n tibble
cd %{_builddir}/tibble

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633016135

%install
export SOURCE_DATE_EPOCH=1633016135
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
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
/usr/lib64/R/library/tibble/doc/digits.R
/usr/lib64/R/library/tibble/doc/digits.Rmd
/usr/lib64/R/library/tibble/doc/digits.html
/usr/lib64/R/library/tibble/doc/extending.Rmd
/usr/lib64/R/library/tibble/doc/extending.html
/usr/lib64/R/library/tibble/doc/formats.R
/usr/lib64/R/library/tibble/doc/formats.Rmd
/usr/lib64/R/library/tibble/doc/formats.html
/usr/lib64/R/library/tibble/doc/index.html
/usr/lib64/R/library/tibble/doc/invariants.R
/usr/lib64/R/library/tibble/doc/invariants.Rmd
/usr/lib64/R/library/tibble/doc/invariants.html
/usr/lib64/R/library/tibble/doc/numbers.R
/usr/lib64/R/library/tibble/doc/numbers.Rmd
/usr/lib64/R/library/tibble/doc/numbers.html
/usr/lib64/R/library/tibble/doc/tibble.R
/usr/lib64/R/library/tibble/doc/tibble.Rmd
/usr/lib64/R/library/tibble/doc/tibble.html
/usr/lib64/R/library/tibble/doc/types.R
/usr/lib64/R/library/tibble/doc/types.Rmd
/usr/lib64/R/library/tibble/doc/types.html
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
/usr/lib64/R/library/tibble/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/tibble/help/figures/logo.png
/usr/lib64/R/library/tibble/help/paths.rds
/usr/lib64/R/library/tibble/help/tibble.rdb
/usr/lib64/R/library/tibble/help/tibble.rdx
/usr/lib64/R/library/tibble/html/00Index.html
/usr/lib64/R/library/tibble/html/R.css
/usr/lib64/R/library/tibble/tests/testthat.R
/usr/lib64/R/library/tibble/tests/testthat/_snaps/add.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/as_tibble.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/enframe.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/error.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/msg.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/names.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/new.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/print.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/rownames.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/str.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/subsetting.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/tbl_df.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/tbl_sum.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/tibble.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/tidy_names.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/tribble.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/utils-msg-format.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/utils-tick.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/vignette-digits/digits.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/vignette-extending/extending.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/vignette-formats/formats.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/vignette-invariants/invariants.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/vignette-numbers/numbers.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/vignette-tibble/tibble.md
/usr/lib64/R/library/tibble/tests/testthat/_snaps/vignette-types/types.md
/usr/lib64/R/library/tibble/tests/testthat/helper-api.R
/usr/lib64/R/library/tibble/tests/testthat/helper-data.R
/usr/lib64/R/library/tibble/tests/testthat/helper-encoding.R
/usr/lib64/R/library/tibble/tests/testthat/helper-error.R
/usr/lib64/R/library/tibble/tests/testthat/helper-expectations.R
/usr/lib64/R/library/tibble/tests/testthat/helper-my.R
/usr/lib64/R/library/tibble/tests/testthat/helper-output.R
/usr/lib64/R/library/tibble/tests/testthat/helper-pillar.R
/usr/lib64/R/library/tibble/tests/testthat/helper-testthat.R
/usr/lib64/R/library/tibble/tests/testthat/helper-type-sum.R
/usr/lib64/R/library/tibble/tests/testthat/helper-unknown-rows.R
/usr/lib64/R/library/tibble/tests/testthat/helper-zzz.R
/usr/lib64/R/library/tibble/tests/testthat/test-add.R
/usr/lib64/R/library/tibble/tests/testthat/test-as_tibble.R
/usr/lib64/R/library/tibble/tests/testthat/test-enframe.R
/usr/lib64/R/library/tibble/tests/testthat/test-error.R
/usr/lib64/R/library/tibble/tests/testthat/test-has-name.R
/usr/lib64/R/library/tibble/tests/testthat/test-legacy-compat.R
/usr/lib64/R/library/tibble/tests/testthat/test-lst.R
/usr/lib64/R/library/tibble/tests/testthat/test-msg.R
/usr/lib64/R/library/tibble/tests/testthat/test-names.R
/usr/lib64/R/library/tibble/tests/testthat/test-new.R
/usr/lib64/R/library/tibble/tests/testthat/test-options.R
/usr/lib64/R/library/tibble/tests/testthat/test-print.R
/usr/lib64/R/library/tibble/tests/testthat/test-rownames.R
/usr/lib64/R/library/tibble/tests/testthat/test-str.R
/usr/lib64/R/library/tibble/tests/testthat/test-string-to-indices.R
/usr/lib64/R/library/tibble/tests/testthat/test-subsetting-matrix.R
/usr/lib64/R/library/tibble/tests/testthat/test-subsetting.R
/usr/lib64/R/library/tibble/tests/testthat/test-tbl_df.R
/usr/lib64/R/library/tibble/tests/testthat/test-tbl_sum.R
/usr/lib64/R/library/tibble/tests/testthat/test-tibble.R
/usr/lib64/R/library/tibble/tests/testthat/test-tidy_names.R
/usr/lib64/R/library/tibble/tests/testthat/test-tribble.R
/usr/lib64/R/library/tibble/tests/testthat/test-type_sum.R
/usr/lib64/R/library/tibble/tests/testthat/test-utils-msg-format.R
/usr/lib64/R/library/tibble/tests/testthat/test-utils-tick.R
/usr/lib64/R/library/tibble/tests/testthat/test-utils.R
/usr/lib64/R/library/tibble/tests/testthat/test-vignette-digits.R
/usr/lib64/R/library/tibble/tests/testthat/test-vignette-extending.R
/usr/lib64/R/library/tibble/tests/testthat/test-vignette-formats.R
/usr/lib64/R/library/tibble/tests/testthat/test-vignette-invariants.R
/usr/lib64/R/library/tibble/tests/testthat/test-vignette-numbers.R
/usr/lib64/R/library/tibble/tests/testthat/test-vignette-tibble.R
/usr/lib64/R/library/tibble/tests/testthat/test-vignette-types.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-add.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-data-frame.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-enframe.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-glimpse.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-has-name.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-lst.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-matrix.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-msg-format.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-msg.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-name-repair.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-options.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-rownames.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-string-to-indices.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-syntactic-names.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-tbl-df.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-tidy_names.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-tribble.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-trunc-mat.R
/usr/lib64/R/library/tibble/tests/testthat/test-zzz-type_sum.R
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/glimpse/5.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/glimpse/all-35.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/glimpse/all-50.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/glimpse/all-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/glimpse/iris-70-na-nrow.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/glimpse/iris-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/glimpse/iris-empty-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/glimpse/iris-nested-df-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/glimpse/iris-nested-tbl-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/glimpse/mtcars-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/glimpse/non-syntactic.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/str/5.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/str/all-35.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/str/all-50.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/str/all-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/str/iris-70-na-nrow.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/str/iris-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/str/iris-empty-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/str/iris-nested-df-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/str/iris-nested-tbl-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/str/mtcars-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/str/non-syntactic.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/POSIXlt-8-60.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/all--30.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/all--300.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/all-1-30-0.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/all-1-30-2.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/iris--70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/iris-5-30.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/iris-inf-30.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/iris-neg-30.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/iris_10_unk-10-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/iris_11_unk-10-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/iris_9_unk-10-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/iris_unk-10-70.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/long-5-30.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/long_unk-5-30.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/mtcars-8-30.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/non-syntactic.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/wide-8-60.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/zero-cols_unk-5-30.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/zero-rows_unk-5-30.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/zero_cols-5-30.txt
/usr/lib64/R/library/tibble/tests/testthat/zzz-output/trunc_mat/zero_rows--30.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tibble/libs/tibble.so
/usr/lib64/R/library/tibble/libs/tibble.so.avx2
/usr/lib64/R/library/tibble/libs/tibble.so.avx512
