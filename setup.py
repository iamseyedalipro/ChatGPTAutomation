from setuptools import setup, find_packages

# Read requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ChatGPTAutomation',
    version='0.7.3',
    author='Seyed Ali Hosseini',
    author_email='iamseyedalipro@gmail.com',
    description='A Python package for automating interactions with ChatGPT using Selenium. Chatgpt automation without api. Chatgptautomation',
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
    keywords=[
        'ChatGPT automation',
        'Chatgpt Automation without api',
        "chatgpt selenium",
        "chatgpt selenium automation",
        'Selenium integration',
        'OpenAI chatbot',
        'test automation',
        'web automation',
        'GPT-3',
        'GPT-4',
        'file upload automation',
        'chat history retrieval',
        'login automation',
        'software testing',
        'QA tools',
        'automation engineers',
        'Python library',
        'automation framework',
        'pytest integration',
        'robot framework',
        'browser automation',
        'automated testing',
        'AI chatbot automation',
        'web driver tools'
    ]
    python_requires='>=3.8',
    project_urls={
        'Documentation': 'https://github.com/iamseyedalipro/ChatGPTAutomation#readme',
        'Source': 'https://github.com/iamseyedalipro/ChatGPTAutomation',
        'Tracker': 'https://github.com/iamseyedalipro/ChatGPTAutomation/issues'
    }
)
