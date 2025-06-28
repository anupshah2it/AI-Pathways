import argparse
from core.router import Router

parser = argparse.ArgumentParser(description="Interface Engine CLI")
parser.add_argument("command", choices=["start", "stop"])
parser.add_argument("--config", default="channels.json")

args = parser.parse_args()

router = Router(args.config)

if args.command == "start":
    try:
        router.start()
        print("Engine started. Press Ctrl+C to stop.")
        while True:
            pass
    except KeyboardInterrupt:
        router.stop()
elif args.command == "stop":
    router.stop()
