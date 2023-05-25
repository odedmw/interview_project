import unittest
from code import *


class RequirementsTest(unittest.TestCase):
    def test_Requirements_func(self):
        EXPECTED_RESULT = 'altair,asttokens,attrs,backcall,bcrypt,blinker,cachetools,certifi,charset-normalizer,click,colorama,commonmark,cycler,debugpy,decorator,entrypoints,executing,extra-streamlit-components,fonttools,gitdb,GitPython,graphviz,idna,importlib-metadata,ipykernel,ipython,ipywidgets,jedi,Jinja2,jsonpath,jsonpath-ng,jsonschema,jupyter-client,jupyter-core,jupyterlab-widgets,kiwisolver,MarkupSafe,matplotlib,matplotlib-inline,nest-asyncio,numpy,packaging,pandas,parso,path-dict,pickleshare,Pillow,plotly,ply,prompt-toolkit,protobuf,psutil,pure-eval,pyarrow,pydeck,Pygments,PyJWT,Pympler,pyparsing,pyrsistent,python-dateutil,pytz,pytz-deprecation-shim,pywin32,PyYAML,pyzmq,requests,rich,semver,six,smmap,stack-data,streamlit,streamlit-authenticator,tenacity,toml,toolz,tornado,traitlets,turtle,typing_extensions,tzdata,tzlocal,urllib3,validators,watchdog,wcwidth,widgetsnbextension,zipp,ode,ad,dap,isr,dog'
        result = get_requirements(__file__.replace("test.py", "") + 'requirements.txt')
        self.assertEqual(result, EXPECTED_RESULT)




if __name__ == '__main__':
    unittest.main()