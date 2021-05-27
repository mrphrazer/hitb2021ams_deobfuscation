# Semi-Automatic Code Deobfuscation

This repository contains slides, samples and code of the 2h code deobfuscation workshop at [HITBSECCONF2021](https://conference.hitb.org/hitbsecconf2021ams/). In the first part, we use [`Miasm`](https://github.com/cea-sec/miasm) to automatically identify opaque predicates in the `X-Tunnel` APT128-malware using symbolic execution and SMT solving. Afterward, we remove the opaque predicates via patching. In the second part, we use [`msynth`](https://github.com/mrphrazer/msynth) to simplify Mixed Boolean-Arithmetic (MBA) expressions. In combination with symbolic execution, we explore and simply expressions in the `FinSpy` malware.

The recording will be available soon.

## Installation

```
git clone https://github.com/mrphrazer/hitb2021ams_deobfuscation.git
cd hitb2021ams_deobfuscation
git submodule update --init --rebase --recursive

# install dependencies
pip install -r requirements.txt
```

## Contact

For more information, contact Tim Blazytko ([@mr_phrazer](https://twitter.com/mr_phrazer)).