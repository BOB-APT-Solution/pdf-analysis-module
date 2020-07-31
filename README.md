# pdf-analysis-module
```

pdf-analysis-module$ python3 main.py file.pdf --obfuscate  # javascript 난독화 해제하여 추출
pdf-analysis-module$ python3 main.py file.pdf --no-obfuscate # 난독화 안된 javascript의 경우 사용

```
## dependency
* python3.6.9
* python2.7.17
* pip install slimit (python2.7 pip로 수행)

## how to run
**1, 2 번은 클론 후 최초 1회만 실행**
1. pdf-analysis-module$ git submodule init
2. pdf-analysis-module$ git submodule update
3. pdf-analysis-module$ python3 main.py your-pdf.pdf

## output
your-pdf.js

