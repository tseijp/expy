
# ExPy 1.2.2

The sophisticated tool needed for scientific computing.

- **Documentation:** ~https://youseitakei.github.io/expy~
- **Source code:** https://github.com/YouseiTakei/expy
- **Contributing:** coming soon
- **Bug reports:** coming soon
- **Website:** https://tsei.jp
- **Contact** contact@tsei.jp

It provides:

 - useful rendering formula, Formula deformation.
 - simply converting Jupyter notebook to PDF based on nbconvert.

To get the latest version :

- from https://pypi.python.org/project/expy-python/
- `$ pip install expy-python`

To get the latest version do:

- `$ git clone git://github.com/YouseiTakei/expy.git`
- `$ cd expy`
- `$ python setup.py install`

Documentation and usage:

- Everything is at: coming soon

From this directory, start Jupyter notebook and:
```python
>>> from expy  import F, x_, y_,
>>> f = F(y_, x_**x_)
>>> f.set(x_, 0)
>>> f()
```

Convert your Jupyter notebook. start cmd line and:
```cmd
$ nbc -a -p -t
```

Usage Example:

|Usage|Detail|  
|:-|:-|  
|`nbc -h`| check args help|  
|`nbc -i test.ipynb`| convert to pdf|  
|`nbc -a test_dir  `| convert all file in your directory|  
|`nbc -r test.pdf  `| remove converted pdf file or all files in directory|  
|`nbc -i test.ipynb -o html`| convert to html|  
|`nbc -a test_dir   -o html`| convert all files to html|  
|`nbc -r test_dir   -o html`| remove all html files in directory|  
|`nbc -i test.ipynb -p result\today\    `| use output path|  
|`nbc -i test.ipynb -t data\article.tplx`| use your template|  

Other Usage Hints:
- If you want to change template file, you can edit file in `~/.expy/latex/article.tplx`
- If you don't have auth and can't install this, you can use `$pip install expy-python --user`
- If you can't convret pd.DataFrame, you should run 'ep.init_ep()'

Call for Contributions:
----------------------

If you have found ExPy to be useful in your work, research or company,
please consider making a donation to the project commensurate with your resources.
