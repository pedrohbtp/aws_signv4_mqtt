import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='aws_signv4_mqtt',  
     version='0.1.3',
     py_modules=['aws_signv4_mqtt'],
     scripts=[] ,
     author="Pedro Torres",
     author_email="",
     description="Utility to sign urls for aws mqtt",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/pedrohbtp/aws_signv4_mqtt",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     entry_points={
    'console_scripts': [
        'generate_signv4_mqtt_boto  =aws_signv4_mqtt:generate_signv4_mqtt_boto',
        'generate_signv4_mqtt  =aws_signv4_mqtt:generate_signv4_mqtt'
        ]
    }
 )