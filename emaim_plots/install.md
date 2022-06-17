# Installation of Prerequisite Libraries
I created a Conda environment for these bokeh plots:
```bash
conda create --name bokeh
```
   1. [TensorFlow](#tensorflow)
   2. [Keras](#keras)
   3. [TQDM](#tqdm) Progress Meter

## Tensorflow
```bash
# Installed v1.14.0
conda install -c conda-forge tensorflow
```
<details>
  <summary> Installation Log</summary>
      $ conda install -c conda-forge tensorflow
      Collecting package metadata (current_repodata.json): done
      Solving environment: done


      \=\=> WARNING: A newer version of conda exists. <\=\=
        current version: 4.10.3
        latest version: 4.13.0

      Please update conda by running

          $ conda update -n base -c defaults conda



      ## Package Plan ##

        environment location: C:\Users\Matt\.conda\envs\bokeh

        added / updated specs:
          - tensorflow


      The following packages will be downloaded:

          package                    |            build
          ---------------------------|-----------------
          absl-py-1.1.0              |     pyhd8ed1ab_0          94 KB  conda-forge
          astor-0.8.1                |     pyh9f0ad1d_0          25 KB  conda-forge
          ca-certificates-2022.6.15  |       h5b45459_0         188 KB  conda-forge
          cached-property-1.5.2      |       hd8ed1ab_1           4 KB  conda-forge
          cached_property-1.5.2      |     pyha770c72_1          11 KB  conda-forge
          gast-0.5.3                 |     pyhd8ed1ab_0          20 KB  conda-forge
          google-pasta-0.2.0         |     pyh8c360ce_0          42 KB  conda-forge
          grpcio-1.42.0              |   py37hc60d5dd_0         1.8 MB
          h5py-3.2.1                 |nompi_py37he280515_100         1.0 MB  conda-forge
          hdf5-1.10.6                |nompi_he0bbb20_101        19.4 MB  conda-forge
          importlib-metadata-4.11.4  |   py37h03978a9_0          33 KB  conda-forge
          intel-openmp-2022.1.0      |    h57928b3_3787         3.7 MB  conda-forge
          keras-applications-1.0.8   |             py_1          30 KB  conda-forge
          keras-preprocessing-1.1.2  |     pyhd8ed1ab_0          34 KB  conda-forge
          libblas-3.9.0              |     15_win64_mkl         5.6 MB  conda-forge
          libcblas-3.9.0             |     15_win64_mkl         5.6 MB  conda-forge
          liblapack-3.9.0            |     15_win64_mkl         5.6 MB  conda-forge
          libprotobuf-3.19.1         |       h23ce68f_0         1.9 MB
          markdown-3.3.7             |     pyhd8ed1ab_0          67 KB  conda-forge
          mkl-2022.1.0               |     h6a75c08_874       182.7 MB  conda-forge
          numpy-1.21.6               |   py37h2830a78_0         5.3 MB  conda-forge
          openssl-1.1.1o             |       h8ffe710_0         5.7 MB  conda-forge
          pip-22.1.2                 |     pyhd8ed1ab_0         1.5 MB  conda-forge
          protobuf-3.19.1            |   py37hd77b12b_0         238 KB
          pyreadline-2.1             |py37h03978a9_1005         146 KB  conda-forge
          python-3.7.12              |h7840368_100_cpython        17.9 MB  conda-forge
          python_abi-3.7             |          2_cp37m           4 KB  conda-forge
          scipy-1.7.3                |   py37hb6553fb_0        24.4 MB  conda-forge
          setuptools-62.3.4          |   py37h03978a9_0         1.3 MB  conda-forge
          six-1.16.0                 |     pyh6c4a22f_0          14 KB  conda-forge
          tbb-2021.5.0               |       h2d74725_1         148 KB  conda-forge
          tensorboard-1.14.0         |           py37_0         3.2 MB  conda-forge
          tensorflow-1.14.0          |       h1f41ff6_0          23 KB  conda-forge
          tensorflow-base-1.14.0     |   py37hc8dfbb8_0        57.3 MB  conda-forge
          tensorflow-estimator-1.14.0|   py37h5ca1d4c_0         646 KB  conda-forge
          termcolor-1.1.0            |             py_2           6 KB  conda-forge
          typing_extensions-4.2.0    |     pyha770c72_1          27 KB  conda-forge
          werkzeug-2.1.2             |     pyhd8ed1ab_1         237 KB  conda-forge
          wrapt-1.14.1               |   py37hcc03f2d_0          48 KB  conda-forge
          zipp-3.8.0                 |     pyhd8ed1ab_0          12 KB  conda-forge
          ------------------------------------------------------------
                                                 Total:       346.1 MB

      The following NEW packages will be INSTALLED:

        absl-py            conda-forge/noarch::absl-py-1.1.0-pyhd8ed1ab_0
        astor              conda-forge/noarch::astor-0.8.1-pyh9f0ad1d_0
        ca-certificates    conda-forge/win-64::ca-certificates-2022.6.15-h5b45459_0
        cached-property    conda-forge/noarch::cached-property-1.5.2-hd8ed1ab_1
        cached_property    conda-forge/noarch::cached_property-1.5.2-pyha770c72_1
        gast               conda-forge/noarch::gast-0.5.3-pyhd8ed1ab_0
        google-pasta       conda-forge/noarch::google-pasta-0.2.0-pyh8c360ce_0
        grpcio             pkgs/main/win-64::grpcio-1.42.0-py37hc60d5dd_0
        h5py               conda-forge/win-64::h5py-3.2.1-nompi_py37he280515_100
        hdf5               conda-forge/win-64::hdf5-1.10.6-nompi_he0bbb20_101
        importlib-metadata conda-forge/win-64::importlib-metadata-4.11.4-py37h03978a9_0
        intel-openmp       conda-forge/win-64::intel-openmp-2022.1.0-h57928b3_3787
        keras-applications conda-forge/noarch::keras-applications-1.0.8-py_1
        keras-preprocessi~ conda-forge/noarch::keras-preprocessing-1.1.2-pyhd8ed1ab_0
        libblas            conda-forge/win-64::libblas-3.9.0-15_win64_mkl
        libcblas           conda-forge/win-64::libcblas-3.9.0-15_win64_mkl
        liblapack          conda-forge/win-64::liblapack-3.9.0-15_win64_mkl
        libprotobuf        pkgs/main/win-64::libprotobuf-3.19.1-h23ce68f_0
        m2w64-gcc-libgfor~ conda-forge/win-64::m2w64-gcc-libgfortran-5.3.0-6
        m2w64-gcc-libs     conda-forge/win-64::m2w64-gcc-libs-5.3.0-7
        m2w64-gcc-libs-co~ conda-forge/win-64::m2w64-gcc-libs-core-5.3.0-7
        m2w64-gmp          conda-forge/win-64::m2w64-gmp-6.1.0-2
        m2w64-libwinpthre~ conda-forge/win-64::m2w64-libwinpthread-git-5.0.0.4634.697f757-2
        markdown           conda-forge/noarch::markdown-3.3.7-pyhd8ed1ab_0
        mkl                conda-forge/win-64::mkl-2022.1.0-h6a75c08_874
        msys2-conda-epoch  conda-forge/win-64::msys2-conda-epoch-20160418-1
        numpy              conda-forge/win-64::numpy-1.21.6-py37h2830a78_0
        openssl            conda-forge/win-64::openssl-1.1.1o-h8ffe710_0
        pip                conda-forge/noarch::pip-22.1.2-pyhd8ed1ab_0
        protobuf           pkgs/main/win-64::protobuf-3.19.1-py37hd77b12b_0
        pyreadline         conda-forge/win-64::pyreadline-2.1-py37h03978a9_1005
        python             conda-forge/win-64::python-3.7.12-h7840368_100_cpython
        python_abi         conda-forge/win-64::python_abi-3.7-2_cp37m
        scipy              conda-forge/win-64::scipy-1.7.3-py37hb6553fb_0
        setuptools         conda-forge/win-64::setuptools-62.3.4-py37h03978a9_0
        six                conda-forge/noarch::six-1.16.0-pyh6c4a22f_0
        sqlite             conda-forge/win-64::sqlite-3.38.5-h8ffe710_0
        tbb                conda-forge/win-64::tbb-2021.5.0-h2d74725_1
        tensorboard        conda-forge/win-64::tensorboard-1.14.0-py37_0
        tensorflow         conda-forge/win-64::tensorflow-1.14.0-h1f41ff6_0
        tensorflow-base    conda-forge/win-64::tensorflow-base-1.14.0-py37hc8dfbb8_0
        tensorflow-estima~ conda-forge/win-64::tensorflow-estimator-1.14.0-py37h5ca1d4c_0
        termcolor          conda-forge/noarch::termcolor-1.1.0-py_2
        typing_extensions  conda-forge/noarch::typing_extensions-4.2.0-pyha770c72_1
        ucrt               conda-forge/win-64::ucrt-10.0.20348.0-h57928b3_0
        vc                 conda-forge/win-64::vc-14.2-hb210afc_6
        vs2015_runtime     conda-forge/win-64::vs2015_runtime-14.29.30037-h902a5da_6
        werkzeug           conda-forge/noarch::werkzeug-2.1.2-pyhd8ed1ab_1
        wheel              conda-forge/noarch::wheel-0.37.1-pyhd8ed1ab_0
        wrapt              conda-forge/win-64::wrapt-1.14.1-py37hcc03f2d_0
        zipp               conda-forge/noarch::zipp-3.8.0-pyhd8ed1ab_0
        zlib               anaconda/win-64::zlib-1.2.11-vc14h1cdd9ab_1


      Proceed ([y]/n)? y


      Downloading and Extracting Packages
      pyreadline-2.1       | 146 KB    | ################################################################################################################# | 100%
      google-pasta-0.2.0   | 42 KB     | ################################################################################################################# | 100%
      gast-0.5.3           | 20 KB     | ################################################################################################################# | 100%
      cached-property-1.5. | 4 KB      | ################################################################################################################# | 100%
      liblapack-3.9.0      | 5.6 MB    | ################################################################################################################# | 100%
      pip-22.1.2           | 1.5 MB    | ################################################################################################################# | 100%
      h5py-3.2.1           | 1.0 MB    | ################################################################################################################# | 100%
      termcolor-1.1.0      | 6 KB      | ################################################################################################################# | 100%
      tensorflow-1.14.0    | 23 KB     | ################################################################################################################# | 100%
      intel-openmp-2022.1. | 3.7 MB    | ################################################################################################################# | 100%
      astor-0.8.1          | 25 KB     | ################################################################################################################# | 100%
      zipp-3.8.0           | 12 KB     | ################################################################################################################# | 100%
      tensorflow-base-1.14 | 57.3 MB   | ################################################################################################################# | 100%
      six-1.16.0           | 14 KB     | ################################################################################################################# | 100%
      mkl-2022.1.0         | 182.7 MB  | ################################################################################################################# | 100%
      protobuf-3.19.1      | 238 KB    | ################################################################################################################# | 100%
      importlib-metadata-4 | 33 KB     | ################################################################################################################# | 100%
      cached_property-1.5. | 11 KB     | ################################################################################################################# | 100%
      libcblas-3.9.0       | 5.6 MB    | ################################################################################################################# | 100%
      setuptools-62.3.4    | 1.3 MB    | ################################################################################################################# | 100%
      openssl-1.1.1o       | 5.7 MB    | ################################################################################################################# | 100%
      tensorboard-1.14.0   | 3.2 MB    | ################################################################################################################# | 100%
      libblas-3.9.0        | 5.6 MB    | ################################################################################################################# | 100%
      keras-preprocessing- | 34 KB     | ################################################################################################################# | 100%
      wrapt-1.14.1         | 48 KB     | ################################################################################################################# | 100%
      absl-py-1.1.0        | 94 KB     | ################################################################################################################# | 100%
      scipy-1.7.3          | 24.4 MB   | ################################################################################################################# | 100%
      ca-certificates-2022 | 188 KB    | ################################################################################################################# | 100%
      tbb-2021.5.0         | 148 KB    | ################################################################################################################# | 100%
      typing_extensions-4. | 27 KB     | ################################################################################################################# | 100%
      grpcio-1.42.0        | 1.8 MB    | ################################################################################################################# | 100%
      tensorflow-estimator | 646 KB    | ################################################################################################################# | 100%
      python_abi-3.7       | 4 KB      | ################################################################################################################# | 100%
      libprotobuf-3.19.1   | 1.9 MB    | ################################################################################################################# | 100%
      numpy-1.21.6         | 5.3 MB    | ################################################################################################################# | 100%
      werkzeug-2.1.2       | 237 KB    | ################################################################################################################# | 100%
      markdown-3.3.7       | 67 KB     | ################################################################################################################# | 100%
      keras-applications-1 | 30 KB     | ################################################################################################################# | 100%
      hdf5-1.10.6          | 19.4 MB   | ################################################################################################################# | 100%
      python-3.7.12        | 17.9 MB   | ################################################################################################################# | 100%
      Preparing transaction: done
      Verifying transaction: done
      Executing transaction: done
</details>


## Keras
```bash
# Installed v2.3.1
conda install -c conda-forge keras
```
<details>
    <summary>Installation Log</summary>
    $ conda install -c conda-forge keras
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.10.3
  latest version: 4.13.0

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: C:\Users\Matt\.conda\envs\bokeh

  added / updated specs:
    - keras


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    keras-2.3.1                |   py37h21ff451_0         591 KB  conda-forge
    libgpuarray-0.7.6          |    h8ffe710_1003         345 KB  conda-forge
    mako-1.2.0                 |     pyhd8ed1ab_1          60 KB  conda-forge
    markupsafe-2.1.1           |   py37hcc03f2d_1          25 KB  conda-forge
    pygpu-0.7.6                |py37hec80d1f_1003         595 KB  conda-forge
    pyyaml-6.0                 |   py37hcc03f2d_4         151 KB  conda-forge
    theano-1.0.5               |   py37hf2a7229_3         3.7 MB  conda-forge
    vs2017_win-64-19.16.27033  |       hb90652a_6          15 KB  conda-forge
    vswhere-3.0.3              |       h57928b3_0         243 KB  conda-forge
    yaml-0.2.5                 |       h8ffe710_2          62 KB  conda-forge
    ------------------------------------------------------------
                                           Total:         5.8 MB

The following NEW packages will be INSTALLED:

  keras              conda-forge/win-64::keras-2.3.1-py37h21ff451_0
  libgpuarray        conda-forge/win-64::libgpuarray-0.7.6-h8ffe710_1003
  mako               conda-forge/noarch::mako-1.2.0-pyhd8ed1ab_1
  markupsafe         conda-forge/win-64::markupsafe-2.1.1-py37hcc03f2d_1
  pygpu              conda-forge/win-64::pygpu-0.7.6-py37hec80d1f_1003
  pyyaml             conda-forge/win-64::pyyaml-6.0-py37hcc03f2d_4
  theano             conda-forge/win-64::theano-1.0.5-py37hf2a7229_3
  vs2017_win-64      conda-forge/win-64::vs2017_win-64-19.16.27033-hb90652a_6
  vswhere            conda-forge/win-64::vswhere-3.0.3-h57928b3_0
  yaml               conda-forge/win-64::yaml-0.2.5-h8ffe710_2


Proceed ([y]/n)? y


Downloading and Extracting Packages
vswhere-3.0.3        | 243 KB    | ################################################################################################################# | 100%
mako-1.2.0           | 60 KB     | ################################################################################################################# | 100%
keras-2.3.1          | 591 KB    | ################################################################################################################# | 100%
pygpu-0.7.6          | 595 KB    | ################################################################################################################# | 100%
yaml-0.2.5           | 62 KB     | ################################################################################################################# | 100%
vs2017_win-64-19.16. | 15 KB     | ################################################################################################################# | 100%
pyyaml-6.0           | 151 KB    | ################################################################################################################# | 100%
libgpuarray-0.7.6    | 345 KB    | ################################################################################################################# | 100%
markupsafe-2.1.1     | 25 KB     | ################################################################################################################# | 100%
theano-1.0.5         | 3.7 MB    | ################################################################################################################# | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
</details>

## TQDM
```bash
# Installed v4.64.0
conda install -c conda-forge tqdm
```

<details>
  <summary>Installation Log</summary>
  $ conda install -c conda-forge tqdm
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.10.3
  latest version: 4.13.0

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: C:\Users\Matt\.conda\envs\bokeh

  added / updated specs:
    - tqdm


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    colorama-0.4.5             |     pyhd8ed1ab_0          18 KB  conda-forge
    tqdm-4.64.0                |     pyhd8ed1ab_0          81 KB  conda-forge
    ------------------------------------------------------------
                                           Total:          99 KB

The following NEW packages will be INSTALLED:

  colorama           conda-forge/noarch::colorama-0.4.5-pyhd8ed1ab_0
  tqdm               conda-forge/noarch::tqdm-4.64.0-pyhd8ed1ab_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
colorama-0.4.5       | 18 KB     | ################################################################################################################# | 100%
tqdm-4.64.0          | 81 KB     | ################################################################################################################# | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
</details>
