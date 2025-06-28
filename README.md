# Interface Engine

This project provides a modular interface engine for healthcare data exchange.

## Features
- Plugin-based adapters
- Configurable channels in `channels.json`
- Simple JavaScript translators
- CLI to start/stop the engine
- Docker support

## Development

```bash
pip install -r requirements.txt
pytest
```

## Running

```bash
python -m cli.main start --config channels.json
```

See `translators/sample.js` for an example translator.
