#!/usr/bin/env python
# Shebang line: Tells the system to run this file using the default Python interpreter

"""Django's command-line utility for administrative tasks."""
# This is a docstring that describes the purpose of this script

import os
# Imports the 'os' module to interact with the operating system (like setting environment variables)

import sys
# Imports the 'sys' module to access command-line arguments

def main():
    # Main function that will run when the script is executed

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom_project.settings')
    # Sets the default Django settings module to 'ecom_project.settings'
    # This tells Django which settings file to use for the project

    try:
        from django.core.management import execute_from_command_line
        # Imports Django’s command-line utility for executing management commands
        # (like runserver, migrate, makemigrations, etc.)

    except ImportError as exc:
        # If the Django module is not found (not installed), an ImportError will be raised

        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        # Displays a helpful error message if Django is not installed or not found

    execute_from_command_line(sys.argv)
    # Executes the command-line arguments passed to the script using Django’s command handler
    # Example: python manage.py runserver

if __name__ == '__main__':
    # Checks if this file is being run directly (not imported as a module)

    main()
    # Calls the main function to start the script
