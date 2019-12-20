import syslog
from subprocess import run, CompletedProcess

list_of_night_mode_programs = ["steam", "signal-desktop", "slack", "chrome"]


def is_unknown_error(result: CompletedProcess):
    return result.returncode is not 0 and "no process found" not in str(result.stderr)


def close_requested_programs(programs):
    for program in programs:
        result = run(["killall", "-3", program], capture_output=True)
        if is_unknown_error(result):
            syslog.syslog(
                f"Failed to close program '{program}'. "
                f"Killall exited with code {result.returncode} and error {result.stderr}"
            )


if __name__ == "__main__":
    close_requested_programs(list_of_night_mode_programs)
