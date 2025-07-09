# MongoDB Connector RSTD

A Python package for connecting to restricted MongoDB databases with separate configurations for Capstone and Macro databases.

## Installation

You can install this package directly from GitHub using pip:

```bash
pip install git+https://github.com/yourusername/test-restricted_mongodb_access.git
```

## Usage

```python
from mongodb_connector_rstd import capstone, macro

# Access Capstone database collections
agent_01_collection = capstone.collection_agent_01
agent_02_collection = capstone.collection_agent_02

# Access Macro database collections
global_collection = macro.collection_global
test_collection = macro.collection_test
```

## Features

- Separate connections for Capstone and Macro databases
- Pre-configured collections for easy access
- Environment-based configuration management

## Requirements

- Python 3.7+
- pymongo
- python-dotenv

## License

MIT License
