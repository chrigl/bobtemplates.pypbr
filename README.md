# bobtemplates to create python packages with pbr

Creating python packages that use [pbr](http://docs.openstack.org/developer/pbr/) via [mr.bob](https://pypi.python.org/pypi/mr.bob/).

## Install
```
pip install bobtemplates.python_pbr
```

## Usage
```
mrbob bobtemplates.python_pbr:package
...
mrbob bobtemplates.python_pbr:namespace_package
```

## Variables

Set in ```~/.mrbob```

```
[variables]
user.name = My Name
user.email = my.name@example.com
user.homepage = http://www.example.com/
```

You will be asked for the relevant values anyway, but the default values of
the fields will be the defined ones.

If these variables are not defined, they are queried via git.

## Templates

### python\_package

Usual python package with [pbr](http://docs.openstack.org/developer/pbr/)

```
python-simple_package
python-simple_package/.gitignore
python-simple_package/LICENSE
python-simple_package/MANIFEST.in
python-simple_package/README.md
python-simple_package/setup.cfg
python-simple_package/setup.py
python-simple_package/simple_package
python-simple_package/simple_package/__init__.py
```

### python\_namespace\_package

python namspace package with [pbr](http://docs.openstack.org/developer/pbr/)

```
python-simple-namespace
python-simple-namespace/.gitignore
python-simple-namespace/LICENSE
python-simple-namespace/MANIFEST.in
python-simple-namespace/README.md
python-simple-namespace/setup.cfg
python-simple-namespace/setup.py
python-simple-namespace/simple
python-simple-namespace/simple/__init__.py
python-simple-namespace/simple/namespace
python-simple-namespace/simple/namespace/__init__.py
```
