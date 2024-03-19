# Packaging Python Projects with `pyproject.toml` and `setup.cfg`

The `pyproject.toml` file is a modern approach to specifying project metadata and dependencies for Python packages. Alongside it, a `setup.cfg` file is used for configuration in the traditional packaging setup.

In this guide, we'll walk through creating a `pyproject.toml` file and a `setup.cfg` file step by step.

This README provides a comprehensive overview of the package that this project pertains to. If you're a newcomer to the concept of a package, or if you seek to broaden your understanding, you're welcome to visit the example directory. The tutorial in there is created with the intent to demonstrate the function and structure of a package. Taking the time to explore it will be beneficial
```
mypackage/
 └── examples/ # THERE !
     ├── 0_course_what_is_a_package.md
     ├── 1_Tuto_packaging_1.md
     └── example.py
```


## Table of Contents

- [1 Project Structure](#1-project-structure)
  - [1.1 Writing pyproject.toml](#11-writing-pyprojecttoml)
  - [1.2 Writing setup.cfg](#12-writing-setupcfg)
  - [1.3 src folder](#13-src-folder)
  - [1.4 exemple folder](#14-exemple-folder)
  - [1.5 Purpose of the 'tests' Directory in Python Packages (optional)](#15-purpose-of-the-tests-directory-in-python-packages-optional)
  - [1.6 README.md Example (optional but advised)](#16-readmemd-example--optional-but-advised)
  - [1.7 License](#17-license)
- [2 Installing a Python Package](#2Installing-a-Python-Package)
- [Conclusion](#conclusion)

## 1 Project Structure

Before creating the `pyproject.toml` and `setup.cfg` files, ensure your project has the following directory structure:

```
mypackage/
 ├── pyproject.toml (mandatory)
 ├── setup.cfg (mandatory)
 ├── LICENSE (optional but advised)
 ├── README.md (optional but highly recommended)
 ├── tests/ (optional but advised)
 ├── src/ (mandatory)
 │      ├── mypackage/
 │      │   ├── __init__.py (minimum)
 │      │   ├── moduleO.py (minimum)
 │      │   ├── subpackages1/
 │      │   │   ├── __init__.py
 │      │   │   ├── module1.py
 └── examples/
     └── example.py
```

The proposed structure follows the "src layout," which is considered best practice for Python packaging. It makes it clear where to find package-related files, source code, and tests.

**The Importance of `__init__.py` in Python Packages**

The `__init__.py` file must be included in each subdirectory of a Python package to signal that it should be treated as part of the package. This empty file is crucial for proper module imports. Without it, imports from the subdirectory will fail.

### 1.1 Writing `pyproject.toml`

In your `pyproject.toml` file, define your package metadata. Here's an example:

```toml
[build-system]
requires = ["setuptools>=42", "wheel", "setuptools_scm"]
build-backend = "setuptools.build_meta"

```

This `pyproject.toml` file specifies project metadata for 'mypackage' using a standard format.

### 1.2 Writing `setup.cfg`

Create a `setup.cfg` file in your project directory with the following content:

```ini
[metadata]
name = mypackage
version = 1.0.0
description = A minimal Python package
author = Your Name
author_email = your@email.com
license = MIT

[options]
packages = find:
python_requires = >=3.7
install_requires =
    numpy>=1.0

[options.packages.find]
where = src

```

This `setup.cfg` file specifies project metadata and build configuration for 'mypackage' in the traditional packaging setup.

### 1.3 src folder
The src folder is a conventional structure in Python projects, adopting the "src layout" best practice.
It serves as the primary directory where the source code of your package resides.

Inside the src folder, you find a subdirectory that represents your package, typically named after the package itself. This naming is crucial because it's the identifier you'll use in your code when importing modules from this package.

```
  ── src/
        ├── mypackage/ # Name of the package you will use in 'import mypackage'
        │   ├── __init__.py # Allows the detection of .py in the package for short
        │   ├── moduleO.py (minimum) # Example module within your package.
        │   ├── subpackages1/ # Subpackage directory.
        │   │   ├── __init__.py
        │   │   ├── module1.py # Example module within a subpackage.
```
It's important to note that the package name in the src directory does not have to match the package name specified in setup.cfg, although they often do for simplicity. The name in setup.cfg is used for distribution and should be unique on repositories like PyPI, while the directory name in src is used within your code for imports.

### 1.4 example folder 
The examples folder is optional but recommended. 
It can contain example scripts that demonstrate how to use your package. 
For instance, you can have an example.py file showcasing your package's functionality.

The current examples folder is both for learners to understand what a package is and how to create 
one. The tutorials inside this folder are presenting what is a package in details and 
step-by-step tutorials on how to create and use a package inside python.


### 1.5 Purpose of the 'tests' Directory in Python Packages (optional)

The 'tests' directory is crucial in Python packages for ensuring code correctness, reliability, and quality.

This directory is optional but recommended. It should contain test scripts that verify the correct functionality of your package's functions and classes. You can organize your tests using a testing framework like 'unittest' or 'pytest'.

### 1.6 README.md Example (optional but advised)

In the README.md file of your project, it's crucial to provide helpful information about installation, minimal examples, and a detailed explanation of your package. Here's a template for your README.md:

- **Installation:** Explain how users can install your package. For instance: `pip install mypackage`.
- **Usage:** Provide a minimal usage example of your package.
- **Detailed Explanation:** Offer a comprehensive explanation of your package, including its purpose, features, and how users can benefit from it. You can use [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/) for formatting.

### 1.7 LICENSE (optional but advised)
This file is optional but highly recommended. It contains the licensing information for your package. You can choose a license that suits your project, and you should include the full text of the license you've chosen.


## 2 Installing a Python Package

Python packages are often installed using the 'pip' tool, which allows you to easily manage and install packages from various sources. Here's how you can use 'pip' to install your package and test it:

**Using pip for Installation:**

You can use 'pip' to install your package and verify that it functions correctly. Follow these steps:

1. Navigate to the directory that contains your package, ensuring you are in the directory above your package folder.

2. Open a Windows command prompt or terminal.

3. Run the following command to install the package:

   ```bash
   py -m pip install <path to folder>
   ```

   Replace `<path to folder>` with the actual path to your package folder.

**Development Mode Installation:**

You can also install your package from a local source in development mode. This means that your project will appear as installed, but it will remain editable within your project directory. To do the following instead at step 3:

3. Run the following command:

   ```bash
   py -m pip -e install <path to folder>
   ```

   Replace `<path to folder>` with the actual path to your package folder.

**Using PyCharm:**

If you prefer using PyCharm, you can also install the package within a virtual environment. Follow these steps:

1. Open PyCharm and your project.
2. Go to 'Python Packages' within the PyCharm IDE.
3. Choose 'Add Package' and then 'From disk.'
4. Navigate to your package folder and select it.

By following these methods, you can install your Python package using 'pip' and test its functionality. This allows you to verify that your package works as expected before sharing it with others or deploying it in different environments.


## Conclusion

Creating a `pyproject.toml` and `setup.cfg` file is a modern and efficient approach to specifying project metadata and dependencies for Python packages. By using these files, you can prepare your package for distribution and make it accessible to others.

For more advanced use cases or customization, refer to the official Python packaging documentation and best practices.

Happy packaging!
