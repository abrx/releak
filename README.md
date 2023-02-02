# releak

Follow releases, CVE and patch notes from the software and code you use

## Set your env

```bash
git clone https://github.com/abrx/releak.git
python -m venv releak-venv
source releak-venv/bin/activate
pip install -r requirements.txt
```

## Just get the releases

Only github releases supported by now.
Add user:repo in `config/versions.yml` :

```yaml
github:
  grafana: grafana
  traefik: traefik
```

Then launch main.py to get releases tags from followed repo:

```bash
python main.py
```

## Get releases in your browser

Launch Django server:

```
python manage.py runserver
```

Then go to http://127.0.0.1:8000/releak/ 

## Roadmap

Features :
[ ] Get full release data: date, is breaking, link, description
[ ] Set current releases states (e.g.: grafana = "9.3.1" ) with click and/or config file
[ ] Export current release state
[ ] Just launch a job that report differences between upstream and current state
[ ] Add concept of application to follow different set of releases 
[ ] Support SBOM ?

GUI:
[ ] Nice homepage
[ ] Add a repository to follow via GUI
[ ] Add stats tab to see how far are we from upstream and breaking changes
[ ] Add CVE-dedicated tab

Deployment:
[ ] Provide docker image
[ ] Build docker image via CI
[ ] Provide kubernetes deployment template

Supported sources:
[ ] gitlab
[ ] gitea
[ ] kubernetes releases
[ ] public CVE database

Refactoring:
[ ] 
