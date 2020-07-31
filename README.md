# pdf-analysis-module
### USAGE
```

pdf-analysis-module$ python3 main.py file.pdf --obfuscate  # javascript 난독화 해제하여 추출
pdf-analysis-module$ python3 main.py file.pdf --no-obfuscate # 난독화 안된 javascript의 경우 사용

```
## dependency
* python3.6.9
* python2.7.17

## how to install
1. pdf-analysis-module$ git submodule init
2. pdf-analysis-module$ git submodule update
3. pip install slimit (python2.7 pip로 수행)

## output
your-pdf.js

