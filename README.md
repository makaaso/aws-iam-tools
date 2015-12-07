aws-iam-tools
------------

前提条件

* virtualenvwrapper

動作確認環境

* Ubuntu14.04
* python3.4

環境設定

```
mkdir /opt/aws/aws-iam-tools/log
export AWSIAMTOOLS=<PRO or DEV>
mkvirtualenv reporting3.4 --python=/usr/local/bin/python3.4
workon reporting3.4
pip install boto3
pip install pyyaml
pip install argparse
```

