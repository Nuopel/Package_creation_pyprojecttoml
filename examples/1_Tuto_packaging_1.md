
# Beginner's Guide to Creating a Python Package


## Introduction
This tutorial offers a concise guide to creating a Python package, covering the essentials 
needed to structure and prepare your code for distribution. We'll explore how to establish a package, setting a foundation for more advanced topics like testing and documentation in future tutorials. Packaging is a vital skill for Python developers for code reusability, collaboration, distribution, and version control, facilitating efficient code sharing and modularity within the developer community. By the end of this guide, you'll understand how to package your Python code effectively, laying the groundwork for further enhancement and distribution.$
## Real-World Examples and Use Cases

Understanding the practical applications and benefits of creating Python packages can illuminate why mastering this skill is crucial. Here are a few real-world scenarios where creating a Python package is essential:

1. **Code Reusability**: Imagine you've developed a set of functions that can perform complex data analysis. By packaging these functions, you can easily reuse them across various projects without copying and pasting code.

2. **Collaboration**: When working on a team, packaging code helps ensure consistency. Team members can install the same package and utilize its functionality, ensuring that everyone is working with the same code base.

3. **Distribution**: If you've created a useful tool or library and want to share it with the broader Python community, packaging allows you to distribute your software such that others can easily install and use it, for example, through the Python Package Index (PyPI).

4. **Version Control**: Packages allow for versioning, enabling users to work with specific versions of your software, which is particularly important for maintaining compatibility and stability in production environments.

Through this tutorial, you'll gain the knowledge to structure, configure, and distribute your Python code as a package, empowering you to leverage these benefits in your own projects and contributions to the Python ecosystem.
## Understanding the Minimal Package Structure

A Python package requires a specific structure, which we'll create using terminal commands. The 
`src` layout is used here

Here's how to create the initial directory structure:

```bash
mkdir mypackage
cd mypackage
mkdir src
touch src/__init__.py  
touch pyproject.toml 
touch setup.cfg
```

This structure organizes your package as follows:

```
mypackage/
|-- src/
|   |-- __init__.py
|-- pyproject.toml
|-- setup.cfg
```

- `src/`: This directory contains your package's source code. Inside, the `__init__.py` file makes Python treat the directories as containing packages.
- `pyproject.toml`: Defines build system requirements and provides metadata for your package.
- `setup.cfg`: Offers metadata and configuration settings for your package, used by setuptools.
### Why Use the `src` Layout?

The `src` layout involves placing your package's source code in a subdirectory (typically named `src`). This structure is a best practice in Python packaging for several reasons:

1. **Isolates Source Code**: Keeps the source code separate from other project components like tests and documentation, reducing the risk of accidental mix-ups.
2. **Improves Testing**: Forces testing on the installed version of the package, catching potential installation or packaging issues.
3. **Prevents Namespace Collisions**: Avoids conflicts between your package's modules and other installed packages or standard library modules.
4. **Ensures Clean Installation**: Only the contents of the `src` directory are installed, preventing unnecessary files from being included.
5. **Enhances Reproducibility**: Mimics the installation environment, promoting consistency across development, testing, and production.

Adopting the `src` layout contributes to a cleaner, more maintainable, and reliable package structure.


### Writing the pyproject.toml File

The `pyproject.toml` file is a configuration file for building Python projects. Here's a basic template:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

This file specifies that your project uses setuptools as its build system and requires the wheel package.

### Writing the setup.cfg File

The `setup.cfg` file contains metadata about your package. Here's a simple example:

```ini
[metadata]
name = mypackage
version = 0.0.1
```


### Writing the setup.cfg File (More Details)

The `setup.cfg` file not only includes basic metadata about your package but can also specify dependencies, package information, and more. Here's an expanded example:

```ini
[metadata]
name = mypackage
version = 0.0.1
description = A simple example package
author = Your Name
author_email = your.email@example.com
license = MIT

[options]
packages = find:
install_requires =
    numpy >= 1.18.5
    requests >= 2.24.0
python_requires = >=3.6

[options.packages.find]
where = src 
```

This configuration includes essential details about the package and specifies that it requires Python 3.6 or newer, along with specific versions of `numpy` and `requests`.

### Creating a Basic Submodule with a Function

Let's create a simple submodule within our package:

1. Add a new Python file for our submodule inside the `src/mypackage` directory:

   ```bash
   touch src/mypackage/mymodule.py
   ```

2. Define a simple function in `mymodule.py`:

   ```python
   # src/mypackage/mymodule.py
   def greet(name):
       return f"Hello, {name}!"
   ```

### Installing the Package in Development Mode

When developing a Python package, you may want to test your changes as you code. Installing the package in editable (development) mode with `pip install -e .` allows you to do just that. This command creates a link from the installation directory to your source code directory. As a result, any modifications you make to the source code will be immediately reflected in the package behavior without the need for reinstallation.

```bash
pip install -e . #path to the package, where the pyproject is located
```

### Understanding Standard Installation

By contrast, the standard installation method, using `pip install package_name` or `pip install .`, copies the package files to the Python site-packages directory. This means the installed package is a snapshot of the code at the time of installation. If you update the source code, those changes won't be reflected in the installed package unless you perform another installation.

The standard installation is ideal for final or production environments, where you want the package to remain consistent and unaffected by further code changes.

In summary:

- **Development Mode (`-e` flag)**: Links the installed package to the source code, allowing live changes without reinstallation. It's perfect for ongoing development.
- **Standard Installation**: Copies the package to the site-packages directory, making it independent of the source code. This is suitable for deploying stable versions of the package in production environments.

### Testing Your Function with Import

After installation, you can test the function by importing and calling it:

```python
from mypackage.mymodule import greet
print(greet("World"))
```

This should output:

```
Hello, World!
```

By following these steps, you've expanded the `setup.cfg` for more detailed package configuration, created a simple submodule with a function, installed the package in development mode, and tested your function successfully.

## Error Handling and Common Pitfalls

When creating and developing a Python package, you might encounter several common issues. Here are some troubleshooting tips for typical errors:

1. **Missing `__init__.py`**: Ensure each package directory contains an `__init__.py` file. Without it, Python won't recognize the directory as a package, leading to import errors.

2. **Incorrect Module Imports**: Verify that your import statements match the directory structure. For example, if you have a submodule `mymodule` in the `mypackage` directory, you should import it using `from mypackage.mymodule import <function>`.

3. **Dependency Issues**: If your package relies on external libraries, ensure they are specified in the `install_requires` section of `setup.cfg`. If you encounter an error related to missing dependencies, check that you've listed all necessary libraries and their correct versions.

4. **Installation Errors**: When installing the package, if you face any errors, make sure you're in the root directory of the project (where `pyproject.toml` and `setup.cfg` reside). Also, ensure you have the necessary permissions to install packages in the target directory.


## Further Reading

To deepen your understanding of Python package development and configuration files, here are some resources:

1. **`setup.cfg`**:
   - [Python Packaging User Guide: setup.cfg](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#setup-cfg): A comprehensive guide to using `setup.cfg` in your Python package, detailing various configuration options.
   - [Setuptools Documentation](https://setuptools.pypa.io/en/latest/setuptools.html): The official setuptools documentation, providing in-depth information on various features, including `setup.cfg`.

2. **`pyproject.toml`**:
   - [PEP 518 -- Introducing pyproject.toml](https://www.python.org/dev/peps/pep-0518/): The Python Enhancement Proposal that introduced `pyproject.toml`, outlining its purpose and usage.
   - [Python Packaging User Guide: pyproject.toml](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-pyproject-toml): A tutorial on how to use `pyproject.toml` for Python projects, explaining its role in the packaging and build process.
3. PEP, or Python Enhancement Proposal, is a document that proposes and details new features or improvements for Python. PEPs are vital for ensuring a transparent, consensus-driven process in Python's evolution. For package developers, understanding PEPs like PEP 518, which introduces `pyproject.toml`, is key to adhering to Python's community standards, enhancing package consistency and reliability. For further details on PEPs and Python packaging, refer to the [Python Packaging User Guide](https://packaging.python.org) and [PEP Index](https://www.python.org/dev/peps/).

### Conclusion

This tutorial has provided a comprehensive overview of the essential steps involved in creating a minimal Python package. The process began with the establishment of a structured package directory utilizing the `src` layout, highlighting its significance in maintaining a clean and organized codebase. Following this, the tutorial covered the configuration of the package using `pyproject.toml` and `setup.cfg` files, which included defining essential metadata and dependencies.

The addition of a simple submodule illustrated the method of integrating functionality within the package's structure. The tutorial also demonstrated the advantages of installing the package in development mode, emphasizing the efficiency of reflecting source code changes in real-time, in contrast to the more static nature of standard installation.

Testing the functionality within the package served to validate the setup and underscored the practical benefits of the development mode installation.

### Looking Ahead

This foundational tutorial paves the way for further exploration and enhancement of Python packaging skills. The forthcoming intermediate tutorial will build on this base, incorporating additional elements such as unit tests, a README file, and licensing information, which are vital for improving a package's usability, maintainability, and distributability.

The next steps will equip individuals with the knowledge to develop more sophisticated and robust Python packages, facilitating their distribution within the Python community or integration into larger projects.

The subsequent tutorial will delve deeper into intermediate topics, continuing to refine the understanding and application of Python packaging practices.