# Night Mode

### Dependencies

python 3.6+

### Setup

```bash
python3 -m venv .venv
```

To make script close programs need to add cron job.

```bash
crontab -e # add following line: to the end: `*/1    00-07        *     * *     /path/to/script/night_mode.sh`
```
