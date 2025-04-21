from setuptools import Command, setup, find_packages
import os

def prints():
    """
    This function runs during package installation.
    You can add custom code here, such as print statements or other operations.
    """
    print("Exploit successful")
    
    return True

# Custom command that ensures our code executes during pip install
class CustomInstallCommand(Command):
    description = "Custom install command that runs exploit code"
    user_options = []  # Required for Command subclass
    
    def initialize_options(self):
        """Required method for Command subclass"""
        pass
    
    def finalize_options(self):
        """Required method for Command subclass"""
        pass
    
    def run(self):
        """This is what actually gets executed when the command is run"""
        prints()
        # Make sure to run the standard install command
        self.run_command('install_lib')
        self.run_command('install_scripts')

# Execute custom code during setup
prints()

setup(
    name="merbe",
    version="0.0.1",
    author="Merzouka Youness",
    author_email="ya.merzouka@esi-sba.dz",
    description="Dummy module for security presentation",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="git@github.com:merzouka/dependency-confusion.security.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
