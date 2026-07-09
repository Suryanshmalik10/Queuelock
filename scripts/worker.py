import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.config import settings
from app.services.queue import dequeue_and_process
from app.services.hold_expiry import handle_hold_expiry


def handle_test_echo(payload: dict):
    print(f"    -> test_echo payload: {payload}")


HANDLERS = {
    "test_echo": handle_test_echo,
    "hold_expiry": handle_hold_expiry,
}


def main():
    worker_name = sys.argv[1] if len(sys.argv) > 1 else "worker-1"
    print(f"[{worker_name}] starting, polling every {settings.worker_poll_interval_seconds}s")

    while True:
        job = dequeue_and_process(HANDLERS, worker_name=worker_name)
        if job is None:
            time.sleep(settings.worker_poll_interval_seconds)


if __name__ == "__main__":
    main()
