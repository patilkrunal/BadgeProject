#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from pathlib import Path
import sys
import os


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BadgeProject.settings')

    root_path = os.path.abspath(os.path.split(__file__)[0])
    sys.path.insert(0, root_path)

    PARENT_DIR = Path(__file__).resolve().parent.parent
    sys.path.insert(1, PARENT_DIR)
    
    """ 
    print("****************************************************************************************")
    print(PARENT_DIR)
    print("****************************************************************************************")
    print(sys.path)
    print("****************************************************************************************") 
    """

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
