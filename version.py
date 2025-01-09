try:
    import pyinstaller_versionfile
except ImportError:
    print("pyinstaller_versionfile is not installed. Please install it using pip.")
    print("Trying to install it...")
    import os

    os.system("pip install pyinstaller-versionfile")
    try:
        import pyinstaller_versionfile
    except ImportError:
        print("Failed to install pyinstaller_versionfile. Please install it manually.")
        exit(1)

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Generate version file for PyInstaller."
    )
    parser.add_argument("version", type=str, help="Version number (e.g., 0.0.1)")
    args = parser.parse_args()

    # Remove leading 'v' if present
    version = args.version.lstrip("v")

    pyinstaller_versionfile.create_versionfile(
        output_file="versionfile.txt",
        version=version,
        company_name="spoo.me",
        file_description="A preview app for the hPyT library",
        internal_name="hPyT Preview",
        legal_copyright="© spoo.me. All rights reserved.",
        original_filename="hPyT-Preview.exe",
        product_name="hPyT Preview",
    )


if __name__ == "__main__":
    main()
