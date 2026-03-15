# Autotask Explorer CLI

A lightweight Python CLI tool to quickly explore and test Kaseya Autotask REST API capabilities.

## Prerequisites

- Python 3.8+
- Kaseya Autotask API User credentials (Username, Password, and Integration Code)

## Setup

1. **Clone or download** this repository.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Environment Variables**:
   Create a `.env` file in the root directory (you can copy `.env.example`):
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and fill in your details:
   - `AUTOTASK_INTEGRATION_CODE`: Your API Integration Code (Tracking Identifier).
   - `AUTOTASK_USERNAME`: Your API User email.
   - `AUTOTASK_SECRET`: Your API User password.
   - `AUTOTASK_VERBOSE`: (Optional) Set to `True` for general logs.
   - `AUTOTASK_DEBUG`: (Optional) Set to `True` for detailed request/response logs including full URL, headers, and body.

## Usage

Run the tool using:
```bash
python run.py
```

### Features

- **Entity Support**: CRUD for Companies (Companies), Contacts, Opportunities, Sales Orders, and Service Desk Tickets.
- **Viewing**: List up to 25 records with optional field-based filtering.
- **Details**: View full JSON structure for any record by ID.
- **CRUD Operations**:
  - **Create**: Prompts for required fields and allows adding optional fields.
  - **Update**: Update specific fields by ID using PATCH (partial update).
  - **Delete**: Supports record deletion by ID (Note: some entities may only support status-based deactivation).

### Querying Examples

When prompted to filter by field:
- **Field**: `companyName`
- **Operator**: `=`
- **Value**: `Acme Corp`

### Project Structure

- `autotask_cli/main.py`: Main entry point and menu logic.
- `autotask_cli/client.py`: API client with zone discovery, auth, and retries.
- `autotask_cli/entities/`: Entity definitions and CRUD logic.
- `autotask_cli/cli/`: Formatting and UI utilities.

## Troubleshooting

- **Zone Discovery**: The tool automatically discovers your Autotask zone based on your username.
- **API Errors**: Detailed error messages from the Autotask API are printed when a request fails.
- **Rate Limiting**: The tool includes basic retry logic with backoff for 429 (Rate Limit) errors.
