# concatenate gitignore files based on what the user specifies at the command line
import argparse
import sys
from pathlib import Path


def validate_input_files(file_paths):
    """Validate that all input files exist."""
    missing_files = []
    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists():
            missing_files.append(file_path)

    if missing_files:
        print("Error: The following files do not exist:")
        for file_path in missing_files:
            print(f"  - {file_path}")
        sys.exit(1)

def check_output_file_exists(output_path, force):
    """Check if output file exists and handle accordingly."""
    output_file = Path(output_path)
    if output_file.exists() and not force:
        response = input(f"File '{output_path}' already exists. Overwrite? (y/N): ")
        if response.lower() not in ['y', 'yes']:
            print("Operation cancelled.")
            sys.exit(0)

def write_concatenated_files(output_path, input_files):
    """Write concatenated gitignore files to output."""
    output_file = Path(output_path)
    try:
        with output_file.open('w') as f:
            f.write("# Generated gitignore file\n")
            f.write(f"# Created by concatenating: {', '.join(input_files)}\n")
            f.write(f"# Generated on: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            for i, file_path in enumerate(input_files):
                # Add separator between files
                if i > 0:
                    f.write("\n" + "="*50 + "\n")

                f.write(f"# From: {file_path}\n")
                f.write("="*50 + "\n")

                input_file = Path(file_path)
                content = input_file.read_text()
                # Remove trailing whitespace and ensure single newline at end
                content = content.rstrip() + "\n"
                f.write(content)

                f.write("\n")

        print(f"Successfully created '{output_path}' by concatenating {len(input_files)} file(s):")
        for file_path in input_files:
            print(f"  - {file_path}")

    except IOError as e:
        print(f"Error writing to output file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(
        description="Concatenate multiple gitignore files into a single .gitignore file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "\nExamples:"
            "\n  python create_git_ignore_file.py generic-gitignore python-gitignore"
            "\n  python create_git_ignore_file.py -o my-gitignore generic-gitignore python-gitignore"
        )
    )

    # Add arguments
    parser.add_argument(
        'gitignore_files',
        nargs='+',
        help='One or more gitignore files to concatenate'
    )

    parser.add_argument(
        '-o', '--output',
        default='.gitignore',
        help='Output file name (default: .gitignore)'
    )

    parser.add_argument(
        '--force',
        action='store_true',
        help='Overwrite output file if it exists'
    )

    # Parse arguments
    args = parser.parse_args()

    # Validate and process
    check_output_file_exists(args.output, args.force)
    validate_input_files(args.gitignore_files)
    write_concatenated_files(args.output, args.gitignore_files)

if __name__ == "__main__":
    main()
