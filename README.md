# Marketplace

Marketplace is a Django web application for buying and selling products.

## Getting Started

### Installation Requirements

- Python 3.10 or above
- [Poetry](https://python-poetry.org/docs/#installation)
- [GNU Make](https://www.gnu.org/software/make/) (optional)

### Installation

```bash
make install
# OR
poetry install
```

### Run Server

```bash
make run-server
```
OR, if you don't have GNU Make installed. Run the following command inside the `marketplace` directory:

```bash
poetry run python manage.py runserver
```
