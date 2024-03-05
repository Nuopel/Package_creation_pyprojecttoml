
### 1. Introduction

#### 1.1 Objective:
The primary goal of this tutorial is to demystify the process of creating a Python package from scratch.
By the end of this guide, you will have a clear understanding of how to structure a Python 
package, write functional code within it, and prepare it for distribution.

This tutorial is designed to provide hands-on experience, taking you through the essential 
steps of package creation, including setting up your environment, defining the package structure,
writing code, and using your package.

Whether you're a beginner looking to gain practical 
experience or an intermediate programmer aiming to solidify your understanding of Python 
packages, this tutorial is tailored to help you achieve a solid foundation in Python package development. Our journey will start with the basics of package creation and advance through to distribution, ensuring that you're equipped with the knowledge to create your own Python packages in the future.

#### 1.2 Prerequisites:
Before diving into this tutorial, ensure you meet the following prerequisites to have a smooth learning experience. This tutorial assumes you have a basic understanding of Python and its ecosystem. If you're new to Python or need a refresher, consider reviewing some of the resources linked below.

- **Python Installation**: You should have Python installed on your system. This tutorial is compatible with Python 3.6 and above. If you haven't installed Python yet or are unsure about your Python version, you can download it from the [official Python website](https://www.python.org/downloads/). Use the provided code snippet in your terminal or command prompt to check your Python version:
  ```bash
  python --version
  ```
  or, on some systems, you might need to use `python3` instead:
  ```bash
  python3 --version
  ```

- **Basic Python Syntax**: Familiarity with basic Python syntax is necessary. If you're new to Python or need to brush up on your skills, there are numerous free resources available online. [Codecademy's Python Course](https://www.codecademy.com/learn/learn-python-3) and [Python.org's Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide) are excellent places to start.

- **Virtual Environment**: Knowledge of using virtual environments in Python is recommended. Virtual environments allow you to manage dependencies for different projects separately. If you're not familiar with virtual environments, the [Python Packaging Authority's guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) is a comprehensive resource to get started.

- **Text Editor or IDE**: You'll need a text editor or an Integrated Development Environment 
  (IDE) to write your code. Popular choices include [Visual Studio Code](https://code.
  visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), [Sublime Text]
  (https://www.sublimetext.com/) or spyder.

- **Command Line Basics**: Basic familiarity with the command line or terminal. You'll be using 
  the command line to execute Python scripts, manage virtual environments, and install packages.
  If you're new to using the command line, [Codecademy's Command Line tutorial](https://www.
  codecademy.com/learn/learn-the-command-line) offers a beginner-friendly introduction.

Ensure that your setup meets these requirements before proceeding to the next section of the 
tutorial.  This will help in avoiding unnecessary interruptions and will make the learning 
process smoother and more enjoyable.

### 2. Conceptual Overview

In Python, the terms "package" and "module" are related but distinct concepts used to organize and structure code. Here's a brief explanation of each, followed by their differences:

- **Module**: A module in Python is a single file containing Python definitions and statements. The file name (minus the `.py` extension) is the module name. Modules are the simplest form of code organization in Python, allowing you to group related functions, classes, and variables. When you want to use a function or a class from a module, you can import it into your current script or interactive session.

- **Package**: A package is a collection of Python modules organized within a directory hierarchy. It's a way of structuring Python’s module namespace by using “dotted module names”. A package must contain a special file named `__init__.py` (which can be empty) to be recognized by Python as a package.  Packages allow for a hierarchical structuring of the module namespace using dot notation (e.g., `package.subpackage.module`).

#### 2.1 Key Differences Illustrated:

1. **Structural Difference**:
   - A **module** is a single `.py` file.
   - A **package** is a directory that contains multiple modules or sub-packages and includes an `__init__.py` file.

2. **Use Case**:
   - Use a **module** to organize related code in a single file.
   - Use a **package** to organize a larger collection of related modules and possibly further sub-packages into a structured hierarchy.

3. **Import Syntax**:
   - For a **module** named `module.py`, you import it using `import module` or `from module import function`.
   - For a **package**, you might use `import package.module` or `from package.subpackage import module`.

#### 2.2 Simple Diagram:

Imagine a filesystem tree where a directory represents a package and a file represents a module:

```
my_package/ (package)
│
├── __init__.py
├── moduleA.py (module)
└── subpackage/ (sub-package)
    ├── __init__.py
    └── moduleB.py (module)
```

- `my_package` is a package because it contains an `__init__.py` file.
- `moduleA.py` and `moduleB.py` are modules.
- `subpackage` is a sub-package of `my_package`, also containing its own `__init__.py` file.

This structure allows for modular development and organization of larger Python projects, facilitating reuse and namespace management.- A high-level directory structure diagram based on your project layout.

#### Screenshots:
- Example of `pyproject.toml` and `setup.cfg` with highlighted sections to explain their roles.

### 3. Step-by-Step Guide: Getting Started 

This section will guide you through the initial steps of setting up your environment to use the Python package we're focusing on. Follow these steps to download the package, set up your environment, and begin exploring its functionalities.

#### 3.1 Download the Python Package if not done:
Create a directory where you will store your files and experiments.

Then, clone the repository containing the Python package to your local machine. Open your 
terminal in your folder and run the following command:
```bash
git clone https://github.com/Nuopel/Package_creation_pyprojecttoml
```
This command downloads the package source code so you can work with it directly. You can also 
directly download the project on the provided link.

#### 3.2 Environment Setup 

#### 3.2 Environment Setup
##### 3.2.1 Environment Setup (PyCharm based):
For those using PyCharm, setting up a virtual environment is straightforward:

1. Open PyCharm and open  your folder as a new project.
2.  navigate to `File > Settings`, Under `Project: <YourProjectName>`, select `Project Interpreter`.
3. Click on the gear icon, then `Add`.
4. In the left pane of the dialog that appears, select `Virtualenv Environment`. Then, choose `New environment`.
5. Specify the location for your new virtual environment or accept the default. Ensure the base interpreter is set to the Python version you intend to use.
6. Click `OK` to create and select this interpreter for your project.

##### 3.2.2 Environment Setup (terminal based):
To isolate your project dependencies, create a virtual environment by running the following commands in your terminal:

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```
This creates a virtual environment named `env` and activates it. While activated, any Python or pip commands will use the versions in the virtual environment, not your global Python installation.

#### 3.3 Installing the Python Package 

##### 3.2.1 Installing the Python Package (terminal based):
To install the package locally (making it usable within your project), navigate to the package directory in your terminal. Ensure your virtual environment is activated, then run:
```bash
pip install .
```
This command tells pip to install the package found in the current directory.

##### 3.3.1 Installing the Python Package (PyCharm based):
PyCharm Package Management: PyCharm also offers a graphical interface for managing packages 
via :
- Preferences > Project: YourProjectName > Python Interpreter. Here, you can see a list of 
installed packages and add or remove packages using the GUI, although for installing a local 
  package,  using the terminal as described is necessary.
- Or navigate to the bottom of the IDE and look for a tab named Python Packages (you might have to 
   click on the square icon with four squares to find it if it's not immediately visible).  This 
  tab opens the Python Packages tool window. Then use 'add package' and select the downloaded 
  package in the opened windows.

#### 3.4 Playing Around with the Package:

Now that the package is installed in your local environment, let's explore some of its capabilities.
Run `examples/example.py`. You'll explore two import methods:

- **Relative Local Import**: A temporary workaround demonstrating Python's adaptable import system, illustrating flexibility but advised against for general use due to maintenance challenges.

- **Direct Import**: The standard practice of directly importing a function from an installed package, emphasizing proper installation and showcasing best practices for straightforward and effective package utilization.

##### 3.4.1 Importing the Package

Begin by importing the package in a Python script or interactive session:
```bash
python import mypackage
```    
##### 3.4.2 Accessing a Module

If there are sub-modules in `my_package`, you can access them using the dot notation. For 
example, if you want to access the module `module0` from `my_package`, use:
```bash
python import mypackage.module0
```    

##### 3.4.3 Using Functions or Classes from the Package

After importing the module, you can use any functions or classes within it. For instance, if 
there is a function named `hello` in `module0`, call it if it doesn't require any argument:

Replace `hello()` with any functions that are available in the module `module0`.
```bash
python my_package.modulep0.hello()
```   

##### 3.4.4 Exploring Package Content

To explore more about what's inside your package or any Python package, you can use the `dir()` function.
```bash
python print(dir(my_package))
```   
This will list all the functions, classes, and sub-packages within `my_package`.

Remember to replace `my_package` and `moduleA` with the actual names from your package and its sub-modules respectively. Happy exploring!

#### 3.5 Conclusion : Why Direct Import is preferred over Relative Local Import ?

Direct Import ensures a clean and maintainable codebase by capitalizing on the structured and predictable nature of installed packages. This approach avoids complexities and potential pitfalls associated with Relative Local Import, such as:

- **Portability Problems**: Direct Import does not rely on the project's directory structure, ensuring code is easily transferable and works consistently across different environments without modification.

- **Inconsistent Versions**: By using Direct Import from installed packages, you avoid the risk of having multiple, inconsistent versions of the same function or module scattered across different projects, which can lead to confusion and errors.

This method promotes best practices in software development, making your code more robust, easier to manage, and scalable.

##### What you have learn :
- **Package Installation**: Learned how to properly install a Python package, ensuring it's correctly integrated into the development environment.
- **Utilizing Imports**: Mastered the use of import statements to access and utilize functions from installed packages, enhancing code functionality and modularity.
