# Git Ignore Files Concatenator

A Python utility that combines multiple gitignore files into a single `.gitignore` file. This tool is useful when you're working on projects that involve multiple technologies and need to merge different gitignore templates.

For more gitignore templates, check out the [GitHub gitignore repository](https://github.com/github/gitignore/).

## Features

- ✅ Concatenate any number of gitignore files
- ✅ Customizable output filename
- ✅ Safe overwrite protection with user confirmation
- ✅ Force overwrite option for automation
- ✅ Clear file validation with helpful error messages
- ✅ Well-formatted output with source file identification
- ✅ Cross-platform compatibility using `pathlib`

## Installation

No installation required! Just clone this repository:

```bash
git clone https://github.com/MarkFawcett/create_gitignore_file.git
cd git-ignore-files
```

## Usage

### Basic Usage

Concatenate gitignore files and create a `.gitignore` file:

```bash
python create_git_ignore_file.py generic-gitignore python-gitignore
```

### Specify Custom Output File

```bash
python create_git_ignore_file.py -o my-custom-gitignore generic-gitignore python-gitignore js-gitignore
```

### Force Overwrite (Skip Confirmation)

```bash
python create_git_ignore_file.py --force generic-gitignore python-gitignore
```

### View Help

```bash
python create_git_ignore_file.py --help
```

## Command Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `gitignore_files` | - | One or more gitignore files to concatenate (required) | - |
| `--output` | `-o` | Output file name | `.gitignore` |
| `--force` | - | Overwrite output file without confirmation | `False` |

## Available Templates

This repository includes several pre-made gitignore templates:

- **`generic-gitignore`** - General files (Mac .DS_Store, etc.)
- **`python-gitignore`** - Python-specific ignores (\_\_pycache\_\_, .pyc, virtual environments, etc.)
- **`js-gitignore`** - JavaScript/Node.js ignores (node_modules, package-lock.json, etc.)

## Output Format

The generated file includes:
- Header with creation timestamp and source files
- Clear sections showing which content came from which source file
- Proper formatting with separators between different sources

Example output:
```gitignore
# Generated gitignore file
# Created by concatenating: generic-gitignore, python-gitignore
# Generated on: 2025-08-14 10:30:45

# From: generic-gitignore
==================================================
# Mac junk
.DS_Store

==================================================
# From: python-gitignore
==================================================
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
...
```

## Examples

### Web Development Project (Python + JavaScript)
```bash
python create_git_ignore_file.py generic-gitignore python-gitignore js-gitignore
```

### Python Data Science Project
```bash
python create_git_ignore_file.py generic-gitignore python-gitignore -o .gitignore
```

### Custom Project with Specific Output
```bash
python create_git_ignore_file.py -o project-gitignore generic-gitignore python-gitignore
```

## Adding Your Own Templates

You can easily add your own gitignore templates:

1. Create a new file with your gitignore patterns
2. Use it with the script:
   ```bash
   python create_git_ignore_file.py generic-gitignore your-custom-template
   ```

## Requirements

- Python 3.4+ (uses `pathlib`)
- No external dependencies

## Error Handling

The script includes comprehensive error handling:

- **Missing files**: Validates all input files exist before processing
- **File permissions**: Handles write permission errors gracefully
- **Overwrite protection**: Prompts before overwriting existing files (unless `--force` is used)
- **Clear error messages**: Provides helpful feedback for all error conditions

## Contributing

Feel free to contribute additional gitignore templates or improvements to the script:

1. Fork the repository
2. Add your gitignore template or make improvements
3. Submit a pull request

## License

This project is open source. Feel free to use and modify as needed.
