# IML-diHiggs
Codes for reproducing the results of arXiv:2207.04157 (https://arxiv.org/abs/2207.04157)  

Machine learning the trilinear and light-quark Yukawa couplings from Higgs pair kinematic shapes  
Lina Alasfar, Ramona Gröber, Christophe Grojean, Ayan Paul, Zhuoni Qian  


### Dependencies

    - arviz
    - corner
    - matplotlib
    - networkx
    - numpy
    - pandas
    - pickle
    - pymc3
    - theano
    - scikitlearn   
    - scipy
    - shap
    - XGBoost

    


### Contents of the repository:

__fits__: contains the Bayesian and Frequentist fitting routines of from the ML results for the couplings  
__machine_learning__: contains the machine learning algorithms used to perform the analyse  
__plots__: contains the generated plots (for the paper and otherwise)  
__plotting-routins__: contains the plotting routines used during this work  
__results__: contains the confusion matrices and machine learning models (XGBoost)  
__simulation__: contains the simulated data  

```
.
├── fits
│   ├── data.yaml
│   ├── Fit-2P-FCC-hh.ipynb
│   ├── Fit-2P-HL-LHC.ipynb
│   ├── Fit-3P-HL-LHC-FCC-hh.ipynb
│   ├── freq_fits.ipynb
│   │   ├── sigma_br_FCC_hh.cpython-36.pyc
│   │   └── sigma_br_HL_LHC.cpython-36.pyc
│   ├── sigma_br_FCC_hh.py
│   └── sigma_br_HL_LHC.py
├── LICENSE
├── machine_learning
│   ├── Mega-BDT-kappa-lambda-FCC-hh.ipynb
│   ├── Mega-BDT-kappa-lambda-HL-LHC.ipynb
│   ├── Mega-BDT-ku-kd-FCC-hh.ipynb
│   └── Mega-BDT-ku-kd-HL-LHC.ipynb
├── plots
│   ├── FCC-hh-shap-bbxaa-bbh-tth-hhsm-kd-only.pdf
│   ├── FCC-hh-shap-bbxaa-bbh-tth-hhsm-kd.pdf
│   ├── FCC-hh-shap-bbxaa-bbh-tth-hhsm-ku-kd.pdf
│   ├── FCC-hh-shap-bbxaa-bbh-tth-hhsm-ku-only.pdf
│   ├── FCC-hh-shap-bbxaa-bbh-tth-hhsm-ku.pdf
│   ├── FCC-hh-shap-bbxaa-bbh-tth-hhsm.pdf
│   ├── FCC-hh-shap-bbxaa-bbh-tth-hhsm-SM.pdf
│   ├── FCC-hh-shap-ku-kd-hhsm.pdf
│   ├── FCC-hh-shap-ku-kd.pdf
│   ├── FCC-hh-sig100.pdf
│   ├── HL-LHC-shap-bbxaa-bbh-tth-hhsm-kd-only.pdf
│   ├── HL-LHC-shap-bbxaa-bbh-tth-hhsm-kd.pdf
│   ├── HL-LHC-shap-bbxaa-bbh-tth-hhsm-ku-kd-kl.pdf
│   ├── HL-LHC-shap-bbxaa-bbh-tth-hhsm-ku-kd.pdf
│   ├── HL-LHC-shap-bbxaa-bbh-tth-hhsm-ku-only.pdf
│   ├── HL-LHC-shap-bbxaa-bbh-tth-hhsm-ku.pdf
│   ├── HL-LHC-shap-bbxaa-bbh-tth-hhsm.pdf
│   ├── HL-LHC-shap-bbxaa-bbh-tth-hhsm-SM.pdf
│   ├── HL-LHC-shap-ku-kd-hhsm.pdf
│   ├── HL-LHC-shap-ku-kd.pdf
│   ├── HL-LHC-sig14.pdf
│   ├── kappa_d-kappa_l-FCC-hh.pdf
│   ├── kappa_d-kappa_l-HL-LHC.pdf
│   ├── kappa_u-kappa_d-FCC-hh.pdf
│   ├── kappa_u-kappa_d-HL-LHC.pdf
│   ├── kappa_u-kappa_d-kappa_l-FCC-hh.pdf
│   ├── kappa_u-kappa_d-kappa_l-HL-LHC.pdf
│   ├── kappa_u-kappa_l-FCC-hh.pdf
│   ├── kappa_u-kappa_l-HL-LHC.pdf
│   ├── kdku-HL-LHC.pdf
│   ├── kukl-HL-LHC.pdf
│   ├── networks-signal.pdf
│   ├── networks-signal-progression.pdf
│   ├── pph_hh_14Tev.pdf
│   └── ueberblick.pdf
├── plotting-routines
│   ├── bounds_review.ipynb
│   ├── networks.ipynb
│   ├── plot-maker-FCC-hh.ipynb
│   ├── plot-maker-HL-LHC.ipynb
│   │   ├── sigma_br_FCC_hh.cpython-36.pyc
│   │   └── sigma_br_HL_LHC.cpython-36.pyc
│   ├── sigma_br_FCC_hh.py
│   ├── sigma_br_HL_LHC.py
│   └── single-vs-di-Higgs.ipynb
├── README.md
├── results
│   ├── confusion
│   │   ├── FCC-hh-BDT
│   │   │   ├── hh-BDT-2class-ku-kd.confusion.json
│   │   │   ├── hh-BDT-2class-ku-kd-hhsm.confusion.json
│   │   │   ├── hh-BDT-3class-hhsm-SM.confusion.json
│   │   │   ├── hh-BDT-4class-kd-only.confusion.json
│   │   │   ├── hh-BDT-4class-ku-only.confusion.json
│   │   │   ├── hh-BDT-5class-hhsm.confusion.json
│   │   │   ├── hh-BDT-5class-ku-kd.confusion.json
│   │   │   ├── hh-BDT-6class-kd.confusion.json
│   │   │   ├── hh-BDT-6class-ku.confusion.json
│   │   │   └── hh-BDT-7class-ku-kd.confusion.json
│   │   └── HL-LHC-BDT
│   │       ├── hh-BDT-2class-ku-kd.confusion.json
│   │       ├── hh-BDT-2class-ku-kd-hhsm.confusion.json
│   │       ├── hh-BDT-3class-hhsm-SM.confusion.json
│   │       ├── hh-BDT-4class-kd-only.confusion.json
│   │       ├── hh-BDT-4class-ku-only.confusion.json
│   │       ├── hh-BDT-5class-hhsm.confusion.json
│   │       ├── hh-BDT-5class-ku-kd.confusion.json
│   │       ├── hh-BDT-6class-kd.confusion.json
│   │       ├── hh-BDT-6class-ku.confusion.json
│   │       └── hh-BDT-7class-ku-kd.confusion.json
│   └── models
│       ├── FCC-hh-BDT
│       │   ├── hh-BDT-2class-ku-kd-hhsm.pickle.dat
│       │   ├── hh-BDT-2class-ku-kd.pickle.dat
│       │   ├── hh-BDT-3class-hhsm-SM.pickle.dat
│       │   ├── hh-BDT-4class-kd.pickle.dat
│       │   ├── hh-BDT-4class-ku.pickle.dat
│       │   ├── hh-BDT-5class-hhsm.pickle.dat
│       │   ├── hh-BDT-5class-ku-kd.pickle.dat
│       │   ├── hh-BDT-6class-kd.pickle.dat
│       │   ├── hh-BDT-6class-ku.pickle.dat
│       │   └── hh-BDT-7class-ku-kd.pickle.dat
│       └── HL-LHC-BDT
│           ├── hh-BDT-2class-ku-kd-hhsm.pickle.dat
│           ├── hh-BDT-2class-ku-kd.pickle.dat
│           ├── hh-BDT-3class-hhsm-SM.pickle.dat
│           ├── hh-BDT-4class-kd.pickle.dat
│           ├── hh-BDT-4class-ku.pickle.dat
│           ├── hh-BDT-5class-hhsm.pickle.dat
│           ├── hh-BDT-5class-ku-kd.pickle.dat
│           ├── hh-BDT-6class-kd.pickle.dat
│           ├── hh-BDT-6class-ku.pickle.dat
│           └── hh-BDT-7class-ku-kd.pickle.dat
└── simulations
    ├── FCC-hh
    │   ├── bbxaa.tar.gz
    │   ├── HH-box.tar.gz
    │   ├── HH-int.tar.gz
    │   ├── HH-tri.tar.gz
    │   ├── kd-225.tar.gz
    │   ├── ku-480.tar.gz
    │   ├── ttH.tar.gz
    │   ├── yb2.tar.gz
    │   ├── ybyt.tar.gz
    │   ├── yt2.tar.gz
    │   └── zh.tar.gz
    └── HL-LHC
        ├── bbxaa.tar.gz
        ├── HH-box.tar.gz
        ├── HH-int.tar.gz
        ├── HH-tri.tar.gz
        ├── kd-800.tar.gz
        ├── ku-1600.tar.gz
        ├── ttH.tar.gz
        ├── yb2.tar.gz
        ├── ybyt.tar.gz
        ├── yt2.tar.gz
        └── zh.tar.gz
```

If you use the code or the results of the paper please cite

```
@article{Alasfar:2022vqw,
    author = {Alasfar, Lina and Gr\"ober, Ramona and Grojean, Christophe and Paul, Ayan and Qian, Zhuoni},
    title = "{Machine learning the trilinear and light-quark Yukawa couplings from Higgs pair kinematic shapes}",
    eprint = "2207.04157",
    archivePrefix = "arXiv",
    primaryClass = "hep-ph",
    reportNumber = "DESY 22-085 | HU-EP-21/34-RTG",
    month = "7",
    year = "2022"
}

```