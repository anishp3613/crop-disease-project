## LOGS
==> Cloning from https://github.com/anishp3613/crop-disease-project
==> Checking out commit f1e8f3b33d27318529d2b7a844a8494ffafbca7d in branch main
==> Installing Python version 3.10.7...
==> Using Python version 3.10.7 via environment variable PYTHON_VERSION
==> Docs on specifying a Python version: https://render.com/docs/python-version
==> Using Poetry version 2.1.3 (default)
==> Docs on specifying a Poetry version: https://render.com/docs/poetry-version
==> Running build command 'pip install -r requirements.txt'...
Collecting flask
  Downloading flask-3.1.3-py3-none-any.whl (103 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.4/103.4 kB 2.4 MB/s eta 0:00:00
Collecting gunicorn
  Downloading gunicorn-25.3.0-py3-none-any.whl (208 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 208.4/208.4 kB 12.3 MB/s eta 0:00:00
Collecting tensorflow
  Downloading tensorflow-2.21.0-cp310-cp310-manylinux_2_27_x86_64.whl (572.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 572.2/572.2 MB 1.1 MB/s eta 0:00:00
Collecting numpy
  Downloading numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.8/16.8 MB 85.8 MB/s eta 0:00:00
Collecting pandas
  Downloading pandas-2.3.3-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (12.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.8/12.8 MB 103.7 MB/s eta 0:00:00
Collecting pillow
  Downloading pillow-12.2.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (7.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 120.7 MB/s eta 0:00:00
Collecting scikit-learn
  Downloading scikit_learn-1.7.2-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (9.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.7/9.7 MB 109.4 MB/s eta 0:00:00
Collecting matplotlib
  Downloading matplotlib-3.10.8-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (8.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.7/8.7 MB 117.1 MB/s eta 0:00:00
Collecting itsdangerous>=2.2.0
  Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Collecting markupsafe>=2.1.1
  Downloading markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (20 kB)
Collecting click>=8.1.3
  Downloading click-8.3.1-py3-none-any.whl (108 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 108.3/108.3 kB 28.9 MB/s eta 0:00:00
Collecting werkzeug>=3.1.0
  Downloading werkzeug-3.1.7-py3-none-any.whl (226 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 226.3/226.3 kB 43.8 MB/s eta 0:00:00
Collecting blinker>=1.9.0
  Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Collecting jinja2>=3.1.2
  Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.9/134.9 kB 33.4 MB/s eta 0:00:00
Collecting packaging
  Downloading packaging-26.0-py3-none-any.whl (74 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 74.4/74.4 kB 18.7 MB/s eta 0:00:00
Collecting ml_dtypes<1.0.0,>=0.5.1
  Downloading ml_dtypes-0.5.4-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (5.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.0/5.0 MB 115.6 MB/s eta 0:00:00
Collecting astunparse>=1.6.0
  Downloading astunparse-1.6.3-py2.py3-none-any.whl (12 kB)
Collecting keras>=3.12.0
  Downloading keras-3.12.1-py3-none-any.whl (1.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.5/1.5 MB 89.5 MB/s eta 0:00:00
Collecting absl-py>=1.0.0
  Downloading absl_py-2.4.0-py3-none-any.whl (135 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 135.8/135.8 kB 33.1 MB/s eta 0:00:00
Collecting requests<3,>=2.21.0
  Downloading requests-2.33.1-py3-none-any.whl (64 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.9/64.9 kB 18.0 MB/s eta 0:00:00
Collecting six>=1.12.0
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Collecting grpcio<2.0,>=1.24.3
  Downloading grpcio-1.80.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (6.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.8/6.8 MB 116.3 MB/s eta 0:00:00
Collecting h5py<3.15.0,>=3.11.0
  Downloading h5py-3.14.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 120.3 MB/s eta 0:00:00
Requirement already satisfied: setuptools in ./.venv/lib/python3.10/site-packages (from tensorflow->-r requirements.txt (line 3)) (63.2.0)
Collecting wrapt>=1.11.0
  Downloading wrapt-2.1.2-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (113 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 113.6/113.6 kB 29.2 MB/s eta 0:00:00
Collecting protobuf<8.0.0,>=6.31.1
  Downloading protobuf-7.34.1-cp310-abi3-manylinux2014_x86_64.whl (324 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 324.3/324.3 kB 59.2 MB/s eta 0:00:00
Collecting google_pasta>=0.1.1
  Downloading google_pasta-0.2.0-py3-none-any.whl (57 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.5/57.5 kB 14.9 MB/s eta 0:00:00
Collecting opt_einsum>=2.3.2
  Downloading opt_einsum-3.4.0-py3-none-any.whl (71 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.9/71.9 kB 17.3 MB/s eta 0:00:00
Collecting gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1
  Downloading gast-0.7.0-py3-none-any.whl (22 kB)
Collecting flatbuffers>=25.9.23
  Downloading flatbuffers-25.12.19-py2.py3-none-any.whl (26 kB)
Collecting libclang>=13.0.0
  Downloading libclang-18.1.1-py2.py3-none-manylinux2010_x86_64.whl (24.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 24.5/24.5 MB 73.2 MB/s eta 0:00:00
Collecting termcolor>=1.1.0
  Downloading termcolor-3.3.0-py3-none-any.whl (7.7 kB)
Collecting typing_extensions>=3.6.6
  Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.6/44.6 kB 10.1 MB/s eta 0:00:00
Collecting python-dateutil>=2.8.2
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 44.7 MB/s eta 0:00:00
Collecting tzdata>=2022.7
  Downloading tzdata-2025.3-py2.py3-none-any.whl (348 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 348.5/348.5 kB 59.7 MB/s eta 0:00:00
Collecting pytz>=2020.1
  Downloading pytz-2026.1.post1-py2.py3-none-any.whl (510 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 510.5/510.5 kB 80.3 MB/s eta 0:00:00
Collecting joblib>=1.2.0
  Downloading joblib-1.5.3-py3-none-any.whl (309 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 309.1/309.1 kB 55.4 MB/s eta 0:00:00
Collecting scipy>=1.8.0
  Downloading scipy-1.15.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (37.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 37.7/37.7 MB 45.6 MB/s eta 0:00:00
Collecting threadpoolctl>=3.1.0
  Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Collecting contourpy>=1.0.1
  Downloading contourpy-1.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (325 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 325.0/325.0 kB 44.9 MB/s eta 0:00:00
Collecting fonttools>=4.22.0
  Downloading fonttools-4.62.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 MB 122.3 MB/s eta 0:00:00
Collecting cycler>=0.10
  Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Collecting pyparsing>=3
  Downloading pyparsing-3.3.2-py3-none-any.whl (122 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 122.8/122.8 kB 3.7 MB/s eta 0:00:00
Collecting kiwisolver>=1.3.1
  Downloading kiwisolver-1.5.0-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 101.4 MB/s eta 0:00:00
Collecting wheel<1.0,>=0.23.0
  Downloading wheel-0.46.3-py3-none-any.whl (30 kB)
Collecting rich
  Downloading rich-14.3.3-py3-none-any.whl (310 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 310.5/310.5 kB 57.7 MB/s eta 0:00:00
Collecting optree
  Downloading optree-0.19.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (419 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 419.7/419.7 kB 70.3 MB/s eta 0:00:00
Collecting namex
  Downloading namex-0.1.0-py3-none-any.whl (5.9 kB)
Collecting certifi>=2023.5.7
  Downloading certifi-2026.2.25-py3-none-any.whl (153 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 153.7/153.7 kB 41.5 MB/s eta 0:00:00
Collecting urllib3<3,>=1.26
  Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 131.6/131.6 kB 35.1 MB/s eta 0:00:00
Collecting idna<4,>=2.5
  Downloading idna-3.11-py3-none-any.whl (71 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.0/71.0 kB 20.3 MB/s eta 0:00:00
Collecting charset_normalizer<4,>=2
  Downloading charset_normalizer-3.4.6-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (207 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 207.9/207.9 kB 41.7 MB/s eta 0:00:00
Collecting pygments<3.0.0,>=2.13.0
  Downloading pygments-2.20.0-py3-none-any.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 101.1 MB/s eta 0:00:00
Collecting markdown-it-py>=2.2.0
  Downloading markdown_it_py-4.0.0-py3-none-any.whl (87 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 87.3/87.3 kB 24.5 MB/s eta 0:00:00
Collecting mdurl~=0.1
  Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Installing collected packages: pytz, namex, libclang, flatbuffers, wrapt, urllib3, tzdata, typing_extensions, threadpoolctl, termcolor, six, pyparsing, pygments, protobuf, pillow, packaging, opt_einsum, numpy, mdurl, markupsafe, kiwisolver, joblib, itsdangerous, idna, gast, fonttools, cycler, click, charset_normalizer, certifi, blinker, absl-py, wheel, werkzeug, scipy, requests, python-dateutil, optree, ml_dtypes, markdown-it-py, jinja2, h5py, gunicorn, grpcio, google_pasta, contourpy, scikit-learn, rich, pandas, matplotlib, flask, astunparse, keras, tensorflow
Successfully installed absl-py-2.4.0 astunparse-1.6.3 blinker-1.9.0 certifi-2026.2.25 charset_normalizer-3.4.6 click-8.3.1 contourpy-1.3.2 cycler-0.12.1 flask-3.1.3 flatbuffers-25.12.19 fonttools-4.62.1 gast-0.7.0 google_pasta-0.2.0 grpcio-1.80.0 gunicorn-25.3.0 h5py-3.14.0 idna-3.11 itsdangerous-2.2.0 jinja2-3.1.6 joblib-1.5.3 keras-3.12.1 kiwisolver-1.5.0 libclang-18.1.1 markdown-it-py-4.0.0 markupsafe-3.0.3 matplotlib-3.10.8 mdurl-0.1.2 ml_dtypes-0.5.4 namex-0.1.0 numpy-2.2.6 opt_einsum-3.4.0 optree-0.19.0 packaging-26.0 pandas-2.3.3 pillow-12.2.0 protobuf-7.34.1 pygments-2.20.0 pyparsing-3.3.2 python-dateutil-2.9.0.post0 pytz-2026.1.post1 requests-2.33.1 rich-14.3.3 scikit-learn-1.7.2 scipy-1.15.3 six-1.17.0 tensorflow-2.21.0 termcolor-3.3.0 threadpoolctl-3.6.0 typing_extensions-4.15.0 tzdata-2025.3 urllib3-2.6.3 werkzeug-3.1.7 wheel-0.46.3 wrapt-2.1.2
[notice] A new release of pip available: 22.2.2 -> 26.0.1
[notice] To update, run: pip install --upgrade pip
==> Uploading build...
==> Uploaded in 26.5s. Compression took 8.7s
==> Build successful 🎉
==> Deploying...
==> Setting WEB_CONCURRENCY=1 by default, based on available CPUs in the instance
==> No open ports detected, continuing to scan...
==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
==> Running 'gunicorn app:app'
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1775099433.839744      55 cudart_stub.cc:31] Could not find cuda drivers on your machine, GPU will not be used.
I0000 00:00:1775099435.442683      55 cpu_feature_guard.cc:227] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1775099474.146263      55 cudart_stub.cc:31] Could not find cuda drivers on your machine, GPU will not be used.
==> No open ports detected, continuing to scan...
==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
Matplotlib is building the font cache; this may take a moment.
E0000 00:00:1775099507.776436      55 cuda_platform.cc:52] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)
/opt/render/project/src/app.py:24: FutureWarning: DataFrame.applymap has been deprecated. Use DataFrame.map instead.
  fert_df = fert_df.applymap(lambda x: x.strip().lower() if isinstance(x, str) else x)
[2026-04-02 03:11:53 +0000] [55] [INFO] Starting gunicorn 25.3.0
[2026-04-02 03:11:53 +0000] [55] [INFO] Listening at: http://0.0.0.0:10000 (55)
[2026-04-02 03:11:53 +0000] [55] [INFO] Using worker: sync
[2026-04-02 03:11:53 +0000] [92] [INFO] Booting worker with pid: 92
[2026-04-02 03:11:53 +0000] [55] [INFO] Control socket listening at /opt/render/.gunicorn/gunicorn.ctl
127.0.0.1 - - [02/Apr/2026:03:11:54 +0000] "HEAD / HTTP/1.1" 200 0 "-" "Go-http-client/1.1"
==> Your service is live 🎉
==> 
==> ///////////////////////////////////////////////////////////
==> 
==> Available at your primary URL https://crop-disease-project-1.onrender.com
==> 
==> ///////////////////////////////////////////////////////////
