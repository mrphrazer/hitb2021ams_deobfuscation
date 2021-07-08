# Semi-Automatic Code Deobfuscation
This repository contains slides, samples and code of the 2h code deobfuscation workshop at [HITBSecConf2021 AMSTERDAM](https://conference.hitb.org/hitbsecconf2021ams/). In the first part, we use [`Miasm`](https://github.com/cea-sec/miasm) to automatically identify opaque predicates in the `X-Tunnel` APT128-malware using symbolic execution and SMT solving. Afterward, we remove the opaque predicates via patching. In the second part, we use [`msynth`](https://github.com/mrphrazer/msynth) to simplify Mixed Boolean-Arithmetic (MBA) expressions. In combination with symbolic execution, we explore and simplify expressions in the `FinSpy` malware.

The recording will be available soon.

## Installation
```sh
# on debian/ubuntu based systems:
sudo apt-get install python-dev

# clone repository and init submodules
git clone https://github.com/mrphrazer/hitb2021ams_deobfuscation.git
cd hitb2021ams_deobfuscation
git submodule update --init --rebase --recursive

# on windows systems (from a Visual Studio 2019 command prompt):
cd msynth\miasm
python setup.py build
cd ..\..

# install dependencies
pip install -r requirements.txt
```

## Contact
For more information, contact Tim Blazytko ([@mr_phrazer](https://twitter.com/mr_phrazer)).
