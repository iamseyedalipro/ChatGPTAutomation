from setuptools import setup, find_packages

# Read requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ChatGPTAutomation',
    version='0.6.0',
    author='Seyed Ali Hosseini',
    author_email='iamseyedalipro@gmail.com',
    description='A Python package for automating interactions with ChatGPT using Selenium.',
    long_description=open('README.md', encoding="utf8").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/iamseyedalipro/ChatGPTAutomation',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    keywords='chatgpt automation selenium openai chatbot test automation webdriver gpt-3 automation gpt-4 automation file upload automation chat history retrieval login automation developers QA testers automation engineers pytest robot framework python library automation library best chatgpt automation tool selenium chatgpt integration',
    python_requires='>=3.8',
)
