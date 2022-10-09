# ISS/INFN Data Downloader

This module serves as a downloader for **Istituto Superiore di Sanità** /
**Istituto Nazionale di Fisica Nucleare** data on COVID-19.

## Configuration

Before running the script, you should prepare a file containing the required
environment variables.

```bash
# .env
DEST_FOLDER=/home/user/Downloads
```

## Installation and Use

The main dependencies of this package are `python-dotenv` and `requests`.

In order to get the proper packages ready for use issue the following command.

```console
poetry install
```

Activate the environment by issuing the following command.

```console
$ source "$( poetry env list --full-path | grep Activated | cut -d' ' -f1 )/bin/activate"
```

The script can be executed by issuing the following command.

```console
(iss_downloader_env) $ python main.py
```

## Impressum

Shoichi Yip // 2022

This tool contributes to the **AIACE project** (UniTrento).

- Principal Investigator: [prof. Luca Tubiana](https://sbp.physics.unitn.it/luca-tubiana/)
- Postdoctoral Student: [dr. Jules Morand](https://sbp.physics.unitn.it/jules-morand/)
- Research Assistant: Shoichi Yip