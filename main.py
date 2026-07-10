from download import download_logs
from parser import load_events
from report import generate_report
from config import LOCAL_LOG


def main():

    if not download_logs():
        return

    events = load_events(LOCAL_LOG)

    generate_report(events)


if __name__ == "__main__":
    main()