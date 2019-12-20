# Night Mode

We don't have infinite amount of willpower. Especially in the evenings I have a risk of running out. This small program intends to remind me of my decisions to stay away of some programs when I have run out of willpower- at night.

Program will close listed programs that you list automatically night hours.

### Dependencies

python 3.6+

### Setup

```bash
python3 -m venv .venv
```

To make script close programs need to add cron job.

```bash
crontab -e # add following line to the end: `*/1    00-07        *     * *     /path/to/script/night_mode.sh` <- this will make programs close every minute between midnight and 7 am.
```

List programs you don't want yourself to use in `night_mode.py` variable `list_of_night_mode_programs`. Program names need to be same as they are displayed in task manager (in `ps`, `top`, etc).
