from setuptools import setup

package_name = 'image_system'

setup(

    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'image_system',
        'detect_human/HandNet',
        'detect_human/FaceNet',
        'detect_human/CocoPoseNet',
        'detect_human/entity',
        'detect_human/pose_detector',
        'detect_human/detect_human',
        'detect_human/classifier',
        'detect_human/model',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='ItoMasaki',
    author_email='is0449sh@ed.ritsumei.ac.jp',
    maintainer='ItoMasaki',
    maintainer_email='is0449sh@ed.ritsumei.ac.jp',
    keywords=['ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='image syste is made using ROS2',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_system = image_system:main',
            'detect_human = detect_human.detect_human:main',
        ],
    },
)
